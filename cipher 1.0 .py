def find_in_list(query, mainlist):
    mainlist_len = len(mainlist)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
            return index

chars =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in plain_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg == encrypted_msg + character 
    return  encrypted_msg     
def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in encrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg =decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
    return decrypted_msg      
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!").lower()
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        print(encrypt_message(plain_message))
    elif choice == 'd':
        encrypted_msg = input("Enter message to decrypt?")
        print(decrypt_message(encrypted_msg))
    # else:
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)").upper()
    if play_again == 'Y':
        continue
    elif play_again == 'N':
        break