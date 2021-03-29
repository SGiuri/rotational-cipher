def rotate(text, key):
    cyphred_text = ""
    for letter in text:

        if ord(letter.lower()) in range(ord("a"), ord("z") + 1):

            new_ord = ord(letter.lower()) + key

            if new_ord > ord("z"):
                new_ord = new_ord - (ord("z") - ord("a") + 1)
            new_letter = chr(new_ord)
            if letter == letter.upper():
                new_letter = new_letter.upper()
            cyphred_text += new_letter
        else:
            cyphred_text += letter

    return cyphred_text
