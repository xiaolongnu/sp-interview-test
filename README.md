# sp-interview-test

## Brief introduction & approach

##### Programming lanaguage: python
##### Version: 2.7
##### External Libaries: pandas

The python programminglanaugage was chosen because its my most fluent language at the moment and host a compresensive range of libraries.

The first thing that comes to my mind was to select to a suitable data structure to present the keypad.
It have to quickly look up values given a word or number and fairly easy to use.
Hence, the dataframe data structure was selected, which represents the properties of the keypad in a tabular form.

pandas library is utilise to provide the dataframe data structure for this program.
### The dataframe consists of 3 columns which represents:
	* Numbers in the keypad
	* Letters associated with the number 
	* Key presses needed to enter the letter

The total number of rows is about 26 which consist of all the letters.
The table can view in `numpad.csv` file.

### Approach for each question
#### Question 1:
Simply use the dataframe to look up the keypresses for each letter in the input then sum them.

##### Question 2:
Similiar to question 1, look up the number keys based on the letters from the input then string them together.

##### Question 3:
Utilise "product" function from the itertools module in python standard library to perform permutation.
Since the function allows indefinite amount of arguments, can just supply a list which contains list of letters from each each number in the input 

##### Question 4:
Stores the words dictionary in a "set" data strucuture, which works like a hash table, hence able to search quickly for words in the dictionary.
Get a list of all possible words based on the input by calling question 3's function.
Perform set's intersection operation against the said list and words dictionary, which results in only words from the list and words dictionary.


## Installation & Usage

### Manual installation

Make a new virtualenv for the project, install pandas, run:

    pip install -r requirements.txt


Syntax to execute the program:

    python main.py q<question no.> <input>

Example:

	python main.py q1 hello  #Output: 13
	python main.py q2 hello  #Output: 43556
	python main.py q3 23  	 #Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
	python main.py q4 2355	 #Output: ['cell', 'bell']


### Docker installation
Start the Docker program then build the image:

	docker build -t sp-interview-test .


Syntax to execute the program:

	docker run sp-interview-test python main.py q<question no.> <input>

Example:

	docker run sp-interview-test python main.py q1 hello  #Output: 13
	docker run sp-interview-test python main.py q2 hello  #Output: 43556
	docker run sp-interview-test python main.py q3 23     #Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
	docker run sp-interview-test python main.py q4 2355   #Output: ['cell', 'bell']
