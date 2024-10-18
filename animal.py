import sys

def dog():
    print("Bawww")

def cat():
    print("Meow")

def default():
    print("Hello Py")

def main():
    # Check if there are any command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == 'dog':
            dog()
        elif sys.argv[1] == 'cat':
            cat()
        else:
            default()
    else:
        default()

if __name__ == '__main__':
    main()

