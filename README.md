# CPSC581_project
# Ensure Swi-Prolog is installed (Prolog):
#   Link for download
#   https://www.swi-prolog.org/download/stable

# Emsure PySwip is installed (PysSwip running in Python Virtual Environment):
#   Link for explanation
#   https://pyswip.readthedocs.io/en/stable/get_started.html
#   Run the following commands in console/terminal
#   pip install -U pyswip

# The above may require additional installs including
#   Python
#        https://www.python.org/downloads/
#   pip Install Packages (PIP)
#        https://packaging.python.org/en/latest/tutorials/installing-packages/

# Entire program runs in main.py
# Running the script will open a main menu
# You can search the knowledge base for how to build one of the valid machines

# A list of valid machines can be accessed by entering 2 in the main menu.
# This is far from a complete list of all possible machines in minecraft,
# but serves as a demonstration of some rather complex machines and their
# recommended build processes from zero items.

# A particularly complex farm is a "complete storage system" - consisting of enough item sorters to roughly sort every item in the game
# You could query this by:
# Running main.py
# Select menu option 1 (press 1, then ENTER)
# Input "completestoragesystem" (without quotes, then press ENTER)
# See the log of the iterative search for how each component is constructed, then how each raw resource is accounted for, including
# several farms which will be determined are necessary to gather enough of the given resource.