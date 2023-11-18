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
        self.sects = []

class CourseSection:
    def __init__(self):
        self.val = ""
        self.infos = []

class CourseInfo:
    def __init__(self):
        self.day = ""
        self.time = ""
        self.lecturer = ""

class CourseTable:
    def __init__(self, s_code, sect):
        self.code = s_code
        self.sect = sect.val  # string form
        self.vrects = [[],[]]

        n_rects = []
        for info in sect.infos:
            n_rect = Rect()

            n_time1 = CourseTable.parseTime(self.time, 0)
            n_time2 = CourseTable.parseTime(self.time, self.time.find('- ') + 2)
            n_time2 = n_time2 + 720 if n_time1 > n_time2 else n_time2

            n_time_const = CourseTable.getTimeOffset(self.time, n_time1, n_time2)

            n_time1 = n_time1 + n_time_const
            n_time2 = n_time2 + n_time_const

            dict_dtoi = {       # dtoi = day to index
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

            for x in dict_dtoi[self.day]:
                n_rect = Rect()
                n_rect.x = x
                n_rect.y = n_time1
                n_rect.w = 0
                n_rect.h = n_time2 - n_time1

                n_rects.append(n_rect)

            self.vrects.append(n_rects)

    @staticmethod
    def isTablesCollide(table1, table2):  # must be in discrete form
        for rects1 in table1.vrects:
            for rect1 in rects1:
                for rects2 in table2.vrects:
                    for rect2 in rects2:
                        if rect1.x == rect2.x:
                            b_case1 = rect1.y >= rect2.y and rect1.y < rect2.y + rect2.h # rect1 overlap rect2
                            b_case2 = rect2.y >= rect1.y and rect2.y < rect1.y + rect1.h # rect2 overlap rect1
                            if b_case1 or b_case2:
                                return True
        return False

    @staticmethod
    def getParseTime(s_time, n_offset):
        n_sum = 0
        n_carry = 0
        n_min_const = 60
        s_time = s_time[n_offset:]

        while True:
            if s_time[0] == ".":
                n_min_const = 1
                n_carry = n_sum
                n_sum = 0
            elif s_time[0] != " ":
                n_sum = n_sum * 10 + float(s_time[0]) * n_min_const
            else:
                return n_sum + n_carry
            s_time = s_time[1:]

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

class Rect:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
    
class Counter:
    def __init__(self, varrs, start_offset):
        self.counter = [0] * len(varrs)
        self.counter[0] = start_offset if start_offset < len(self.counter[0]) else 0
        self.limit = [0] * len(varrs)

        for i in range(len(varrs)):
            self.limit[i] = len(varrs[i])

    def increment(self):
        for i in range(len(self.counter)):
            if self.counter[i] + 1 < self.limit[i]:
                self.counter[i] += 1
                return True
            else:
                self.counter[i] = 0
        return False
    
    def get(self, index):
        return self.counter[index]

    def reset(self):    # Unused function
        for i in range(len(self.counter)):
            self.counter[i] = 0