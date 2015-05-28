
# Sentence splitting to words function
def split2words (input_string):
    return input_string.split()


sentence = "We Like Code"
wordsArray = split2words(sentence)

# Print result
for i in wordsArray:
    print(i)

