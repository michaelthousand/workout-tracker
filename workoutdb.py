import os, sys, string, re, pickle

class Workout:
    def __init__(self, date, month, year, time, duration, wo_type):
        self.date = date
        self.time = time
        self.month = month
        self.year = year
        self.duration = duration
        self.wo_type = wo_type

    def __str__(self):
        return '\nDate: %s\nTime: %s\nDuration: %s\nType: %s\n' % (self.date,self.time,self.duration,self.wo_type)

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


    def add(self, date, month, year, time, duration, wo_type):
        self.db.append(Workout(date,month,year,time,duration, wo_type))

    
    def search(self, date='', time='', duration='', wo_type=''):
        results = []
        if date:
            found = Sessiondb.search(date)
            results.extend(found)
        if wo_type:
            srch = re.compile(laid,re.I)
            found = []
            for item in self.db:
                if srch.search(item.wo_type):
                    found.append(item)
            results.extend(found)
        return results
            

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
            
    # Not working
    def __getitem__(self,key):
        try:
            index = int(key)
            return self.db[index]
        except ValueError:
            found = 0
            for item in self.db:
                if item.date == key:
                    found = 1
                    return item
            if not found:
                raise KeyError(key)

        
