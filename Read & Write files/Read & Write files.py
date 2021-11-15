# Use open function to read the contents of a file
f = open('sample.txt')  #by default the mode is r
f = open('sample.txt', 'r')
Data = f.read()
print(Data)
f.close()
Data = f.read(5)       #reads first 5 characters of file


#READLINE

f = open('sample.txt')    #by default the mode is r
Data = f.readline()
print(Data)                 

#reads 2nd line
Data = f.readline()
print(Data)
f.close()                  

# and so on....


# #Write a file
f = open("another.txt", "w")
f.write("Please write this to the data")
f.close()

#append a file
f = open("another.txt", "a")
f.write("Hey i am appending")
f.close()

f = open("sample.txt", "a")
f.write("\nHey i am appending")
f.close()

# with statement, we dont need to write close() in with statement
with open("another.txt", "w") as f:
    a = f.write("writing in with statement")
print(a)