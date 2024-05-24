import sys
import os


def on_type(args):
    command = args[1]
    if command in builtins:
        print(f"{command} is a shell builtin")
        return
    
    path = os.environ.get("PATH")
    if path is None:
        unknown(command)
        return

    for p in path.split(":"):
        if not p.endswith("/"):
            p += "/"
        filename = p + command
        if os.path.exists(filename):
            print(f"{command} is {filename}")
            return

    unknown(command)

builtins = {
    "exit": lambda args: sys.exit(int(args[1])),
    "echo": lambda args: print(" ".join(args[1:])),
    "type": on_type,
}
unknown = lambda command: print(f"{command}: command not found")



def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        args = input().split()
        command = args[0]
        action = builtins.get(command, None)
        if action is not None:
            action(args)
            continue

        unknown(command)


if __name__ == "__main__":
    main()
