# # print("hello world!")

# # myList = ["sana", "Samreen"]
# # # Operations on lists

# # myList.append("Asma")

# # #2.  myList.insert(1,"Shahin")

# # # print(myList)
# # #3. print(myList[0])

# # myList.sort()
# # print(myList)

# # # # Tuples
# # # # tuples are ordered , unchangeable ,and allow duplicates.
# # # #  tuple is defined within round brackets
# # myTuple = ("orange", "mango", "Apple","kiwi")
# # print(myTuple)
# # print(myTuple[2])   
# # print(myTuple[0:3])

# # # Note we cannot update the tuple instead we can convert it into list ,update the list and then again convert it into tuple
# # myTuple = (23,45,72)
# # y = list(myTuple)
# # y.append("dragon fruit")
# # y[1] = "dragon fruit"
# # x=tuple(y)
# # print(x)

# # # # Adding tuples
# tuple1=(1,2,3)
# tuple2=("sana", "Amaira")
# tuple2=tuple1+tuple2
# print(tuple2)

# # Sets, these are unordered , unindexed , and unchangable built-in data type
# #Advantage : They does not contain any duplictaes and have unique elements.
# # the sets are defined within the curly braces {}
# mySet = {1,2,3,3,4,5,1}
# # print(mySet)

# # Since sets are unindexed, you cannot access them using its index value, instead use a for loop.
# # for x in mySet:
# #  print(x)

# #  you can add items to the set using the add() method
# # mySet.add("orange")
# # for x in mySet:
# #  print(x)

# #  you can add two sets by using the update() method
# # newSet= {"dogs", "cats"}
# # newSet.update(mySet)
# # for x in newSet:
# #  print(newSet)

# # Dictionaries
# # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# # A dictionary is a kind of data structure that stores items in key-value pairs
# # mydictionary ={
# #    " RollNo" : 2,
# #    "Name" : "Sana",
# #   " Section" : "A"
# # }
# # print(mydictionary)
# # # you can access a particular item in a dictionary using its key avlue
# # print(mydictionary["Section"])

# # Functions 
# #1.  def myName(name):
# #  print("my name is  " + name)

# # myName("Amaira")

# #  lamda function: it is a anonymus function which can take any no. of arguments but return only one expression.
# x= lambda a:a+10
# print(x(9))
 

# # Conditions and if statements
# # 1. equal to
# # 2. not equal to
# # 3.greater than
# # 4.less than
# # 5. greater than or equal to
# # 6. less than or equal to

# # String manipulations
# my_name =" My name is Sana"
# print(my_name.upper())
# print(my_name.lower())
# print(my_name.title())
# print(my_name.capitalize())


# # a=10
# # b=20
# # if(a>b):
# #     print("true")
# # else:
# #     print("false")

# # while loop
# # i=10
# # while i>=0:
# #     print(i)
# #     i-=1


# # if elif else loop example
# # num=10
# # if num>10:
# #     print("greater than 10")
# # elif num == 10:
# #     print("Equal to 10")
# # else :
# #     print("less than 10")

# # For loop to print each item in fruit list
# # fruit = ["Apple","Banana","orange","kiwi"]
# # for x in fruit:
# #     print(x)

# # continue: continue keyword is used to end the current iteration
# #  in a for loop or a while loop and coninue to the next iteration.
# fruit = ["Apple","Banana","orange","kiwi"]
# for x in "fruit":
#     if x=="i":
#       continue
# print(x)


# # list
# myList = ["orange", "mango", "apple"]
# print(myList)

# myList = [1,2,3]
# print(myList)

# # append(): 
# myList.append(5)
# print(myList)

# # acessing dataitem from a list
# print(myList[1])
# newList =[2,6,4,7,0]
# newList.sort(newList)

# Tuples: are also indexed, ordered and unmodified

# myTuple = ("orange", "mango","Apple")
# print(myTuple)
# print(myTuple[1])
# print(myTuple[0:])

# newTuple =(1,3,4,5)
# y=list(newTuple)
# y.insert(1,7)
# x=tuple(y)
# print(x)

# Sets : unordored, unindexed and it does not allow any duplicates.
# mySet = {1,3,4,6,7,9,6,6}
# print(mySet)

# for x in mySet:
#     print(x)


# # Dictionaries: 
# myDictionary = {
#     id:2,
#     "name": "Raj",
#     "Age":25
# }
# # print(myDictionary)
# print("name is"+ myDictionary(id))

# Functions: functions divide a program into smaller chunks, to specify a particular task.

# def myFunction(name):
#     print(name)
# myFunction("Sana")

# Conditional Statements: 
# greater than >
# lessthan <
# equal to =
# not equal to !=
# greater than >=
# lessthan <=

# age= 12
# # if(age>18):
# #     print("true")
# if(age>18):
#     print("true")
# else:
#     print("False")

# Strings 
# name = "rahul"
# # print(name)

# # upperCase
# print(name.upper())
# # Lowecase
# print(name.lower())
# # Capitalize
# print(name.capitalize())

# continue:
myList = [1,3,4,5,6]
for x in myList:
    if(x==3):
        continue
    print(x)




