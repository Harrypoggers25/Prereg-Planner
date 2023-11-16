from course_engine import CourseEngine

ce = CourseEngine()
ce.loadCourses(n_kulliyah=0, n_session=0, n_ctype=0)
# ce.selectCourse('AAUD 1204')
# ce.selectCourse('AHBS 1213')
# ce.selectCourse('AHCC 1313')
# ce.selectCourse('AHDT 2312')
# ce.generateDiscreteSelectedRects()

for course in ce.loaded_courses.values():
    print(f"Title: {course.title}")
    print(f"Code: {course.code}")
    for sect in course.sect:
        print(f"Sect: {sect.val}")
        for i in range(len(sect.info)):
            print(f"Day{i + 1}: {sect.info[i].day}")
            print(f"Time{i + 1}: {sect.info[i].time}")
            print(f"Lect{i + 1}: {sect.info[i].lecturer}")
    print("")

#####################################################################################

# ce = CourseEngine()
# dict_day = dict()

# for i in range(21):
#     for j in range(3):
#         for k in range(2):
#             ce.loadCourses(n_kulliyah=i, n_session=j, n_ctype=k)
#             for course in ce.loaded_courses.values():
#                 for sect in course.sect:
#                     for info in sect.info:
#                         if not info.day in dict_day:
#                             dict_day[info.day] = 1
#                         else:
#                             dict_day[info.day] += 1
# for day in dict_day:
#     print(f'{day}: {dict_day[day]}')

######################################################################################

# ce = CourseEngine()
# dict_time = dict()

# for i in range(21):
#     for j in range(3):
#         for k in range(2):
#             ce.loadCourses(n_kulliyah=i, n_session=j, n_ctype=k)
#             for course in ce.loaded_courses.values():
#                 for sect in course.sect:
#                     for info in sect.info:
#                         if not info.time in dict_time:
#                             dict_time[info.time] = 1
#                         else:
#                             dict_time[info.time] += 1
# for time in dict_time:
#     print(f'{time}: {dict_time[time]}')

#####################################################################################

# ce = CourseEngine()
# ce.loadCourses(n_kulliyah=0, n_session=0, n_ctype=0)

# for course in ce.loaded_courses.values():
#     print(f"Title: {course.title}")
#     print(f"Code: {course.code}")
#     for sect in course.sect:
#         print(f"Sect: {sect.val}")
#         for i in range(len(sect.info)):
#             print(f"Day{i + 1}: {sect.info[i].day}")
#             print(f"Time{i + 1}: {sect.info[i].time}")
#             print(f"Lect{i + 1}: {sect.info[i].lecturer}")
#     print("")

######################################################################################

# from kulliyah_engine import KulliyahEngine

# ke = KulliyahEngine()
# ke.setParam(n_kulliyah=3, n_session=0, n_ctype=0)
# dict_course = ke.getCourses()

# for course in dict_course.values():
#     print(f"Title: {course.title}")
#     print(f"Code: {course.code}")
#     for sect in course.sect:
#         print(f"Sect: {sect.val}")
#         for i in range(len(sect.info)):
#             print(f"Day{i + 1}: {sect.info[i].day}")
#             print(f"Time{i + 1}: {sect.info[i].time}")
#             print(f"Lect{i + 1}: {sect.info[i].lecturer}")
#     print("")