import sys

def dog():
    print("woof!woof!")

def main():
    if sys.argv[1] == "dog":
        dog()
    else:
        default()

def default():
    print('hello,dyh')

if __name__ == '__main__':
    main()
