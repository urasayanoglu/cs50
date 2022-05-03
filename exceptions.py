status = True
while True:
    userinput = input("Give the file name: ")
    try:
        openedfile = open(userinput, "r")
        readfile = openedfile.read()
    except IOError:
        print("There seems to be no file with that name.")
    else: 
        try:
            conversedfile = int(readfile)
        except (TypeError, ValueError):
            print("The file contents were unsuitable.")
        except Exception:
            print("There was a problem with the program.")
        else:
            result = conversedfile / 1000
            print(f"The result was {result}")


