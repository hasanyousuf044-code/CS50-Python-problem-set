def main():
    user_input = input()
    final_output = convert(user_input)
    print(final_output)

def convert(text):
    text = text.replace(":)", "🙂")

    text = text.replace(":(", "🙁")

    return text
main()
