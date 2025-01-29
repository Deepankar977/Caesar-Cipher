import string

# Function to display the menu and get user input for encryption or decryption
def menu():
    try:
        user_input = input("""To Encrypt : E\n
To Decrypt : D\n
Enter: """)
        if user_input.lower() in ['e', 'd']:
            return user_input.lower()
        else:
            raise ValueError("Invalid menu option. Please choose from E or D")
    except ValueError as e:
        print(e)
        return menu()  # Recursively call the menu until valid input is received

# Removes spaces from a given list
def remove_spaces(lst):
    return [i for i in lst if i != ' ']  # List comprehension to remove spaces

# Formats text by replacing spaces with hyphens
def format(lst):
    text = "".join(lst)
    return text.replace(" ", "-")  # Replace spaces with hyphens for encoding

# Adds hyphens between characters for readability
def format_readability(lst2):
    init_sent = format(lst2)
    l = []
    for z in init_sent:
        l += z+'-'  # Adds a hyphen between characters for readability
    l.pop(len(l)-1)  # Remove last extra hyphen
    return "".join(l)

# Fetches characters based on shift mapping
def fetcher_shift(original_dict, lst):
    new_dict = {}
    for key in lst:
        if key in original_dict:
            new_dict[key] = original_dict[key]  # Fetches the corresponding shifted values
    return new_dict

# Encryption function: Converts characters to their corresponding encrypted values based on the shift
def encrypt(s, shift=0):
    letters = string.ascii_lowercase
    actual = ''
    for i in letters:
        actual += i+','
    li_let = actual.split(',')
    li_let.pop(len(li_let)-1)  # Remove last empty element

    # Creating a dictionary where letters are mapped to shifted numbers
    default_caesar = {}  
    for j, alphabet in enumerate(li_let):
        default_caesar[alphabet] = str(j+1+shift)

    chunked = []
    raw = s
    for k in raw:
        for l in k:
            chunked.append(l.lower())

    remove_spaces(chunked)  # Removes spaces from the character list
    ordered = sorted(set(chunked))  # Orders the chunked list for mapping
    caesar = fetcher_shift(default_caesar, ordered)

    encrypted = ""
    s3 = format(s)
    s4 = format_readability(s3)
    for char in s4:
        if char.isalpha():
            encrypted += caesar.get(char.lower(), char)  # Convert letters to numbers
        else:
            encrypted += char  # Preserve punctuation and spaces

    print(f"Encrypted: {encrypted}")

# Decryption function: Converts numbers back to letters based on the shift
def decrypt(encrypted_sen, shift2=0):
    letters = string.ascii_lowercase
    actual2 = ''
    for i in letters:
        actual2 += i + ','
    li_let2 = actual2.split(',')
    li_let2.pop(len(li_let2) - 1)  # Remove last empty element

    # Creating reverse dictionary for number-to-letter mapping
    keys = {str(j + 1 + shift2): alpha for j, alpha in enumerate(li_let2)}

    decrypted = ""
    parts = encrypted_sen.split('-')  # Split by hyphens to extract numbers

    for part in parts:
        if part.isdigit():
            decrypted += keys.get(part, part)  # Convert numbers to letters
        elif part in [',', '.', '!', '?']:  # Preserve punctuation
            decrypted += part
        else:
            decrypted += ' '  # Restore spaces

    print(f"Decrypted: {decrypted.capitalize()}")  # Capitalize first letter for readability

# Running the menu selection to either encrypt or decrypt based on user input
match menu():
    case "e":
        sen = str(input('Enter your message to encrypt: '))
        try:
            KEY = int(input("Enter the shift/key you want in the encryption: "))
            encrypt(sen, KEY)
        except ValueError:
            print("Invalid input. Please enter an integer for shift value.")  # Error handling for invalid shift input
    case "d":
        sen2 = str(input('Enter your encrypted message to decrypt: '))
        try:
            KEY2 = int(input("Enter the shift/key which has been used in the encryption: "))
            decrypt(sen2, KEY2)
        except ValueError:
            print("Invalid input. Please enter an integer for shift value.")  # Error handling for invalid shift input