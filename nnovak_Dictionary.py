# Nicholas Novak
# Introduction to Python course assignment


#Open the included file
dictionary_file = open("lab5_dictionary.txt","r")
dictionary_file.readlines()


# In this assignment, I created a function to find the longest word in a dictionary text file along with any ties for the longest word in that file.
# Notably, each line of the dictionary ends in '\n' which means the ending characters have to be stripped before adding a word to the output list.




## Created function:
def long_word(file_name):
    with open(file_name, 'r') as infile:
        words = infile.read().split() #This automatically closes a file after reding it.
        
    max_len = len(max(words, key=len)) #This creates an integer equal to the length of the longest word iterated over

    
    return[i for i in words if len(i) == max_len] #Return statement that returns a list consisting of the longest words found in the file.



long_word("lab5_dictionary.txt") # Calling created function for the included text file.

#-----------------------------------------

# Next, the dictionary will be iterated through to find words containing the most amount of unique letters.
# A list will be output that contains all words tied for most unique letters.



import string
alphabet_string = string.ascii_lowercase #All letters of alphabet as a string
print(alphabet_string)


# Function to open the file
def open_dict(filename):

    with open(filename, 'r') as f:
        words = f.readlines()
        #Open file and close when done

    return words

#Function to determine the amount of unique characters in a word
def uniqueness(word):

    uniques = set() #Using a set here allows the formation of a series of string swith no repeats. In this case, it is more efficient than a slower loop block.
    
    for character in word:
        uniques.add(character)
    
    return word, len(uniques)


#Funciton to determine the longest word(s) in the dictionary file
def unique_words(filename):
    dictionary = open_dict(filename)
    #Open the file as a set or list
    
    most_unique, unique_count = uniqueness(dictionary[0])
    #Reference dictionary words as the unique letter length and unique words
    
    print("Most unique words list:\n")
    for word in dictionary[1:]:

        curr_word, curr_count = uniqueness(word)
        #For the current word and length of uniqueness, set it equal to the uniqueness function
        
        if curr_count >= unique_count:
            most_unique, unique_count = curr_word, curr_count
            #Add the current word to the unique words list
            
            if curr_count == 17:
                #By running this program once without this section, it was found that 17 was the maximum number
                #therefore, if the word has 17 unique characters, it is added to the result.
                
                print('This unique word is', most_unique, 'with', unique_count, 'unique characters\n')
        


unique_words('lab5_dictionary.txt')


#-----------------------------------------
# For the final exercise, I determined if an anagram of a user input exists within the dictionary file.
#
# For  example, the following words do have anagrams in the included dictionary file:
# 
# 1) restful
# 
# 2) bluster
# 
# 3) binary
# 
# Return all anagrams found.


# Provided function
def is_anagram(string1,string2):
    
    return sorted(string1) == sorted(string2) # Determines if a sorted word is equal to another sorted word. Basically, is it an anagram?




def anagram_finder():
    with open("lab5_dictionary.txt", 'r') as infile2:
        dictionary_file_2 = infile2.readlines()
    user_input = input("Please enter the word you would like to find an anagram for:") # User input
    print("anagrams below:\n\n")
   

    ana_list = [] # Create list for results
    for s in dictionary_file_2:
        
        if is_anagram(s,user_input+"\n") == True: # Check if a word is an anagram
            
            print(s) # Display found string
            
            ana_list.append(s.rstrip()) # Strip the newline characters before appending to the list
    return ana_list # Return stripped list



print(anagram_finder()) # Run the function
