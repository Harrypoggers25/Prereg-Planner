class Kulliyah:
    def __init__(self):
        self.name = ""
        self.val = ""

class Session:
    def __init__(self):
        self.sem = ""
        self.year = ""

class Course:
    def __init__(self):
        self.param = ""
        self.title = ""
        self.code = ""
        self.sect = []

class CourseSection:
    def __init__(self):
        self.val = ""
        self.info = []

class CourseInfo:
    def __init__(self):
        self.day = ""
        self.time = ""
        self.lecturer = ""
        self.rect = []

    def updateDiscreteRects(self):
        n_time1 = CourseRect.parseTime(self.time, 0)
        n_time2 = CourseRect.parseTime(self.time, self.time.find('- ') + 2)
        n_time2 = n_time2 + 720 if n_time1 > n_time2 else n_time2

        n_time_const = CourseRect.getTimeOffset(self.time, n_time1, n_time2)

        n_time1 = n_time1 + n_time_const
        n_time2 = n_time2 + n_time_const

        n_y = n_time1
        n_h = (n_time2 - n_time1)

        dict_day_to_index = {
            'TUE': [1],
            'FRI': [4],
            'THUR': [3],
            'MON': [0],
            'WED': [2],
            'T-W': [1, 2],
            'W-TH': [2, 3],
            'TH-FRI': [3, 4],
            'MTWTHF': [0, 1, 2, 3, 4],
            'MTTHF': [0, 1, 3, 4],
            'M-W': [0, 3],
            'T-TH': [1, 3],
            'TUE-SUN': [1, 6],
            'SUN': [6],
            'M-TH': [0, 3],
            'MTWTH': [0, 1, 2, 3],
            'MTW': [0, 1, 2],
            'TWTH': [1, 2, 3],
            'SAT': [5],
            'M-F': [0, 4],
            'SUN-T': [1, 6],
            'SAT-SUN': [5, 6],
            'W-TH-F': [2, 3, 4]
        }

        for x in dict_day_to_index[self.day]:
            rect = CourseRect()
            rect.x = x
            rect.y = n_y
            rect.w = 0
            rect.h = n_h
            self.rect.append(rect)
    
    def clearRects(self):
        for rect in self.rect:
            rect.pop()

class CourseRect:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    @staticmethod
    def parseTime(time, offset):
        n_sum = 0
        n_carry = 0
        n_min_const = 60
        time = time[offset:]

        while True:
            if time[0] == ".":
                n_min_const = 1
                n_carry = n_sum
                n_sum = 0
            elif time[0] != " ":
                n_sum = n_sum * 10 + float(time[0]) * n_min_const
            else:
                return n_sum + n_carry
            time = time[1:]

    @staticmethod
    def getTimeOffset(str_time, n_time1, n_time2):
        if n_time1 > 720 or n_time2 > 720:
            n_time_const = 0
        else:
            n_time_const = 720 if str_time.find('PM') >= 0 else 0
                
            b_time1 = n_time1 + n_time_const > 0 and n_time1 + n_time_const < 480
            b_time2 = n_time2 + n_time_const > 0 and n_time2 + n_time_const < 480

            if b_time1 or b_time2:
                n_time_const = 720 if n_time_const == 0 else 720
        return n_time_const
    
    # @staticmethod
    # def isCollision(rect1, rect2):
    #     if rect1.x >= rect2.x + rect2.w:
    #         return False
    #     if rect1.x + rect1.w <= rect2.x:
    #         return False
    #     if rect1.y >= rect2.y + rect2.h:
    #         return False
    #     if rect1.y + rect1.h <= rect2.y:
    #         return False
    #     return True


                
        
