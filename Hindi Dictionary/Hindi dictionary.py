Mydict = {
    "kitaab": "Book",
    "taala": "Lock",
    "zameen" : "Ground",
    "basta" : "Bag"
}
print(Mydict)
print(Mydict["zameen"])

print("Options are: ", Mydict.keys())
m = input("Enter a hindi word: ")
# print("The meaning of the word is ", Mydict[m])

#below line will not throw an error if the key is not present in the dictionary
print("The meaning of the word is ", Mydict.get(m))




