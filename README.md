# Virtual_Pet
A small virtual pet game in Python, played in the terminal.

You give a name to your little friend, then you take care of it by choosing actions (play, pet, feed, sleep...). Each action changes its happiness, and its mood changes with it.

# How to play
Run the script:
```
python virtual_pet.py
```
Give your pet a name, then type one of these commands:

| Command     | What it does                              | Happiness |
|-------------|-------------------------------------------|-----------|
| `play`      | Play ball with your pet                   | +2        |
| `pet`       | Pet your pet                              | +2        |
| `feed`      | Choose a food: cupcake, pizza, pancakes or burger | +3 |
| `sleep`     | Put your pet to bed                       | +1        |
| `beat`      | Not nice...                               | -2        |
| `!commands` | Show the list of commands                 | -         |
| `bye`       | Say goodbye and end the game              | -         |

# Mood levels
Happiness starts at 10. After each action, the pet tells you how it feels:
- 15 or more: Very Happy
- 10 to 14: Happy
- 5 to 9: Sad
- under 5: Very Sad

# How I worked
I wrote all the project by myself, I used an AI assistant as a learning aid, the same way I would use documentation or a tutorial.

# What the AI helped me with:
- Explaining concepts I didn't know yet (e.g. lists, while loops, f-strings)
- Suggesting how to organise the project into steps
- Helping me understand error messages when I was stuck

# What I did myself:
- Wrote and tested every line of code
- Designed the game logic (actions, happiness gauge and mood levels)
- Wrote the pet's dialogues and the commands menu
- Fixed bugs, using the explanations to understand the cause
- Managed the project with Git (commits, branches)
# I can explain every part of this code and why it works the way it does.

# What I learned
- Storing data in lists and tuples, and checking if a value is in a list with `in`
- Using a while loop that runs until the user types "bye"
- Using random.choice() to pick a random goodbye message
- Updating a variable with += and -= to manage a happiness gauge
- Using if / elif / else to turn a number into a mood
- Displaying variables in text with f-strings (f"Happiness: {Jauge_humeur}")
- Reading user input with input() and displaying results with print()