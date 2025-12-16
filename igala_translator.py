# This program translates English words to Igala
# It uses a dictionary to store English words and their Igala meanings


# Step 1: Create a dictionary for English and Igala words
igala_dictionary = {
    "book": "otakada",
    "water": "omi ofo",
    "food": "ujenwu",
    "drink": "omi",
    "clothe": "ukpo",
    "house": "unyi",
    "bag": "ikpa",
    "cap": "otajiya",
    "shoe": "eda",
    "light": "ugane",
    "door": "alugbona",
    "car": "motokeke",
    "rain": "omi ojale",
    "hand": "owo",
    "head": "oji",
    "happy": "edo ebo",
    "sad": "edo ekpbie",
    "bed": "ate",
    "cold": "eridodo",
    "heat": "utola"
}


# Step 2: Create a function to translate a word
def translate_to_igala(word):
    # Convert the word to lowercase so it matches the dictionary keys
    word = word.lower()

    # Check if the word exists in the dictionary
    if word in igala_dictionary:
        return igala_dictionary[word]
    else:
        return "Word not found in the Igala dictionary."


# Step 3: Main program starts here
print("English to Igala Dictionary Translator")
print("------------------------------------")

# Step 4: Keep asking the user for input until they type 'exit'
while True:
    english_word = input("Enter an English word (or type 'exit' to quit): ")

    # If the user wants to stop the program
    if english_word.lower() == "exit":
        print("Thank you for using the translator.")
        break

    # Translate the word
    igala_word = translate_to_igala(english_word)

    # Display the result
    print("Igala meaning:", igala_word)
    print()
