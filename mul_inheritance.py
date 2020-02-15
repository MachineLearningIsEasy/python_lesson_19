class Run:
    def can_run(self):
        return 'I can run'
    def sport(self):
        return 'Run'

class Swim:
    def can_swim(self):
        return 'I can swim'
    def sport(self):
        return 'Swim'

class Ride:
    def can_ride(self):
        return 'I can ride'
    def sport(self):
        return 'Ride'

class Triatlon( Swim, Run, Ride):
    pass

if __name__ == '__main__':
    a = Triatlon()
    print(isinstance(a, Run), isinstance(a, Swim), isinstance(a, Ride), isinstance(a, int))

    print(dir(a))

    print(a.sport())

    print(Triatlon.mro())