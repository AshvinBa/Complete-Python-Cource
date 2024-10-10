letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''

name = input("Enter the name: ")
date = input("Enter the date: ")

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)

print(letter)