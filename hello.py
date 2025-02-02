def greet(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

def main():
    greet()

if __name__ == "__main__":
    main()
