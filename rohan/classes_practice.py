'''
Classes practice problem:

Create a class called 'Time'
initialize it with hours, minutes, seconds
have a function add_time(self,  t2) which returns self + t2 time
'''

#creating class 'Time'
class Time:

    #initializing the class with default value 0:0:0
    def __init__(self, h = 0, m = 0, s =0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    #creating the x:x:x format for display
    def __str__(self):
        return '{}:{}:{}'.format(self.hours, self.minutes, self.seconds)

    #creating the add_time function

    def add_time(self, t2):
        #initializing the new time
        new = Time()

        #calculating new seconds value
        new.seconds = self.seconds + t2.seconds
        if (new.seconds >= 60):
            new.minutes += 1
            new.seconds = new.seconds - 60

        #calculating new minutes value
        new.minutes = new.minutes + self.minutes + t2.minutes
        if (new.minutes >= 60):
            new.hours += 1
            new.minutes = new.minutes - 60

        #calculating new hours value
        new.hours = new.hours + self.hours + t2.hours
        if (new.hours >= 24):
            new.hours = new.hours - 24

        #returning the new time
        return new


if __name__ == '__main__':

    #input prompts
    h1 = int(input('Enter hours: '))
    m1 = int(input('Enter minutes: '))
    s1 = int(input('Enter seconds: '))
    h2 = int(input('Enter hours: '))
    m2 = int(input('Enter minutes: '))
    s2 = int(input('Enter seconds: '))

    #assigning the times
    t1 = Time(h1, m1, s1)
    t2 = Time(h2, m2, s2)



    print('times added =', t1.add_time(t2))
