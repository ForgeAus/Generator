""" 4-Element List Printer"""

list_items = []

for count in range(4) :
    list_items.append(input("Type the next list item : \n"))

print ("\nThe items in the list are : \n")
for count in range(4) :
    print (list_items[count])
