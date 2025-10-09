def Palindrome():
    word: str = input("Enter a word: ")
    reversed_word = word[::-1]

    if reversed_word == word:
        print("Palindrome")
    else:   
        print("No Palindrome")

Palindrome()