print()
with open("colors.txt") as color_file:
    for line in color_file:
        clean_line = line.strip()
        print(clean_line)

print()

with open("phrase.txt") as phrase_file:
    for line in phrase_file:
        words = line.split(" ")
        for word in words:
            print(word,end="-" )