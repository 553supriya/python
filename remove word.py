def remove_word(str,word):
    str2=str.replace(word,'')
    return str2
str3="hello good morning hello hi hello"
print("before remove")
print(str3)
str4=remove_word(str3,"hello")
print("after remove")
print(str4)
