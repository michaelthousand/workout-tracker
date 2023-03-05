import PySimpleGUI as sg
import workout_utils
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sg.theme('Reddit')

# Home screen
def win1():
    banner = sg.Text('Welcome to the Workout Tracker App!', font=('Helvetica', 20), size=20, expand_x=True, justification = 'center')
    file_text = sg.Text('Enter a username: ', expand_x=True)
    file_input = sg.Input(key='-FILE-')
    add_btn = sg.Button('Add a new entry', expand_x=True, font=('Helvetica', 12), key='-ADD-')
    stats_btn = sg.Button('View statistics', expand_x=True, font=('Helvetica', 12), key='-STATS-')
    day_btn = sg.Button('Check a certain day', expand_x=True, font=('Helvetica', 12), key='-DAY-')
    import_btn = sg.Button('Import from Excel', expand_x=True, font=('Helvetica', 12), key='-IMPORT-')
    export_btn = sg.Button('Export to CSV', expand_x=True, font=('Helvetica', 12), key='-EXPORT-')
    exit_btn = sg.Button('Exit', expand_x=True, font=('Helvetica', 12))
    layout = [ [banner],
            [file_text, file_input],
            [add_btn, stats_btn, day_btn],
            [import_btn, export_btn, exit_btn]]

    return sg.Window('Workout Tracker - Home', layout, size=(715,250), finalize = True, enable_close_attempted_event = True, icon='weights.ico')

# Add entry screen
def win2():
    sg.set_options(font='Helvetica')
    banner = sg.Text('Add a New Entry', font=('Helvetica', 20), size=20, expand_x=True, justification = 'center')
    date_text = sg.Text('Enter a date in the format MM/DD/YY: ', expand_x=True, font=('Helvetica', 12))
    date_input = sg.Input(key='-DATE-')
    time_text = sg.Text('Time of day: ', expand_x = True, font=('Helvetica', 12))
    r1 = sg.Radio('Morning', 'time', key='morning')
    r2 = sg.Radio('Afternoon', 'time', key='afternoon')
    r3 = sg.Radio('Evening', 'time', key='evening')
    r4 = sg.Radio('Night', 'time', key='night')
    dur_text = sg.Text('Enter a duration in minutes: ', expand_x=True, font=('Helvetica', 12))
    dur_input = sg.Input(key='-DUR-')
    type_text = sg.Text('Select the type of workout: ', expand_x=True, font=('Helvetica', 12))
    c1 = sg.Checkbox('Weights', key='-WEIGHTS-')
    c2 = sg.Checkbox('Cardio', key='-CARDIO-')
    c3 = sg.Checkbox('Hiking/Walking', key='-HIKING-')
    c4 = sg.Checkbox('Running', key='-RUN-')
    c5 = sg.Checkbox('Cycling', key='-CYCLING-')
    c6 = sg.Checkbox('Yoga', key='-YOGA-')
    c7 = sg.Checkbox('High-Intensity Interval Training (HIT)', key='-HIT-')
    c8 = sg.Checkbox('Hockey', key='-HOCKEY-')
    c9 = sg.Checkbox('Oculus', key='-OCULUS-')
    c10 = sg.Checkbox('Other', key='-OTHER-')
    cal_txt = sg.Text('Number of calories burned: ', expand_x=True, font=('Helvetica', 12))
    cal_input = sg.Input(key='-CAL-')
    notes_txt = sg.Text('Notes:', expand_x=True, font=('Helvetica', 12))
    notes_field = sg.Multiline(size= (70, 5), key='-NOTES-')
    entry_submit = sg.Button('Submit Workout', key='-SUBMIT-')
    exit_submit = sg.Button('Cancel', key='-CANCEL-')
    layout = [ [banner],
            [date_text, date_input],
            [time_text, r1, r2, r3, r4],
            [dur_text, dur_input],
            [cal_txt, cal_input],
            [type_text, c1,c2,c3,c4],
            [c5, c6, c7, c8, c9, c10],
            [notes_txt, notes_field],
            [entry_submit, exit_submit]
            ]
    return sg.Window('Workout Tracker - Add an Entry', layout, finalize=True, enable_close_attempted_event = True, element_justification='c', icon='weights.ico')

# View stats screen
def win3():
    banner = sg.Text('View statistics', font=('Helvetica', 20), size=20, expand_x=True, justification = 'center')
    avg_duration_btn = sg.Button('Average Workout Duration', key='-AVG-DUR-', expand_x=True)
    weekly_avg_btn = sg.Button('Weekly Averages', key = '-WEEK-AVG-', expand_x=True)
    month_wo_btn = sg.Button('Workouts by Month', key = '-WO-MONTH-',expand_x=True)
    year_wo_btn = sg.Button('Workouts by Year', key = '-WO-YEAR-', expand_x=True)
    wo_by_type_btn = sg.Button('Workouts by Type', key = '-WO-TYPE-',expand_x=True)
    txt1 = sg.Text(key='txt1')
    txt2 = sg.Text(key='txt2')
    txt3 = sg.Text(key='txt3')
    txt4 = sg.Text(key='txt4')
    txt5 = sg.Text(key='txt5')
    txt6 = sg.Text(key='txt6')
    txt7 = sg.Text(key='txt7')
    txt8 = sg.Text(key='txt8')
    txt9 = sg.Text(key='txt9')
    txt10 = sg.Text(key='txt10')
    txt11 = sg.Text(key='txt11')
    txt12 = sg.Text(key='txt12')
    txt13 = sg.Text(key='txt13')
    txt14 = sg.Text(key='txt14')
    txt15 = sg.Text(key='txt15')
    txt16 = sg.Text(key='txt16')
    txt17 = sg.Text(key='txt17')
    txt18 = sg.Text(key='txt18')
    txt19 = sg.Text(key='txt19')
    txt20 = sg.Text(key='txt20')
    txt21 = sg.Text(key='txt21')
    txt22 = sg.Text(key='txt22')
    txt23 = sg.Text(key='txt23')
    txt24 = sg.Text(key='txt24')

    layout = [ [banner],
            [avg_duration_btn, weekly_avg_btn, month_wo_btn, year_wo_btn, wo_by_type_btn],
            [txt1, txt2],
            [txt3, txt4],
            [txt5, txt6],
            [txt7, txt8],
            [txt9, txt10],
            [txt11, txt12],
            [txt13, txt14],
            [txt15, txt16],
            [txt17, txt18],
            [txt19, txt20],
            [txt21, txt22],
            [txt23, txt24],]
    
    return sg.Window('Workout Tracker - View Statistics', layout, finalize=True, enable_close_attempted_event = True, element_justification='c', icon='weights.ico')

# View certain day screen
def win4():
    banner = sg.Text('View a Certain Day', font=('Helvetica', 20), size=20, expand_x=True, justification = 'center')
    date_txt = sg.Text('Enter a date in the format MM/DD/YY: ', expand_x=True, font=('Helvetica', 12))
    date_srch = sg.Input(key='-DATE-SRCH-')
    srch_btn = sg.Button('Search', key='-SRCH-BTN-')
    wo_1_time_txt = sg.Text('Time of workout:', font=('Helvetica', 14), text_color='DarkBlue')
    wo_1_time = sg.Text('', key='-WO-1-TIME-', font=('Helvetica', 12))
    wo_1_dur_txt = sg.Text('Duration:', font=('Helvetica', 14), text_color='DarkBlue')
    wo_1_dur = sg.Text('', key='-WO-1-DUR-', font=('Helvetica', 12))
    wo_1_cals_txt = sg.Text('Calories burned:', font=('Helvetica', 14), text_color='DarkBlue')
    wo_1_cals = sg.Text('', key='-WO-1-CALS-', font=('Helvetica', 12))
    wo_1_type_txt = sg.Text('Workout type:', font=('Helvetica', 14), text_color='DarkBlue')
    wo_1_type = sg.Text('', key='-WO-1-TYPE-', font=('Helvetica', 12))
    wo_1_notes_txt = sg.Text('Notes:', font=('Helvetica', 14), text_color='DarkBlue')
    wo_1_notes = sg.Text('', key='-WO-1-NOTES-', font=('Helvetica', 12))

    layout = [[banner],
            [date_txt, date_srch, srch_btn],
            [wo_1_time_txt, wo_1_time],
            [wo_1_dur_txt, wo_1_dur], 
            [wo_1_cals_txt, wo_1_cals],
            [wo_1_type_txt, wo_1_type],
            [wo_1_notes_txt, wo_1_notes],]
    return sg.Window('Workout Tracker - View Certain Day', layout, finalize=True, enable_close_attempted_event = True, element_justification='c', icon='weights.ico')

window1 = win1()
window2 = None

# Main program loop
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        try:
            window.close()
            print('User exit command')
        except AttributeError:
            exit()
    if window == window2:
        window2 = None

    # Launches the add entry window
    if event == '-ADD-': 
        # Ensures the file name isn't blank
        if values['-FILE-'] != '':
            window2 = win2()
            file = values['-FILE-'] + '.pickle'
        else:
            sg.popup('Please enter a save file name')


    # Launches the stats window
    elif event == '-STATS-':
        # Ensures the file name isn't blank
        if values['-FILE-'] != '':
            window2 = win3()
            file = values['-FILE-'] + '.pickle'
        else:
            sg.popup('Please enter a save file name')

    
    # Launches the search for day window
    elif event == '-DAY-':
        # Ensures the file name isn't blank
        if values['-FILE-'] != '':
            window2 = win4()
            file = values['-FILE-'] + '.pickle'
        else:
            sg.popup('Please enter a save file name')

    
    # When the user hits the submit button, takes the values from the form and passes them to function that enters them in the db
    # Also checks for bad enteries
    if event == '-SUBMIT-':
        date = values['-DATE-']
        if values['morning'] == True:
            time = 'morning'
        elif values['afternoon'] == True:
            time = 'afternoon'
        elif values['evening'] == True:
            time = 'evening'
        elif values['night'] == True:
            time = 'night'

        wo_type = []
        if values['-WEIGHTS-'] == True:
            wo_type.append('weights')
        if values['-CARDIO-'] == True:
            wo_type.append('cardio')
        if values['-HIKING-'] == True:
            wo_type.append('hiking/walking')
        if values['-RUN-'] == True:
            wo_type.append('running')
        if values['-CYCLING-'] == True:
            wo_type.append('cycling')
        if values['-YOGA-'] == True:
            wo_type.append('yoga')
        if values['-HIT-'] == True:
            wo_type.append('HIT')
        if values['-HOCKEY-'] == True:
            wo_type.append('hockey')
        if values['-OCULUS-'] == True:
            wo_type.append('oculus')
        if values['-OTHER-'] == True:
            wo_type.append('other')
        
        wo_type = ', '.join(wo_type)
           
        duration = values['-DUR-']
        cals_brn = values['-CAL-']
        notes = str(values['-NOTES-'])

        if len(date) == 8 and date[:2].isnumeric() and date[3:5].isnumeric() and date[6:].isnumeric() and int(date[:2]) > 0 and int(date[:2]) < 13 and int(date[3:5]) > 0 and int(date[3:5]) < 32 and int(date[6:]) > 19 and int(date[6:]) < 24:
            if time == 'morning' or time == 'afternoon' or time == 'evening' or time == 'night':
                if values['-DUR-'].isnumeric():
                    if values['-CAL-'] != '':
                        if wo_type != '':
                            sg.popup('Thank you for your submission!')
                            workout_utils.add_entry(file, date, time, duration, wo_type, cals_brn, notes)
                            window.close()
                        else:
                            sg.popup('Please enter at least one type of workout')
                    else:
                        sg.popup('Please enter the number of calories burned.\nEnter "NA" if not tracked for this workout.')
                else:
                    sg.popup('Please enter a valid workout duration.')
            else:
                sg.popup('Please make a time selection.')
        else:
            sg.popup('Please enter a valid date.')
    # Checks if the user hit the cancel button and verifies their selection
    elif event == '-CANCEL-':
        if sg.popup_yes_no('Are you sure you want to cancel?') == 'Yes':
            window.close()
    

    # Runs if the user hits the average duration button
    if event == '-AVG-DUR-':
        avgs = workout_utils.wo_duration(file)
        window['txt1'].update('Overall average workout duration:')
        window['txt2'].update(avgs[0])
        window['txt3'].update('2020 average workout duration:')
        window['txt4'].update(avgs[1])
        window['txt5'].update('2021 average workout duration:')
        window['txt6'].update(avgs[2])
        window['txt7'].update('2022 average workout duration:')
        window['txt8'].update(avgs[3])
        window['txt9'].update('2023 average workout duration:')
        window['txt10'].update(avgs[4])
        window['txt11'].update('')
        window['txt12'].update('')
        window['txt13'].update('')
        window['txt14'].update('')
        window['txt15'].update('')
        window['txt16'].update('')
        window['txt17'].update('')
        window['txt18'].update('')
        window['txt19'].update('')
        window['txt20'].update('')
        window['txt21'].update('')
        window['txt22'].update('')
        window['txt23'].update('')
        window['txt24'].update('')

    # Runs if the user hits the monthly total button    
    if event == '-WO-MONTH-':
        months = workout_utils.wo_months(file)
        window['txt1'].update('January:')
        window['txt2'].update(months[0])
        window['txt3'].update('February:')
        window['txt4'].update(months[1])
        window['txt5'].update('March:')
        window['txt6'].update(months[2])
        window['txt7'].update('April:')
        window['txt8'].update(months[3])
        window['txt9'].update('May:')
        window['txt10'].update(months[4])
        window['txt11'].update('June:')
        window['txt12'].update(months[5])
        window['txt13'].update('July:')
        window['txt14'].update(months[6])
        window['txt15'].update('August:')
        window['txt16'].update(months[7])
        window['txt17'].update('September:')
        window['txt18'].update(months[8])
        window['txt19'].update('October:')
        window['txt20'].update(months[9])
        window['txt21'].update('November:')
        window['txt22'].update(months[10])
        window['txt23'].update('December:')
        window['txt24'].update(months[11])
    
    # Runs if the user hits the yearly total button
    if event == '-WO-YEAR-':
        years = workout_utils.wo_year(file)
        window['txt1'].update('Overall total:')
        window['txt2'].update(years[0])
        window['txt3'].update('2020 total:')
        window['txt4'].update(years[1])
        window['txt5'].update('2021 total:')
        window['txt6'].update(years[2])
        window['txt7'].update('2022 total:')
        window['txt8'].update(years[3])
        window['txt9'].update('2023 total:')
        window['txt10'].update(years[4])
        window['txt11'].update('')
        window['txt12'].update('')
        window['txt13'].update('')
        window['txt14'].update('')
        window['txt15'].update('')
        window['txt16'].update('')
        window['txt17'].update('')
        window['txt18'].update('')
        window['txt19'].update('')
        window['txt20'].update('')
        window['txt21'].update('')
        window['txt22'].update('')
        window['txt23'].update('')
        window['txt24'].update('')

    # Runs if the user hits the weekly averages button
    if event == '-WEEK-AVG-':
        avgs = workout_utils.weekly_avgs(file)
        window['txt1'].update('Overall weekly average:')
        window['txt2'].update(avgs[0])
        window['txt3'].update('2020 weekly average:')
        window['txt4'].update(avgs[1])
        window['txt5'].update('2021 weekly average:')
        window['txt6'].update(avgs[2])
        window['txt7'].update('2022 weekly average:')
        window['txt8'].update(avgs[3])
        window['txt9'].update('2023 weekly average:')
        window['txt10'].update(avgs[4])
        window['txt11'].update('')
        window['txt12'].update('')
        window['txt13'].update('')
        window['txt14'].update('')
        window['txt15'].update('')
        window['txt16'].update('')
        window['txt17'].update('')
        window['txt18'].update('')
        window['txt19'].update('')
        window['txt20'].update('')
        window['txt21'].update('')
        window['txt22'].update('')
        window['txt23'].update('')
        window['txt24'].update('')

    # Runs if the user hits the workout by type button
    if event == '-WO-TYPE-':
        types = workout_utils.wo_by_type(file)
        window['txt1'].update('Weights total:')
        window['txt2'].update(types[0])
        window['txt3'].update('Cardio total:')
        window['txt4'].update(types[1])
        window['txt5'].update('Hiking/Walking total:')
        window['txt6'].update(types[2])
        window['txt7'].update('Running total:')
        window['txt8'].update(types[3])
        window['txt9'].update('Cycling total:')
        window['txt10'].update(types[4])
        window['txt11'].update('Yoga total:')
        window['txt12'].update(types[5])
        window['txt13'].update('HIT total:')
        window['txt14'].update(types[6])
        window['txt15'].update('Hockey total:')
        window['txt16'].update(types[7])
        window['txt17'].update('Oculus total:')
        window['txt18'].update(types[8])
        window['txt19'].update('Other total:')
        window['txt20'].update(types[9])
        window['txt21'].update('')
        window['txt22'].update('')
        window['txt23'].update('')
        window['txt24'].update('')
    
    # Runs when they hit the search button to view a certain day
    if event == '-SRCH-BTN-':
        srch_date = values['-DATE-SRCH-']
        info = workout_utils.search(file, srch_date)
        window['-WO-1-TIME-'].update(info[0])
        window['-WO-1-DUR-'].update(str(info[1]) + ' minutes')
        window['-WO-1-CALS-'].update(info[2])
        window['-WO-1-TYPE-'].update(info[3])
        window['-WO-1-NOTES-'].update(info[4])

    # Runs when the user hits the import from file button
    if event == '-IMPORT-':
        # Ensures the file name isn't blank
        if values['-FILE-'] != '':
            file = values['-FILE-'] + '.pickle'
            file_name = sg.popup_get_text('Enter a filename to import:', title='File Selection')
            workout_utils.import_file(file, file_name)
            sg.popup('Import complete!')
        else:
            sg.popup('Please enter a username.')
    
    # Runs when the user hites the export to file button
    if event == '-EXPORT-':
        # Ensures the file name isn't blank
        if values['-FILE-'] != '':
            file = values['-FILE-'] + '.pickle'
            file_name = sg.popup_get_text('Enter a filename to export:', title='File Selection')
            check = workout_utils.export_file(file, file_name)
            if check == 'error':
                sg.popup('Error! The chosen filename already exists!')
            else:
                sg.popup('Export complete!')
        else:
            sg.popup('Please enter a username.')





