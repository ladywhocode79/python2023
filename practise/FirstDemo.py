print("hello")
# comments to be tested
a=3
print(a)

Str ="Hello world"
print(Str)

a , b, c = 4, 5.5, "great"

print(a)
print(b)
print(c)

#print("Value is : " +b)
print("{}  {} ".format("Value is", b))
print(type(c))

#list
values = [1, 2, 3.8, "sonal"]
print(values[0])
print(values[2])
print(values[3])

#prints value last in the list
print(values[-1])
print (values[1:3])

values.insert(4, "singh")
print(values)

values.append("hello")
print(values)

values[2] = "sona"
print(values)

del values[2]
print(values)

#tuple

val = (1,3,2,"sonal")
print(val)

print(val[3])

# val[3] = 5
# print(val)

#dictionary

dic = {"a" : 3, 2:"sonal" , "c" : 4}
print(dic)

print(dic["a"])

print(dic[2])

#add value in dictionary at runtime

dict ={}
dict["first name"] = "Sonali"

print(dict)
dict[2] ="singh"

print(dict[2])
