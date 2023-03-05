import os, sys, pickle

class Workout:
    def __init__(self, date, month, year, time, duration, wo_type, cals_brn, notes):
        self.date = date
        self.time = time
        self.month = month
        self.year = year
        self.duration = duration
        self.wo_type = wo_type
        self.cals_brn = cals_brn
        self.notes = notes

    def __str__(self):
        return '\nDate: %s\nTime: %s\nDuration: %s\nType: %s\nCalories burned: %s\nNotes: %s\n' % (self.date,self.time,self.duration,self.wo_type,self.cals_brn,self.notes)

    def __repr__(self):
        return self.__str__()


class Workoutdb:
    def __init__(self, file = None):
        if file == None:
            print('Must provide a filename')
            return
        self.file = file
        if os.path.isfile(file):
            try:
                f = open(file, 'rb')
            except IOError:
                sys.stderr.write('Problem opening file %s' % file)
                return
            try:
                self.db = pickle.load(f)
                return
            except pickle.UnpicklingError:
                sys.stderr.write('Not a pickled database')
                return
            f.close()
        else:
            self.db = []


    def add(self, date, month, year, time, duration, wo_type, cals_brn, notes):
        self.db.append(Workout(date,month,year,time,duration, wo_type, cals_brn, notes))
            

    def store(self,file=None):
        try:
            f = open(self.file, 'wb')
        except IOError:
            sys.stderr.write('Problem opening file %s for write' % self.file)
            return
        pickle.dump(self.db, f)
        f.close()

    def __del__(self):
        if self.db:
            self.store()
