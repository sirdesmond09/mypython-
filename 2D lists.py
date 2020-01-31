# matrix = [
#     [1, 2, 3],
#     [4, 2, 5],
#     [3, 0, 10]
# ]
# print (matrix[2][2])

numbers=[2,3,3,5,6,1,2]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
        unique.sort()
print (unique)

your_number = input("Phone: ")
phone = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output=""
for item in your_number:
   output += phone.get(item, '!') + " "
print (output)

#List comprehension
a =[1,3,5,7,9,11]
b=[x*2 for x in a]
b.sort()
b.reverse()
print (b)

# sets