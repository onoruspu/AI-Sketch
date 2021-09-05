## Info

Hello!

This is my AI project inspired by [Elements of AI](https://www.elementsofai.com).

Below you will some sketching and thinking about a potential AI project.

# AI-Sketch
Building AI course project

Learning to create an AI project.

## Summary
The idea for this AI project is using artificial intelligence to determine if a given word is in either Finnish or English. Will be using common words for training data and k-nearest neighbours algorithm (k-NN) for the calculations. See below for more details.

## Background
For Finnish people it's somewhat common (my observation) to sometimes unintentionally and without noticing type English words in Finnish texts or vice versa Finnish words in English texts. So a modification of this AI that automatically scans the text being written could notice the writer that the language of some words isn't the same as the text is otherwise. This would be a further implementation, the start is to just categorize or give probabilities for one word.

## How is it used?
User starts the program which is trained by AI. User enters the word (or words) which they are interested in knowing if they're Finnish or English. The assumption is that the word is either Finnish or English so other inputs aren't controlled. Then the program can either categorize the word to Finnish or English or it could be done to tell the probability for that, whichever is more likely. The details will be fine tuned when (and if) this is implemented in real life.

## Data sources and AI methods
For training we need some word data. With quick search I found two lists that claim to contain the 1000 most common words in English and Finnish (I have no way to guarantee these are the most common ones). Check Acknowledgments for sources. The data could be split to training and testing data for example 900 to 100. The problem can be thought to be a classification problem so an algorithm for that is what we're looking for. One relatively simple one is the nearest neighbours algorithm (k-NN). So that would be the first one to be implemented.

## Challenges
The data set contains only 1000 words in both languages which isn't that much considering how much words there are. But also using all the words would mean the task isn't about using artificial intelligence. We could also argue that the most common words aren't the best ones, rather some rarer and more obscure words could be better with training. Common words have the tendency to be somewhat short(no source for this - sadly) and maybe not the best for categorising. Also if using the nearest neighbours algorithm the k value could be finetuned with experiments and educational guesses. So there exists easy ways to improve this. The AI is also very limited handling only two languages out of the thousands there are. And also only in written form. Still this isn't a worthless project.

## What next?
Check Challenges for ways to improve the AI. Next would be to create some kind of code sketching and thinking, maybe even some working demo or similar things. I would do this myself with Python because that is the language I have learned. Also looking for more resources about AIs, generally about Python programming, maybe connecting with other people and asking for help with other things could further this project. But the main obstacle is most likely time, finding the desire and hours for this project. So most of this is just sketching and nothing too real yet, still useful with teaching.

## Demo
The file demo.py contains some Python code sketching for a possible implementation. The code can be run at the momement but doesn't do anything meaningful.

## Acknowledgments
This project and the structure of this README is inspired by [Elements of AI](https://www.elementsofai.com).

AI training data for Finnish from [1000 Most Common Words](https://1000mostcommonwords.com/1000-most-common-finnish-words/). And AI training data for English from [WordExample](https://www.wordexample.com/list/most-common-words-1k).

Thank you everyone for your assistance (you know who you are).