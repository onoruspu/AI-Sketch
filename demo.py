# We could either have another program for training and then just import the values.
# Or we could have the training and the usage in the same program.
# But this would mean that the training is done everytime the program is run
# which doesn't really make sense. So storing the training values and
# then just importing those would make the most sense.

# Considering there are two choices (between Finnish and English), the
# random guessing accuracy would be 50%, so anything over that would
# be an improvement. But to be really useful the accuracy would need
# to be very high (over 99%).

# Get the user input
def user_input():
    print("Give the word you're interested in:", end=" ")
    word = input()
    return word

# Get number out of word
# This will be a huge problem. How are we supposed to represent words as
# numbers so that we can compare them?
# The current implementation is just something so the code can be run.
# It should not be that great of a choice. The summing loses
# very much information about the words and creates some cases
# where two very different words can have the same sum.
# On top of all the other problems it creates.
def word_as_number(word):
    # Gets the ASCII char nhei umber and sums those together.
    sum = 0
    for char in word:
        sum += ord(char)
    return sum

# k-nearest neighbour
def knn(word):
    word_number = word_as_number(word) # To represent words as numbers
    output = "nothing yet implemented... But have the 'value' of your word:"
    print("Output: ",output,word_number)
    pass

print("Starting AI-Sketch")
word = user_input()
knn(word)