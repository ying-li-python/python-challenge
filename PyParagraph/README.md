# PyParagraph 

Suppose you want to assess the complexity of a written passage (whether it is for peer-reviewed research or for assessing high students' essays). Let's create a simple metric to analyze a single paragraph. 

This folder contains the script that prints out the word count, sentence count, average sentence length, and average letter count.

## Getting Started 
You will need to provide a paragraph saved as a text file. In this case, we have an example passage saved in [paragraph.txt](https://github.com/ying-li-python/python-challenge/blob/master/PyParagraph/paragraph.txt). 

Example passage: 
> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”

## Demostration 

For a passage, we would like to know: 
- Total word count 
- Total number of sentences 
- Average sentence length
- Average letter count

For this python script, we created lists and for-loops, ```.split()``` and ```len()``` function, the re module for [regular expressions](https://docs.python.org/3/library/re.html), and the csv module to write our results. 


To run the script: 
```
cd PyParagraph 
python main.py 
```

Example results in terminal:

<img src="https://raw.githubusercontent.com/ying-li-python/python-challenge/master/PyParagraph/Images/results.png">

