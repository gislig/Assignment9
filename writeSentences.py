sentence = ""
longword = open("words.txt", 'r', encoding='utf-8')
for word in longword:
    word = word.replace("\n"," ")
    if word in ' .':
        sentence += word + "\n"
    else:
        sentence += word
longword.close()

new_file = open("sentences.txt", 'w')
new_file.write(sentence)
new_file.close()

print(sentence)