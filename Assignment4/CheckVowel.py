def CheckVowel():

    vowelList = ['a', 'e', 'i', 'o', 'u']
    c = 'b'
    while c != 'x':

        c = input("Enter a character (to exit enter x): ")
        if len(c) > 1 or len(c) < 1:
            print("Enter a single character")
            continue
        
        if c in vowelList:
            print(c + " is a vowel")
        else:
            print(c + " is not a vowel")


CheckVowel()

    
