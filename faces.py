def main():
    text = input("Hello, add a frowny face or smiley face. ").replace(":)", "🙂").replace(":(", "🙁")
    convert(text)

def convert(reply):
    print(f"{reply}")

main()