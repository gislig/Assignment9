
#Longest word is 'innflutningstollum' of length 18
lastword_count = 0
longestword_count = 0
longestword_char = ""
with open("words.txt", 'r', encoding='utf-8') as longword:
    for word in longword:
        lastword_count = int(len(word.replace("\n","")))
        if longestword_count < lastword_count:
            longestword_count = lastword_count
            longestword_char = word.replace("\n","")

print("Longest word is '" + longestword_char + "' of length",longestword_count)