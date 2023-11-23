from Prereg_Engines.kulliyah_engine import KulliyahEngine
from Prereg_Engines.models import CourseTable, Counter

class CourseEngine:
    def __init__(self):
        self.loaded_courses = dict()
        self.selected_courses = dict()
        self.current_param = ""             # to remove duplicates between loaded and selected courses

    def loadCourses(self, n_kulliyah : int | None, n_session : int | None, n_ctype : int | None):
        kulliyah_engine = KulliyahEngine()
        kulliyah_engine.setParam(n_kulliyah=n_kulliyah, n_session=n_session, n_ctype=n_ctype)
        self.current_param = f"{n_kulliyah}_{n_session}_{n_ctype}"
        self.loaded_courses = kulliyah_engine.getCourses()

        del kulliyah_engine

        for code in self.selected_courses:
            if code in self.loaded_courses:
                self.loaded_courses.pop(code) # remove duplicate

    def selectCourse(self, code : str):
        self.selected_courses[code] = self.loaded_courses.pop(code)

    def deselectCourse(self, code : str):
        if self.selected_courses[code].param == self.current_param:
            self.loaded_courses[code] = self.selected_courses.pop(code)
        else:
            del self.selected_courses[code]

    def getVCombinations(self):
        tbl_vcourses = [] # separating sections per course
        for course in self.selected_courses.values():
            tbl_courses = []
            for sect in course.sects:
                tbl_course = CourseTable(course.code, sect)
                tbl_courses.append(tbl_course)
            tbl_vcourses.append(tbl_courses)

        vcombinations = []    # stores 2D list of course combinatons
        counter = Counter(tbl_vcourses, -1)
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

            vcombinations.append(tbl_combinations)
        return vcombinations

    def isTablesCollide(self, table, tbl_combinations):
        for tbl_course in tbl_combinations:
            if CourseTable.isTablesCollide(table, tbl_course):
                return True
        return False