def main():
    text = input("State the first three colors of the rainbow ").replace(" ", "...")
    slow(text)

def slow(user_text):
    print(f"Slow down: {user_text}")

main()
