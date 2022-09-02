""" Random Generator """
 
import random
 
class TemplateError( Exception ):
    """Key error for when no matching listnames are found"""
 
class NotANumber( Exception ):
    """Type or Value error for when the input was not a number"""
 
lists = {}
 
def num_entry( question ):
    """A function that takes in a number and assigns it to an integer"""
    result = 0
    entry = ""
    
    while result < 1:
        
        entry = input( question )
        try:
            result = int( entry )            
        except (TypeError, ValueError):
            raise NotANumber( f"Sorry, unable to get a number from {entry}" )
 
    return result
 
num_lists = num_entry( "Please enter how many lists:" )
 
for list_count in range( num_lists ):
    list_name = input( "\nPlease enter a unique title for this list: \n" )
    lists[list_name] = []
    
    print( f"Please add a new entry to {list_name} or use an empty line to end the list: \n" )
    while True:
        item = input()
    
        if item == "":
            break
        
        lists[list_name].append( item )
 
 
gen_count = num_entry( "Please enter how many items to generate: \n" )
 
gen_format = input( "Please enter a template: \n(for example): This random character has <hair_color> hair and <eye_color> eyes.\n" )
 
print( "\nThe Generated items are : \n" )
 
for gen_index in range( gen_count ):
    
    gen_string = gen_format
    for field in lists:
        try:
            while (f"<{field}>") in gen_string:
                gen_string = gen_string.replace( f"<{field}>", random.choice( lists[field] ), 1 )
        except KeyError:
            raise TemplateError( f"Cannot find a list called <{field}> \n" )
    
    print( gen_string )
    
