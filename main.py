# Import Statements
from pyswip import Prolog

# Global Variables
PROLOG = Prolog()
DEBUG = False
VALID_MACHINES = ["stone", "plank", "stick", "redstoneTorch", "comparator"]
QUIT_WORDS = ["", "exit", "close", "quit"]


def prologInitialize():
    if DEBUG:
        print("function prologInitialize() begins")

    # Initial facts for the Knowledge Base (KB)
    PROLOG.assertz("raw(redstone)")
    PROLOG.assertz("raw(log)")
    PROLOG.assertz("raw(quartz)")
    PROLOG.assertz("raw(cobblestone)")
    PROLOG.assertz("raw(stick)")
    PROLOG.assertz("notRaw(Item) :- not(raw(Item))")
    PROLOG.assertz("composedOf(stone, cobblestone, 1)")
    PROLOG.assertz("composedOf(redstoneTorch, redstone, 1)")
    PROLOG.assertz("composedOf(redstoneTorch, stick, 1)")
    PROLOG.assertz("composedOf(comparator, redstoneTorch, 3)")
    PROLOG.assertz("composedOf(comparator, quartz, 1)")
    PROLOG.assertz("composedOf(comparator, stone, 3)")
    PROLOG.assertz("composedOf(stick, plank, 0.5)")
    PROLOG.assertz("composedOf(plank, log, 0.25)")
    PROLOG.assertz("rawComposition(Item, Component, Qty) :- composedOf(Item, Component, Qty), raw(Component)")
    PROLOG.assertz("rawComposition(Item, Subcomponent, TotalQty) :- composedOf(Item, Component, Qty), notRaw(Item), rawComposition(Component, Subcomponent, SubQty), TotalQty is Qty * SubQty")
    #PROLOG.assertz("")
    #PROLOG.assertz("")
    #PROLOG.assertz("")
    #PROLOG.assertz("")
    #PROLOG.assertz("")
    #PROLOG.assertz("")


    
def prologQuery(finalResources):
    if DEBUG:
        print("function prologQuery() begins")

    # Create query for KB
    query = "rawComposition(comparator, X, Y)"

    # Search KB
    for result in PROLOG.query(query):
        # Store value in finalResources

        # If the key isn't initialized
        if result["X"] not in finalResources:
            finalResources[result["X"]] = result["Y"]
        
        # If the key is already initialized
        else:
            finalResources[result["X"]] = result["Y"] + finalResources[result["X"]]

    # Backup of different methods to query prolog
    #result = list(PROLOG.query(query))
    #print(result)
    #print("result type is:")
    #print(type(result))




##########
# INPUT VALIDATION
##########

def intInput(prompt, minInt, maxInt):
    if DEBUG:
        print("function intInput() begins")

    userInput = minInt - 1

    while True:
        print(prompt, end="")
        userInput = input()
        try:
            userInput = int(userInput)
        except:
            print("Entry must be a whole number.\n")
            continue
        if userInput < minInt:
            print("Sorry, minimum value is " + str(minInt) + "\n")
            continue
        elif userInput > maxInt:
            print("Sorry, maximum value is " + str(maxInt) + "\n")
            continue
        break
    return userInput


def stringInput(prompt, minLength, maxLength):
    if DEBUG:
        print("function stringInput() begins")

    userInput = ""

    while True:
        print(prompt, end="")
        userInput = input()
        try:
            userInput = str(userInput)
        except:
            print("Sorry, it looks like that wasn't a valid entry. Please try again.\n")
            continue
        if userInput == "":
            print("Entry cannot be blank\n")
            continue

        elif len(userInput) < minLength:
            print("Sorry, minimum number of characters is " + str(minLength) + "\n")
            continue

        elif len(userInput) > maxLength:
            print("Sorry, maximum number of characters is " + str(maxLength) + "\n")
            continue
        break
    return userInput

##############################
# WIP
##############################

##############################
# USER QUERY
##############################

def getUserQuery():
    if DEBUG:
        print("function getUserQuery() begins")

    # Variables to hold results
    finalResources = {}         # Dictionary to tabulate all resources needed
    finalProcedure = []         # List to document steps for player to follow
    '''
    #farmCutoff = {}             # Amount of resources where a farm will be recommended (instead of gathering manually)
    #^ do this in prolog

    # Initialize any preexisting resources
    #finalResources["redstone"] = 15

    # Initialize any preexisting procedures
    #finalProcedure.insert(0, "Get money")
    #finalProcedure.insert(0, "Fuck bitches")
    '''

    # Get User Query

            ##### WIP #####

    # Query KB
    #prologQuery(finalResources)


    # Build Procedure

            ##### WIP #####


    # Display Results
    print("\nfinalResources is:")
    print(finalResources)
    print("finalProcedure is:")
    print(finalProcedure)





##############################
# MAIN MENU
##############################

def displayMainMenu():
    if DEBUG:
        print("function displayMainMenu() begins")

    print("________________")
    print("\nMain Menu\n")
    print("1. Search Knowledge Base")
    print("2. WIP")
    print("3. Exit\n")


# Main program loop
def main():
    if DEBUG:
        print("function main() begins")

    # Initialize knowledge base
    prologInitialize()

    # Main Menu
    userSelection = -1
    prompt = "Your selection: "
    while userSelection != 3:
        displayMainMenu()
        userSelection = intInput(prompt, 1, 3)

        if userSelection == 1:
            getUserQuery()
        
        elif userSelection == 2:
            print("\n\nThis section is a work in progress - more to come!\n\n")
        
        elif userSelection == 3:
            break

    print("\n\nThank you for using this program!\n\n")



if __name__ == "__main__":
    main()
