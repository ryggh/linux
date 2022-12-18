import sys

def dog():
    print("woof!woof!")

def cat():
    print('mewmew')

def main():
    if sys.argv[1] == "cat":
        cat()
    elif sys.argv[1] == "dog":
        dog()
    else:
        default()

def default():
    print('hello,dyh')

if __name__ == '__main__':
    main()
