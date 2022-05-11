import time, pickle

listexample = []
filename = open("notebook.dat","wb") #No default notebook was found, created one.

pickle.dump(listexample,filename)
filename.close()

status = True
while status:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Edit a note")
    print("(4) Delete a note")
    print("(5) Save and quit")
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
        sourcefile = open("notebook.dat","wb")
        addedtext = input("Write a new note: ")
        notetime = time.strftime("%X %x")
        finaltext = addedtext + ":::" + notetime
        pickle.dump(finaltext, sourcefile)
        sourcefile.close()
    elif user_selection == 3:
        print("Notes deleted.")
        sourcefile = open("notebook.txt", "w")
        sourcefile.close()
    elif user_selection == 4:
        print(f"The list has {len(listexample)} notes.")
        deletednote = int(input("Which of them will be deleted?: "))
        if deletednote < 0  or deletednote > (len(listexample) - 1):
            print("Incorrect selection.")
            continue
        else:
            print("Deleted note", listexample.pop(deletednote) +  ":::", time.strftime("%X %x"))

        sourcefile = open("notebook.txt", "w")
        sourcefile.close()
    elif user_selection == 5:
        print("Notebook shutting down, thank you.")
        status = False
        break
    
		

