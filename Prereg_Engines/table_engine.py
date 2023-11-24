import copy

from Prereg_Engines.models import CourseTable, Counter
from HP_Framework.objects import HpRgbColor

class TableEngine():
    def __init__(self):
        self.vtblcourses = [] # stores 2d list of courses sorted by section
        self.vcombinations = [] # stores 2D list of course combinatons
        self.vvrects = []
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

    def setVTblCourses(self, vtblcourses, bselected_courses = None):
        self.vtblcourses = vtblcourses
        self.bselected_courses = bselected_courses if bselected_courses else [True] * len(self.vtblcourses)

        if len(self.color) < len(self.vtblcourses):
            n_diff = len(self.vtblcourses) - len(self.color)
            self.color.extend(self.color[:n_diff])

        self.generateCombinations()

    def generateCombinations(self):
        n_size = 0
        vtbl_courses = []
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

        self.vcombinations = self.vcombinations

        for combinations in self.vcombinations:
            n_vrects = []
            for table in combinations:
                n_rects = []
                for rects in table.vrects:
                    n_rects.extend(copy.deepcopy(rects)) # same list, different reference
                n_vrects.append(n_rects)
            self.vvrects.append(n_vrects)

    def setIndex(self, index):
        self.index = index

    def getCombinations(self, SCREEN_SIZE_X, SCREEN_SIZE_Y):
        n_vrects = self.vvrects[self.index]
        n_lower = n_upper = n_left = n_right = 0

        for rects in n_vrects:
            for rect in rects:
                if n_lower == 0 and n_upper == 0 and n_left == 0 and n_right == 0:
                    n_lower = rect.y
                    n_upper = rect.y + rect.h
                    continue
                if rect.y < n_lower:
                    n_lower = rect.y
                if rect.y + rect.h > n_upper:
                    n_upper = rect.y + rect.h
                if rect.x < n_left:
                    n_left = rect.x
                if rect.x > n_right:
                    n_right = rect.x
        N_W = SCREEN_SIZE_X / (n_right - n_left + 1)  # day width constant
        N_H = SCREEN_SIZE_Y / (n_upper - n_lower)     # time height constant

        for i in range(len(self.vcombinations[self.index])):
            self.vcombinations[self.index][i].color = self.color[i]
            for j in range(len(self.vcombinations[self.index][i].vrects)):
                size_rects = len(self.vcombinations[self.index][i].vrects[j])
                for k in range(size_rects):
                    l = j * size_rects + k
                    rect = self.vcombinations[self.index][i].vrects[j][k]
                    
                    rect.x = n_vrects[i][l].x * N_W
                    rect.y = (n_vrects[i][l].y - n_lower) * N_H
                    rect.w = N_W
                    rect.h = n_vrects[i][l].h * N_H

        return self.vcombinations[self.index]
    
    @staticmethod
    def isTablesCollide(table, tbl_combinations):
        for tbl_course in tbl_combinations:
            if CourseTable.isTablesCollide(table, tbl_course):
                return True
        return False 