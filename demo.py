import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    # add a loop here that goes through all the vectors in x_train and finds the one that
    # is nearest to x_test. return the index (between 0, ..., len(x_train)-1) of the nearest
    # neighbor
    nearest_len = np.Inf
    nearest_index = -1
    index = 0
    for vector in x_train:
        if dist(vector, x_test) < nearest_len:
            nearest_len = dist(vector, x_test)
            nearest_index = index
        index += 1
    print(nearest_index)

nearest(x_train, x_test)

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