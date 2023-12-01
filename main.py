
def morse_code(text):
    with open("code_dictionary", mode="r") as file:
        letters_list = file.readlines()
        letters_dict = {el.split(":")[0]: el.split(":")[1].strip() for el in letters_list if ":" in el}

    trans_text = ""

    for letter in text.upper():
        if letter == " ":
            next_letter = "   "
        else:
            next_letter = letters_dict[letter]

        trans_text += next_letter + "   "

    print(trans_text)


morse_code("Hello, World!")

