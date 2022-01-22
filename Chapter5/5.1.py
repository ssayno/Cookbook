import re


def about_newline(file):
    print(f"This is a test for {re.split(r'[.]', file)[0].capitalize()} System")
    with open(file, 'r') as f:
        line = f.read()
        print(line)
        print(repr(line))

    with open(file, 'r', encoding='utf-8', newline='') as f:
        line = f.read()
        print(line)
        print(repr(line), flush=True)


if __name__ == '__main__':
    files = ['linux', 'Windows.txt', 'Mac.txt']
    for file in files:
        about_newline(file)
