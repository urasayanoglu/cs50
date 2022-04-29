status = True
while status:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit")
    try:
        user_selection = int(input("Please select one: "))
    except ValueError:
        print("Incorrect selection")
    if user_selection == 1:
        sourcefile = open("notebook.txt", "r")
        content = sourcefile.readlines()
        for i in content:
            print(i[:-1])
        sourcefile.close()
    elif user_selection == 2:
        sourcefile = open("notebook.txt", "a")
        addedtext = input("Write a new note: ")
        sourcefile.write(addedtext + "\n")
        sourcefile.close()
    elif user_selection == 3:
        print("Notes deleted.")
        sourcefile = open("notebook.txt", "w")
        sourcefile.close()
    elif user_selection == 4:
        print("Notebook shutting down, thank you.")
        status = False
        break
    
		

