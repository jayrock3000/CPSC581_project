
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