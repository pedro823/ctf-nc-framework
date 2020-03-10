from lib.types import IStdin, IStdout

def main(stdin: IStdin, stdout: IStdout):
    stdout.write('Hello, world!\n')

    stdout.write('What is your name?')
    stdout.flush()
    name = stdin.readline().strip()

    stdout.write(f'Hello, {name}!\n')