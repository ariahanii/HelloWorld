from time import sleep

result = input('What do you want to write?\n').lower()
letters = [',', '!', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#creating empty space for the word
# It's also appealing visually
word = list('')
for i in result:
    word.append('#')


result = list(result)

for i in range(len(result)):
    while True:
        if word[i] == result[i]:
            break
        for j in letters:
            word[i] = j
            print("".join(word))
            sleep(0.03)
            if word[i] == result[i]:
                break

#causing the command prompt not to close 
input('Press ENTER to exit')