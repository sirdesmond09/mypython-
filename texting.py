# total = 0
# c = list(range (1 , 5))
# print (c)
# for i in range(1,5):
#     total += i
#     print (total)
# tat = 0
# b = [20, 10, 5]
# for e in b:
#     print (e)
#     tat += e
#     print(tat)
o = (list(range(1,100)))
too = 0
for i in o:
    if i % 3 == 0 or i % 5 == 0:
       too += i
print(too)
# given_list = (5, 4, 4, 3, 1, -2, -3, -5)
# total3 = 0
# i = 0
# while given_list[i] > 0:
#     total3 += given_list[i]
#     i += 1
# print (total3)
# print (len(given_list))

tee = 0
given_list3 = (7, 5, 4, 4, 3, 1, -2, -3, -5, -7)
for i in given_list3:
    if i < 0:
        tee += i
print (tee)     
desmond = {
    "Age": 15,
    "lOCATION": "SURULERE",
    "class": "sss2"
}
for key, value in desmond.items():
    print ("key:")
    print (key)
    print ("value:")
    print(value)
    print()
name = 'jennifer'
print(name.find('e'))