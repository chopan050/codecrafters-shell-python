import sys
import os


def find_in_path(command: str) -> str | None:
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

def run_builtin_exit(args: list[str]) -> None:
    sys.exit(int(args[1]))

def run_builtin_echo(args: list[str]) -> None:
    print(" ".join(args[1:]))

def run_builtin_type(args: list[str]) -> None:
    command = args[1]
    if command in shell_builtins:
        print(f"{command} is a shell builtin")
        return
    
    filename = find_in_path(command)
    if filename is not None:
        print(f"{command} is {filename}")
        return
    
    print(f"{command}: not found")

def run_default(args: list[str]) -> None:
    command = args[0]
    if os.path.exists(command):
        filename = command
    else:
        filename = find_in_path(command)
    if filename is not None:
        os.system(" ".join([filename] + args[1:]))
        return

    print(f"{command}: command not found")


shell_builtins = {
    "exit": run_builtin_exit,
    "echo": run_builtin_echo,
    "type": run_builtin_type,
}

def main() -> None:
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        args = input().split()
        run_action = shell_builtins.get(args[0], run_default)
        run_action(args)


if __name__ == "__main__":
    main()
