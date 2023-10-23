Category = ['fruit', 'sales', 'food', 'gadgets']

Miscelleneous = [
  'fruit orange', 'food Fried_rice', 'sales 34400', 'sales 56834',
  'gadgets PDA', 'fruit apple', 'fruit pear', 'food yam','gadgets Smart_Watch']

#Problem:
#Use the Category and Miscelleneous list to categorise the items.
#Hint:
#Dictionary = {key:value}
#Dict = {Category:[items]}
#Categorised = {'fruit':['orange','pear'], 'sales':['56834']}

categorised_items = {}

# Add categories to empty dictionary
for category in Category:
    categorised_items[category] = []

# Categorize the items
for items in Miscelleneous:
    category, content = items.split(' ')
    categorised_items[category].append(content)

#print(categorised_items)





#Write a function that will replace duplicates numbers in a string with _ and leave only the last item

#Example 1     #Example 2     #Example 3    #Example 4
#11234         #112233        #22344        #2345
#Answer        #Answer        #Answer       #Answer
#_1234         #_1_2_3        #_23_4        #2345

def replace_duplicate(string):
  previous_char = ""
  substitute_char = "_"
  lis = []

  for next_char in string:
    if previous_char == next_char:
      previous_char = substitute_char + next_char
      lis.append(previous_char) 
    else:
      previous_char = next_char
    data = " ".join(lis)
  print(data)  

string = "AABBCCDDEEFFGGHHII112233445566778899"

replace_duplicate(string)





#New Task
#Write a function to find the first non-repeating character in a string.

#Example String 1: hello    #String 2 : abracadabra    #String 3: aabbcc          #String 4: programming
#Expected: h                #Expected: c               #Expected: None            #Expected: p



def non_repeat(string):
  check_char = ""
  lis = []
  for char in string:


string = "characteristics"
non_character(string)



#1.Write a function that takes a sentence as input and returns the most frequent word in the sentence.

def freq_word(sentence):
  store_freq = {}
  for word in sentence.split(" "):
    if word in store_freq:
      store_freq[word] = store_freq[word] + 1
    else:
      store_freq[word] = 1
  print(f"{store_freq}")

sentence = "Peter Parker is not the same as Peter Pan."

#freq_word(sentence)






