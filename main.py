# import any functions that will be needed
import random
import time
# create lists of cities
tropicCity = ["Bangkok", "Papua", "Ayun Pa", "Tanete", "Miami", "Sao Paulo", "Xpujil", "Juara"]
desertCity = ["Riyadh", "Antananarivo", "Tsogtchandman", "Mhamid", "Las Vegas", "Lima", "Kotzebue", "Toconao"]
east = ["Bangkok", "Papua", "Ayun Pa", "Tanete", "Riyadh", "Antananarivo", "Tsogtchandman", "Mhamid"]
west = ["Miami", "Sao Paulo", "Xpujil", "Juara", "Las Vegas", "Kotzebue", "Toconao"]
urban = ["Bangkok", "Papua", "Miami", "Sao Paulo", "Riyadh", "Antananarivo", "Las Vegas", "Lima"]
rural = ["Ayun Pa", "Tanete", "Xpujil", "Juara", "Tsogtchandman", "Mhamid", "Kotzebue", "Toconao"]
northern = ["Bangkok", "Ayun Pa", "Miami", "Xpujil", "Riyadh", "Tsogtchandman", "Las Vegas", "Kotzebue"]
southern = ["Papua", "Tanete", "Sao Paulo", "Juara", "Antananarivo", "Mhamid", "Lima", "Toconao"]
# create empty choice lists
choice1 = []
choice2 = []
choice3 = []
choice4 = []

# ask the user for their input and check if the input is valid
temp = input("What climate do you like? Type T for tropical or D for desert and hit enter: ")
print()
longitude = input("Which hemisphere would you like to explore? Type E for east or W for west:  ")
print()
population = input("How dense would you like the population? Type R for rural or U for urban: ")
print()
latitude = input("What latitude do you prefer. Type N for north or S for South: ")
print()

# create proper formatting and if the user has entered invalid values, ask them to enter a value again
temp = temp.strip()
temp = temp.capitalize()
if temp.isalpha() == False:
    temp = input("It seems you have entered an invalid value. Type T for tropical or D for desert: ")
longitude = longitude.strip()
longitude = longitude.capitalize()
if longitude.isalpha() == False:
    longitude = input("It seems you have entered an invalid value. Type E for east or W for west:  ")
population = population.strip()
population = population.capitalize()
if population.isalpha() == False:
    population = input("It seems you have entered an invalid value. Type R for rural or U for urban: ")
latitude = latitude.strip()
latitude = latitude.capitalize()
if latitude.isalpha() == False:
    latitude = input("It seems you have entered an invalid value. Type N for north or S for South: ")


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

# create a function that will turn all choice lists into sets and the find the element they all have in common
# turn the common element into a list and return the value of that list, it should have one value which is the destination
def final():
    f = list(set(choice1) & set(choice2) & set(choice3) & set(choice4))
    return f

# call the function that looks for shared elements and assign its value to a variable
# the function returns a list but we want a string so simply index the first (and only) value of the list and assign it to a variable
fin = final()
fin = fin[0]

# this part is cosmetic, but a loading screen was made as a preview to the results
# a timer function was used to delay print statements
print("\t \t \t \t \t l o a d i n g...")
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
time.sleep(.25)
for i in range(5):
    print("\u2708 ", end = "")
print()
time.sleep(.25)

#print the city that matches all of the values whihc the user inputed
print("Wow you have made some excellent choices! We recommend visiting the city of " + fin)
print()
print("Since you're vacationing in a hot climate you should stay hydrated, let's pick you a drink!")
print()
# we want to ask the user what kind of drink they want
# intialize a multidimesnional list where each element is a list of a type of drink, our list had a list of juices water and soda
drinks = [["Pineapple juice", "Grape juice", "Orange juice"],["Coke", "Sprite", "Fanta"],["Warm water","Room temp water", "Cold water"]]
# ask the user which type of drink they want and assign the drinks options to index positions on the list
# format the input properly
bev = input("Would you like a juice, soda, or a water? Type J S or W? ")
print()
bev = bev.capitalize()
bev = bev.strip()

# depending on the user's input, randomly select an element inside one the multidimensional list's elements and print
while bev == "J":
    x = 0
    d = random.randint(0,2)
    print(drinks[x][d] + " would be a great choice of drink!")
    break

while bev == "S":
    x = 1
    d = random.randint(0,2)
    print(drinks[x][d] + " would be a great choice of drink!")
    break

while bev == "W":
    x = 2
    d = random.randint(0,2)
    print(drinks[x][d] + " would be a great choice of drink!")
    break






