import urllib.request

from Prereg_Engines.html_parsers import HTMLMPParser
from Prereg_Engines.html_parsers import HTMLCPParser

class KulliyahEngine:
    def __init__(self):
        self.kulliyahs = []
        self.sessions = []
        self.params = None

        webObj = urllib.request.urlopen('https://myapps.iium.edu.my/StudentOnline/schedule1.php')
        str_code = str(webObj.getcode())

        if str_code != "200":
            print("Failed to load menu page data")
        else:
            p_html = HTMLMPParser(webObj.read().decode("utf8"))

            self.kulliyahs = p_html.parseKulliyah()
            self.sessions = p_html.parseSession()
            
        webObj.close()

    def setParam(self, n_kulliyah=0, n_session=0, n_ctype=0):
        self.params = {
            'kuly': self.kulliyahs[n_kulliyah].val,
            'ctype': "<" if n_ctype == 0 else ">=",
            'sem': self.sessions[n_session].sem,
            'ses': self.sessions[n_session].year,
            'val': f"{n_kulliyah}_{n_session}_{n_ctype}"
        }

    def generateLink(self, n_page):
        link = "https://myapps.iium.edu.my/StudentOnline/schedule1.php?action=view&"
        link = link + f"view={n_page * 50}&"
        link = link + f"kuly={self.params['kuly']}&"
        link = link + f"tot_pages={n_page}&"
        link = link + f"ctype={self.params['ctype']}&course=&"
        link = link + f"sem={self.params['sem']}&"
        link = link + f"ses={self.params['ses']}"

        return link
    
    def getCourses(self):
        dict_course = dict()
        n_page = 1
        while True:
            str_url = self.generateLink(n_page)
            webObj = urllib.request.urlopen(str_url)
            str_code = str(webObj.getcode())
            if str_code != "200":
                print(f"Failed to load course page {n_page} data")
                webObj.close()
            else:
                parsed_courses = HTMLCPParser.parsePage(webObj.read().decode("utf8"))
                if len(parsed_courses) == 0:
                    webObj.close()
                    return dict_course
                else:
                    for code in parsed_courses:
                        parsed_courses[code].param = self.params['val']
                        if not code in dict_course:
                            dict_course[code] = parsed_courses[code]
                        else:
                            dict_course[code].sects.extend(parsed_courses[code].sects)
            n_page = n_page + 1
