# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

def admin():
    var = input()
    updated_var = [var, 'something else idk']
    return updated_var

def list_files():
    string = ''
    oops = 'z'
    list1 = ['-r', '-f', '-s', '-e']
    directory = input("What\'s the directory of the file? ex. c:\\users\\andyh\\desktop\\myjournal.dsu\n")
    string = directory
    ## GETS FIRST INPUT
    program_feature1 = input('''What do program feature do you want?
-r Output directory content recursively.
-f Output only files, excluding directories in the results.
-s Output only files that match a given file name.
-e Output only files that match a give file extension.
example input: -r\n''').strip()
    ## CHECKS IF INPUT IS VALID
    if program_feature1 in list1:
        ## ADDS TO STRING
        oneone = string + ' ' + program_feature1
        ## CHECKING FOR -R
        if program_feature1 == list1[0]:
            programfeature2 = input('''Do you want another program feature?
-f Output only files, excluding directories in the results.
-s Output only files that match a given file name.
-e Output only files that match a give file extension.
or enter n for no other feature
example input: -r\n''').strip()
            ## CHECKING FOR VALIDITY
            if programfeature2 in list1[1:]:
                second = oneone + ' ' + programfeature2
                ## CHECKING FOR -F
                if programfeature2 == list1[1]:
                    woah = ' ' + second
                    return woah
                 ## CHECKING FOR -S
                if programfeature2 == list1[2]:
                    file_name = input('What file name do you want to search for?\n').strip()
                    final = ' ' + second + ' ' + file_name
                    return final
                 ## CHECKING FOR -E
                if programfeature2 == list1[3]:
                    extension = input('What extention do you want to search for?\n').strip()
                    final = ' ' + second + ' ' + extension
                    return final
            elif programfeature2 == 'no':
                woah = ' ' + oneone
                return woah
         ## CHECKING FOR -F
        if program_feature1 == list1[1]:
            woah = ' ' + oneone
            return woah
         ## CHECKING FOR -S
        if program_feature1 == list1[2]:
            file_name = input('What file name do you want to search for?\n').strip()
            final = ' ' + oneone + ' ' + file_name
            return final
         ## CHECKING FOR -E
        if program_feature1 == list1[3]:
            extension = input('What extention do you want to search for?\n').strip()
            final = ' ' + oneone + ' ' + extension
            return final
    else:
        return oops

def create_files():
    directory = input('''What\'s the directory of the file you're trying to create? 
NOTE: File will be a dsu file\n''').strip()
    name = input('What do you want to name your file?\n').strip()
    final = directory + ' ' + '-n' + ' ' + name
    return final

def delete_files():
    directory = input('''What\'s the directory of the file you're trying to delete? 
    NOTE: File must me a .dsu file
    ex. c:\\users\\andyh\\desktop\\myjournal.dsu\n''').strip()
    return directory

def read_files():
    file = input('''What\'s the directory of the file you're trying to read? 
    NOTE: File must me a .dsu file
    ex. c:\\users\\andyh\\desktop\\myjournal.dsu\n''').strip()
    return file

def open_files():
    directory = input('''What\'s the directory of the file you're trying to oepn? 
    NOTE: File has to be a .dsu file
    ex. c:\\users\\andyh\\desktop\\myjournal.dsu\n''').strip()
    return directory

def edit_files():
    truths = True
    final = ''
    x = ''' Here's the Edit Menu:
    -usr [USERNAME]

    -pwd [PASSWORD]

    -bio [BIO]

    -addpost [NEW POST]

    -delpost [ID] (a number such as 1, 2, 3...)
    
    ** NO WHITESPACES IN USERNAME OR PASSWORD, IF YOU DO WILL RESULT IN ERROR **'''
    print(x)

    while truths:
        selection = input('''Enter a edit:
        Just the first part:
            ex. -usr, -pwd, -bio...\n''')
        change = input('''Enter the change you want to make\n''')
        end = input('''Do you want to make more edits? y/n:
        ** Only enter the letter y or n\n''').strip()
        one = final
        two = selection + ' ' + change + ' '
        final = one + two
        if end == 'n':
            truths = False
    
    updated_final = final.strip()

    return updated_final

def print_files():
    truths = True
    final = ''
    x = '''Here's the Print Menu:
    -usr Prints the username stored in the profile object

    -pwd Prints the password stored in the profile object

    -bio Prints the bio stored in the profile object

    -posts Prints all posts stored in the profile object with id (using list index is fine)

    -post [ID] Prints post identified by ID numbered starting from 1

    -all Prints all content stored in the profile object'''
    print(x)
    while truths:
        selection = input('''Enter what you want to print out:
        Just the first part:
            ex. -usr, -pwd, -bio...\n''')
        end = input('''Do you want to print anything else? y/n:
        ** Only enter the letter y or n\n''').strip()
        one = final
        two = selection + ' '
        final = one + two
        if end == 'n':
            truths = False
    
    updated_final = final.strip()

    return updated_final

def starting():
    initial = input('''Are you trying to list (L), create (C), delete(D), read (R),  or open (O) files?
If you already loaded a file you can edit (E) or print(P) the contents of the file.
If you want to quit enter Q : ''')
    initial1 = initial.upper().strip()
    list1 = ['L', 'C', 'D', 'R', 'O','Q', 'E', 'P']
    
    
    if initial1 == 'ADMIN':
        final = admin()
        return final
    elif initial1 in list1:
        
        if initial1 == list1[0]: ## L
            thing1 = list_files()
            final = initial1 + thing1
            return final
        if initial1 == list1[1]: ## C
           thing1 = create_files()
           final = initial1 + ' ' + thing1
           return final
        if initial1 == list1[2]: ## D
            thing1 = delete_files()
            final = initial1 + ' ' + thing1
            return final
        if initial1 == list1[3]: ## R
            thing1 = read_files()
            final = initial1 + ' ' + thing1
            return final
        if initial1 == list1[4]: ## O
            thing1 = open_files()
            final = initial1 + ' ' + thing1
            return final
        if initial1 == list1[5]: ## Q
            return initial1
        if initial1 == list1[6]: ## E
            thing1 = edit_files()
            final = initial1 + ' ' + thing1
            return final
        if initial1 == list1[7]: ## P
            thing1 = print_files()
            final = initial1 + ' ' + thing1
            return final
    else:
        return initial1

if __name__ == "__main__":
    global var
    var = ''
   

# NAME
# EMAIL
# STUDENT ID
