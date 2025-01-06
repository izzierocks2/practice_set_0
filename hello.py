"""#Ask user for name
name = input("Whats your name? ")
#Remove whitespace
name = name.strip()
#Capitalize user name
name = name.title()
#Say hello
print(f"Hello, {name}")"""

"""name = input("Whats your name? ").strip().title()

def hello():
    print(f"Hello, {name}")

hello()"""

def main():
    name = input("Whats your name? ").strip().title()
    hello(name)

def hello(user_name):
    print(f"Hello, {user_name}")


main()