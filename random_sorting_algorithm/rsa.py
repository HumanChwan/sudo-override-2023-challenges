#!/usr/bin/python3

from Crypto.Util.number import getPrime, bytes_to_long
import random
import sys

flag = 'I think someone is trying to get our flag: sudo{th4t_wa5nt_4_s0rt1n6_4lg0r1t8m_oWo}'

def menu() -> int:
    print("Options:")
    print("1. Intercept a connection.")
    print("2. exit")
    try:
        opt = input("> ")
        if opt == '1': return 1
        elif opt == '2': return 2
        else:
            print("ERROR: That's not a valid option :/")
            return menu()
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

def print_intercepted_message():
    e = 3 + 2 * random.randint(0, 10);
    p = getPrime(512)
    q = getPrime(512)
    n = p * q

    M = bytes_to_long(flag.encode('utf-8'))
    c = pow(M, e, n)

    print(f'Encrypted Text = {c}')
    print(f'N = {n}')
    print(f'e = {e}', end="\n\n")

def main():
    print("Welcome to Gotcha! Intercept portal.")

    while True:    
        option = menu()
        
        if option == 1: print_intercepted_message()
        elif option == 2:
            break

    print("Press (Ctrl-C) to exit...")


if __name__ == "__main__":
    main()
