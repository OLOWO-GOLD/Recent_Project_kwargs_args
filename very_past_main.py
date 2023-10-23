#New Task
#Write a function to find the first non-repeating character in a string.
#Example String 1: hello
#Expected: h
#String 2 : abracadabra
#Expected: c
#String 3: aabbcc
#Expected: None
#String 4: programming
#Expected: p

#def non_character(string):
  #store_char = []
  #for char in string:


  #new_char.append(char)
  #print(new_char)    


#string = "characteristics"

#non_character(string)


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

freq_word(sentence)





#2. Write a function to capitalize the first letter of each word in a given string

def capitalize_letter(sentence):
  new_string = []
  for char in sentence.split(" "):
    capitalized = char.capitalize()
    new_string.append(capitalized)
    capitalize_letter = " ".join(new_string)
  print(capitalize_letter)


sentence  = "The beginning of the world, God proclaimed let there be light\n" 

#capitalize_letter(sentence)





#3. Write a function that takes a string as input and returns a new string where each word is reversed.

def reverse(string):
  previous_string = ""
  for word in string:
    previous_string = word + previous_string
  return previous_string


#integrated code
def inverted_string(sentence):
  reversed_string = ""
  for word in sentence.split(" "):
    string = word
    reversed = reverse(string)
    reversed_string = reversed_string+ " " +reversed
  print(reversed_string)

sentence  = "The beginning of the world, God proclaimed let there be light"  
#inverted_string(sentence)




#cd ..
#mkdir linear-redo
#cd linear-redo
#git init
#git remote add origin https://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@github.com/OLOWO-GOLD/function_assignments.git
#echo "Readme file" > README.md
#echo "#python file" > main.py
#git add .
#git commit -m "whatever"
#git branch -M main
#git push -u origin main






