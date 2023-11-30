from bs4 import BeautifulSoup

from Prereg_Engines.models import Session, Kulliyah, Course, CourseInfo, CourseSection

# Main Page Parser
class HTMLMPParser:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def parseKulliyah(self):
        list_kulliyah = []
        select_element = self.soup.find('select', {'name': 'kuly'})
        if select_element:
            for option in select_element.find_all('option'):
                kulliyah = Kulliyah()
                kulliyah.val = option['value']
                kulliyah.name = option.text
                list_kulliyah.append(kulliyah)
        return list_kulliyah
    
    def parseSession(self):
        list_session = []
        select_element = self.soup.find('select', {'name': 'sem'})
        if select_element:
            for option in select_element.find_all('option'):
                session = Session()
                str_option = option.text
                session.year = str_option[:str_option.find(' ')]
                session.sem = str_option[str_option.find('sem ') + 4:]
                list_session.append(session)
        return list_session

# Course Page Parser
class HTMLCPParser:
    @staticmethod
    def parsePage(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        dict_course = dict()
        table1 = soup.find_all('table')[1]  # selects 2nd main table
        for row in table1.find_all('tr', {'valign': 'top'}, recursive=False):
            datas = row.find_all('td')

            code = datas[0].text
            course = Course()
            if not code in dict_course:
                course.code = code
                course.title = datas[2].text
                course.ch = int(datas[3].text)
                dict_course[code] = course

            sect = CourseSection()
            sect.val = datas[1].text

            subtable = datas[4].find_all('table')[0]  
            for subrow in subtable.find_all('tr'):
                info = CourseInfo()
                subdatas = subrow.find_all('td')
                info.day = subdatas[0].text
                info.time = subdatas[1].text
                info.lecturer = subdatas[3].text
                if info.day != "" and info.time != "" and info.time != " " and info.time != ' AM' and info.time != ' PM':
                    sect.infos.append(info)
            if len(sect.infos) != 0:
                dict_course[code].sects.append(sect)
        return dict_course