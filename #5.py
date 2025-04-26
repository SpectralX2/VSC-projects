while True:
    word = input("Enter a word (or type 'stop' to quit): ")

    if word.lower() == "stop":
        break

    for letter in word:
        print(letter)
