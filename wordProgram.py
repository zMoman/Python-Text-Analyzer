#COMP 1005
#Mohammed Al Amri
#101203169
#Assignment 4:

import words


def read_from_file(filename):
    '''Opens the file called filename and returns a string with the 
       contents of the file (including all newline characters)
       If filename is not in the same directory as this program, or 
       a problem occurs when reading, the function will return the empty string.
    ''' 
    try:
        with open(filename, 'r') as wordFile:
            all_words = wordFile.read()
        return all_words
    except Exception as e:
        print(f'Something wrong trying to open/read from {filename}')
        print(e)       
    return ""


def main():
    '''   this is the "program"   '''
    
    str=''
    print('Hi there!')
    filename = input('Name of file: ')
    
    chars = input("Input the characters you want: ")
    
    #If user inputs only enter, chars are alphabet
    if chars=='':
        chars='abcdefghijklmnopqrstuvwxyz'
    
    
    data = read_from_file(filename)
    
    #Adding borders and components to string.
    str+= f"{filename} stats\n"
    str+="-"*len(filename) +"------"+ "\n"
    length= len(words.unique_words(data))
    str+=(f"Number of unique words: {length}\n")
    
    #Unpacks the 5 top words in txt file.
    unpack= words.top_words(data,5)
    str+="Top 5 words used: " 
    
    #Adds each unique word to the string with a ',' except for last element
    for i in range(0,len(unpack)):
        
        str+=(f"{unpack[i][0]}")
        if i !=len(unpack)-1:
            str+=', '
        

        print(str)
        print(words.display_stats(data, chars))


if __name__ == '__main__': 
    main()