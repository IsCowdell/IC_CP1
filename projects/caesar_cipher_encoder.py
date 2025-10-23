#IC 1st caesar

# This function \does encoding or decoding
def caesar_cipher(text, shift, mode):
    new_text = ""  # Start with an empty string to build the result

    # Go through each letter in the message
    for letter in text:
        # more stupid proofing
        if letter.isalpha():
            # Figure out if it's uppercase or lowercase #btw i asked my brother how to do this so thats why there is ord and chr i know what they do 
            if letter.isupper():
                base = ord('A')  # value for 'A'
            else:
                base = ord('a')  # value for 'a'

            # Shift the letter forward or backward depending on mode
            new_letter = chr((ord(letter) - base + (shift if mode == "encode" else -shift)) % 26 + base)

            # Add the new letter to the result
            new_text += new_letter
        else:
            # If it's not a letter, just add it as-is
            new_text += letter

    # Return the final encoded or decoded message
    return new_text

# This is what runs when the program starts
def main():
    # Ask the user what they want to do
    print("Choose action (1 for encode, 2 for decode): ", end="")
    choice = input()

    # Figure out if they picked encode or decode
    if choice == "1":
        mode = "encode"
    elif choice == "2":
        mode = "decode"
    else:
        # stupid proofing 
        print("that's not a valid choice")
        return

    # Ask for the message
    message = input("Enter the message: ")

    # Ask for the shift value
    try:
        shift = int(input("Enter the shift value: "))
    except:
        print("Shift has to be a number")
        return

    # Call the function to do the cipher stuff
    result = caesar_cipher(message, shift, mode)

    # Show the final result
    print(f"Here is your {mode}d message: {result}")

# Run the main function
main()