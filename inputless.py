from time import sleep

letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = list('###########')
result = list("hello world")

# 11 is the number of letters in hello world
for i in range(11):
    while True:
        if word[i] == result[i]:
            break
        for j in letters:
            word[i] = j
            print("".join(word))
            sleep(0.05)
            if word[i] == result[i]:
                break
