# Sistema de hotel para animais de estimação em Python.

import datetime

staffID = 'admin'
password = 'admin'

petName = []
petType = []
bookingID = []
roomID = []

boardedPets = []
history = []
roomInUse = []
roomToUse = []
roomRates = {'dogs':50, 'cats':45, 'birds':30, 'rodents':25}
dogcatRoomsAvailable = 60
birdRoomsAvailable = 80
rodentRoomsAvailable = 100
totalPriceStr = ""

# Login Function
# Requests user for staffID and password to gain access to the menu system
def loginFunction(s, p):
    # Login inputs
    staffID = input("Enter Staff ID: ")
    password = input("Password: ")

    # Check if staffID and password is correct;
    # If input is not valid, it informs user that ID and password is invalid and requests again
    loginTrust = False
    while (loginTrust is False):
        if (staffID == 'admin') and (password == 'admin'):
            print("Successfully logged in")
            loginTrust = True

        else:
            print("Wrong ID or Password. Please enter again. ")
            loginTrust = False
            staffID = input("Enter Staff ID: ")
            password = input("Password: ")

# Check In Function
# Allows user to check in customers' pets
def checkIn(petNm, petTy, bookID, roomuse):
    global dogcatRoomsAvailable
    global birdRoomsAvailable
    global rodentRoomsAvailable

    # Pet Name Input
    petName= input("Enter pet name: ")
    petNm.append(petName)

    #Pet Type Input
    petType= input("\n'Dog', 'Cat', 'Bird', 'Rodent'\n Enter pet type: ")

    # Check if petType is valid
    petTyCheck = False
    while petTyCheck == False: 
        if (petType.lower() == 'dog' or petType.lower() == 'cat' or petType.lower() == 'bird' or petType.lower() == 'rodent'):
            # Check if rooms are still available
            if (dogcatRoomsAvailable != 0):
                petTy.append(petName)
                petTyCheck = True
            elif (birdRoomsAvailable != 0): 
                petTy.append(petName)
                petTyCheck = True
            elif (rodentRoomsAvailable != 0): 
                petTy.append(petName)
                petTyCheck = True
            else: 
                print("Rooms for dogs & cats are not available anymore. ")
                print(boardedPets)
                petTyCheck = True
                FrontDeskMenu()
        else: 
            print("Pet type must be only from the list")
            petTyCheck = False
            petType= input("\n'Dog', 'Cat', 'Bird', 'Rodent'\n Enter pet type: ")

    # Check In Date Allocators 
    checkInDate = datetime.datetime.now()
    cIdString = str(checkInDate)
    bookingID = str(cIdString[0:4] + cIdString[5:7] + cIdString[8:10] + cIdString[11:13] + cIdString[14:16] + cIdString[17:19])
    bookID.append(bookingID)

    # Check Out Date Default
    checkOutDate = 'Nil'

    # Room Allocators
    # Pet type input
    print("\nRules when assigning rooms: \nFor dogs: 'D' + any numbers \nFor cats: 'C' + any numbers \nFor birds: 'B' + any numbers \nFor rodents: 'R' + any numbers")
    print("Remember to insert letter and number plates in front of the kennel after bring the pets in! ")
    roomToUse = input('\nAssign a room for the pet: ')
    roomCheck = False
    rIU = roomToUse[0]
    print(rIU)

    # Check if rooms are assigned accordingly for the animal
    if (petType.lower() == 'dog'):
            # Check if input starts with 'D' and is not in use
            while roomCheck == False: 
                if (rIU.lower() == 'd' and (roomInUse.count(roomToUse.upper()) == 0)):
                    roomInUse.append(roomToUse.upper())
                    dogcatRoomsAvailable = dogcatRoomsAvailable - 1
                    print("Rooms left: ", dogcatRoomsAvailable)
                    roomCheck = True

                # If input does not start with 'D'
                elif (rIU.lower() != 'd'): 
                    print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'D'. ")
                    roomCheck = False
                    roomToUse = input('Assign a room for the pet: ')
                    rIU = roomToUse[0]

                # If room is in use
                elif (roomInUse.count(roomToUse.upper()) != 0): 
                    print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'D'. ")
                    roomCheck = False
                    roomToUse = input('Assign a room for the pet: ')
                    rIU = roomToUse[0]
                else: 
                    None


    if (petType.lower() == 'cat'):
            # Check if input starts with 'C' and is not in use
        while roomCheck == False: 
            if (rIU.lower() == 'c' and (roomInUse.count(roomToUse.upper()) == 0)):
                roomInUse.append(roomToUse.upper())
                dogcatRoomsAvailable = dogcatRoomsAvailable - 1
                print("Rooms left: ", dogcatRoomsAvailable)
                roomCheck = True

                # If input does not start with 'C'
            elif (rIU.lower() != 'c'): 
                print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                roomCheck = False
                roomToUse = input('Assign a room for the pet: ')
                rIU = roomToUse[0]

                # If room is in use
            elif (roomInUse.count(roomToUse.upper()) != 0): 
                print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                roomCheck = False
                roomToUse = input('Assign a room for the pet: ')
                rIU = roomToUse[0]
            else: 
                None

    if (petType.lower() == 'bird'):
            # Check if input starts with 'C' and is not in use
        while roomCheck == False: 
            if (rIU.lower() == 'b' and (roomInUse.count(roomToUse.upper()) == 0)):
                roomInUse.append(roomToUse.upper())
                birdRoomsAvailable = birdRoomsAvailable - 1
                print("Rooms left: ", birdRoomsAvailable)
                roomCheck = True

                # If input does not start with 'C'
            elif (rIU.lower() != 'b'): 
                print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                roomCheck = False
                roomToUse = input('Assign a room for the pet: ')
                rIU = roomToUse[0]

                # If room is in use
            elif (roomInUse.count(roomToUse.upper()) != 0): 
                print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'C'. ")
                roomCheck = False
                roomToUse = input('Assign a room for the pet: ')
                rIU = roomToUse[0]
            else: 
                None

    if (petType.lower() == 'rodent'):
            # Check if input starts with 'R'
        while roomCheck == False: 
            if (rIU.lower() == 'r' and (roomInUse.count(roomToUse.upper()) == 0)):
                roomInUse.append(roomToUse.upper())
                rodentRoomsAvailable = rodentRoomsAvailable - 1
                print("Rooms left: ", rodentRoomsAvailable)
                roomCheck = True

                # If input does. not start with 'R'
            elif (rIU.lower() != 'r'): 
                print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'R'. ")
                roomCheck = False
                roomToUse = input('Assign a room for the pet: ')
                rIU = roomToUse[0]

                # If room is in use
            elif (roomInUse.count(roomToUse.upper()) != 0): 
                print("Room Number is either invalid or the room may be in use. Make sure the first letter starts with a 'R'. ")
                roomCheck = False
                roomToUse = input('Assign a room for the pet: ')
                rIU = roomToUse[0]
            else: 
                None

    # Put information into boardedPets
    boardedPets.append([bookingID, petName.title(), petType.title(), cIdString, roomToUse.title(), checkOutDate])
    print(boardedPets)
    print(roomInUse)
    print(len(roomInUse))
    print(petName)

    # Call back the menu after finishing task
    FrontDeskMenu()


def CheckOut(): 
    # Requests for bookingID to checkout
    cObid = str(input("Please enter booking ID: "))
    counter = 0
    outCheck = False
    # Misc
    cBidLenC = [cObid[i:i+1] for i in range(0, len(cObid), 1)]
    print(cBidLenC)
    boardNum = len(boardedPets)
    print("Boarded pets left: ", boardNum)

    # Check out date to be assigned
    checkOutDate = datetime.datetime.now()
    cOdString = str(checkOutDate)

    if (len(cBidLenC) > 14):
        print("Invalid booking ID")
        cObid = str(input("Please enter booking ID: "))
    elif (len(cBidLenC) < 14):
        print("Invalid booking ID")
        cObid = str(input("Please enter booking ID: "))
    elif (len(cBidLenC) == 14): 
        print("Correct booking ID: ")

        # Check out the pets 
        # Remove pet to check out from boardedPets list
        # Insert the pet into history list
        while outCheck == False:
            for e in boardedPets: # for each list in boardedpets
                print('xyz')
                for element in e: # for each element in list
                    print('abc')

                    if cObid in element:
                        print('qwe')

                        # Payment
                        checkInDay = int(e[3][8:10])
                        checkOutDay = int(cOdString[8:10])
                        daysStayed = checkOutDay - checkInDay

                        if (e[2] == 'Dog'): 
                            # Assume same day checkout rate is also the rate of one day
                            if (daysStayed == 0):
                                totalPrice = roomRates['dogs'] * daysStayed + roomRates['dogs']
                                print("Total days stayed: ", daysStayed)
                                print("Total: ", totalPrice)
                                totalPriceStr = ("$" + str(totalPrice))
                            elif (daysStayed >= 1):
                                totalPrice = roomRates['dogs'] * daysStayed
                                print("Total days stayed: ", daysStayed)
                                print("Total price: $", totalPrice)

                        elif (e[2] == 'Cat'): 
                            # Assume same day checkout rate is also the rate of one day
                            if (daysStayed == 0):
                                totalPrice = roomRates['cats'] * daysStayed + roomRates['cats']
                                print("Total days stayed: ", daysStayed)
                                print("Total: ", totalPrice)
                                totalPriceStr = ("$" + str(totalPrice))
                            elif (daysStayed >= 1):
                                totalPrice = roomRates['birds'] * daysStayed
                                print("Total days stayed: ", daysStayed)
                                print("Total price: $", totalPrice)

                        elif (e[2] == 'Bird'): 
                            # Assume same day checkout rate is also the rate of one day
                            if (daysStayed == 0):
                                totalPrice = roomRates['birds'] * daysStayed + roomRates['birds']
                                print("Total days stayed: ", daysStayed)
                                print("Total: ", totalPrice)
                                totalPriceStr = ("$" + str(totalPrice))
                            elif (daysStayed >= 1):
                                totalPrice = roomRates['birds'] * daysStayed
                                print("Total days stayed: ", daysStayed)
                                print("Total price: $", totalPrice)

                        elif (e[2] == 'Rodent'): 
                            # Assume same day checkout rate is also the rate of one day
                            if (daysStayed == 0):
                                totalPrice = roomRates['rodents'] * daysStayed + roomRates['rodents']
                                print("Total days stayed: ", daysStayed)
                                print("Total: ", totalPrice)
                                totalPriceStr = ("$" + str(totalPrice))
                            elif (daysStayed >= 1):
                                totalPrice = roomRates['rodents'] * daysStayed
                                print("Total days stayed: ", daysStayed)
                                print("Total price: $", totalPrice)            

                        # Data manipulations
                        outCheck = True
                        e.pop(5) 
                        e.insert(5, cOdString) 
                        e.append(totalPriceStr)

                        history.append(e)
                        boardedPets.pop(counter)
                        print("Checked out. Remaining: ", len(boardedPets))
                        print(boardedPets)
                        print("History length: ", len(history))
                        print(history)

                counter += 1
    if outCheck == True:
        print("Finished checkout. ")
    else:
        print("Booking ID not found. Please enter again. ")
        cObid = str(input("Please enter booking ID: "))


    # Call back the menu after finishing task
    FrontDeskMenu()

# Room Availability 
# Check for availability of rooms
def roomAvailability(): 
    print("\nRoom Availability\n")

    print("Dogs: ", dogcatRoomsAvailable)
    print("Birds: ", birdRoomsAvailable)
    print("Rodents: ", rodentRoomsAvailable)

    FrontDeskMenu()

# History function
# Reads history of pets boarded
def History():
    print(history)
    FrontDeskMenu()

# Search function
# note: the booking ID is ALWAYS sorted
def SearchFunction(): 
    boardedIDList = []
    count = 0

    search = str(input("Enter booking ID: "))

    while (count < len(boardedPets)):
        bc = boardedPets[count][0]
        boardedIDList.append(bc)
        count = count + 1

    search = ("Enter booking ID: ")
    for el in boardedIDList: 
        print(el)

    print(boardedIDList)
    FrontDeskMenu()
# Menu
# Menu used for calling functions
def FrontDeskMenu():
    print("\nTaylor's Pet Hotel\nFront Desk Admin")
    print("A. Check in pets")
    print("B. Check out pets")
    print("C. Rooms Availability")
    print("D. History")
    print("E. Binary Search")
    print("F. Exit\n")

    # Input for calling functions
    userInput = input("What would you like to do today?: ")

    # Check if userInput is valid; if input is not valid, it continues to ask for a valid input
    inputCheck = False
    while (inputCheck is False):
        # Checks userInput and exccute function as requested by user
        if (userInput.lower() == 'a'):
            checkIn(petName, petType, bookingID, roomInUse)
            inputCheck = True
        elif (userInput.lower() == 'b'):
            CheckOut()
            inputCheck = True
        elif (userInput.lower() == 'c'): 
            roomAvailability()
            inputCheck = True
        elif (userInput.lower() == 'd'): 
            History()
            inputCheck = True
        elif (userInput.lower() == 'e'): 
            SearchFunction()
            inputCheck = True
        elif (userInput.lower() == 'f'):
            quit()
        else: 
            print("Invalid value! Please try again.")
            userInput = input("What would you like to do today?: ")
            inputCheck = False


loginFunction(staffID, password)
FrontDeskMenu()
print(boardedPets)