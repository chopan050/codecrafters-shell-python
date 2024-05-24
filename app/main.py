import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    while True:
        # Wait for user input
        args = input().split()
        if True:
            print(f"{args[0]}: command not found")


if __name__ == "__main__":
    main()
