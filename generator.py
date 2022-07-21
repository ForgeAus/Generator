""" Random List Printer"""

import random

list_items = []

list_len = int( input ("How long is the list: \n") )

for make_list in range( list_len ) :
    list_items.append( input( "Type the next list item : \n" ) )

gencount = int( input( "Type how many items to generate: \n" ) )

print( "\nThe items in the list are : \n" )
for print_count in range(gencount) :
    print( list_items[int( random.randint( 0, ( list_len - 1 ) ) )] )
