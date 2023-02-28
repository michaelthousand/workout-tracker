import time, pickle
from workoutdb import Workout, Workoutdb
file = ('Workouts.pickle')
wdb = Workoutdb(file)

# Function for adding a new entry to the database
def add_entry():
    print('\nPreparing new form. Please wait.')
    time.sleep(1)

    while True:
        try:
            file = ('Workouts.pickle')
            wdb = Workoutdb(file)
            while True:
                date = input('Please enter a date in the format MM/DD/YY: ')
                if len(date) == 8 and date[:2].isnumeric() and date[3:5].isnumeric() and date[6:].isnumeric() and int(date[:2]) > 0 and int(date[:2]) < 13 and int(date[3:5]) > 0 and int(date[3:5]) < 32 and int(date[6:]) > 19 and int(date[6:]) < 24: 
                    month = date[:2]
                    year = date[6:]
                    break
                else:
                    print('\nInvalid date: date must be in the MM/DD/YY format\n')
            
            while True:
                timeday = input('\nPlease enter a time of day (morning, afternoon, evening, night): ')
                if timeday == 'morning' or timeday == 'afternoon' or timeday == 'evening' or timeday == 'night':
                    break
                else:
                    print('\nInvalid time selection. Please try again.\n')

            while True:
                duration = input('\nPlease enter a duration in minutes: ')
                if duration.isnumeric():
                    break
                else:
                    print('\nInvalid duration entry. Please try again.\n')

            while True:
                wo_type = input('\nEnter a workout type (cardio, weights, oculus, other): ')
                if wo_type == 'cardio' or wo_type == 'weights' or wo_type == 'oculus' or wo_type == 'other':
                    break
                else:
                    print('\nInvalid entry. Please try again.\n')

            print('\nProcessing...Please wait...')
            time.sleep(2)
            print('\n\nHere are your inputs:')
            print('Date:', date)
            print('Time:', timeday)
            print('Duration:', duration)
            print('Type:', wo_type)
            repeat = input('\nIs the above information correct? ')
            if repeat.lower() == 'y' or repeat.lower() == 'yes':
                print("\nThank you for your submission! You will now be returned to the main menu.")
                time.sleep(2)
                print("\n\n")
                wdb.add(date, month, year, timeday, duration, wo_type)
                break
            else:
                print('\nResetting...\n')
                time.sleep(2)
            

            
        except ValueError:
            print("Error. Please try again.")
            continue


# Function for searching for a particular date        
def search(date):
    with open(file, 'rb') as f:
        workouts = pickle.load(f)
        for workout in workouts:
            if date == workout.date:
                print(workout)


# Function for printing statistics
def stats():
    while True:
        print('''Please select which statistics you would like to view:\n
Option 1 - Average workout duration\nOption 2 - Workouts by type\nOption 3 - Workouts by month\nOption 4 - Workouts by year\nOption 5 - exit''')
        option = input('> ')
        with open(file, 'rb') as f:

            # Prints the average workout duration overall
            if option == '1':
                workouts = pickle.load(f)
                total = 0
                for workout in workouts:
                    total = total + int(workout.duration)
                
                print('\nAverage workout duration: %.2f minutes' % (total / len(workouts)), '\n')

            # Prints the workouts by type
            elif option == '2':
                cardio_count = 0
                weights_count = 0
                oculus_count = 0
                other_count = 0
                workouts = pickle.load(f)
                for workout in workouts:
                    if workout.wo_type == 'cardio':
                        cardio_count += 1
                    elif workout.wo_type == 'weights':
                        weights_count += 1
                    elif workout.wo_type == 'oculus':
                        oculus_count += 1
                    elif workout.wo_type == 'other':
                        other_count += 1
                print('\nCardio:', cardio_count)
                print('Weights:', weights_count)
                print('Oculus:', oculus_count)
                print('Other:', other_count, '\n')

            # Prints the number of workouts by month
            elif option == '3':
                jan = 0
                feb = 0
                mar = 0
                workouts = pickle.load(f)
                for workout in workouts:
                    if workout.year == '23':
                        if workout.month == '01':
                            jan += 1
                        elif workout.month == '02':
                            feb += 1
                        elif workout.month == '03':
                            mar += 1
                print('\nJanuary:', jan)
                print('February:', feb)
                print('March:', mar, '\n')

            # Prints the number of workouts by year
            elif option == '4':
                twenty20 = 0
                twenty21 = 0
                twenty22 = 0
                twenty23 = 0
                workouts = pickle.load(f)
                for workout in workouts:
                    if workout.year == '20':
                        twenty20 += 1
                    elif workout.year == '21':
                        twenty21 += 1
                    elif workout.year == '22':
                        twenty22 += 1
                    elif workout.year == '23':
                        twenty23 += 1
                print('\n2020:', twenty20)
                print('2021:', twenty21)
                print('2022:', twenty22)
                print('2023:', twenty23, '\n')

            # Exits the statistics menu
            elif option == '5' or option.lower() == 'exit':
                break
            else:
                print('\nInvalid selection. Please try again.\n')
            
    
