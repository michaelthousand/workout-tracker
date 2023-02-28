import time, workoututils, pickle
from workoutdb import Workout, Workoutdb

user_input = ''
file = ('Workouts.pickle')
wdb = Workoutdb(file)

while user_input != 'exit':
    print('Welcome to the workout tracker app!')
    print('Option 1: Add a new entry\nOption 2: Check statistics\nOption 3: View a certain day')
    user_input = input('\nWhich of the above would you like to do? Enter exit to end: ')
    if user_input.lower() == 'exit':
        print('Goodbye')
        time.sleep(2)
        break
    elif user_input == '1':
        workoututils.add_entry()
    elif user_input == '2':
        workoututils.stats()
    elif user_input == '3':
        srch = input('Please enter a date to search for: ')
        time.sleep(1)
        workoututils.search(srch)
        time.sleep(1)
    elif user_input == '9':
        with open(file, 'rb') as f:
            workout_list = pickle.load(f)
            for workout in workout_list:
                print(workout)
    else:
        print('\nInvalid selection. Please try again.\n')
