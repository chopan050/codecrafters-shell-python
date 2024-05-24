import sys


def main():
    builtins = ["exit", "echo", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        args = input().split()
        if args[0] == "exit":
            sys.exit(int(args[1]))
        elif args[0] == "echo":
            print(" ".join(args[1:]))
        elif args[0] == "type":
            if args[1] in builtins:
                print(f"{args[1]} is a shell builtin")
            else:
                print(f"{args[1]}: not found")
        else:
            print(f"{args[0]}: command not found")


if __name__ == "__main__":
    main()
