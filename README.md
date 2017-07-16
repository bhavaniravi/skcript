# Word Magic

Project built to perform the following task 
[Task specification](https://gist.github.com/swaathi/3356d2d2a1476be21f6938b77d61f82d)

### Requirements 

`Python 3.5`

### Project Structure 

```
Word Magic
 |__ Solution
 		|__ skcript.py
 		|__ cli.py
 |__ Tests
 		|__ test.py
 |__ Mainfest.in
 |__ README.md
 |__ requirements.txt
 |__setup.py
```

### Setup

1. Clone the project from `https://github.com/bhavaniravi/word_magic`
2. Create a virutalenv 
3. Install required packages using `pip install requirements.txt`

### Running the programm

1. To run the program you can run skcript.py
2. In use it in your python program use `magic` and `longest` as follows. Make sure your python file is in the same directory as `skcript.py`


```
from solution.skcript import Main
main = Main()
main.magic("abcd??","abcdef")
main.longest("????????????????")

```

### Command line tool

1. Clone the project from `https://github.com/bhavaniravi/word_magic`
2. `cd word_magic`
3. `python setup.py install`
4. To use magic command
	`magic -s "abcd??"  -w "abcdef"`
5. To use longest command 
	`longest -s "aa"`
