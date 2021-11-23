#using replace function
letter = '''Dear <| NAME |>
Greetings from ABC consultants, I am happy to tell you about your selection
You are selected!
HR will coordinate with you for further documentation process
Have a great day ahead.

Thanks & Regards
Bill

Date: <| DATE |>
'''

name = input("Enter your Name: ")
date = input("Enter the date: ")

#if we just run letter.replace changes will not get into actual letter for that put it into a variable

letter = letter.replace("<| NAME |>", name)
letter = letter.replace("<| DATE |>", date)
print(letter)