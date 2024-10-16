import sys
import os
import unittest


def main():
    builtins = ["exit", "echo", "type", "pwd", "cd"]

    executable_paths = os.environ["PATH"].split(":")
    executables = {}
    for executable_path in executable_paths:
        if os.path.exists(executable_path):
            for executable in os.listdir(executable_path):
                executables[executable] = executable_path

    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        if command[:4] == "exit":
            sys.exit(0)
        elif command[:4] == "echo":
            sys.stdout.write(command[5:])
            sys.stdout.write("\n")
        elif command[:4] == "type":
            sys.stdout.write(command[5:])
            if command[5:] in builtins:
                sys.stdout.write(" is a shell builtin\n")
            elif command[5:] in executables.keys():
                sys.stdout.write(" is ")
                sys.stdout.write(os.path.join(executables[command[5:]], command[5:]))
                sys.stdout.write("\n")
            else:
                sys.stdout.write(": not found\n")
        elif command[:3] == "pwd":
            sys.stdout.write(os.getcwd())
            sys.stdout.write("\n")
        elif command[:2] == "cd":
            if command[3:] == "~":
                os.chdir(os.environ["HOME"])
            elif os.path.exists(command[3:]):
                os.chdir(command[3:])
            else:
                sys.stdout.write("cd: " + command[3:] + ": No such file or directory\n")
        elif command.split()[0] in executables.keys():
            os.system(os.path.join(executables[command.split()[0]], command.split()[0]) + command[len(command.split()[0]):])
        else:
            print(command + ": command not found")


if __name__ == "__main__":
    main()