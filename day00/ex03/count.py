import string

def text_analyzer(input_str = ""):
    """
    Displays the sums of upper characters, lower characters, punctiation
    characters and spaces in a given text.

    Accepts only one parameter: the text to be analyze. If none entered, the
    user is prompted to give one.
    """
    qty_punctuation = 0
    qty_lower = 0
    qty_spaces = 0
    qty_upper = 0
    text = input_str

    if input_str == "":
        print("What is the text to analyze? Type the text and press enter.")
        text = input()
  
    if text != "":
        for i in text:
            if i in string.punctuation:
                qty_punctuation += 1
            if i.isupper():
                qty_upper += 1
            if i.islower():
                qty_lower += 1
            if i == ' ':
                qty_spaces += 1

        print("The text contains " + str(len(text)) + " characters:\n")        
        print("- " + str(qty_upper) + " upper letters\n")
        print("- " + str(qty_lower) + " lower letters\n")
        print("- " + str(qty_punctuation) + " punctuation marks\n")
        print("- " + str(qty_spaces) + " spaces")