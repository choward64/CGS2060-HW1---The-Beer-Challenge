
from HW1BeerFunctions import prepareYeast



infile = open("HW_1_Data.txt","r")
Gallons_Of_Beer = int(infile.readlines().strip())
Ratio_Of_Malt = int(infile.readlines().strip())
Pounds_Of_Hops = int(infile.readlines().strip())
Grams_Of_Yeast = int(infile.readlines().strip())

WORLD = 0

try:
    done = prepareYeast(Grams_Of_Yeast, WORLD)
    if done == 0:
        raise ValueError
    else:
        print("Yeast has been prepared")
except ValueError:
    print("Something went wrong")
    exit(-1)