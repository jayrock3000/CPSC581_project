# Import Statements
from pyswip import Prolog

# Global Variables
PROLOG = Prolog()
DEBUG = False
VALID_MACHINES = ["comparator", "observer", "repeater", "witchfarm", "itemsorter", "piston", "stickypiston", "raidfarm", "villagerfarm"]
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
    PROLOG.assertz("raw(slime)")
    PROLOG.assertz("raw(iron)")
    PROLOG.assertz("raw(honey)")
    PROLOG.assertz("raw(obsidian)")
    PROLOG.assertz("raw(terracotta)")
    PROLOG.assertz("raw(sand)")
    PROLOG.assertz("raw(spiderspawner)")
    PROLOG.assertz("raw(zombiespawner)")
    PROLOG.assertz("raw(skeletonspawner)")
    PROLOG.assertz("raw(copper)")
    PROLOG.assertz("raw(glowstone)")
    PROLOG.assertz("raw(ice)")
    PROLOG.assertz("raw(bamboo)")
    PROLOG.assertz("raw(goldnugget)")
    PROLOG.assertz("raw(shulkershell)")
    PROLOG.assertz("raw(turtleegg)")
    PROLOG.assertz("raw(coral)")
    PROLOG.assertz("raw(magmablock)")
    PROLOG.assertz("raw(soulsand)")
    PROLOG.assertz("raw(gunpowder)")
    PROLOG.assertz("raw(spidereye)")
    PROLOG.assertz("raw(bottle)")
    #PROLOG.assertz("raw()")
    #PROLOG.assertz("raw()")


    PROLOG.assertz("notRaw(Item) :- not(raw(Item))")

    
    # Farm cutoffs for raw resources
    PROLOG.assertz("farmCutoff(redstone, 64)")
    PROLOG.assertz("farmCutoff(log, 400)")
    PROLOG.assertz("farmCutoff(quartz, 200)")
    PROLOG.assertz("farmCutoff(cobblestone, 2000)")
    PROLOG.assertz("farmCutoff(stick, 200)")
    PROLOG.assertz("farmCutoff(string, 64)")
    PROLOG.assertz("farmCutoff(emerald, 200)")
    PROLOG.assertz("farmCutoff(villager, 2)")
    PROLOG.assertz("farmCutoff(slime, 10)")
    PROLOG.assertz("farmCutoff(iron, 64)")
    PROLOG.assertz("farmCutoff(honey, 32)")
    PROLOG.assertz("farmCutoff(obsidian, 128)")
    PROLOG.assertz("farmCutoff(terracotta, 2000)")
    PROLOG.assertz("farmCutoff(sand, 2000)")
    PROLOG.assertz("farmCutoff(spiderspawner, 1)")
    PROLOG.assertz("farmCutoff(zombiespawner, 1)")
    PROLOG.assertz("farmCutoff(skeletonspawner, 1)")
    PROLOG.assertz("farmCutoff(copper, 1000)")
    PROLOG.assertz("farmCutoff(glowstone, 200)")
    PROLOG.assertz("farmCutoff(ice, 2000)")
    PROLOG.assertz("farmCutoff(bamboo, 400)")
    PROLOG.assertz("farmCutoff(goldnugget, 500)")
    PROLOG.assertz("farmCutoff(shulkershell, 32)")
    PROLOG.assertz("farmCutoff(turtleegg, 1)")
    PROLOG.assertz("farmCutoff(coral, 64)")
    PROLOG.assertz("farmCutoff(magmablock, 500)")
    PROLOG.assertz("farmCutoff(soulsand, 1000)")
    PROLOG.assertz("farmCutoff(gunpowder, 64)")
    PROLOG.assertz("farmCutoff(spidereye, 32)")
    PROLOG.assertz("farmCutoff(bottle, 1000)")
    #PROLOG.assertz("farmCutoff(, )")
    #PROLOG.assertz("farmCutoff(, )")


    # item composition
    PROLOG.assertz("composedOf(stone, cobblestone, 1)")
    PROLOG.assertz("composedOf(redstonetorch, redstone, 1)")
    PROLOG.assertz("composedOf(redstonetorch, stick, 1)")
    PROLOG.assertz("composedOf(comparator, redstonetorch, 3)")
    PROLOG.assertz("composedOf(comparator, quartz, 1)")
    PROLOG.assertz("composedOf(comparator, stone, 3)")
    PROLOG.assertz("composedOf(stick, plank, 0.5)")
    PROLOG.assertz("composedOf(plank, log, 0.25)")
    PROLOG.assertz("composedOf(observer, cobblestone, 6)")
    PROLOG.assertz("composedOf(observer, redstone, 2)")
    PROLOG.assertz("composedOf(observer, quartz, 1)")
    PROLOG.assertz("composedOf(repeater, redstone, 1)")
    PROLOG.assertz("composedOf(repeater, redstonetorch, 2)")
    PROLOG.assertz("composedOf(repeater, stone, 3)")
    PROLOG.assertz("composedOf(piston, plank, 3)")
    PROLOG.assertz("composedOf(piston, cobblestone, 4)")
    PROLOG.assertz("composedOf(piston, redstone, 1)")
    PROLOG.assertz("composedOf(piston, iron, 1)")
    PROLOG.assertz("composedOf(stickypiston, piston, 1)")
    PROLOG.assertz("composedOf(stickypiston, slime, 1)")
    PROLOG.assertz("composedOf(slimeblock, slime, 9)")
    PROLOG.assertz("composedOf(redstoneblock, redstone, 9)")
    PROLOG.assertz("composedOf(honeyblock, honey, 4)")
    PROLOG.assertz("composedOf(glazedterracotta, terracotta, 1)")
    PROLOG.assertz("composedOf(glass, sand, 1)")
    PROLOG.assertz("composedOf(chest, plank, 8)")
    PROLOG.assertz("composedOf(hopper, chest, 1)")
    PROLOG.assertz("composedOf(hopper, iron, 5)")
    PROLOG.assertz("composedOf(dropper, cobblestone, 7)")
    PROLOG.assertz("composedOf(dropper, redstone, 1)")
    PROLOG.assertz("composedOf(dispenser, cobblestone, 7)")
    PROLOG.assertz("composedOf(dispenser, redstone, 1)")
    PROLOG.assertz("composedOf(dispenser, bow, 1)")
    PROLOG.assertz("composedOf(bow, stick, 3)")
    PROLOG.assertz("composedOf(bow, string, 3)")
    PROLOG.assertz("composedOf(redstonelamp, redstone, 4)")
    PROLOG.assertz("composedOf(redstonelamp, glowstoneblock, 1)")
    PROLOG.assertz("composedOf(glowstoneblock, glowstone, 4)")
    PROLOG.assertz("composedOf(lever, cobblestone, 1)")
    PROLOG.assertz("composedOf(lever, stick, 1)")
    PROLOG.assertz("composedOf(stonebutton, stone, 1)")
    PROLOG.assertz("composedOf(woodbutton, plank, 1)")
    PROLOG.assertz("composedOf(packedice, ice, 9)")
    PROLOG.assertz("composedOf(scaffolding, bamboo, 1)")
    PROLOG.assertz("composedOf(scaffolding, string, 0.2)")
    PROLOG.assertz("composedOf(goldingot, goldnugget, 9)")
    PROLOG.assertz("composedOf(shulkerbox, shulkershell, 2)")
    PROLOG.assertz("composedOf(shulkerbox, chest, 1)")
    PROLOG.assertz("composedOf(itemsorter, comparator, 1)")
    PROLOG.assertz("composedOf(itemsorter, redstone, 3)")
    PROLOG.assertz("composedOf(itemsorter, repeater, 1)")
    PROLOG.assertz("composedOf(itemsorter, hopper, 3)")
    PROLOG.assertz("composedOf(itemsorter, chest, 1)")
    PROLOG.assertz("composedOf(trapdoor, plank, 3)")
    PROLOG.assertz("composedOf(deadcoral, coral, 1)")
    PROLOG.assertz("composedOf(plankslab, plank, 0.5)")
    PROLOG.assertz("composedOf(composter, plankslab, 7)")
    PROLOG.assertz("composedOf(bucket, iron, 3)")
    PROLOG.assertz("composedOf(lava, bucket, 1)")
    PROLOG.assertz("composedOf(tnt, gunpowder, 5)")
    PROLOG.assertz("composedOf(tnt, sand, 4)")
    PROLOG.assertz("composedOf(tripwirehook, iron, 1)")
    PROLOG.assertz("composedOf(tripwirehook, plank, 1)")
    PROLOG.assertz("composedOf(tripwirehook, stick, 1)")
    PROLOG.assertz("composedOf(minecart, iron, 5)")
    #PROLOG.assertz("composedOf(, , )")
    #PROLOG.assertz("composedOf(, , )")
    #PROLOG.assertz("composedOf(, , )")
    #PROLOG.assertz("composedOf(, , )")
    #PROLOG.assertz("composedOf(, , )")
    #PROLOG.assertz("composedOf(, , )")


    # Get the raw materials composing a component
    PROLOG.assertz("rawComposition(Item, Component, Qty) :- composedOf(Item, Component, Qty), raw(Component)")  # Returns raw components of an item
    PROLOG.assertz("rawComposition(Item, Subcomponent, TotalQty) :- composedOf(Item, Component, Qty), notRaw(Item), rawComposition(Component, Subcomponent, SubQty), TotalQty is Qty * SubQty") # Recursively calls subcomponents until a raw item is found

    # FARMS - track what they produce, materials required to make them, and how much effort it takes
    PROLOG.assertz("produces(witchfarm, stick, 500)")
    PROLOG.assertz("produces(witchfarm, redstone, 250)")
    PROLOG.assertz("produces(witchfarm, glowstone, 250)")
    PROLOG.assertz("produces(witchfarm, gunpowder, 250)")
    PROLOG.assertz("produces(witchfarm, spidereye, 250)")
    PROLOG.assertz("produces(witchfarm, bottle, 250)")
    PROLOG.assertz("produces(witchfarm, sugar, 250)")
    PROLOG.assertz("composedOf(witchfarm, composter, 21)")
    PROLOG.assertz("composedOf(witchfarm, string, 49)")
    PROLOG.assertz("composedOf(witchfarm, stickypiston, 21)")
    PROLOG.assertz("composedOf(witchfarm, comparator, 21)")
    PROLOG.assertz("composedOf(witchfarm, trapdoor, 21)")
    PROLOG.assertz("composedOf(witchfarm, tripwirehook, 42)")
    PROLOG.assertz("composedOf(witchfarm, minecart, 24)")
    PROLOG.assertz("composedOf(witchfarm, itemsorter, 7)")
    PROLOG.assertz("effort(witchfarm, low)")

    PROLOG.assertz("produces(villagerfarm, redstone, 50)")
    PROLOG.assertz("produces(villagerfarm, emerald, 100)")
    PROLOG.assertz("produces(villagerfarm, villager, 100)")
    PROLOG.assertz("composedOf(villagerfarm, villager, 2)")
    PROLOG.assertz("effort(villagerfarm, medium)")

    PROLOG.assertz("produces(raidfarm, stick, 1000)")
    PROLOG.assertz("produces(raidfarm, redstone, 500)")
    PROLOG.assertz("produces(raidfarm, glowstone, 500)")
    PROLOG.assertz("produces(raidfarm, gunpowder, 500)")
    PROLOG.assertz("produces(raidfarm, spidereye, 500)")
    PROLOG.assertz("produces(raidfarm, bottle, 500)")
    PROLOG.assertz("produces(raidfarm, sugar, 500)")
    PROLOG.assertz("produces(raidfarm, emerald, 2000)")
    PROLOG.assertz("composedOf(raidfarm, villager, 4)")
    PROLOG.assertz("composedOf(raidfarm, composter, 4)")
    PROLOG.assertz("composedOf(raidfarm, glass, 40)")
    PROLOG.assertz("composedOf(raidfarm, magmablock, 16)")
    PROLOG.assertz("composedOf(raidfarm, lava, 4)")
    PROLOG.assertz("composedOf(raidfarm, soulsand, 16)")
    PROLOG.assertz("composedOf(raidfarm, piston, 16)")
    PROLOG.assertz("composedOf(raidfarm, comparator, 4)")
    PROLOG.assertz("composedOf(raidfarm, repeater, 4)")
    PROLOG.assertz("composedOf(raidfarm, dispenser, 1)")
    PROLOG.assertz("composedOf(raidfarm, dropper, 2)")
    PROLOG.assertz("composedOf(raidfarm, itemsorter, 14)")
    PROLOG.assertz("effort(raidfarm, veryhigh)")


    #PROLOG.assertz("")
    #PROLOG.assertz("")



    
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
    resourcesFound = []         # Tracks resources produced by farms recommended (so far)
    procedureFinal = []         # List to document steps for player to follow

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

    # Build Procedure
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