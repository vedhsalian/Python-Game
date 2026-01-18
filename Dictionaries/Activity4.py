def char_frequency(s):
    texts={}
    for character in s:
        if character != " ":
            if character in texts:
                texts[character]+=1
            else:
                texts[character]=1
    return (texts)

s1=input("Enter your text")

answer=char_frequency(s1)

print (answer)