# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(inList):
    if not inList: #check to see if the list if empty
        return None
    else:
        counter=1 #counter for the longest repetition
        #assign the first element as a candidate for the longest repetition
        candidate=inList[0] 
        #Save the results into the list of lists: element of the input list and number of 
        #times it occurred in a row
        result = [[inList[0],1]]
        #Go through all elements starting from the first one in the input list
        for i in range(1,len(inList)):
        #check whether an element is the same as the candidate
            if inList[i]==candidate:
            #if the element is the same as the candidate (=previous element)
            #then we need to increase the counter
                counter=counter+1
                #In this terrible nested loop I find the element in the list and 
                #update the counter
                for j in range(0,len(result)):
                    if result[j][0]==inList[i]:
                        result[j][1]=counter
            else:
                #If the element is not the same as the candidate, it means that
                #we broke the streak, assign the element to be the new candidate
                candidate=inList[i]
                #restart the counter
                counter=1
                #This is a weird way to see whether I have inList[i] in the result
                check = 0
                for j in range(0,len(result)):
                    if result[j][0]==candidate:
                        check=1
                #So basically if I didn't see the element, I need to add it
                if check==0:
                    result.append([inList[i],1])
        #The following piece of code finds the max repetition in the result and
        #returns the element that is the most repeated
        maxVal = result[0][1]
        entry = result[0][0]
        for j in range(1,len(result)):
            if maxVal<result[j][1]:
                maxVal=result[j][1]
                entry=result[j][0]
            
        return entry


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2,2,2,3,3,3])

