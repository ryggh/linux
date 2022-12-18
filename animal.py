import sys

def cat():
    print('mewmew')

def main():
    if sys.argv[1] == "cat":
        cat()
    else:
        default()

def default():
    print('hello,dyh')

if __name__ == '__main__':
    main()
