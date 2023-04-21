# if else condition
greetings = "good morning"

if greetings == "morning":
    print("matched")
    print("hello people")
else:
    print("didnt matched")

print("nothing matched")

b = 9
if b == 10:
    print("b macthed")
else:
    print(" b not matched")

# for loop

obj = [2, 3, 4, 2, 6, 7]

for i in obj:
    print("{}  {} ".format("Value of obj is", i))

# sum of firt five natural numbers

summation = 0
for j in range(1, 6):  # range = 1 to 5
    summation = summation + j
print("{} {}".format("sum of first five numbers is ", summation))

#add index to add
for k in range(2,20,2):
    print("{} {}" .format("Add +2 :", k))

#skip start index so it starts from 0
for m in range(5):
    print("{} {}".format("skip first index :", m))

#while loop

it = 4
while it > 1:
    print(it)
    it= it - 1
print("While loop is completed")

its = 10
while its > 1:
    if its ==3:
        break
    print(its)
    its = its -1

print("end of while loop")


