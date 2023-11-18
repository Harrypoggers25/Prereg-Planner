from kulliyah_engine import KulliyahEngine
from models import CourseTable, Counter

class CourseEngine:
    def __init__(self):
        self.loaded_courses = dict()
        self.selected_courses = dict()
        self.current_param = ""             # to remove duplicates between loaded and selected courses
        self.vcourse_combinations = [[], []]    # stores 2D list of courses

    def loadCourses(self, n_kulliyah=None, n_session=None, n_ctype=None):
        kulliyah_engine = KulliyahEngine()
        kulliyah_engine.setParam(n_kulliyah=n_kulliyah, n_session=n_session, n_ctype=n_ctype)
        self.current_param = f"{n_kulliyah}_{n_session}_{n_ctype}"
        self.loaded_courses = kulliyah_engine.getCourses()

        del kulliyah_engine

        for code in self.selected_courses:
            if code in self.loaded_courses:
                self.loaded_courses.pop(code) # remove duplicate

    def selectCourse(self, code):
        self.selected_courses[code] = self.loaded_courses.pop(code)

    def deselectCourse(self, code):
        if self.selected_courses[code].param == self.current_param:
            self.loaded_courses[code] = self.selected_courses.pop(code)
        else:
            del self.selected_courses[code]

    def generateCourseCombinations(self, SCREEN_SIZE_X, SCREEN_SIZE_Y):
        tbl_vcourses = [[],[]] # separating sections per course
        for course in self.selected_courses:
            tbl_courses = []
            for sect in course.sects:
                tbl_course = CourseTable(course.code, sect)
                tbl_courses.append(tbl_course)
            tbl_vcourses.append(tbl_courses)

        counter = Counter(tbl_vcourses)
        while counter.increment():
            tbl_combinations = []

            for i in range(len(tbl_vcourses)):
                tbl_course = tbl_vcourses[i][counter.get(i)]
                if len(tbl_combinations) == 0:
                    tbl_combinations.append(tbl_course)
                    continue
                elif self.isTablesCollide(tbl_course, tbl_combinations):
                    break
                tbl_combinations.append(tbl_course)
            if len(tbl_combinations) < len(tbl_vcourses):   # collision occured
                continue

            # get bounds => dimension constants
            n_lower = 0
            n_upper = 0
            n_left = 0
            n_right = 0
            for tbl_course in tbl_combinations:
                for rects in tbl_course.vrects:
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

            for i in range(len(tbl_combinations)):
                for j in range(len(tbl_combinations[i])):
                    for k in range(len(tbl_combinations[i][j])):
                        n_x = tbl_combinations[i][j][k].x
                        n_y = tbl_combinations[i][j][k].y
                        n_h = tbl_combinations[i][j][k].h

                        tbl_combinations[i][j][k].x = n_x * N_W
                        tbl_combinations[i][j][k].y = n_y * N_H
                        tbl_combinations[i][j][k].w = N_W
                        tbl_combinations[i][j][k].h = n_h * N_H

    def isTablesCollide(self, table, tbl_combinations):
        for tbl_course in tbl_combinations:
            if CourseTable.isTablesCollide(table, tbl_course):
                return True
        return False