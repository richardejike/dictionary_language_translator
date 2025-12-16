igbo_word = {
    "Mother": "Nne",
    "Father": "Nna",
    "Brother": "Nwanne nwoke",
    "Sister": "Nwanne nwaanyị",
    "Child": "Nwa",
    "House": "Ụlọ",
    "Food": "Nri",
    "Water": "Mmiri",
    "School": "Ụlọ akwụkwọ",
    "University": "Mahadum",
    "Yes": "Ee",
    "No": "Mba",
    "Good": "Ọma",
    "Bad": "Ọjọọ",
    "Five": "Ise",
    "Ten": "Iri",
    "One": "Otu",
    "Help": "Enyemaka",
    "Please": "Biko",
    "Thank You": "Daalụ"
}

key = input("Enter an English word: ")

if key in igbo_word:
    print(f"{key} means {igbo_word[key]}")
else:
    print("Sorry, word not found")