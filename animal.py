import sys

def dog():
    print("Bawww")

def default():
    print("Hello Py")

def main():
    default()

if __name__ == '__main__':
    # Check if there are any command-line arguments
    if len(sys.argv) > 1 and sys.argv[1] == 'dog':
        dog()
    else:
        main()

