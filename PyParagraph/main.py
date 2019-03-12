# import dependencies 
import os
import re

# open and read text file containing paragraph 

file = open("paragraph.txt", "r")

# create empty list for words and letter count set at 0 

word_list = []
letter_total = 0

# create for loop, to iterate each word in the txt file 
for char in file: 

    # create a list of words by split() function 
    word_list = char.split()

    # count the number of words in the paragraph
    word_count = len(word_list)

    # use re to split the paragraph into distinct sentences (which ends by ?!.)
    sentence = re.split("(?<=[.!?]) +", char)

    # count the number of sentences in the paragraph
    sentence_count = len(sentence)

    # create for loop to count the letters for each word 
    for word in word_list:

        # calculate the length for each word and the sum of letters 
        word_length = len(word)
        letter_total += word_length

    for words in sentence: 
        sentence_length = len(sentence)

# solution to calculate average letter count 
letter_count = letter_total / word_count

# solution to calculate the average sentence length 
final_sentence_length = word_count / sentence_count
        
# print results in terminal 
print("Paragraph Analysis")
print("----------------")
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Sentence Count: {sentence_count}')
print(f'Average Letter Count: {letter_count}')
print(f'Average Sentence Length: {final_sentence_length}')