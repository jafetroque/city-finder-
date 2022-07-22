# create lists of cities
tropicCity = ["Bangkok", "Papua", "Ayun Pa", "Tanete", "Miami", "Sao Paulo", "Xpujil", "Juara"]
desertCity = ["Riyadh", "Antananarivo", "Tsogtchandman", "Mhamid", "Las Vegas", "Lima", "Kotzebue", "Toconao"]
east = ["Bangkok", "Papua", "Ayun Pa", "Tanete", "Riyadh", "Antananarivo", "Tsogtchandman", "Mhamid"]
west = ["Miami", "Sao Paulo", "Xpujil", "Juara", "Las Vegas", "Kotzebue", "Toconao"]
urban = ["Bangkok", "Papua", "Miami", "Sao Paulo", "Riyadh", "Antananarivo", "Las Vegas", "Lima"]
rural = ["Ayun Pa", "Tanete", "Xpujil", "Juara", "Tsogtchandman", "Mhamid", "Kotzebue", "Toconao"]
northern = ["Bangkok", "Ayun Pa", "Miami", "Xpujil", "Riyadh", "Tsogtchandman", "Las Vegas", "Kotzebue"]
southern = ["Papua", "Tanete", "Sao Paulo", "Juara", "Antananarivo", "Mhamid", "Lima", "Toconao"]

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
