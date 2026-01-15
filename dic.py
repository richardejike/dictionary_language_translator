igbo_word = {
    "Nne": "Mother" ,
    "Nna": "Father" ,
    "Nwanne nwoke": "Brother" ,
    "Nwanne nwaanyi": "Sister" ,
    "Nwa": "Child",
    "Ulo": "House",
    "Nri": "Food",
    "Mmiri": "Water",
    "Ulo akwukwo": "School",
    "Mahadum": "University",
    "Ee": "Yes",
    "Mba": "No",
    "Oma": "Good",
    "Ojoo": "Bad",
    "Ise": "Five",
    "Iri": "Ten",
    "Otu": "One",
    "Enyemaka": "Help",
    "Biko": "Please",
    "Daalụ": "Thank You"
}

key = input("Enter an English word: ")

if key in igbo_word:
    print(f"{key} means {igbo_word[key]}")
else:

    print("Sorry, word not found")
