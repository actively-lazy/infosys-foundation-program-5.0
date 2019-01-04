import random
import re
def word_scrambler(normal_word):
    scrambled_word = ""
    while normal_word:
        index = random.randrange(len(normal_word))
        scrambled_word += normal_word[index]
        normal_word = normal_word[:index] + normal_word[index + 1:]
    return scrambled_word

try:
    normal_text_file_path = input("Enter the path of the file you want to scramble: ")
    normal_text_file = open(normal_text_file_path,"r")
    words = normal_text_file.read()
    normal_text_file.close()

    words_list = words.split(" ");
    punctuations = (',','?','.',';','!')
    scrambled_words = ""
    scrambled_word = ""

    for word in words_list:
        if len(word)<3 or (len(word)==4 and (word[len(word)-1] in punctuations)):
            scrambled_word = word
        else:
            if word[len(word)-1] in punctuations:
                scrambled_word = word_scrambler(word[1:len(word) - 2])
                scrambled_word = word[0] + scrambled_word + word[len(word)-2]+word[len(word)-1]
            else:
                scrambled_word = word_scrambler(word[1:len(word) - 1])
                scrambled_word = word[0] + scrambled_word + word[len(word)-1]
        scrambled_words += scrambled_word +" "

    normal_text_file_path_split = normal_text_file_path.split("\\")
    scrambled_text_file_path = ""
    for p in range(0,len(normal_text_file_path_split)-1):
        scrambled_text_file_path += normal_text_file_path_split[p] + "\\"
    scrambled_text_file_path += "scrambled_text.txt"

    scrambled_text_file =open(scrambled_text_file_path,"w")
    scrambled_text_file.write(scrambled_words)
    scrambled_text_file.close()

except PermissionError:
        print("Error occured in getting permission")
except IOException:
        print("Error occured in file")



