class Time:

    def __init__(self, hh=12, mm=0, s=0):
        '''(Time)-> None'''
        self.hour = hh
        self.minute = mm
        self.second = s

        self.setTime(self.hour,self.minute,self.second)

    def setTime(self, hh=12, mm=0, s=0):
        '''(Time)-> None'''
        
        if s>59:
            self.minute+=(self.second//60)
            self.second = self.second%60
        if mm>59:
            self.hour+=(self.minute//60)
            self.minute= self.minute%60
        if hh>23:
            self.hour = self.hour%24
