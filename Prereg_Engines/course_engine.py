import copy

from Prereg_Engines.kulliyah_engine import KulliyahEngine
from Prereg_Engines.models import CourseTable, Course, CourseSection, CourseInfo

class CourseEngine:
    def __init__(self):
        self.loaded_courses = dict()
        self.selected_courses = dict()
        self.current_param = ""             # to remove duplicates between loaded and selected courses
        self.kulliyah_engine = KulliyahEngine()

    def loadCourses(self, n_kulliyah : int | None, n_session : int | None, n_ctype : int | None):
        self.kulliyah_engine.setParam(n_kulliyah=n_kulliyah, n_session=n_session, n_ctype=n_ctype)
        self.current_param = f"{n_kulliyah}_{n_session}_{n_ctype}"
        self.loaded_courses = self.kulliyah_engine.getCourses()

    def selectCourse(self, code : str):
        self.selected_courses[code] = self.loaded_courses[code]

    def deselectCourse(self, code : str):
        self.selected_courses.pop(code)

    def getVTableCourses(self):
        vtbl_courses = [] # separating sections per course
        for course in self.selected_courses.values():
            tbl_courses = []
            tbl_course = None
            sect = None
            sections = copy.deepcopy(course.sects)
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
    
    def getKulliyahs(self):
        return [kulliyah.name for kulliyah in self.kulliyah_engine.kulliyahs]

    def getSessions(self):
        return [f"Sem {session.sem}, {session.year}" for session in self.kulliyah_engine.sessions]

    def writeFile(self, dir):
        file = open(dir, "w")

        for course in self.selected_courses.values():
            file.write(f'{course.title}//{course.code}//{course.ch}//{course.index}//{course.param}//c\n')
            for sect in course.sects:
                file.write(f'{sect.val}//s\n')
                for info in sect.infos:
                    file.write(f'{info.day}//{info.time}//{info.lecturer}//i\n')
            file.write(';\n')
        file.close()

    def readFile(self, dir):
        file = open(dir, "r")
        lines = file.readlines()
        course = None
        section = None
        info = None
        dict_courses = dict()
        for i in range(len(lines)):
            line = lines[i][:-1]
            if line[-3:] == '//c':
                line = line[:-3]
                datas = line.split('//')
                course = Course()
                course.title = datas[0]
                course.code = datas[1]
                course.ch = float(datas[2])
                course.index = int(datas[3])
                course.param = datas[4]
            elif line[-3:] == '//s':
                section = CourseSection()
                section.val = line[:-3]
                course.sects.append(section)
            elif line[-3:] == '//i':
                info = CourseInfo()
                line = line[:-3]
                datas = line.split('//')
                info.day = datas[0]
                info.time = datas[1]
                info.lecturer = datas[2]
                section.infos.append(info)
            else:
                dict_courses[course.code] = course
        file.close()
        self.selected_courses = dict_courses

    def clear(self):
        self.loaded_courses = dict()
        self.selected_courses = dict()
        self.current_param = ""      

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

