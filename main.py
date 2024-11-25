
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("father(michael, john)")
prolog.assertz("father(michael, craig)")

'''
for result in prolog.query("father(X, Y)"):
    print(result["X"], "is the father of", result["Y"])

print(result)
'''

for result in prolog.query("father(michael, X)"):
    print(result)