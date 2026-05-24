#Print with a string
print("Olá, gringa! Já Já to ai...")
print("Só tô dando um jeito aqui, já já to ai...")

#Print with a numbers
print(10+8)
print(20-2)
print(6*3)
print(36/2)
print(2*3**2)
print("7" + "3")
print("Hello", 7, "times")

#Variables
sales = 250
cost = 50
goal = 150
profit = sales - cost

#Print with a variable and a string
print("Your profit is:", profit)
print("Your cost is:", cost)
print("Your sales are:", sales)
name = "Rafael"
weight = 65
my_age = 5*3
print("My name is", name, ", my age is", my_age, "and my weight is", weight, "kg.")

#If, elif and else
if profit == goal:
    print("Great Job")
elif profit < goal:
    print("Not bad, but you can do better!")
else:
    print("excellent Work")

#Lists
List = ["Cpu", "Ram", "Ssd", "Motherboard"]
print(List[2])
print(List[1*2])
for item in List:
    print(item)


Listprice = [200, 150, 100, 300]
for price in Listprice:
    print(price*2)

#Loops
for i in range(3):
    print("Idk what to say, but I have to say something...")

#Input
your_name =  input("Insert your name:")
your_age = input ("insert your age:")
day = input("What a day of your birthday?")
month = input("What a month of your birthday?")
year  = input("What a year of your bithday?")
print("Your name is", your_name, "and your age is", your_age, "and your bithday is", day, "of", month, "of", year,"Right?")
print("Hello", your_name, "! Nice to meet you!")
input("press enter to continue")