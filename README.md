Assignment 2: Journal

This assignment includes the following starter files:

* __a2.py__: Use this file as the main module for your program.
* __input_processor.py__: Use this file for your user interface module.
* __Profile.py__: Use this file to manage saving and loading of user data. Do not edit.

Please visit the course website for a detailed overview of the assignment.

Assignment 2: Journal
Introduction
The goal for assignment 1 was to learn how to work with the Python Standard Library, use recursion, and start to familiarize yourself with error handling. If you were able to complete all of the requirements for assignment 1, you should now have a fully functional command line program that allows you to find, create, read, and delete files on your computer.

Though useful, so far your program doesn’t offer any functionality that is not available from existing command line tools already on your computer. So for assignment 2, you are going to extend your a1 code to enable a user to capture their thoughts by writing journal posts and storing them in a text file. You will use the features that you implemented in a1 to provide the basic file management and user interface aspects of your new program while you add new features to support basic journaling and journal management functionality.

Summary of Program Requirements
Manage user data using a file store

Design a command line user interface

Implement a custom file format using JSON (Javascript Object Notation)

Learning Goals
Working with modules

Integrate existing code into your program

Improving error handling

Working with JSON

Program Requirements
Unlike the previous assignment, you will have a lot more flexibility in how you design your program’s user interface. You will not receive a validity checker for this assignment, so the input and output of your program is largely up to you. However, there are some conditions:

You must divide your program into at least two modules, not including the Profile module that is provided in the starter code. Your modules should be named and loosely modeled after the descriptions below.

a2.py: Your first module will be the entry point to your program.

ui.py: A module that is responsible for processing all commands in the official input command format (see next item).

You must retain the input command format for any new commands your program may need, which if you recall looks like this:

[COMMAND] [INPUT] [[-]OPTION] [INPUT]
You must use the Profile.py module that accompanies this assignment without modification (more on that below).

You must support the ability to enter an “admin” mode when your program starts. The admin mode should function similarly to assignment 1, where instead of a user interface the user can enter any supported command according to the input command format used for in this course.

All modules that you edit must include the following comment on the first three lines:


# NAME
# EMAIL
# STUDENT ID

Otherwise, you are free to design your program any way you like. This means if you would like to provide more helpful feedback after error conditions, for example, you are free to do so.

The program you will be creating is divided into two parts. Start by reading through both parts so that you have a clear picture of what the complete program should do, then focus on completing part 1 first. Ensure that part 1 is reliably working before continuing on to part 2.

Note

A good approach to ensuring reliability is by writing your own tests!

Part 1: Extending A1
Your program should extend the C (create) command from a1. However, now when a user enters the C command, your program should create a new file and automatically append it with the extension (or suffix) .dsu (we will learn more about why it’s called ‘dsu’ in the next assignment). The use of the C command should also prompt the user using the input function to collect the following data:

username: a unique name to associate the user with posts.

password: a password to protect access to user journal entries.

bio: a brief description about the user.

The collected data should be contained in a Profile object while the user is running the program and saved to the file system when the program exits (though, saving can and should occur whenever data is changed). The Profile module has built-in functionality for saving data stored in a Profile object, all you have to do is supply the filename collected from the user (e.g., specified by the C command or collected from an input) as a parameter to the save_profile method.

Program Feature

Extend the ‘C’ create DSU file command to collect profile information about the user and store the profile information using the Profile module.

Once implemented, a user should be able to enter the following command into your program and start using it to write journal entries (“myjournal” is the journal name chosen by your user).

C c:\users\mark -n myjournal
When the input command above is entered into your program it should respond by performing the data collection discussed earlier. This is your opportunity to design your own user interface, so we will not provide any examples here!

At this point, your program should allow a user to search for and load a DSU file using the input command conventions established in a1 and the new features you have added to the C command. But what happens when a user wants to use an existing DSU file? To support the use of existing files, you will need to add code for loading a DSU file.

As you might recall, in a1 you performed a very similar operation when you implemented the ‘R’ command. We don’t want to change the behavior of the ‘R’ command, as there may be conditions in which a user might like to check the contents of a DSU file before loading it. Therefore, you will need to add a new input command to support loading an existing DSU file. Conceptually we can think of the task as ‘opening’ a file, similar to how you might open a docx file in Microsoft Word, so let’s use the input command O for ‘Open’:

Program Feature

Add new command to user interface to support loading DSU files.

O - Open an existing file of the type dsu

When implemented, a user should be able to enter the following command into your program and start using the program to write journal entries.

O c:\users\mark\myjournal.dsu
Since you already have collected the required user data (username, password, bio), you do not need to add any additional input functions for this feature. However, you might consider adding some type of output to the user that the requested DSU file has been successfully loaded. For example, you might print a simple confirmation message or you might print a message that outputs the username, password, and bio associated with the DSU file. It’s up to you.

Part 2: Managing Data with the Profile Module
You must use the Profile module that is included in your starter code to store the data you collect from the user. The Profile module has two primary functions:

Provides properties to store user input.

Provides encode and decode functions to support saving profile data to a DSU file using the JSON format.

We will not be explicitly covering the functionality of the Profile module in class. To understand how to use it, you will be required to learn the module on your own by reviewing its code, code comments, and discussion with the class. Don’t worry, the module is well documented and includes code snippets that demonstrate how each class method should work.

A good starting place to understand how the Profile module works is to create a test file that imports the module. Write some sample code using the two classes available to you in the module. You are free to share any sample tests you write with your classmates on Zulip.

Here are a few tasks you might try in your test program:

Create a new Profile object and save it.

Open an existing Profile file (created in previous task).

Add username and password to Profile object, save the object, check the DSU file to confirm.

Create a Post and add it to a Profile object, save the object, check the DSU file to confirm.

Code Reading Tip

Asking questions and working with others is a critical component to becoming a successful programmer. So rather than tell you exactly how to use the Profile class, I want you to help each other figure it out. Although you are not allowed to share the code you write for this assignment with each other, you are allowed to share what you learn about the Profile module. My only requirement is that you do so publicly using the a2-qa channel in Zulip. We will keep an eye on conversation and make sure you are all headed in the right direction.

Once you have a good understanding of how the Profile module works you are ready to implement the required features in your program. So far you have created the ability to create or open a DSU file. Next you will need to introduce some editing capability so that your users can store data in their journal.

Program Feature

Add new command to user interface to support editing a DSU file.

E - Edit the DSU file loaded by C or O commands

The edit command will be used in combination with the different options supported by the Profile module.

Program Feature

Add new command to user interface to support editing a DSU file.

-usr [USERNAME]

-pwd [PASSWORD]

-bio [BIO]

-addpost [NEW POST]

-delpost [ID]

Your program should support either one option at a time or any combination of options for a single print command.

Finally, a user should always be able to review the contents of their journal. To support this feature, you will create one final command for printing the data that has been stored in a DSU file.

Program Feature

Add new command to user interface to support printing data in a DSU file.

P - Print data in the DSU file loaded by C or O commands

The print command will be used in combination with the different options supported by the Profile module.

Program Feature

Add new command options to user interface to support printing a DSU file.

-usr Prints the username stored in the profile object

-pwd Prints the password stored in the profile object

-bio Prints the bio stored in the profile object

-posts Prints all posts stored in the profile object with id (using list index is fine)

-post [ID] Prints post identified by ID

-all Prints all content stored in the profile object

Like the E command, your program should support either one option at a time or any combination of options for a single print command. When all program features have been implemented, the following code should run in your program:


# create a new journal called 'myjournal' (could also use O for existing file)
C c:\users\mark -n myjournal

# add a username and password to 'myjournal'
E -usr "mark b" -pwd "password123"

# add a bio to 'myjournal'
E -bio "Hi my name is Mark, this is my bio."

# add a post to 'myjournal'
E -addpost "Hello, this is my first post!"

# print the contents of 'myjournal'
P -all

# print all posts stored in 'myjournal'
P -posts

# print single post by id stored in 'myjournal'
P -post 1

# delete a post in 'myjournal' by id
E -delpost 1

Note

For the E and P commands, any combination of options is valid. So for example, a single E command can contain all available options in a single input.

Part 3: The User Interface
“User interface” is a term used to describe the inputs and outputs that a person can use to interpret and control your program. In Python, a simple user interface can be programmed using the input and print functions. You created a user interface for assignment 1, but you were required to follow a very specific set of rules for both input and output. Although your program did have an interface it was not very user friendly. A user was required to know how to write input commands without any help from the program.

For this assignment we will be loosening control quite a bit and allow you to create your own custom input and output. This means that you will create a friendly user interface that informs users how to interact with your program. Your user interface should provide prompts that clearly instruct the user on how to use your program. A good place to start is with a printed menu that lists the various input options that your program understands. You might find it helpful to write out your program flow on paper first, then write the code to implement what you have written.

Ultimately, how you decide to create your interface is up to you, but it should replace the difficult to use input commands with some type of friendly interaction. For example, the following replaces the C and L commands with an instructive prompt:

>>> Welcome! Do you want to create or load a DSU file (type 'c' to create or 'l' to load):
>>> l
>>> Great! What is the name of the file you would like to load?
>>> /path/to/my/file/MY_FILE_NAME.dsu
Which ever format you decide to use, remember, your program must still accept and handle the input command structure from a1 and Part 2 when in admin mode.

User Interface Requirements
As discussed, you are allowed to design your user interface however you like, but there are a few requirements that must also be met.

Admin Mode
You may be wondering how the input commands will work if you design a custom user interface. Well, you will support input commands by implementing an administrator mode. The entry point of your program should enter into administrator mode when receiving the user input admin. When in administrator mode your user interface should be disabled so that your program only responds to input commands. So building on an earlier example, the following output should work in your program:

 > Welcome! Do you want to create or load a DSU file (type 'c' to create or 'l' to load): admin
 > 
Notice that if the keyword admin is entered, even if it is not one of the options required by the input, the program falls back to input command functionality. In admin mode, a user could enter any of the input commands required for this assignment and expect to see only the output generated by the input command. So, in the case of the print command, your program should print the desired output according to the command option. For other commands, like edit or open, any custom print output that you have created can continue to function normally. The only difference is that in admin mode your program no longer needs to ask the user for input.

Note

When in admin mode, your program MUST NOT print any messages using the input() function! You can, however, still print messages using print().

Some Additional Considerations
Usernames and passwords must not contain whitespace

If the user creates a new DSU file, but that file already exists, you should load the file instead

If the user exits program before data collection is complete, do not create a file

If the user attempts to load a file that is not in a valid DSU file format, this is an error

Any user input that is an empty string or whitespace should not be added to a file

When processing the E command, if one option has an error, you should stop the operation rather than continue processing options

E commands should support both single and double quotes for relevant options

Preparing for Submission
As this program will be growing in complexity for the rest of the quarter, you should start getting used to writing tests. A good place to start is to ensure that your program is properly loading and saving profile data after it has been supplied by the user. Here are a few additional conditions to consider (HINT: the autograder will likely test these!):

Create a file using an existing file name

Open file that does not exist

Open dsu file that does not follow the Profile format

Starter Project
Assignment 2 Starter Repository

How we will grade your submission
This assignment will be graded on a 150 point scale, with the 150 points being allocated completely to whether or not you submitted something that meets all of the above requirements. The following rubric will be used:

Requirements and Function | 100 pts
Does the program do what it is supposed to do?

Does the ui.py module function independently of the rest of the program?

Are there any bugs or errors?

Module Usage | 30 pts
Are all required modules named and used as specified?

Quality and Design | 20 pts
Is the code well designed?

Is the code clearly documented?

Now that you have successfully completed on large program, we will start to look at the quality and design criteria a little more closely. If you have not been putting time into organizing and documenting your code, now is a good time to start.
