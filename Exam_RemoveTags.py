# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.


#This code was accepted. It is probably not the most efficient because I deal with 
#splitting the words by spaces afterwards.
def remove_tags(st):
    result=[] #list where I will write everything that was found outside of <>
    word=0 #assume that a word begins as the first letter of the string
    while len(st)>0:
        tagOpen = st.find("<") #find the first opening tag
        if tagOpen == -1: #if it is not found, then it means that we deal with plain text
            result.append(st) #return the whole string 
            break #and jump out of the loop
        #If the position of the opening tag is bigger than the position of the word
        #then we need to take everything from the word to the opening tag
        elif tagOpen>word:
            result.append(st[word:tagOpen])
            tagClose=st.find(">") #now we need to find the closing tag
            #Trim the string to start from the next position after the closing tag
            st = st[tagClose+1:] 
            word=0 #reassign the word postion
        else:
            #If the tagOpen is equal to the position of the word if means
            #that we don't have a word before the opening tag
            #Now we need to find the closing tag, trim the string and 
            #reassign the position of the word
            tagClose=st.find(">")
            st = st[tagClose+1:]
            word=0
    #Create a new list which will contain the output split by spaces
    output = []
    for el in result:
        output+=el.split() #use this notation rather than append
        #because split generates a list and we want to add each element of it
        #rather than the entire list
    return output

print remove_tags('''<h1>Title</h1><p>This is a<a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']