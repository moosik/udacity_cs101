# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. Itcan 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


#I decided that this is what will work for me. Not sure what else they expected
def make_converter(match, replacement):
    return match, replacement #it returns a tuple




def apply_converter(converter, string):
    while len(string)>len(converter[1]): #go through the loop until the size of
    #the string in bigger then the string we want to use as a replacement
        match = string.find(converter[0]) #find the match
        if match == -1: # if no match find get out of the loop, this was crucial
            break
        else:
            #otherwise, take the piece of the string before the match, the replacement
            #and after the match and create a new string
            string=string[0:match]+converter[1]+string[(match+len(converter[0])):]
       #print string
    return string



# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever). 
# It is interesting, that my code actually terminates with this example. I wonder
# what they expected to see
