yoruba_dictionary = {
    "Ẹ káàrọ̀": "Good morning",
    "Ẹ káàsán": "Good afternoon",
    "Ẹ kú alẹ́": "Good evening",
    "Bẹ́ẹ̀ni": "Yes",
    "Rárá": "No",
    "Jọ̀ọ́": "Please",
    "Ẹ ṣé": "Thank you",
    "Dáadáa": "Good / Fine",
    "Bàbá": "Father",
    "Ìyá": "Mother",
    "Ọmọ": "Child",
    "Ọrẹ́": "Friend",
    "Ilé": "House",
    "Omi": "Water",
    "Oúnjẹ": "Food",
    "Owó": "Money",
    "Ilú": "City / Town",
    "Iṣẹ́": "Work / Job",
    "Ìwé": "Book",
    "Orúkọ": "Name"
}

word_key = input("Enter a Yoruba word or phrase (e.g., "Ẹ káàrọ̀"): ")
if word_key in yoruba_word:
    print (f"translation: {yoruba_words[word_key]}")
    else:
    print("Word not found in list.")
    
