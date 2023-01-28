#include <fstream>
#include <iostream>
#include <cstdlib>
#include <string>
#include <chrono>
#include <queue>

#define MONKE 0

void exit_help() {
    std::cout << "Press (Ctrl-C) to exit...\n";
}

void populate_flag(std::string& flag) {
    std::fstream file;
    file.open("flag.txt");
    if (file.fail()) {
        std::cout << "It seem we are facing some issues right now! Please try again later.\n";
        exit_help();
        exit(1);
    }
    file << flag;
}

struct Node {
    Node* LEFT, *RIGHT;
    bool leaf = false;
    union { int num; char oper; };

    Node(int n): leaf(true), num(n), LEFT(nullptr), RIGHT(nullptr) {}
    Node(char c): leaf(false), oper(c), LEFT(nullptr), RIGHT(nullptr)  {}

    ~Node() { if (LEFT) delete LEFT; if (RIGHT) delete RIGHT; }
};

// as Depth goes to 5, the probability of being a leaf goes to 100% from 0%
// i.e. depth = 0 => prob = 0%
// &    depth = 5 => prob = 100%
// => prob = (depth * 5)%

int max_depth = 5;
const char* OPERATORS = "+-*";
Node* create_subtree(int depth) {
    int distribution = rand() % 100;
    bool is_leaf = distribution < (depth * 100) / max_depth;
    
    if (is_leaf) {
        Node* leaf = new Node(rand() % 200);
        return leaf;
    }

    // add and subtraction have higher probability
    int op = rand() % 5;
    
    op /= 2;

    Node* subroot = new Node(OPERATORS[op]);
    subroot->LEFT = create_subtree(depth + 1);
    subroot->RIGHT = create_subtree(depth + 1);

    return subroot;
}

int64_t form_expression(Node* root, std::string& expression) {
    if (root->leaf) {
        expression += std::to_string(root->num);
        return root->num;
    }

    bool bracket = root->oper == '*' && !root->LEFT->leaf;
    if (bracket) expression += '(';
    int64_t lval = form_expression(root->LEFT, expression);
    if (bracket) expression += ')';

    // middle part
    expression += " ";
    expression += root->oper;
    expression += " ";

    bracket = (root->oper == '*' || root->oper == '-') && !root->RIGHT->leaf;
    if (bracket) expression += '(';
    int64_t rval = form_expression(root->RIGHT, expression);
    if (bracket) expression += ')';

    if (root->oper == '*') return lval * rval;
    else if (root->oper == '+') return lval + rval;
    else return lval - rval;
}

struct MathExpression {
    std::string expression;
    int64_t result;
};

MathExpression generate_math_expression() {
    Node* root = create_subtree(0);

    MathExpression expr;
    expr.result = form_expression(root, expr.expression);

    delete root;

    return expr;
}

void run_test_case() {
    MathExpression expr = generate_math_expression();
    auto start = std::chrono::system_clock::now();
    std::cout << expr.expression << '\n';
    std::cout << "> ";

    int64_t res;
    std::cin >> res;
    auto end = std::chrono::system_clock::now();

    std::chrono::duration<double> diff = end - start;
    double epsilon = 1.0;
    if (diff.count() > epsilon) {
        std::cout << "Too Slow! Try again :/\n\n";
        exit_help();
        exit(1);
    }

    if (res != expr.result) {
        std::cout << "That doesn't seem like the correct result!\n\n";
        exit_help();
        exit(1);
    }
    std::cout << '\n';
}

void fuck_simple() {
    std::cout << "exit()\n\n";
}

void annoy_max_fuck() {
    std::ifstream payload;
    payload.open("payload.py");
    if (payload.fail()) {
        std::cout << "It seem we are facing some issues right now! Please try again later.\n";
        exit_help();
        exit(1);
    }
    std::cout << payload.rdbuf() << '\n';
}

int main() {
    std::string flag;
    populate_flag(flag);
    
    srand(time(0));
    std::cout << "\t\tGreetings! Are you fast enough? ^_<\n\n";
    
    int rounds = 60 + rand() % 40;
    for (int i = 0; i < rounds; ++i) run_test_case();

    int annoy_max_fuck_rounds = 10 + rand() % 10;
    for (int i = 0; i < annoy_max_fuck_rounds; ++i) {
        int random = rand() % 10;
        if (random < 2) annoy_max_fuck(), i--;
        else if (random < 3) fuck_simple(), i--;
        else run_test_case();
    }

    int single_fuck_rounds = 25 + rand() % 10;
    for (int i = 0; i < single_fuck_rounds; ++i) {
        if (rand() % 10 < 3) fuck_simple(), i--;
        else run_test_case();
    }

    std::cout << "Congratulations big brainer!\nHere is your flag: " << flag << 
        "\nFarewell, We wish all the luck!\n";

    return MONKE;
}
