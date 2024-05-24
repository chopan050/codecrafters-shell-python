import sys
import os


def find_in_filesystem(command: str) -> str | None:
    if os.path.exists(command):
        return command

    path = os.environ.get("PATH")
    if path is None:
        return None

    for p in path.split(":"):
        if not p.endswith("/"):
            p += "/"
        filename = p + command
        if os.path.exists(filename):
            return filename

    return None

def on_type(args: list[str]) -> None:
    command = args[1]
    if command in builtins:
        print(f"{command} is a shell builtin")
        return
    
    filename = find_in_filesystem(command)
    if filename is not None:
        print(f"{command} is {filename}")
        return
    
    print(f"{command}: not found")

builtins = {
    "exit": lambda args: sys.exit(int(args[1])),
    "echo": lambda args: print(" ".join(args[1:])),
    "type": on_type,
}


def main() -> None:
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        args = input().split()
        command = args[0]
        action = builtins.get(command)
        if action is not None:
            action(args)
            continue

        filename = find_in_filesystem(command)
        if filename is not None:
            os.system(filename)
            continue

        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
