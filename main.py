
from pyswip import Prolog

prolog = Prolog()


# Build a for importing prolog statements here as a document, then parse it into these commands
# simple line break for delineation of commands
# each one becomes an assertz in a loop

prolog.assertz("father(michael, john)")
prolog.assertz("father(michael, craig)")

'''
for result in prolog.query("father(X, Y)"):
    print(result["X"], "is the father of", result["Y"])

print(result)
'''

# Section for querying prolog
for result in prolog.query("father(michael, X)"):
    print(result)


def main():
    print("Program begins")
    finalResources = {}         # Dictionary to tabulate all resources needed
    finalProcedure = []         # List to document steps for player to follow

    finalResources.update({"redstone": 3, "stone": 16})
    finalProcedure.insert(0, "Get money")
    finalProcedure.insert(0, "Fuck bitches")

    print(finalResources)
    print(finalProcedure)

    print("Program ended successfully")

if __name__ == "__main__":
    main()