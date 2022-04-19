import json
# after program works for one file, run a for loop for all files in the subdirectory
# start = 636
# end = 715
# base_file = "199920000AB"
# for num in range(start, end+1):
#   file = base_file + str(num) + ".txt" 
#   ...
# file descriptor to open file for reading
info = {"Date": None, "Legislator":None} #add attributes to this python object (dict)
# add other attributes to analyze, ex: did bill get majority of vote, 
# does it need appropriation, is it a local program
# party of legislator that proposed the bill, bill text, topic of bill and etc...

fo = open("199920000AB700.txt") #open and read file descriptor
num = 700 #last 3 digits of bill text
string = fo.read()
arr = string.split(" ") #split string into a list of words
arr_without_empty = [e for e in arr if e] #removes spaces from initial array
unwanted_words = ["\xc2", "\xa0", "\xe2", "\n", "\x80", "\x93", "\x94", "."] #filler words we want to remove
monthes = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
first_date = False; #boolean if we encountered a date yet
legislator = False; #boolean if we encountered a legislator yet

for i in range(len(arr_without_empty)):
  new_word = arr_without_empty[i]
  for word in unwanted_words: #delete parts of word that are in unwanted_words
    new_word = new_word.replace(word, "")
  arr_without_empty[i] = new_word

  if not first_date: # check if this is the date of the bill
    for month in monthes:
      if month in new_word:
        first_date = True
        info["Date"] = new_word
        break
  
  if not legislator: #check if we encountered a legislator yet
    if len(new_word) > len(str(num)) and len(new_word) < len(str(num)) + 4 and str(num) in new_word:
      legislator = True
      if arr_without_empty[i+1] == "as":
        info["Legislator"] = arr_without_empty[i+3]
      else:
        info["Legislator"] = arr_without_empty[i+1]
      break

ret = json.dumps(info) #final json object
print(ret)
