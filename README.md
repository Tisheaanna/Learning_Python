# Find_The_Biggest_Number
A small Python program that creates a list of random numbers and finds the biggest one, without using max().

# How it works
1. The program creates a list of 10 random numbers between 1 and 100.
2. It shows the list and the smallest number (with min()).
3. It compares the first two numbers of the list and removes the smaller one.
4. It repeats this until only one number is left: the biggest one.
5. It shows the result, and checks it with max().

Example:
```
[42, 7, 89, 15, 63, 3, 71, 28, 94, 50]
3
[94]
94
```

# How to run it
```
python find_the_biggest_number.py
```

# How I worked
I wrote all the project by myself, I used an AI assistant as a learning aid, the same way I would use documentation or a tutorial.

# What the AI helped me with:
- Explaining concepts I didn't know yet (e.g. random numbers, lists, while loops)
- Suggesting how to organise the project into steps
- Helping me understand error messages when I was stuck

# What I did myself:
- Wrote and tested every line of code
- Designed the logic to find the biggest number by comparing the numbers two by two
- Checked my result with Python's built-in min() and max()
- Fixed bugs, using the explanations to understand the cause
- Managed the project with Git (commits, branches)
# I can explain every part of this code and why it works the way it does.

# What I learned
- Generating random numbers with random.randint()
- Creating a list with a for loop and append()
- Using a while loop with a condition (len(Liste) > 1)
- Accessing list items with an index (Liste[0], Liste[1])
- Removing items from a list with remove()
- Using the built-in functions min() and max()
