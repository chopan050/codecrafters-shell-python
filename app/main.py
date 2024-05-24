import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        args = input().split()
        if args[0] == "exit":
            sys.exit(int(args[1]))
        if True:
            print(f"{args[0]}: command not found")


if __name__ == "__main__":
    main()
