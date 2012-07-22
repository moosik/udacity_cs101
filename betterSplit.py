##This procedure returns all splits of a string according to a string
##that contains different splits


def better_split(source,splitters):
    if len(splitters)==1:
        return source.split(splitters)
    else:
        firstsplit = source.split(splitters[0])
        temp = []
        for i in range(1,len(splitters)):
            for element in firstsplit:
                temp+=element.split(splitters[i])
            firstsplit=temp
            temp=[]
        formattedOut=[]
        for element in firstsplit:
            if len(element)!=0:
                formattedOut.append(element)
        return formattedOut
        
