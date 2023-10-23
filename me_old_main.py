#*Student Grade Calculation:*

#You have a list of student records with their names and scores in different subjects. Each student has taken a variable number of exams, and their scores are provided as a list of dictionaries. Write a Python program to calculate and display each student's average score across all exams, find the student with the highest average, and determine which subject(s) each student performed best in.

#Example Student Records:

#|   Name   |  Subject  |  Score  |              #Expected Output:
#|----------|-----------|---------|              #- Alice's average score across all exams is 91.67.
#|  Alice   |   Math    |   92    |              #- Bob's average score across all exams is 83.33.
#|  Alice   |  English  |   88    |              #- Charlie's average score across all exams is 88.33.
#|  Alice   |  Science  |   95    |              #- Alice has the highest average score.
#|   Bob    |   Math    |   78    |              #- Alice performed best in Science.
#|   Bob    |  English  |   82    |              #- Bob performed best in Science.
#|   Bob    |  Science  |   90    |              #- Charlie performed best in English.
#| Charlie  |   Math    |   88    |
#| Charlie  |  English  |   92    |
#| Charlie  |  Science  |   85    |

#sort each students score respectively

def student_grade(student_data):
  average = []

  for val in student_data.values():

    average.append(val)
    data_len = len(average)
    data_sum = sum(average)
    Alice_average_score = data_sum/data_len
    Bob_average_score = data_sum/data_len
    Charlie_average_score = data_sum/data_len


  data1 =  "Alice's average score across all exams is %.2f" % Alice_average_score 
  data2 = "Bob's average score across all exams is %.2f" % Bob_average_score
  data3 = "Charlie's average score across all exams is %.2f" % Charlie_average_score
  return data1, data2, data3


student1_data = {'Alice_math': 92, 'Alice_english': 88 , 'Alice_science': 95}
student2_data = {'Bob_math' : 78, 'Bob_english' : 82, 'Bob_science' : 90}
student3_data = {'Charlie_math' : 88, 'Charlie_english' : 92, 'Charlie_science': 85}

abc = student_grade(student1_data)
print(abc)



#write 3 sum function. one to sum only even number and second odd numbers, prime numbers

#list_to_sum = [1,2,3,4,5,6]

#example1: sum_even(1,2,3,4,5) #example:sum_prime(1,2,3,4,6,10)  #example2: sum_odd(1,2,3,4,5)
#example: sum_odd(1,2,3,4,6,7,16,17,18,31)

#sum_even()
#sum_odd()
#sum_prime()

def sum_even_numbers(*args):
  all_even = []
  for num in args:
    if num % 2 == 0:
      all_even.append(num)

  return sum(all_even)

integers = [1,2,3,4,5,6]  
abc = sum_even_numbers(*integers)
#print(abc)


def sum_odd_number(*args):
  all_odd = []
  for num in args:
    if num % 2 == 1:
      all_odd.append(num)

  return sum(all_odd)

xyz = sum_odd_number(*[1,2,3,4,5,6])
#print(xyz)


#test case
#all numbers are divisible by 1 and themselve
#prime number are divisible by other factors

def sum_prime_numbers(*args):
  #prime = True
  all_prime_numbers = []
  for num in args: 
    if num <= 1:
      pass
    if num > 1:

      for value in range(2, num):
        #get all number between 1 and num  
        if num % value  == 0:
          #factors found
          #prime = False
          break
      else: #if prime:
        all_prime_numbers.append(num)
    #prime = True    
  return sum(all_prime_numbers), "is the total sum of list prime number", *all_prime_numbers

total_sum = sum_prime_numbers(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
#print(total_sum)



#New Task
#Write a function to find the first non-repeating character in a string.

#Example String 1: hello    #String 2 : abracadabra    #String 3: aabbcc          #String 4: programming
#Expected: h                #Expected: c               #Expected: None            #Expected: p


def first_nonrepeat(string):
  check_char = {}
  for char in string:
    if char in check_char:
      check_char[char] = check_char[char] + 1

    else:
      check_char[char] = 1
  print(f"{check_char}")

#string = "characteristics"
#first_nonrepeat(string)



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

#replace_duplicate(string)

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



#New Task
#Problem:
#Use the Category and Miscelleneous list to categorise the items.
#Hint:
#Dictionary = {key:value}
#Dict = {Category:[items]}
#Categorised = {'fruit':['orange','pear'], 'sales':['56834']}

Category = ['fruit', 'sales', 'food', 'gadgets']

Miscelleneous = [
  'fruit orange', 'food Fried_rice', 'sales 34400', 'sales 56834',
  'gadgets PDA', 'fruit apple', 'fruit pear', 'food yam','gadgets Smart_Watch']


categorised_items = {}

for stuff in Category:
  categorised_items[stuff] = []

for items in Miscelleneous:
  stuff, content = items.split(" ")
  categorised_items[stuff].append(content)

#print(categorised_items)









#open = OpenFile()
#filename = 'Obj'
#object = open(filename, 'r')
#file_opened = open('sales.txt', 'r')



#old_main.py
#import file
#file = open('old_main.py', 'r')

#method: open()



#print('content of old_main.py below....')
#print('----\n' *10)
#print(file.read())


#'db.csv'
#new_file = open('db.csv', 'w')
#print(new_file.write())
#print(new_file.close())

#write the following to your db.csv file
#Olowogold is a programmer.
#he writes functions.
#he uses data structures.
#uses loops.
#uses variables.

content = open('db.csv', 'w')
content.write('olowogold is a programmer.\nhe writes functions.\nhe uses data structure\nuses loops\nuses variables.')
content.close()
#print('writing to file complete...')
#
read_file = open('db.csv', 'r')
#print(read_file.readlines())
#print(read_file.readline())
read_file.close()

#write the following lines
sentences = """\nSure, here's a content calendar for a TikTok account focused on reviewing real estate listings. You can adjust the posting frequency based on your availability and audience engagement:

Month: November 2023

Week 1: November 1 - 7

Monday: Introduction video - Briefly introduce yourself and the purpose of your TikTok account.
Wednesday: House Tour - Feature an interesting property with a detailed tour.
Friday: Q&A - Answer common real estate questions from your audience.
Week 2: November 8 - 14

Monday: Neighborhood Spotlight - Highlight a popular neighborhood with pros and cons.
Wednesday: Unique Features - Showcase a listing with unique or unusual features.
Friday: Budget-Friendly Options - Review affordable real estate listings.
Week 3: November 15 - 21

Monday: Investment Opportunities - Discuss potential real estate investments.
Wednesday: Tips & Tricks - Share tips for first-time homebuyers.
Friday: Realtor Interview - Feature an interview with a local real estate agent.
Week 4: November 22 - 28

Monday: Luxury Listings - Showcasing high-end real estate properties.
Wednesday: DIY Home Staging - Offer tips for staging a home for sale.
Friday: Live Q&A - Interact with your audience in a live session, answering their questions in real-time.
Remember to use relevant hashtags, engage with your audience's comments, and maintain a consistent posting schedule to grow your TikTok presence and engage with your real estate enthusiast audience."""

sentence_file = open('db.csv', 'a')
sentence_file.write(sentences)
sentence_file.close()
#context managment in file handling
