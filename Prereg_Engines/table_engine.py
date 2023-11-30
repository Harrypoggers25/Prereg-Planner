import copy, math

from Prereg_Engines.models import CourseTable, Counter, Text
from HP_Framework.objects import  HpRgbColor
from Prereg_Engines.models import Vector2n

class TableEngine():
    def __init__(self):
        self.total_ch = 0
        self.vtblcourses = [] # stores 2d list of courses sorted by section
        self.vcombinations = [] # stores 2D list of course combinatons
        self.vvrects = []
        self.texts = []
        self.bselected_courses = [] # list of boolean
        self.index = 0
        self.color = [
            HpRgbColor(238, 36, 36),    # RED
            HpRgbColor(239, 81, 34),    # ORANGE
            HpRgbColor(22, 87, 143),    # BLUE
            HpRgbColor(20, 175, 74),    # GREEN
            HpRgbColor(173, 20, 175),   # PURPLE
            HpRgbColor(0, 94, 33),      # D_GREEN
            HpRgbColor(80, 100, 0),     # D_YELLOW
            HpRgbColor(2, 183, 164),    # D_CYAN
            HpRgbColor(175, 92, 37),    # MUD
            HpRgbColor(239, 88, 61),    # CARROT
            HpRgbColor(50, 80, 140),    # P_BLUE
            HpRgbColor(241, 85, 98),    # P_RED
        ]

    def setVTblCourses(self, vtblcourses, n_chs, bselected_courses = None):
        self.vtblcourses = vtblcourses
        self.bselected_courses = bselected_courses if bselected_courses else [True] * len(self.vtblcourses)

        for i in range(len(n_chs)):
            if self.bselected_courses[i]:
                self.total_ch += n_chs[i]

        if len(self.color) < len(self.vtblcourses):
            n_diff = len(self.vtblcourses) - len(self.color)
            self.color.extend(self.color[:n_diff])

        self.generateVCombinations()

    def setBSelectCourses(self, bselected_courses):
        if bselected_courses:
            for i in range(len(self.bselected_courses)):
                self.bselected_courses[i] = bselected_courses[i]
            self.generateVCombinations()
        
    def generateVCombinations(self):
        n_size = 0
        vtbl_courses = []
        self.vcombinations = []
        self.vvrects = []
        for i in range(len(self.vtblcourses)):
            if self.bselected_courses[i]:
                vtbl_courses.append(self.vtblcourses[i])
                n_size += 1

        counter = Counter(vtbl_courses, -1)
        while counter.increment():
            tbl_combinations = []

            for i in range(len(vtbl_courses)):
                tbl_course = vtbl_courses[i][counter.get(i)]
                if len(tbl_combinations) == 0:
                    tbl_combinations.append(tbl_course)
                    continue
                if TableEngine.isTablesCollide(tbl_course, tbl_combinations):
                    break
                tbl_combinations.append(tbl_course)

            if len(tbl_combinations) < n_size:   # collision occured
                continue

            self.vcombinations.append(tbl_combinations)

        n_areas = []
        for combinations in self.vcombinations:
            n_vrects = []
            for table in combinations:
                n_rects = []
                for rects in table.vrects:
                    n_rects.extend(copy.deepcopy(rects)) # same list, different reference
                n_vrects.append(n_rects)
            
            n_b = TableEngine.getTableBoundaries(n_vrects)
            n_areas.append((n_b['right'] - n_b['left'] + 1) * (n_b['upper'] - n_b['lower']))   # area
            self.vvrects.append(n_vrects)
        
        # sorting algorithm (by area)
        for i in range(len(n_areas)):
            if i == 0:
                continue
            for j in range(i):
                if n_areas[i] == n_areas[j]:
                    continue
                if n_areas[i] < n_areas[j]:
                    n_areas.insert(j, n_areas.pop(i))
                    self.vcombinations.insert(j, self.vcombinations.pop(i))
                    self.vvrects.insert(j, self.vvrects.pop(i))

    def setIndex(self, index):
        self.index = index

    def getCombinations(self, SCREEN_SIZE_X, SCREEN_SIZE_Y):
        self.texts = []

        n_vrects = self.vvrects[self.index]
        n_b = TableEngine.getTableBoundaries(n_vrects)

        N_OFFSET = Vector2n(30, 21)
        N_SIZE = Vector2n(SCREEN_SIZE_X, SCREEN_SIZE_Y)

        args = self.setRectFormat(N_SIZE, N_OFFSET, n_b)
        
        N_SIZE.setParameter(SCREEN_SIZE_X - N_OFFSET.x, SCREEN_SIZE_Y - N_OFFSET.y)
        N_H = args[2]
        
        N_OFFSET.y = N_OFFSET.y + N_OFFSET.y / 2 + args[0] * N_H
        N_SIZE.y = N_SIZE.y - N_OFFSET.y - args[1] * N_H

        self.setRectTable(N_SIZE, N_OFFSET, n_b, n_vrects, args[2])

        return self.vcombinations[self.index]
    

    def setRectFormat(self, N_SIZE, N_OFFSET, n_b):
        N_W = (N_SIZE.x - N_OFFSET.x) / (n_b['right'] - n_b['left'] + 1)  # day width constant
        str_days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        texts = []
        for i in range(n_b['left'], n_b['right'] + 1):
            text = Text()
            text.x = N_W * ((i - n_b['left']) + 0.5) + N_OFFSET.x
            text.y = 0
            text.val = str_days[i]
            texts.append(text)

        N_LOWER = int(math.floor(n_b['lower'] / 60))
        N_UPPER = int(math.ceil(n_b['upper'] / 60))
        N_H = (N_SIZE.y - N_OFFSET.y) / ((N_UPPER - N_LOWER + 1) * 60)     # time height constant
        for i in range(N_LOWER, N_UPPER + 1):
            str_i = str(i)
            if len(str_i) < 2:
                str_i = "0" + str_i
            text = Text()
            text.x = N_OFFSET.x / 2
            text.y = (i - N_LOWER) * 60 * N_H + N_OFFSET.y
            text.val = str_i
            texts.append(text)
        self.texts.append(texts)

        return [(n_b['lower'] - N_LOWER * 60), (N_UPPER * 60 - n_b['upper']), N_H]

    def setRectTable(self, N_SIZE, N_OFFSET, n_b, n_vrects, N_H):
        N_W = N_SIZE.x / (n_b['right'] - n_b['left'] + 1)  # day width constant
        # N_H = N_SIZE.y / (n_b['upper'] - n_b['lower'])     # time height constant

        texts = []
        for i in range(len(self.vcombinations[self.index])):
            self.vcombinations[self.index][i].color = self.color[i]
            for j in range(len(self.vcombinations[self.index][i].vrects)):
                size_rects = len(self.vcombinations[self.index][i].vrects[j])
                for k in range(size_rects):
                    l = j * size_rects + k

                    tbl_course = self.vcombinations[self.index][i]
                    rect = tbl_course.vrects[j][k]
                    rect.x = (n_vrects[i][l].x - n_b['left']) * N_W + N_OFFSET.x
                    rect.y = (n_vrects[i][l].y - n_b['lower']) * N_H + N_OFFSET.y
                    rect.w = N_W
                    rect.h = n_vrects[i][l].h * N_H

                    text = Text()
                    text.x = rect.x + rect.w / 2
                    text.y = rect.y + rect.h / 2
                    text.val = tbl_course.code
                    texts.append(text)
        self.texts.append(texts)

    def getVTblCourses(self):
        return self.vtblcourses

    def getVCombinationsSize(self):
        return len(self.vcombinations)
    
    @staticmethod
    def isTablesCollide(table, tbl_combinations):
        for tbl_course in tbl_combinations:
            if CourseTable.isTablesCollide(table, tbl_course):
                return True
        return False
    
    @staticmethod
    def getTableBoundaries(n_vrects):
        n_b = {
            'upper': 0, # 0
            'right': 0, # 1
            'lower': 0, # 2
            'left': 0,  # 3
        }
        for rects in n_vrects:
            for rect in rects:
                if n_b['upper'] == 0 and n_b['right'] == 0 and n_b['lower'] == 0 and n_b['left'] == 0:
                    n_b['lower'] = rect.y
                    n_b['upper'] = rect.y + rect.h
                    continue
                if rect.y < n_b['lower']:
                    n_b['lower'] = rect.y
                if rect.y + rect.h > n_b['upper']:
                    n_b['upper'] = rect.y + rect.h
                if rect.x < n_b['left']:
                    n_b['left'] = rect.x
                if rect.x > n_b['right']:
                    n_b['right'] = rect.x
        return n_b