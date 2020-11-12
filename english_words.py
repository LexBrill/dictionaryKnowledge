import random

## To use: Type either 0 or just press enter if you don't know a word or press 1 if you do.
## See what percent of the English dictionary you know.

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line

total = 0
correct = 0
known = ""
while True:
    f = open("dictionary.txt", "r")
    print(random_line(f), end = "")
    known = input()
    if known == "1":
        correct += 1
    total += 1
    print(str((correct/total) * 100) + "% known. " + str(correct) + " out of " + str(total))