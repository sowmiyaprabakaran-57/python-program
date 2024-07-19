def analyze_text(text):
    import string
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    num_words = len(words)

    num_characters = len(text.replace(" ", ""))  

    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    print("Number of words:", num_words)
    print("Number of characters (excluding spaces):", num_characters)
    print("Word frequency:")
    for word, frequency in word_frequency.items():
        print(f"  {word}: {frequency}")

text_input = input("Enter a text to analyze: ")
analyze_text(text_input)
