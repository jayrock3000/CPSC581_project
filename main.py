# Import Statements
from pyswip import Prolog

# Global Variables
PROLOG = Prolog()
DEBUG = False
VALID_MACHINES = ["stone", "plank", "stick", "redstonetorch", "comparator", "witchfarm"]
QUIT_WORDS = ["", "3", "exit", "close", "quit"]
MAX_STRING_LENGTH = 99
EFFORT_CONVERSION = {"verylow" : 1, "low" : 3, "medium" : 5, "high" : 7, "veryhigh" : 9}


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
    PROLOG.assertz("raw(emerald)")
    PROLOG.assertz("raw(villager)")

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
    PROLOG.assertz("farmCutoff(quartz, 100)")
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
    PROLOG.assertz("composedOf(villagerfarm, villager, 2)")

    # Drops from farm
    PROLOG.assertz("produces(witchfarm, redstone, 250)")
    PROLOG.assertz("produces(witchfarm, stick, 500)")
    PROLOG.assertz("produces(villagerfarm, redstone, 100)")
    PROLOG.assertz("produces(raidfarm, redstone, 1000)")
    PROLOG.assertz("produces(raidfarm, stick, 2000)")
    PROLOG.assertz("produces(raidfarm, emerald, 5000)")

    # Effort to build farm
    PROLOG.assertz("effort(witchfarm, verylow)")
    PROLOG.assertz("effort(villagerfarm, medium)")
    PROLOG.assertz("effort(raidfarm, veryhigh)")
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
    resourcesNeeded = {}        # Working list of all resources our algorithm must account for
    resourcesToGather = {}      # Resources the player should gather manually
    resourcesFinal = {}         # Dictionary to tabulate all resources needed
    resourcesFound = []
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
    prologCompositionQuery(resourcesNeeded, userQueryInput)
    resourcesFinal = resourcesNeeded

    # Add building the machine to the procedure
    procedureFinal.append(f"Build {userQueryInput}")

    # Build Procedure               # need a resourcesNeeded variable to track in general, a list which gets reduced to zero over time, loop until it's empty
    while True:
        addedResources = {}

        for resource in resourcesNeeded:
            print(f"\nCurrently searching resource: {resource}")

            if resource in resourcesFound:
                print(f"Skipping {resource}, farm already recommended")
                continue

            # Check if the needed amount exceeds the farm cutoff
            amt = resourcesNeeded[resource]
            
            # Get cutoff
            cutOffQuery = f"farmCutoff({resource}, CutoffAmt)"
            cutOff = False
            # Query prolog for the cutoff amount
            for result in PROLOG.query(cutOffQuery):

                # If the amount is small, have user gather it manually
                if amt < result["CutoffAmt"]:
                    resourcesToGather.update({resource: amt})
                    print(f"No farm needed for {resource}, adding to manual gathering list")
                    cutOff = True
            if cutOff:
                continue

            else:
                print(f"Determined farm should be built for {resource}")

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
                print(f"No farms listed for {resource}, adding to manual gathering list")
                resourcesToGather.update({resource : amt})
                continue

            else:
                print(f"Found the following farms: {farmsList}")
                #print(farmsList)

            # Evaluate which farm is best
            suitabilityScore = {}
            for thisFarm in farmsList:
                # Score variable to track analysis
                score = 0     

                # Get all resources produced by the farm
                allProduced = {}
                allProducedQuery = f"produces({thisFarm}, Resource, Amt)"
                for resultORQ in PROLOG.query(allProducedQuery):
                    allProduced.update({resultORQ["Resource"]:resultORQ["Amt"]})

                # Go through each resource produced by the farm and add to the score
                # with less points given to non-essential (byproducts) of the farm
                for x in allProduced:

                    if x in resourcesNeeded:
                        score += allProduced[x]     # Add to the score if resource is necessary
                    else:
                        score += allProduced[x] / 10   # Non-essential products of the farm still count, but less valuable

                # Determine effort required to build farm
                effortQuery = f"effort({thisFarm}, X)"
                effortNum = 0
                for resultEff in PROLOG.query(effortQuery):
                    # Convert effort string (low, medium, high...) to numerical value
                    effortNum = EFFORT_CONVERSION[resultEff["X"]]
                
                # Adjust score based on effort
                score /= effortNum

                # Set suitability score for this farm
                suitabilityScore.update({thisFarm : score})
                #print(f"Suitability score for {thisFarm} is {suitabilityScore[thisFarm]}")

            # Get farm with max score
            bestFarm = ""
            bestScore = 0                
            for thisFarm in suitabilityScore:
                if suitabilityScore[thisFarm] > bestScore:
                    bestFarm = thisFarm
                    bestScore = suitabilityScore[thisFarm]
            
            print(f"Determined best farm for {resource} to be {bestFarm} with a score of {bestScore}")

            # Add farm to the procedure
            procedureFinal.insert(0, f"Build {bestFarm}")

            # Add produce of farm to resourcesFound
            bestFarmProduces = []
            bestFarmProducesQuery = f"produces({bestFarm}, Resource, Amt)"
            for result in PROLOG.query(bestFarmProducesQuery):
                if result["Resource"] not in resourcesFound:
                    resourcesFound.append(result["Resource"])
            
            # Get resources needed to build the farm
            bestFarmRawCompositionQuery = f"rawComposition({bestFarm}, Resource, Amt)"
            for result in PROLOG.query(bestFarmRawCompositionQuery):
                if result["Resource"] not in resourcesFound:
                    if result["Resource"] not in resourcesToGather:
                        if result["Resource"] not in addedResources:
                            addedResources.update({result["Resource"] : result["Amt"]})


        if (len(addedResources) == 0):
            break
        else:
            resourcesNeeded = addedResources
            for x in addedResources:
                resourcesFinal.update({x : addedResources[x]})
            #print(f"resourcesNeeded is now: {resourcesNeeded}, searching again")
            print(f"\nDetermined additional resources needed to consturct farms, searching again")
        #break

    procedureFinal.insert(len(procedureFinal)-1, "Manually gather the resources above")

    # Display Results
    print("\n________________")
    print("SEARCH COMPLETE")
    print("\nTotal resources required:")
    print(resourcesFinal)
    print("__")
    print("\nUser should gather the following resources manually:")
    print(resourcesToGather)
    print("\nProcedure to follow:")
    count = 1
    for procedure in procedureFinal:
        print(f"{count}. {procedure}")
        count += 1
    #print(procedureFinal)


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
            print("\nValid Machines:")
            print(VALID_MACHINES)
        
        elif userSelection == 3:
            break

    print("\n\nThank you for using this program!\n\n")


if __name__ == "__main__":
    main()