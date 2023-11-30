from Prereg_Engines.kulliyah_engine import KulliyahEngine
from Prereg_Engines.models import CourseTable

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
        self.loaded_courses = dict(sorted(self.loaded_courses.items()))

    def getVTableCourses(self):
        vtbl_courses = [] # separating sections per course
        for course in self.selected_courses.values():
            tbl_courses = []
            tbl_course = None
            sect = None
            sections = course.sects
            i = 0
            while len(sections) != 0:
                if not tbl_course:
                    sect = sections.pop(0)
                    tbl_course = CourseTable(course.code, sect)
                    continue
                if i >= len(sections):
                    tbl_courses.append(tbl_course)
                    tbl_course = None
                    sect = None
                    i = 0
                elif CourseEngine.isSectionEqual(sections[i], sect):
                    tbl_course.sects.append(sections.pop(i).val)
                    i = 0
                else:
                    i += 1
            tbl_courses.append(tbl_course)
            vtbl_courses.append(tbl_courses)
        return vtbl_courses
    
    def getCHs(self):
        n_CHs = []
        for course in self.selected_courses.values():
            n_CHs.append(course.ch)
        return n_CHs
    
    @staticmethod
    def isSectionEqual(section1, section2):
        info1 = section1.infos[:]
        info2 = section2.infos[:]

        if len(info1) != len(info2):
            return False
        for i in range(len(info1)):
            for j in range(len(info2)):
                if info1[i].day == info2[j].day and info1[i].time == info2[j].time:
                    info1.pop(i)
                    info2.pop(j)
                    i = j = 0
        return len(info1) == 0 and len(info2) == 0

