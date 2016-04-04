#!/usr/bin/env python3 -tt
"""
Разполагаме с access log от Таковата,
и е необходимо да проверим коя страница е имала най-голямо средно време за отговор,
и какво е средното време на отговор в секунд.
При извеждане на резултата, форматирайте секундите до 3 знака след десетичната запетая.

ВАЖНО: При изчисленията трябва да не вземате предвид никой URL, който завършва на /ws/

Всеки запис във файла е на отделен ред, и изглежда по следния начин:

dt="2016-02-06T13:38:45+00:00" ip="95.43.31.127" m="GET" p="http" url="/student/lecture/568015bf131b1642faa73799/"
req_b="494"
ref="http://python3.softuni.bg/student/course/"
ua="Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
code="200" resp_t="0.032" resp_b="9300"

Времето за отговор е записано в полето resp_t (в секунди), a адресът на страницата - в полето url.

Имайте предвид, при идентифицирането на "страница",
от полето url трябва да се премахнат всички GET параметри.
За целта може да използвате функциите urlparse от модула urllib.parse.


ВХОД:
./takovata-access.log

РЕЗУЛТАТ:
/student/lecture/assignment/56a4ab616e8efb456bd29b06/
0.171

Този резултат включва и заявки за
url /student/lecture/assignment/56a4ab616e8efb456bd29b06/?back=%2Fstudent%2Flecture%2F56801633131b1642fba7379c%2F
Както е отбелязано в условието по-горе,
url /student/activity/ws/ не бива да се взема предвид, въпреки, че неговото време е 18000.000.

"""
import sys
import re
from urllib.parse import urlparse
from collections import Counter
# from pprint import pprint

access_log_file = 'access.log'


def main():

    try:

        # url_re = re.compile(r'url="/[a-zA-Z0-9?%_"=/]*')
        # resp_t_re = re.compile(r'resp_t="[0-9."]+')

        # access_log_file = input()
        with open(access_log_file) as f:
            url_resptime_dict = {}

            for row in f.readlines():
                row_url = re.search(r'url="(.*?)"', row)
                row_resp_t = re.search(r'resp_t="(.*?)"', row)


                print(row_url.group(1))
                # print(row_resp_t.group(1))
                if row_url and row_resp_t:
                    row_url_parse = urlparse(row_url.group(1))
                    row_resp_t_parse = float(row_resp_t.group(1))

                    if row_url_parse.path.endswith('/ws/'):
                        continue
                    else:
                        if not url_resptime_dict.get(row_url_parse.path, None):
                            url_resptime_dict[row_url_parse.path] = [0, 0]

                        url_resptime_dict[row_url_parse.path][0] += row_resp_t_parse
                        url_resptime_dict[row_url_parse.path][1] += 1

            # pprint(url_resptime_dict)
            for k, v in url_resptime_dict.items():
                average_resp = v[0] / v[1]
                url_resptime_dict[k] = average_resp

            # pprint(url_resptime_dict)
            counter = Counter(url_resptime_dict)
            most_common = counter.most_common(1)

            print(most_common[0][0])
            print("{:.3f}".format(most_common[0][1]))

            return 0

    except Exception as e:
        print("INVALID INPUT")
        return 1


if __name__ == '__main__':
    sys.exit(main())
