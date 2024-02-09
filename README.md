# CompTIA Security+ SY0-601 Acronyms Quiz

This is a Python script meant to be executed within the terminal, that generates a quiz using the acronyms listed on the CompTIA Security+ Exam SY0-601 exam objectives. The questions are generated randomly for each quiz so you won't get them in a specific order.

**How to run**

1. Navigate to the directory in your terminal/CLI that holds the _quiz.py_ file and the _acronyms.json_ file.
2. Run the script using the command _python3 quiz.py_ or _python quiz.py_ depending on how you have your path set up (You must have Python3 installed in order to use this script).
3. Once the script runs, you will be prompted to enter a number associated with which page of the acronyms you would like to be quized on (In the actual objectives document, there are four consecutive pages of acronyms in alphabetical order and the pages here are split up the same way). Each page has anywhere from roughly 70-90 acronyms. If you enter "0" or just press the enter key without entering a number, you will get acronyms from all of the pages.
4. Next you will be prompted to enter the number of questions you would like to be asked. The max number you are able to choose will be shown, based on which pages you chose to be quized on. If you press enter without entering a number, the max number will be chosen.
5. When you press enter after a question, your answer will be submitted even if you haven't entered anything.
6. When you finish the quiz, you will be asked wether or not you would like to retake a quiz just on the questions you got wrong. Enter "y" for yes or "n" for no.

**Notes**

- The answers are case-insensitive but punctuation does matter.
- The way I generally do it in the beginning is I just press enter after each question once I've guessed and I don't worry about the actual score. Once I've seen all of the answers enough times and understand how they're written specifically I will start trying to type them in correctly.
