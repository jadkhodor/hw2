file= open("this.txt","r")
text= file.read()
print(text)
for char in (',.?!-'):
    text=text.replace(char,"")

text=text.lower()

word_list = text.split()

w = {}
for word in word_list:
    w[word] = w.get(word, 0) + 1
file.close()
print(w)