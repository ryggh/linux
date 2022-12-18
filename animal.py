import sys

def dog():
    print("Woof!woof!")

def cat():
    print('Mewmew')

def main():
    if sys.argv[1] == "cat":
        cat()
    elif sys.argv[1] == "dog":
        dog()
    else:
        default()

def default():
    print('Hello,dyh')

if __name__ == '__main__':
    main()
