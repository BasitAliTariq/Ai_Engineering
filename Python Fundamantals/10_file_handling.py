# create a new file and write some content to it

# f=open("11_example_file.txt","w")
# f.write('Helo from file handling');
# f.close()


# append mode
# f=open("11_example_file.txt","a")
# f.write('I am basit ali tariq a softweare engineer');
# f.close()

# output Helo from file handlingI am basit ali tariq a softweare engineer



# appending in new line
# f=open("11_example_file.txt","a")
# f.write('\nI am currently working at techClan');
# f.close()



# reading content from file

# f=open("11_example_file.txt","r")
# print(f.read())
# f.close()



# Reading  from file line by line


# We want to create new file that has all the lines in 11_example_file.txt  plus word count for each line


# f=open("11_example_file.txt","r")
# f_out=open("12_word_count.txt","w")
# for line in f:
#     words=line.split(' ') # It gives array of words
#     f_out.write(" wordcount :"+str(len(words))+" " +line)

# f.close()
# f_out.close()


# with statement

with open("12_word_count.txt", "r") as file:
    print(file.read())

