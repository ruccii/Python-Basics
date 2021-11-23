 with open("sample.txt") as a:           #read file
     content = a.read()

 content = content.replace('donkey', '#%$^%&')  #perform task

 with open(f"sample.txt", "w") as a:
     a.write(content)                    #write

#MULTIPLE WORDS REPLACE

words = ["donkey", "is", "animal"]
with open("sample.txt") as a: #read file
     content = a.read()

for word in words:
    content = content.replace(word, '#%$^%&')  #perform task

with open(f"sample.txt", "w") as a:
     a.write(content)

print("done")
