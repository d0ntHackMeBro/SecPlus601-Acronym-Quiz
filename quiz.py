import json
import random


# Load acronyms to test from json file
with open('acronyms.json', 'r') as f:
    acronyms = json.load(f)
    wrong = {}


    # Get total length of dictionary
    dict_length = 0
    for k in acronyms:
        dict_length += len(acronyms[k])


    # Pages to test on
    choices = [c for c in acronyms]
    choices.insert(0, 'all')
    choice_str = ''
    choice_num = 0
    for c in choices:
        choice_str = f'{choice_str}{choice_num}) {c}\n'
        if c != choices[-1]:
            choice_num += 1

    # Prompt user to pick page to test on
    choice = input(f'\nEnter page to test on from this list:\n{choice_str}\nOr press enter for \'all\':\n')
    choice_not_made = True
    wrong_choice = False
    while choice_not_made:
        if wrong_choice:
            choice = input(f'\nPlease enter a valid page from this list:\n{choice_str}\nOr press enter for \'all\':\n')
        try:
            choice = int(choice)
            if choice > choice_num or choice < 0:
                wrong_choice = True
            else:
                choice = choices[choice]
                choice_not_made = False
        except:
            if choice == '':
                choice = 'all'
                choice_not_made = False
            elif choice not in choices:
                wrong_choice = True
            else:
                choice_not_made = False


    # Prompt user for total questions to be asked or default to 10 if nothing is entered
    try:
        if choice != 'all':
            total = int(input(f'\nEnter number of questions to ask. Must be <= {len(acronyms[choice])}: \n'))
            while total > len(acronyms[choice]):
                total = int(input(f'\nPlease enter a number <= {len(acronyms[choice])}: \n'))
        else:
            total = int(input(f'\nEnter number of questions to ask. Must be <= {dict_length}: \n'))
            while total > dict_length:
                total = int(input(f'\nPlease enter a number <= {dict_length}: \n'))
    except:
        if choice != 'all':
            total = len(acronyms[choice])
        else:
            total = dict_length


    # Create a score variable to incrememnt
    score = 0


    # Making a variable that can be decramented by one after each question
    questions = total


    # Generate quiz if choice is 'all'
    if choice == 'all':
        keys = []

        # Put all keys into a list and shuffle them
        for k in acronyms:
            for i in acronyms[k]:
                keys.append(i)
        random.shuffle(keys)

        for key in keys:
            if questions > 0:
                cat = ''
                for i in acronyms:
                    if key in acronyms[i]:
                        cat = i
                answer = input(f'\n{key}: \n')
                if answer.lower() == acronyms[cat][key].lower():
                    print('(CORRECT!) \n')
                    score += 1
                else:
                    print(f'(WRONG!) \n(ANSWER IS: {acronyms[cat][key]}) \n')
                    wrong[key] = acronyms[cat][key]
                questions -= 1
            else:
                break


    # Generate quiz if choice is a specific page
    else:


        # Place all keys from chosen dictionary into a list and shuffle them
        keys = []
        for key, value in acronyms[choice].items():
            keys.append(key)
        random.shuffle(keys)

        for key in keys:
            if questions > 0:
                answer = input(f'\n{key}: \n')
                if answer.lower() == acronyms[choice][key].lower():
                    print('(CORRECT!) \n')
                    score += 1
                else:
                    print(f'(WRONG!) \n(ANSWER IS: {acronyms[choice][key]}) \n')
                    wrong[key] = acronyms[choice][key]
                questions -= 1
            else:
                break


    # Print total score
    print(f'\nYOU GOT A TOTAL SCORE OF {score}/{total} \n')

    # Check to see if user wants to test on missed questions
    if score < total:
        try_again = input('\nWould you like to take a quiz on just the acronyms you got wrong? [y/n]: ').lower()
    else:
        exit()
    
    while True:
        if try_again not in ['n', 'y']:
            try_again = input('\nPlease enter either \'y\' or \'n\': ').lower()
        else:
            break
    
    if try_again == 'y':
        keys = [k for k in wrong]
        score = 0
        total = len(keys)
        for i in range(len(keys)):
            answer = input(f'\n{keys[i]}:\n')
            if answer.lower() == wrong[keys[i]].lower():
                print('(CORRECT!) \n')
                score += 1
            else:
                print(f'(WRONG!) \n(ANSWER IS: {wrong[keys[i]]}) \n')
        print(f'\nYOU GOT A TOTAL SCORE OF {score}/{total} \n')
    else:
        exit()