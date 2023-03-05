import pickle
from workoutdb import Workoutdb
from datetime import date
import pandas as pd
from pathlib import Path

# Function for adding a new entry to the database
def add_entry(file, date, timeday, duration, wo_type, cals_brn, notes):
    wdb = Workoutdb(file)
    if len(date) == 8 and date[:2].isnumeric() and date[3:5].isnumeric() and date[6:].isnumeric() and int(date[:2]) > 0 and int(date[:2]) < 13 and int(date[3:5]) > 0 and int(date[3:5]) < 32 and int(date[6:]) > 19 and int(date[6:]) < 24: 
        month = date[:2]
        year = date[6:]
    wdb.add(date, month, year, timeday, duration, wo_type, cals_brn, notes)
    
# Function for getting the average durations
def wo_duration(file):
    with open(file, 'rb') as f:
        workouts = pickle.load(f)
        total = 0
        total_20 = 0
        num_20 = 0
        total_21 = 0
        num_21 = 0
        total_22 = 0
        num_22 = 0
        total_23 = 0
        num_23 = 0

        for workout in workouts:
            total = total + int(workout.duration)
            if workout.year == '20':
                total_20 = total_20 + int(workout.duration)
                num_20 += 1
            elif workout.year == '21':
                total_21 = total_21 + int(workout.duration)
                num_21 += 1
            elif workout.year == '22':
                total_22 = total_22 + int(workout.duration)
                num_22 += 1
            elif workout.year == '23':
                total_23 = total_23 + int(workout.duration)
                num_23 += 1
        
        if num_20 == 0:
            avg_20 = 0
        else:
            avg_20 = round((total_20 / num_20), 2)
        
        if num_21 == 0:
            avg_21 = 0
        else:
            avg_21 = round((total_21 / num_21), 2)
        
        if num_22 == 0:
            avg_22 = 0
        else:
            avg_22 = round((total_22 / num_22), 2)

        if num_23 == 0:
            avg_23 = 0
        else:
            avg_23 = round((total_23 / num_23), 2)

        avg = round((total / len(workouts)), 2)
        
        return avg, avg_20, avg_21, avg_22, avg_23

# Function for getting the workouts by month
def wo_months(file):
    with open(file, 'rb') as f:
        workouts = pickle.load(f)
        jan = 0
        feb = 0
        mar = 0
        apr = 0
        may = 0
        jun = 0
        jul = 0
        aug = 0
        sep = 0
        oct = 0
        nov = 0
        dec = 0

        for workout in workouts:
            if workout.month == '01':
                jan += 1 
            elif workout.month == '02':
                feb += 1
            elif workout.month == '03':
                mar += 1
            elif workout.month == '04':
                apr += 1
            elif workout.month == '05':
                may += 1
            elif workout.month == '06':
                jun += 1
            elif workout.month == '07':
                jul += 1
            elif workout.month == '08':
                aug += 1
            elif workout.month == '09':
                sep += 1
            elif workout.month == '10':
                oct += 1
            elif workout.month == '11':
                nov += 1
            elif workout.month == '12':
                dec += 1
    
    return jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec

# Function for getting the workouts by year
def wo_year(file):
    with open(file, 'rb') as f:
        workouts = pickle.load(f)
        total = len(workouts)
        twenty_20 = 0
        twenty_21 = 0
        twenty_22 = 0
        twenty_23 = 0

        for workout in workouts:
            if workout.year == '20':
                twenty_20 += 1 
            elif workout.year == '21':
                twenty_21 += 1
            elif workout.year == '22':
                twenty_22 += 1
            elif workout.year == '23':
                twenty_23 += 1 
    
    return total, twenty_20, twenty_21, twenty_22, twenty_23
                
# Function for getting weekly averages
def weekly_avgs(file):
    with open(file, 'rb') as f:
        workouts = pickle.load(f)
        twenty_20 = 0
        twenty_21 = 0
        twenty_22 = 0
        twenty_23 = 0

        for workout in workouts:
            if workout.year == '20':
                twenty_20 += 1 
            elif workout.year == '21':
                twenty_21 += 1
            elif workout.year == '22':
                twenty_22 += 1
            elif workout.year == '23':
                twenty_23 += 1 

        avg_20 = twenty_20 / 52
        avg_20 = round(avg_20, 2)
        avg_21 = twenty_21 / 52
        avg_21 = round(avg_21, 2)
        avg_22 = twenty_22 / 52
        avg_22 = round(avg_22, 2)
            
        weeks = 0
        day = str(date.today())
        if day[5:7] == '01' and int(day[8:]) < 8:
            weeks = 1
        elif day[5:7] == '01' and int(day[8:]) < 15:
            weeks = 2
        elif day[5:7] == '01' and int(day[8:]) < 22:
            weeks = 3
        elif day[5:7] == '01' and int(day[8:]) < 29:
            weeks = 4
        elif day[5:7] == '01' and int(day[8:]) < 32 or day[5:7] == '02' and int(day[8:]) < 5:
            weeks = 5
        elif day[5:7] == '02' and int(day[8:]) < 12:
            weeks = 6
        elif day[5:7] == '02' and int(day[8:]) < 19:
            weeks = 7
        elif day[5:7] == '02' and int(day[8:]) < 26:
            weeks = 8
        elif day[5:7] == '02' and int(day[8:]) < 29 or day[5:7] == '03' and int(day[8:]) < 5:
            weeks = 9
        elif day[5:7] == '03' and int(day[8:]) < 12:
            weeks = 10
        elif day[5:7] == '03' and int(day[8:]) < 19:
            weeks = 11
        elif day[5:7] == '03' and int(day[8:]) < 26:
            weeks = 12
        elif day[5:7] == '03' and int(day[8:]) < 32 or day[5:7] == '04' and int(day[8:]) < 2:
            weeks = 13
        elif day[5:7] == '04' and int(day[8:]) < 9:
            weeks = 14
        elif day[5:7] == '04' and int(day[8:]) < 16:
            weeks = 15
        elif day[5:7] == '04' and int(day[8:]) < 23:
            weeks = 16
        elif day[5:7] == '04' and int(day[8:]) < 30:
            weeks = 17
        elif day[5:7] == '04' and int(day[8:]) < 31 or day[5:7] == '05' and int(day[8:]) < 7:
            weeks = 18
        elif day[5:7] == '05' and int(day[8:]) < 14:
            weeks = 19
        elif day[5:7] == '05' and int(day[8:]) < 21:
            weeks = 20
        elif day[5:7] == '05' and int(day[8:]) < 28:
            weeks = 21
        elif day[5:7] == '05' and int(day[8:]) < 32 or day[5:7] == '06' and int(day[8:]) < 4:
            weeks = 22
        elif day[5:7] == '06' and int(day[8:]) < 11:
            weeks = 23
        elif day[5:7] == '06' and int(day[8:]) < 18:
            weeks = 24
        elif day[5:7] == '06' and int(day[8:]) < 25:
            weeks = 25
        elif day[5:7] == '06' and int(day[8:]) < 31 or day[5:7] == '07' and int(day[8:]) < 2:
            weeks = 26
        elif day[5:7] == '07' and int(day[8:]) < 9:
            weeks = 27
        elif day[5:7] == '07' and int(day[8:]) < 16:
            weeks = 28
        elif day[5:7] == '07' and int(day[8:]) < 23:
            weeks = 29
        elif day[5:7] == '07' and int(day[8:]) < 30:
            weeks = 30
        elif day[5:7] == '07' and int(day[8:]) < 32 or day[5:7] == '08' and int(day[8:]) < 6:
            weeks = 31
        elif day[5:7] == '08' and int(day[8:]) < 13:
            weeks = 32
        elif day[5:7] == '08' and int(day[8:]) < 20:
            weeks = 33
        elif day[5:7] == '08' and int(day[8:]) < 27:
            weeks = 34
        elif day[5:7] == '08' and int(day[8:]) < 32 or day[5:7] == '09' and int(day[8:]) < 3:
            weeks = 35
        elif day[5:7] == '09' and int(day[8:]) < 10:
            weeks = 36
        elif day[5:7] == '09' and int(day[8:]) < 17:
            weeks = 37
        elif day[5:7] == '09' and int(day[8:]) < 24:
            weeks = 38
        elif day[5:7] == '09' and int(day[8:]) < 31:
            weeks = 39
        elif day[5:7] == '10' and int(day[8:]) < 8:
            weeks = 40
        elif day[5:7] == '10' and int(day[8:]) < 15:
            weeks = 41
        elif day[5:7] == '10' and int(day[8:]) < 22:
            weeks = 42
        elif day[5:7] == '10' and int(day[8:]) < 29:
            weeks = 43
        elif day[5:7] == '10' and int(day[8:]) < 32 or day[5:7] == '11' and int(day[8:]) < 5:
            weeks = 44
        elif day[5:7] == '11' and int(day[8:]) < 12:
            weeks = 45
        elif day[5:7] == '11' and int(day[8:]) < 19:
            weeks = 46
        elif day[5:7] == '11' and int(day[8:]) < 26:
            weeks = 47
        elif day[5:7] == '11' and int(day[8:]) < 31 or day[5:7] == '12' and int(day[8:]) < 3:
            weeks = 48
        elif day[5:7] == '12' and int(day[8:]) < 10:
            weeks = 49
        elif day[5:7] == '12' and int(day[8:]) < 17:
            weeks = 50
        elif day[5:7] == '12' and int(day[8:]) < 24:
            weeks = 51
        elif day[5:7] == '12' and int(day[8:]) < 31:
            weeks = 52
                    
        avg_23 = twenty_23 / weeks
        avg_23 = round(avg_23, 2) 

        # Determines how many years worth of data the user has inputed before returning their overall weekly average
        if twenty_20 != 0 and twenty_21 != 0 and twenty_22 != 0 and twenty_23 != 0:
            overall_total = len(workouts)
            total_weeks = weeks + 156
            overall_avg = round((overall_total / total_weeks), 2)
        elif twenty_21 != 0 and twenty_22 != 0 and twenty_23 != 0:
            overall_total = len(workouts)
            total_weeks = weeks + 104
            overall_avg = round((overall_total / total_weeks), 2)
        elif twenty_22 != 0 and twenty_23 != 0:
            overall_total = len(workouts)
            total_weeks = weeks + 52
            overall_avg = round((overall_total / total_weeks), 2)
        elif twenty_23 != 0:
            overall_avg = avg_23

        
    return overall_avg, avg_20, avg_21, avg_22, avg_23   

# Function for viewing workouts by type
def wo_by_type(file):
    cardio_count = 0
    weights_count = 0
    oculus_count = 0
    other_count = 0
    hiking_count = 0
    run_count = 0
    yoga_count = 0
    hit_count = 0
    hockey_count = 0
    cycling_count = 0
    with open(file, 'rb') as f:
        workouts = pickle.load(f)
        for workout in workouts:
            if 'weights' in workout.wo_type.lower():
                weights_count += 1
            if 'cardio' in workout.wo_type.lower():
                cardio_count += 1
            if 'hiking' in workout.wo_type.lower():
                hiking_count += 1
            if 'running' in workout.wo_type.lower():
                run_count += 1
            if 'cycling' in workout.wo_type.lower():
                cycling_count += 1
            if 'yoga' in workout.wo_type.lower():
                yoga_count += 1
            if 'HIT' in workout.wo_type.lower():
                hit_count += 1
            if 'hockey' in workout.wo_type.lower():
                hockey_count += 1
            if 'oculus' in workout.wo_type.lower():
                oculus_count += 1
            if 'other' in workout.wo_type.lower():
                other_count += 1  
    return weights_count, cardio_count, hiking_count, run_count, cycling_count, yoga_count, hit_count, hockey_count, oculus_count, other_count   

# Function for searching for a particular date        
def search(file, date):
    with open(file, 'rb') as f:
        workouts = pickle.load(f)
        timeday = ''
        dur = ''
        cal = ''
        wo_type = ''
        notes = ''
        for workout in workouts:
            if date == workout.date:
                timeday = workout.time
                dur = workout.duration
                cal = workout.cals_brn
                wo_type = workout.wo_type
                notes = workout.notes
    return timeday, dur, cal, wo_type, notes

# Not used in app - prints data to console in order to check enteries
def viewall():
    with open('test_import.pickle', 'rb') as f:
        workouts = pickle.load(f)
        for workout in workouts:
            print(workout)

# set pandas options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# set pandas option to display full contents of each cell
pd.set_option('display.max_colwidth', None)

# Function for importing from file
def import_file(file, file_name):
    path = Path(file)
    df = pd.read_excel(file_name + '.xlsx')
    wdb = Workoutdb(file)
    rows = []

    for index, row in df.iterrows():
        rows.append(row.tolist())

    for row in rows:
        old_date=str(row[0])[:10]
        new_date = old_date[5:7] + '/' + old_date[8:10] + '/' + old_date[2:4]
        month = old_date[5:7]
        year = old_date[2:4]
        timeday = row[1]
        duration = row[2]
        wo_type = row[3]
        cals_brn = row[4]
        notes = row[5]

        # Checks to see if the save file exists - if not, creates it. If it does, checks to make sure the imported file isn't already imported
        if path.is_file():
            with open(file, 'rb') as f:
                workouts = pickle.load(f)

            # Used to cycle through each entry in the database and each entry in the file to make sure there are not duplicates
            already_exists = False
            for workout in workouts:
                if workout.date == new_date:
                    already_exists = True
                    break
            if not already_exists:
                wdb.add(new_date, month, year, timeday, duration, wo_type, cals_brn, notes)
                
        else:
            wdb.add(new_date, month, year, timeday, duration, wo_type, cals_brn, notes)
    
    return

# Function for exporting to file
def export_file(file, file_name):
    path = Path(file)
    file_name = file_name + '.csv'
    path2 = Path(file_name)
    if path.is_file():
        if path2.is_file():
            return 'error'
        else:
            with open(file, 'rb') as f:
                workouts = pickle.load(f)
                lst = [[x.date, x.time, x.duration, x. wo_type, x.cals_brn, x.notes] for x in workouts]
                df = pd.DataFrame(lst, columns=['Date', 'Time', 'Duration', 'Workout Type', 'Calories Burned', 'Notes'])
                df.to_csv(file_name, index=False)
            return 'success'
