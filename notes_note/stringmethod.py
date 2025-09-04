# AS 2nd String Methods notes

# .strip() gets rid of extar spaces on either side (not in middle)
# .lower() makes all lower case
# .upper() makes all upper case
# .capitalize() makes first letter capital
# .title() makes first of each word capital
# .isdigit() checks if is digit
# .find() finds where a word starts in an index
# .replace[word to replace:replacing with]
# "string{}" .format(amount of {} as specified variables)
# f"string{varible}" does same thing as .format





sentence = "The quick brown fox jumps over the lazy dog."
word = input("gimme a word")
start = sentence.find(word)
length = len(word)
print(sentence[start:start + length])