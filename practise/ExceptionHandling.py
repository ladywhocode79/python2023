
itemCart = 0

# if itemCart != 2:
#     raise Exception("No items in the cart")

# assert (itemCart == 3)

# try:
#     with open('file.txt','r') as readers:
#         readers.read()
# except:
#     print("i am continuing")

# try:
#     with open('file.txt','r') as readers:
#         readers.read()
# except Exception as e:
#     print(e)


try:
    with open('file.txt','r') as readers:
        readers.read()
except Exception as e:
    print(e)
finally:
    print("I will run in call condition")
