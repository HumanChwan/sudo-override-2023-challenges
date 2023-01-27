#include <iostream>
#include <vector>
#include <fstream>

#include <cstdlib>

#define MONKE 0
#define TEST_CASES 40

// TODO: change the path pleaseeee
#define FLAG_PATH "flag.txt"

template <class T>
using Grid = std::vector<std::vector<T>>;

void populate_flag(std::string& flag) {
    std::ifstream f;
    f.open(FLAG_PATH);
    if (f.fail()) {
        std::cout << "It seems we are facing some issue! :/ Please try again later.\n";
        exit(1);
    }

    f >> flag;

    f.close();
}

void generate_grid(Grid<char>& grid, int N, int M) {
    std::vector<std::pair<int, int>> path;
    std::pair<int, int> gold = {N - 1, M - 1}, iter = {0, 0};

    Grid<bool> visited(N, std::vector<bool>(M, false));
    visited[0][0] = true;

    int hor = 1;

    while (iter != gold) {
        path.push_back(iter);
        if (iter.first == N - 1) {
            iter.second += 1;
            continue;
        }
        int dist = rand() % 10;
        // 90% go in horizontal direction, 10% vertical
        if (dist < 9) {
            if (hor == 0) {
                if (iter.second == 0) hor = 1;
                else if (iter.second == N - 1) hor = -1;
                else hor = 2 * (rand() % 2) - 1;
            }

            if (0 <= iter.second + hor && iter.second + hor < M) {
                iter.second += hor;
                continue;
            }
        }
        
        iter.first += 1;
        hor = 0;
    }
    path.push_back(iter);
    for (auto &pt : path) {
        grid[pt.first][pt.second] = '.';
    }
    grid[0][0] = '*';
    grid[N - 1][M - 1] = '$';
}

void print_grid(Grid<char>& grid) {
    std::cout << '\n';
    for (auto &r : grid) {
        for (char x : r) {
            std::cout << x;
        }
        std::cout << '\n';
    } 
    std::cout << "\n> ";
}

void pose_maze_to_solve(int N, int M) {
    Grid<char> grid(N, std::vector<char>(M, '#'));
    generate_grid(grid, N, M);
    
    std::pair<int, int> ptr = {0, 0}, gold = {N - 1, M - 1}, old;
    while (1) {
        char x = '`';
        do {
            if (x != '`') std::cerr << "BOO BOO\n";
            print_grid(grid);
            std::cin >> x;
        } while (x != 'w' && x != 'a' && x != 's' && x != 'd');
        
        grid[ptr.first][ptr.second] = '.';
        old = ptr;
        switch(x) {
            case 'w': 
                ptr.first = std::max(ptr.first - 1, 0); 
                break;
            case 'a':
                ptr.second = std::max(ptr.second - 1, 0); 
                break;
            case 'd':
                ptr.second = std::min(ptr.second + 1, M - 1); 
                break;
            case 's':
                ptr.first = std::min(ptr.first + 1, N - 1); 
                break;
            default:
                std::cerr << "ERROR: thats interesting! huh :/\n";
                exit(1);
        }
        // wall collisions
        if (grid[ptr.first][ptr.second] == '#') ptr = old;
        grid[ptr.first][ptr.second] = '*';

        if (ptr == gold) {
            break;
        }
    }
}

int main() {
    srand(time(0));
    std::string flag;
    populate_flag(flag);

    std::cout << "\t\tWelcome to the Maze buster!!\n"
                 "GRID-COMPONENTS: # - Wall, * - You, $ - Gold >_<\n"
                 "GOAL: You wish to reach the Gold, but can't pass through the Walls\n"
                 "CONTROL: w - up, a - left, s - down, d - right\n\n";

    int test_cases = TEST_CASES;
    while (test_cases--) {
        pose_maze_to_solve(15 + (TEST_CASES - test_cases - 1), 10);
        std::cout << "\nSolved: " << TEST_CASES - test_cases << "\n\n";
    }

    std::cout << "\n\nCongratulations! You have busted the Maze in and out!\nHere is your flag: " << flag << 
                 "\nFarewell, my young maze-buster!";
    return MONKE;
}
