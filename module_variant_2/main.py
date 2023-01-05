from importlib import import_module

strutil = import_module("strutil")

def print_to_console():
    print(strutil.concat("Hello", "Pycon"))

if __name__ == "__main__":
    print_to_console()
