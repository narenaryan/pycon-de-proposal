from folder import numutil

# from importlib import import_module
# numutil = import_module("folder.numutil")

# numutil = __import__("folder.numutil")

def print_to_console():
    print(numutil.add(3, 4))

if __name__ == "__main__":
    print_to_console()
