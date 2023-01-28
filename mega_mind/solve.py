from pwn import *

def main():
    conn = remote('139.59.82.253', 3141)
    print(conn.recvline())
    print(conn.recvline())

    while True:
        s = conn.recvline()

        print(s)
        x = eval(s.strip())
        x = (str(x) + '\n').encode('utf-8')
        print(x)
        conn.send(x)
        print(conn.recvline())
        print(conn.recvline())
        print(conn.recvline())

    conn.close()

if __name__ == "__main__":
    main()
