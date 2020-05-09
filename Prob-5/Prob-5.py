# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Ilya Panasevich

def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("\nTypeError: eval() must be a string. Exiting\n")
        exit
    except:
        print("\nunknown exception. Exiting.\n")
        exit

main()