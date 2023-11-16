from kulliyah_engine import KulliyahEngine

class CourseEngine:
    def __init__(self):
        self.loaded_courses = dict()
        self.selected_courses = dict()
        self.current_param = ""
        self.courses_combinations = []

    def loadCourses(self, n_kulliyah=None, n_session=None, n_ctype=None):
        kulliyah_engine = KulliyahEngine()
        kulliyah_engine.setParam(n_kulliyah=n_kulliyah, n_session=n_session, n_ctype=n_ctype)
        self.current_param = f"{n_kulliyah}_{n_session}_{n_ctype}"
        self.loaded_courses = kulliyah_engine.getCourses().copy()

        del kulliyah_engine

        for code in self.selected_courses:
            if code in self.loaded_courses:
                self.loaded_courses.pop(code)

    def selectCourse(self, code):
        self.selected_courses[code] = self.loaded_courses.pop(code)

    def deselectCourse(self, code):
        if self.selected_courses[code].param == self.current_param:
            self.loaded_courses[code] = self.selected_courses.pop(code)
        else:
            del self.selected_courses[code]

    def generateDiscreteSelectedRects(self):
        for course in self.selected_courses.values():
            for sect in course.sect:
                for info in sect.info:
                    info.updateDiscreteRects()

    def isCoursesCollide(self, c1sect, c2sect):
        c1rect = []
        for info in c1sect.info:
            for rect in info.rect:
                c1rect.append(rect)
        
        c2rect = []
        for info in c2sect.info:
            for rect in info.rect:
                c2rect.append(rect)

        for rect1 in c1rect:
            for rect2 in c2rect:
                if (
                        rect1.x < rect2.x + rect2.w
                        and rect1.x + rect1.w > rect2.x
                        and rect1.y < rect2.y + rect2.h
                        and rect1.y + rect1.h > rect2.y
                    ):
                        return True
        return False

    # def generateCourseCombinations(self):
    #     for course in self.selected_courses.values():
    #         if len(course_combina)
    #             course_combinations.append(course)
        

    def clearSelectedRect(self, code):
        course = self.selected_courses[code]
        for sect in course.sect:
                for info in sect.info:
                    info.clearRects()
        
    