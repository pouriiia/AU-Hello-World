from datetime import datetime

def hello():
    print("Hello, world!")
    print("My name is Saeed.")
    print("I am learning Python.")
    print("GitHub is fun!")
    print("This is my improved project.")
    print("-------------------------")

    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    hello()
