while True:
    print('Reverse Text using Function')
    string = input("Enter a string: ")

    if string.isdigit():
         print("Error Reported! Enter text only."); print()

    else:
        reverse = string[::-1]
        print("Output:", reverse); print()
    
    choice = input('Make another conversion? ')
    if choice.lower() != 'yes':
        break