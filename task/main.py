import sys

def main():
    # Print "Hello" and any arguments passed to the program
    print("Hello", " ".join(sys.argv[1:]))

if __name__ == "__main__":
    main()
