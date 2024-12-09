
from pyswip import Prolog

prolog = Prolog()


# Build a for importing prolog statements here as a document, then parse it into these commands
# simple line break for delineation of commands
# each one becomes an assertz in a loop

"""
BACKUP OF INITIAL PROLOG TESTS
prolog.assertz("father(michael, john)")
prolog.assertz("father(michael, craig)")


for result in prolog.query("father(X, Y)"):
    print(result["X"], "is the father of", result["Y"])

print(result)

# Section for querying prolog
for result in prolog.query("father(michael, X)"):
    print(result)
"""
#prolog.assertz("")
prolog.assertz("raw(redstone)")
prolog.assertz("comparator(redstone, 3)")
prolog.assertz("comparator(stick, 2)")
prolog.assertz("nonRaw(X) :- not(raw(X))")
#prolog.assertz("")


query = "thingy(X, Y)"
result = list(prolog.query(query))

# X now the object you're creating
# Y is result[0][X] now a list of the components


print("\n\n\n")
"""
def main():
    print("Program begins")
    finalResources = {}         # Dictionary to tabulate all resources needed
    finalProcedure = []         # List to document steps for player to follow
    farmCutoff = {}             # Amount of resources where a farm will be recommended (instead of gathering manually)

    finalResources.update({"redstone": 3, "stone": 16})
    finalProcedure.insert(0, "Get money")
    finalProcedure.insert(0, "Fuck bitches")

    print(finalResources)
    print(finalProcedure)

    print("Program ended successfully")

if __name__ == "__main__":
    main()
"""