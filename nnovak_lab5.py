# Nicholas Novak
# Introduction to Python course assignment


#Open the included file
dictionary_file = open("lab5_dictionary.txt","r")
dictionary_file.readlines()



# Find the longest word in the dictionary, with a catch.  We want all words that tie the longest word in length, not merely the longest word.  Let's store them in a list.  
# The dictionary text file has each line ending with a newline character '\n'.  
# As you add the words to the list, we can remove that pesky newline character by using rstrip() on the string.  

## Created function:
def long_word(file_name):
    with open(file_name, 'r') as infile:
        words = infile.read().split()
        #Found this technique from an online source. Seems like an effecient way to make sure a program closes
        #automatically after using it
    max_len = len(max(words, key=len))
    #Create an integer that is the maximum length of the words iterated over. The key parameter is used to return 
    #the length of the sorted words without having to use extra lines to do so
    return[i for i in words if len(i) == max_len]
    #Return the word is the length of the word is the maximum length



long_word("lab5_dictionary.txt")



# Now, go through the dictionary and find the word(s) that contain the most unique letters. 
# For example between racecar and boats, racecar contains 4 (r-a-c-e) letters vs boats (b-o-a-t-s) so we would want boats over racecar.  
# We will use the same criteria as above where we want a list of all words that tie the criteria of involving the most letters.


#All letters of alphabet as a string
import string
alphabet_string = string.ascii_lowercase
print(alphabet_string)


# Function to open the file
def open_dict(filename):

    with open(filename, 'r') as f:
        words = f.readlines()
        #Open file and close when done

    return words

#Function to determine the amount of unique characters in a word
def uniqueness(word):

    uniques = set()
    #Using a set here allows the formation of a series of string swith no repeats. In this case, it is more efficient than a clunky loop block.
    
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

# Finally, let's determine if an anagram of a user input exists.
# 
# We can check if an an anagram exists by sorting the word we are looking at and comparing against another word.  
# The function, **is_anagram** was provided. Sorting a word and sorting the word we want to compare against is a very nice easy way to see if we have an anagram.
# 
# Take in a user word (don't worry about error checking) and see if an anagram exists in the dictionary.  
# Little bit of a tricky detail, if a user enters a certain word in, what must you do to make sure it's actually an anagram of the entered word?  
# Recommend using .lower() or .upper() to handle case sensitivity.  Print out each and every word that is anagram of the entered word and not the entered word.  
# If no anagrams are found, report "no anagrams were found!"
# 
# **if the user enters rat, the dictionary will find 'art\n' (length of 4 characters).  Since we have a bigger string, there's no way to build an anagram since the user didn't enter the newline character **
# 
# For testing your function the following words do have anagrams in this dictionary:
# 
# 1) restful
# 
# 2) bluster
# 
# 3) binary
# 
# Return all anagrams found.


#Provided function
def is_anagram(string1,string2):
    #Determines if a sorted word is equal to another sorted word. Basically, is it an anagram?
    return sorted(string1) == sorted(string2)




#Provided function name for anagram finder
def anagram_finder():
    with open("lab5_dictionary.txt", 'r') as infile2:
        dictionary_file_2 = infile2.readlines()
    user_input = input("Please enter the word you would like to find an anagram for:")
    print("anagrams below:\n\n")
   
#Create list for results
    ana_list = []
    for s in dictionary_file_2:
        #Check if a word is an anagram
        if is_anagram(s,user_input+"\n") == True:
            
            #Display found string
            print(s)
            
            #Strip the newline characters before appending to the list
            ana_list.append(s.rstrip())
    return ana_list



print(anagram_finder())