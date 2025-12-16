hausa_words = {
    "ruwa": "water",
    "abinci": "food",
    "gida": "house",
    "littafi": "book",
    "makaranta": "school",
    "namiji": "man",
    "mace": "woman",
    "yaro": "child",
    "hasken rana": "sun",
    "wata": "moon",
    "titi": "road",
    "mota": "car",
    "itace": "tree",
    "wuta": "fire",
    "kudi": "money",
    "aboki": "friend",
    "kasuwa": "market",
    "rana": "day",
    "dare": "night",
    "ruwan sama": "rain"
}

word_key = input("Enter a Hausa word (e.g., 'ruwa'): ")
if word_key in hausa_words:
    print(f"Translation: {hausa_words[word_key]}")
else:
    print("Word not found in list.")