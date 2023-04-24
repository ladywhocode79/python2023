str = "Sonal Singh"
print(str[0])

#substring
print(str[0:6])

str1 =" starting python"
str3="Singh"
#concatenation
str2=str+str1
print(str2)
#substring check
print(str3 in str2)

#split
var = str.split(" ")
print(var)
print(var[0])

#remove spaces removes from front and back of string
str4=" happy "
print(str4.strip())

#remove space from left and remove from right
print(str4.lstrip())
print(str4.rstrip())
