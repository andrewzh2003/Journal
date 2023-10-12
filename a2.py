# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python
from pathlib import Path
from Profile import Profile, Post
from ui import *
from json import load
def quote_checker(second):
    if second[0] == "\"" and second[-1] == "\"":
        section = second[1:-1]
        return section
    elif second[0] == "\'" and second[-1] == "\'":
        section = second[1:-1]
        return section
    else:
        return False

def checker(x):
    y = x.strip()
    if y == "":
        return False
    else:
        return True

def path_validity_checker(master_list):
    location = master_list[0]
    p1 = Path('.') / location
    if p1.exists():
        return True
    else:
        return False
    pass

def input_seperator_norm(x):
    index_of_dash = x.index(' -')
    length_of_input = len(x)
    different_options = x[index_of_dash:length_of_input].split()
    location = x[2:index_of_dash].strip()
    master_list = [location] + different_options

    return master_list

def input_seperator_dif(x): ## for C
    index_of_dash = x.index(' -')
    length_of_input = len(x)
    option1 = x[2:index_of_dash]
    second_part = x[index_of_dash: length_of_input]
    counter = second_part.count(' -')
    if counter == 1:
        first_part = x[index_of_dash + 1:index_of_dash + 3]
        second_ = x[(index_of_dash + 4):length_of_input]
        master_list1 = [option1] + [first_part] + [second_]

        return master_list1
    else:
        print('ERROR')

def sorter(x):
    start = x[0] ## aka the command
    end = x[2:len(x)] ## aka the directory
    final = [end] + [start]

    return final

def simple(x):
    file = []
    dirr = []
    places = x[2:len(x)]
    first = Path(places)
    for obj in first.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        print(i)
    for i in dirr:
        print(i)
    
def r(lists, directory, function_number): ## recursive
    global num
    if function_number == 1:
        file = []
        dirr = []
        locate = Path(directory)
        for obj in locate.iterdir():
            if obj.is_file():
                file.append(obj)
            if obj.is_dir():
                dirr.append(obj)
        for i in file:
            print(i)
        for i in dirr:
            print(i)
            r(lists, i, 1)
    if function_number == 2:
        file = []
        dirr = []
        locate = Path(directory)
        for obj in locate.iterdir():
            if obj.is_file():
                file.append(obj)
            if obj.is_dir():
                dirr.append(obj)
        for i in file:
            print(i)
        for i in dirr:
            r(lists, i, 2)
    if function_number == 3:
        file = []
        dirr = []
        locate = Path(directory)
        for obj in locate.iterdir():
            if obj.is_file():
                file.append(obj)
            if obj.is_dir():
                dirr.append(obj)
        for i in file:
            if lists[3] in str(i):
                print(i)
        for i in dirr:
            r(lists, i, 3)
    if function_number == 4:
        file = []
        dirr = []
        extension = '.' + lists[3]
        locate = Path(directory)
        for obj in locate.iterdir():
            if obj.is_file():
                file.append(obj)
            if obj.is_dir():
                dirr.append(obj)
        for i in file:
            if extension in str(i):
                print(i)
        for i in dirr:
            r(lists, i, 4)

def F(lists): ## just files
    file = []
    dirr = []
    first = Path(lists[0])
    for obj in first.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        print(i)

def S(lists):## finding specific?
    file = []
    dirr = []
    first = Path(lists[0])
    for obj in first.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        if lists[2] in str(i):
            print(i)

def E(lists): ## extension
    file = []
    dirr = []
    extension = '.' + lists[2]
    first = Path(lists[0])
    for obj in first.iterdir():
        if obj.is_file():
            file.append(obj)
        if obj.is_dir():
            dirr.append(obj)
    for i in file:
        if extension in str(i):
            print(i)

def C(master_list): ## creates file
    ## os. path. join(save_path, file_name)
    ## master_list == location command name
    list1 = ['-n']
    ## check that lsit of 1 is location 2 is -n and location 3 is a file name with no '.'
    if master_list[1] in list1:
        global full_name
        corrected_file = master_list[2] + ".dsu"
        x = master_list[0]
        full_name = master_list[0] + x[2] + corrected_file
        potential = [full_name]
        p1 = Path(full_name)
        if not p1.exists():
            global loaded
            loaded = True
            global user1
            if questions == True:
                print('Enter a username: ')
                username = input()
                one = checker(username)
                print(one)
                if one:
                    if ' ' in username:
                        username = username.replace(' ', '')
                    print('Enter a password: ')
                    password = input()
                    two = checker(password)
                    if two:
                        if ' ' in password:
                            password = password.replace(' ', '')
                        print('Enter a bio: ')
                        bio = input()
                        three = checker(bio)
                        if three:
                            p1.touch()
                            user1 = Profile('', username, password)
                            user1.bio = bio
                            user1.save_profile(full_name)
                        else:
                            print("ERROR")
                    else:
                        print("ERROR")
                else:
                    print("ERROR")
            else:
                print('Enter a username: ')
                username = input()
                one = checker(username)
                if one:
                    if ' ' in username:
                        username = username.replace(' ', '')
                    print('Enter a password: ')
                    password = input()
                    one = checker(password)
                    if one:
                        if ' ' in password:
                            password = password.replace(' ', '')
                        print('Enter a bio: ')
                        bio = input()
                        one = checker(bio)
                        if one:
                            p1.touch()
                            user1 = Profile('', username, password)
                            user1.bio = bio
                            user1.save_profile(full_name)
                        else:
                            print("ERROR")
                    else:
                        print("ERROR")
                else:
                    print("ERROR")
        elif p1.exists():
            O(potential)
        else:
            print("ERROR")
    else:
        print("ERROR")
    
    return user1

def D(master_list): ## Deleting
    global loaded
    deletion = False
    if len(master_list) > 3:
        second = master_list[2:len(master_list)] ## the file directory
        reversed_second = second[len(second):None:-1] ## reversing the directory
        location = reversed_second.index('.') ## taking the index of the first . after reversing to find extension
        extension = reversed_second[0:location] ## isolating the extention
        if second == full_name:
            deletion = True
            loaded = False
        p1 = Path(".") / second
    
        if extension == "usd":
            if p1.exists():
                p1.unlink()
                print(f'{second} DELETED')
                if questions == True:
                    if deletion == True:
                        print('LOADED FILE HAS BEEN DELETED')
                    else:
                        pass
                else:
                    pass
            else:
                print('ERROR')
        else:
            print('ERROR')
    else:
        print("ERROR")
    return

def R(master_list):## reading the things
    if len(master_list) > 3:
        tester = True
        second = master_list[2:len(master_list)]
        reversed_second = second[len(second):None:-1]
        location = reversed_second.index('.')
        extension = reversed_second[0:location]
        p1 = Path(".") / second

        if extension == "usd":
            if p1.exists(): # check to see if file exists
                f = p1.open('r')
                single = f.read()
                f.close()
                if single == '':
                    tester = False
                    print("EMPTY")
                if tester:
                    f = p1.open('r')
                    for i in f.readlines():
                        print(i[:-1])
                    f.close()
        else:
            print("ERROR")
    else:
        print("ERROR")
    return
### x is the profile
### masterlist is
def O(x):
    if path_validity_checker(x):    
        global loaded
        loaded = True
        global user1
        global full_name
        try:
            full_name = x[0]
            reverse = full_name[len(full_name):None:-1]
            location = reverse.index('.')
            extension = reverse[0:location]
        except:
            extension = None

        if extension == 'usd':
            bull = None
            try:
                f = open(full_name)
                data = load(f)
                keys = data.keys()
                bull = True
            except:
                bull = False
            if bull == True:
                condition = 0
                list1 = ['dsuserver', "username", "password", "bio", "_posts"]
                for i in keys:
                    if i in list1:
                        condition += 1
                
                if condition == 5 and len(keys) == 5:
                    user1 = Profile()
                    user1.load_profile(x[0])
                    print('File Loaded!')
                    return user1
                else:
                    print('ERROR')
            else:
                print("ERROR")
        else:
            print("ERROR")




            
           

    else:
        print("ERROR")
### E -usr "mark b" -pwd "password123"
def Edit(initial, x):
    if ' -' in initial:
        string = initial[1:len(initial)]
        final = string.split(' -')
        final.pop(0)
        list1 = ['usr', 'pwd', 'bio', 'addpost', 'delpost']
        status = None
        edits = True
        for i in final:
            try:
                y = i.index(' ')
                first = i[0:y]
                second = i[y+1:len(i)]
                status = True
            except:
                print('ERROR')
                edits = False
            if edits == True:
                quote = quote_checker(second)
                if quote == False:
                    status = False
                else:
                    second = quote
                if status == True:
                ## username
                    if first == list1[0]:
                        if ' ' in second:
                            print('ERROR')
                            edits = False
                        else:
                            x.username = second
                            x.save_profile(full_name)
                    ## password
                    if first == list1[1]:
                        if ' ' in second:
                            print('ERROR')
                            edits = False
                        else:
                            x.password = second
                            x.save_profile(full_name)
                    ## bio
                    if first == list1[2]:
                        x.bio = second
                        x.save_profile(full_name)
                    ## addpost
                    if first == list1[3]:
                        words = second
                        po = Post(words)
                        x.add_post(po) 
                        x.save_profile(full_name)
                    ## delpost
                    if first == list1[4]:
                        try:
                            int(second.strip())
                            truth = True
                        except:
                            truth = False
                        if truth == True:
                            number = second
                            try:
                                x.del_post(int(number))
                                x.save_profile(full_name)
                            except:
                                print("ERROR")
                    if first not in list1:
                        edits = False
                        print("ERROR")
                else:
                    print("ERROR")
            else:
                break
    else:
        print("ERROR")
    
def P(initial, x):
    if ' -' in initial:
        string = initial[1:len(initial)]
        final = string.split(' -')
        final.pop(0)
        list1 = ['usr', 'pwd', 'bio', 'posts', 'post', 'all']
        
        for i in final:
            stripped = i.replace(" ", '')
            if stripped == i:
                ## username
                if i == list1[0]:
                    print(x.username)
                ## password
                elif i == list1[1]:
                    print(x.password)
                ## bio
                elif i == list1[2]:
                    print(x.bio)
                ## posts
                elif i == list1[3]:
                    posts = x.get_posts()
                    for i in posts:
                        if i["entry"] == '':
                            print('EMPTY')
                        else:
                            print(i["entry"])
                ## all
                elif i == list1[5]:
                    print(x.dsuserver)
                    print(x.username)
                    print(x.password)
                    print(x.bio)
                    print(posts[0]["entry"])
                    for i in posts:
                        print(i["entry"])
                else:
                    print("ERROR")
            else:
                if ' ' in i:
                    ## post
                    y = i.index(' ')
                    first = i[0:y]
                    second = i[y:len(i)]
                    truth = None
                    try:
                        int(second.strip())
                        truth = True
                    except:
                        truth = False
                    if first == list1[4] and truth == True:
                        post_id = int(second.strip())
                        posts = x.get_posts()
                        if post_id <= len(posts):
                            if posts[post_id - 1]["entry"] == '':
                                print("EMPTY")
                            else:
                                print(posts[post_id - 1]["entry"])
                        else:
                            print("ERROR")
                    else:
                        print("ERROR")
                else:
                    print("ERROR")
    else:
        print("ERROR")

def branches(master_list):
    if path_validity_checker(master_list) == True:
        list1 = ['-r', '-f', '-s', '-e']
        length = len(master_list)
        locc = master_list[0]
        thetruthtables = False

        ## checks to see if first command is -r
        if length > 2 and master_list[1] == list1[2] or master_list[1] == list1[3]:
            if master_list[2] != list1[0] or master_list[2] != list1[1]:
                thetruthtables = True
            else:
                thetruthtables = False
        if length > 2 and master_list[1] != list1[2] or master_list[1] != list1[3] or master_list[1] != list1[1]:
            if master_list[1] != list1[0]:
                pass
            else:
                thetruthtables = True
        if length == 2:
            if master_list[1] in list1:
                thetruthtables = True
            else:
                print('ERROR')


        if thetruthtables == True:
            ## checks to see if the input is valid
            if master_list[1] in list1:
                ## tests for r
                if master_list[1] == list1[0]: 
                    if length == 2:
                        r(master_list, locc, 1)
                    if length == 3:
                        if master_list[2] == list1[1]:
                            ## tests for f after the r
                            if master_list[2] == list1[1]:
                                r(master_list, locc, 2) 
                        else:
                            print('ERROR')
                    if length == 4:
                        if master_list[2] == list1[2] or master_list[2] == list1[3]:
                            ## tests for s after the r
                            if master_list[2] == list1[2]: 
                                r(master_list, locc, 3)
                            ## tests for e after the r
                            if master_list[2] == list1[3]:
                                r(master_list, locc, 4)
                        else:
                            print('ERROR')
                ## tests for f
                if master_list[1] == list1[1]:
                    F(master_list)
                ## tests for s
                if master_list[1] == list1[2]:
                    S(master_list)
                ## tests for e
                if master_list[1] == list1[3]: 
                    E(master_list)
    else:
        pass
    return 
    pass


    pass

def getting_input_for_op():
    x = input()
    main(x)

def main(initial_input):
    global user1

    function_being_called  = initial_input[0:2].strip().upper()
    master = ['l', 'L', 'C', 'D', 'R', 'Q', 'O', 'E', 'P']
    a1_stuff = ['l', 'L', 'C', 'D', 'R', 'Q', 'O']
    a2_stuff = ['E', 'P']
    list_L = ['l', 'L']
    list_C = ['c', 'C']
    thetruthtables = True
    print(function_being_called)
    if function_being_called.upper() not in master:
        print('ERROR')
    if function_being_called.upper() in a2_stuff:
        if loaded == True:
            if function_being_called == 'E':
                Edit(initial_input, user1)
            elif function_being_called == 'P':
                P(initial_input, user1)
        else:
            print('ERROR')
    if function_being_called.upper() in a1_stuff:
        if ' -' in initial_input:
            if function_being_called in list_L:
                masterr = input_seperator_norm(initial_input)
            if function_being_called in list_C: ### ho do dis
                masterr1 = input_seperator_dif(initial_input)
            if function_being_called.upper() == "Q":
                thetruthtables = False
            elif function_being_called.upper() == "L":
                branches(masterr)
            elif function_being_called.upper() == 'C':
                user1 = C(masterr1)
            else:
                print('ERROR')
        else:
            if function_being_called.upper() == 'D':
                D(initial_input)
            elif function_being_called.upper() == 'R':
                R(initial_input)
            elif function_being_called.upper() == list_L[1]:
                simple(initial_input)
            elif function_being_called == 'O':
                a2_thing = sorter(initial_input)
                user1 = O(a2_thing)
            elif function_being_called == "Q" or function_being_called == "q":
                thetruthtables = False
            elif loaded:
                pass
            else:
                print('ERROR')
    
    
    if thetruthtables:
        if op:
            getting_input_for_op()
        else:
            start()

def start():
    global questions
    global op
    inital = starting()
    if type(inital) == list:
        inital = inital[0]
        questions = False
        op = True
    else:
        questions = True
        op = False
    main(inital)

if __name__ == "__main__":
    global loaded ## if loaded in or not
    loaded = False

    global user1 ## not really sure what this does OH WIAT ITS THE PROFILE OBJ
    user1 = None

    global full_name ## directory
    full_name = None

    global num # num.
    num = 0

    global questions
    questions = True

    global op
    op = None

    global edits
    edits = None
    start()
# c:\users\andyh\Testing
## c:\users\andyh\desktop\myjournal.dsu
# NAME Andrew Z. Ho
# EMAIL andrewzh@uci.edu
# STUDENT ID 11211101
