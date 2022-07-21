# create lists of cities
tropicCity = [1, 2, 3, 4, 5, 6, 7, 8]
desertCity = [9, 10, 11, 12, 13, 14, 15, 16]
east = [1, 2, 3, 4, 9, 10, 11, 12]
west = [5, 6, 7, 8, 13, 14, 15, 16]
urban = [1, 2, 5, 6, 9, 10, 13, 14]
rural = [3, 4, 7, 8, 11, 12, 15, 16]
northern = [1, 3, 5, 7, 9, 11, 13, 15]
southern = [2, 4, 6, 8, 10, 12, 14, 16]

# create empty lists
choice1 = []
choice2 = []
choice3 = []
choice4 = []

# ask the user for their input
temp = input("What climate do you like? Type T for tropical or D for desert and hit enter: ")
longitude = input("Which hemisphere would you like to explore? Type E for east or W for west:  ")
population = input("How dense would you like the population? Type R for rural or U for urban: ")
latitude = input("What latitude do you prefer. Type N for north or S for South: ")

# assign values to choice lists based on user input
if temp == "T":
        choice1 = tropicCity
if temp == "D":
        choice1 = desertCity
if longitude == "E":
        choice2 = east
if longitude == "W":
        choice2 = west
if population == "U":
        choice3 = urban
if population == "R":
        choice3 = rural
if latitude == "N":
        choice4 = northern
if latitude == "S":
        choice4 = southern

print(choice1)
print(set(choice1) & set(choice2) & set(choice3) & set(choice4))