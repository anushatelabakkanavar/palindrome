def check_palindrome(text):
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
        print("The given string is a Palindrome")
    else:
        print("The given string is not a Palindrome")


string = input("Enter a string: ")
check_palindrome(string)
