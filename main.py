# Import Statements
from pyswip import Prolog

# Global Variables
PROLOG = Prolog()
DEBUG = False
VALID_MACHINES = ["stone", "plank", "stick", "redstonetorch", "comparator", "witchfarm"]
QUIT_WORDS = ["", "4", "exit", "close", "quit"]
MAX_STRING_LENGTH = 99


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
        '''
        if userInput == "":
            print("Entry cannot be blank\n")
            continue
        '''

        if len(userInput) < minLength:
            print("Sorry, minimum number of characters is " + str(minLength) + "\n")
            continue

        elif len(userInput) > maxLength:
            print("Sorry, maximum number of characters is " + str(maxLength) + "\n")
            continue
        break
    return userInput


##########
# PROLOG
##########


##############################
# WIP
##############################
def prologInitialize():
    if DEBUG:
        print("function prologInitialize() begins")

    # Initial facts for the Knowledge Base (KB)

    # Raw resources
    PROLOG.assertz("raw(redstone)")
    PROLOG.assertz("raw(log)")
    PROLOG.assertz("raw(quartz)")
    PROLOG.assertz("raw(cobblestone)")
    PROLOG.assertz("raw(stick)")
    PROLOG.assertz("raw(string)")

    PROLOG.assertz("notRaw(Item) :- not(raw(Item))")

    
    # Farm cutoffs for raw resources
    '''
    PROLOG.assertz("farmCutoff(redstone, 200)")
    PROLOG.assertz("farmCutoff(log, 400)")
    PROLOG.assertz("farmCutoff(quartz, 200)")
    PROLOG.assertz("farmCutoff(cobblestone, 1000)")
    PROLOG.assertz("farmCutoff(stick, 200)")
    PROLOG.assertz("farmCutoff(string, 64)")
    '''
    PROLOG.assertz("farmCutoff(redstone, 1)")
    PROLOG.assertz("farmCutoff(log, 1)")
    PROLOG.assertz("farmCutoff(quartz, 1)")
    PROLOG.assertz("farmCutoff(cobblestone, 1)")
    PROLOG.assertz("farmCutoff(stick, 1)")
    PROLOG.assertz("farmCutoff(string, 1)")

    # item composition
    PROLOG.assertz("composedOf(stone, cobblestone, 1)")
    PROLOG.assertz("composedOf(redstonetorch, redstone, 1)")
    PROLOG.assertz("composedOf(redstonetorch, stick, 1)")
    PROLOG.assertz("composedOf(comparator, redstonetorch, 3)")
    PROLOG.assertz("composedOf(comparator, quartz, 1)")
    PROLOG.assertz("composedOf(comparator, stone, 3)")
    PROLOG.assertz("composedOf(stick, plank, 0.5)")
    PROLOG.assertz("composedOf(plank, log, 0.25)")
    PROLOG.assertz("rawComposition(Item, Component, Qty) :- composedOf(Item, Component, Qty), raw(Component)")  # Returns raw components of an item
    PROLOG.assertz("rawComposition(Item, Subcomponent, TotalQty) :- composedOf(Item, Component, Qty), notRaw(Item), rawComposition(Component, Subcomponent, SubQty), TotalQty is Qty * SubQty") # Recursively calls subcomponents until a raw item is found

    # mats
    PROLOG.assertz("composedOf(plankslab, plank, 0.5)")
    PROLOG.assertz("composedOf(composter, plankslab, 7)")

    # Materials to create
    PROLOG.assertz("composedOf(witchfarm, composter, 10)")
    PROLOG.assertz("composedOf(witchfarm, string, 50)")

    # Drops from farm
    PROLOG.assertz("produces(witchfarm, redstone, 250)")
    PROLOG.assertz("produces(witchfarm, stick, 500)")
    PROLOG.assertz("produces(villagers, redstone, 100)")

    # witch farm effort
    PROLOG.assertz("effort(witchfarm, low)")
    #PROLOG.assertz("")
    #PROLOG.assertz("")
    #PROLOG.assertz("")

    #Witch Farm
    #
    # Resources it produces
    #   PRODUCES:   Redstone    250     per hour
    #   PRODUCES:   Sticks      250     per hour
    #   PRODUCES:   etc         ...     ...
    #
    # Resources to build it:
    #   RESOURCES:  Composters  10
    #   RESOURCES:  String      50
    #   RESOURCES:  etc         ...
    #           
    # Effort to build it:
    #   EFFORT:     low

############TO DO##########
############TO DO##########
############TO DO##########




    
def prologCompositionQuery(resources, userQuery):
    if DEBUG:
        print("function prologQuery() begins")

    # Build query for KB
    query = "rawComposition(" + userQuery + ", X, Y)"

    # Search KB
    for result in PROLOG.query(query):
        # Store value in finalResources

        # If the key isn't initialized
        if result["X"] not in resources:
            resources[result["X"]] = result["Y"]
        
        # If the key is already initialized
        else:
            resources[result["X"]] = result["Y"] + resources[result["X"]]

    # Backup of different methods to query prolog
    #result = list(PROLOG.query(query))
    #print(result)
    #print("result type is:")
    #print(type(result))


##############################
# USER QUERY
##############################

def getUserQuery():
    if DEBUG:
        print("function getUserQuery() begins")

    # Variables to hold results
    resourcesInProgress = {}    # Working list of all resources our algorithm must account for
    resourcesToGather = {}      # Resources the player should gather manually
    resourcesFinal = {}         # Dictionary to tabulate all resources needed
    procedureFinal = []         # List to document steps for player to follow
    '''
    #farmCutoff = {}             # Amount of resources where a farm will be recommended (instead of gathering manually)
    #^ do this in prolog

    # Initialize any preexisting resources
    #resourcesFinal["redstone"] = 15

    # Initialize any preexisting procedures
    #procedureFinal.insert(0, "Get money")
    #procedureFinal.insert(0, "Fuck bitches")
    '''

    # Get User Query
    userQueryInput = ""
    validInput = False
    prompt = "\nPlease enter a machine: "
    while validInput == False:
        # Get input from User
        userQueryInput = stringInput(prompt, 0, MAX_STRING_LENGTH)

        # Convert userInput to lower case
        userQueryInput = userQueryInput.lower()

        # Check if user wants to return to main menu
        if userQueryInput in QUIT_WORDS:
            print("\nReturning to main menu\n")
            return

        # Check user input a valid machine
        if userQueryInput in VALID_MACHINES:
            validInput = True
        else:
            print("Input needs to be a valid machine, please try again, or type QUIT to return to main menu ")

    # Query KB
    prologCompositionQuery(resourcesInProgress, userQueryInput)

    resourcesFinal = resourcesInProgress

            ##### WIP #####
            ##### WIP #####
            ##### WIP #####
            ##### WIP #####
            ##### WIP #####
            ##### WIP #####

    # Build Procedure               # need a resourcesInProgress variable to track in general, a list which gets reduced to zero over time, loop until it's empty
    while len(resourcesInProgress) > 0:
        for resource in resourcesInProgress:
            print(f"\nCurrently searching resource: ({resource})")
            ### Check min cutoffs
            amt = resourcesInProgress[resource]
            
            # Get cutoff
            cutoffQuery = f"farmCutoff({resource}, CutoffAmt)"

            # Query prolog for the cutoff amount
            for result in PROLOG.query(cutoffQuery):

                # If the amount is small, have user gather it manually
                if amt < result["CutoffAmt"]:
                    resourcesToGather.update({resource: amt})
                    print(f"Added ({resource}) to resourcesToGather")

            # Find all farms that produce this resource
            farmsList = {}
            farmQuery = f"produces(Farmname, {resource}, Amt)"
            farm = {}       # Variable to receive the result of the prolog query
            for farm in PROLOG.query(farmQuery):
                #print("Result of the query was:")
                #print(farm)
                farmsList.update({farm["Farmname"]:farm["Amt"]})

            # Handle exceptions where no farms can be found
            if len(farm) == 0:
                print(f"No farms listed for the resource: ({resource})")
                continue

            else:
                print(f"Found the following farms: {farmsList}")
                #print(farmsList)


            ### Evaluate which farm is best
            # Write down everything you EXPECT to put in here
            # Go farm by farm - do them one at a time
            suitabilityScore = {}
            for thisFarm in farmsList:                  # Currently farmsList is a dictionary where the keys are the name of the farm, the value is the rate it produces our given resource
                print(f"Analyzing farm: {thisFarm}")

                # Score variable to track analysis
                score = 0     

                # Get other resources produced by the farm
                allProduced = {}
                allProducedQuery = f"produces({thisFarm}, Resource, Amt)"
                for resultORQ in PROLOG.query(allProducedQuery):
                    allProduced.update({resultORQ["Resource"]:resultORQ["Amt"]})

                # Loop through otherResources
                for x in allProduced:
                    if x in resourcesInProgress:
                        score += allProduced[x]     # Add to the score if resource is necessary
                    else:
                        score += allProduced[x] / 10   # Non-essential products of the farm still count, but less valuable

                # Need to add/multiply a bunch of things together
                # Start with the 

                # Set suitability score for this farm
                suitabilityScore.update({thisFarm : score})
                print(f"Suitability score for {thisFarm} is {suitabilityScore[thisFarm]}")

            # Compare and rank suitability scores                

    ######## LAST WORKING HERE ##########################
    ######## LAST WORKING HERE ##########################
    ######## LAST WORKING HERE ##########################

            ### Add building the farm to Procedure

            ### Get resources needed to build the farm

            ### Add those resources to resourcesInProgress (purge any that are in a list of farmed resources)

        # Remove manually gathered resources from resourcesInProgress
        for x in resourcesToGather:
            del resourcesInProgress[x]
            print("resourcesInProgress is now:")
            print(resourcesInProgress)

        # Remove this break statement once you can reliably clear the resourcesInProgress dictionary
        break

            ##### WIP #####
            ##### WIP #####
            ##### WIP #####
            ##### WIP #####
            ##### WIP #####
            ##### WIP #####
            ##### WIP #####

    # Display Results
    print("\nThese are all the resources required:")
    print(resourcesFinal)
    print("\nUser should gather the following resources manually:")
    print(resourcesToGather)
    print("Suggested procedure to gather the remaining resources:")
    print("finalProcedure is:")
    print(procedureFinal)

##############################
# MAIN MENU
##############################

def displayMainMenu():
    if DEBUG:
        print("function displayMainMenu() begins")

    print("________________")
    print("\nMain Menu\n")
    print("1. Search Knowledge Base")
    print("2. List Valid Machines")
    print("3. WIP")
    print("4. Exit\n")


# Main program loop
def main():
    if DEBUG:
        print("function main() begins")

    # Initialize knowledge base
    prologInitialize()

    # Main Menu
    userSelection = -1
    prompt = "Your selection: "
    while userSelection != 4:
        displayMainMenu()
        userSelection = intInput(prompt, 1, 4)

        if userSelection == 1:
            getUserQuery()
        
        if userSelection == 2:
            print("\nValid Machines:")
            print(VALID_MACHINES)
        
        elif userSelection == 3:
            print("\n\nThis section is a work in progress - more to come!\n\n")
        
        elif userSelection == 4:
            break

    print("\n\nThank you for using this program!\n\n")


if __name__ == "__main__":
    main()