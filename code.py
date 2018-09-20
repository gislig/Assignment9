f = open("test.txt","r")
f_str = str(f.read())
print(f_str.replace("\n","").replace(" ",""))
f.close()