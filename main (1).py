kalabari = {
    "water": "omi",
    "food": "kiri",
    "house": "wari",
    "come": "bia",
    "go": "pu",
    "man": "boma",
    "woman": "ere",
    "child": "timi",
    "good": "meme",
    "bad": "biri",
    "sun": "tamuno",
    "moon": "soni",
    "fire": "oku",
    "earth": "tari",
    "air": "feni",
    "love": "preye",
    "name": "iri",
    "hand": "bara",
    "leg": "kpo",
    "salt": "kanan"
}

key = input("Enter an English word: ")

if key in kalabari:
    print(f"{key} means {kalabari[key]}")
else:
    print("Sorry, word not found")
