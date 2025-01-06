def main():
    name = input("Whats your name? ").lower().strip()
    hello(name)
def hello(user_name):
    print(f"Hello, {user_name}")

main()