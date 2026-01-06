words = []
inp = input("Enter words, enter a blank space to stop: ")
while inp != "":
    words.append(inp)
    inp = input("Enter words, enter a blank space to stop: ")

new_words = []

for a in words:
    if a not in new_words:
        new_words.append(a)
        print(a)
