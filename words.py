#COMP 1005
#Mohammed Al Amri
#101203169
#Assignment 4:

#Function returns a list with all unique words from text.
def unique_words(text):
    
    text2=text.lower() #Lower case all text
    text2=text2.split() #Split text to list
    
    newList= list(dict.fromkeys(text2)) #Converting to dict gets rid of all duplicates, then back to list.

    return newList


#Function returns a list of tuples of top words in text.
def top_words(text,num):
   
    text2=text.lower() #Lower case all text
    text2=text2.split() #Split text to list
    newMax=0 #newMax used to set highscore in next step.
    newList=[]
   
    #Iterating through text2 to find which words occur the most, inputting it into a tuple, then inserting tuple into list.
    for i in text2:
       
        if text2.count(i)>=newMax:
            newMax=text2.count(i)
            tuple=(i,newMax)
            newList.insert(0,tuple)
            
            
        #If word is not a top occuring word, add to end of list
        else: newList.append((i, text2.count(i)))

    newList=list(dict.fromkeys(newList))
    
    while num<len(newList):

        if newList[num-1][1]==newList[num][1]:
            num+=1

        else:break

        
    
    return newList[0:num]
        



#Function returns string with all chars and how mnay occurnces they had in a scale of # 
def display_stats(text, chars):

    text2=text.lower() 
    newMax=0

    
    #Loops through chars to find most occured char
    for i in chars:
        
        if text2.count(i)>newMax:
            newMax=text.count(i)
            letter=i
        
        
        else: continue
    

    #Loops and adds occurance of every char to sum.
    sum=0
    for i in chars:
        sum+=text2.count(i)

    math=40/newMax
    
    stats=f"Character Stats ({sum} in total)\n-+---------------------------------------- (#={int(math)})\n"

    #Creates display for each char with correct amount of #s
    for j in chars:

        if j==letter: #If most occured char found, set 40 #
            stats+= j + '|' + ('#') * (40) + '\n'
        
        else: stats+= j + '|' + ('#') *text2.count(j) * int(math) + '\n' #Else use same ratio (math) to set number of #s
    
    stats+=("-+----------------------------------------")
    return stats

