import csv
import sys
from subprocess import Popen, PIPE
from urlparse import urlparse
file = open(sys.argv[1])

reader = csv.reader(file)

next(reader)  # skip top comment
next(reader)  # skip table headers

for row in reader:
    url, user, pwd = row[:3]
    data = '{}\nuser: {}\nurl: {}\n'.format(pwd, user, url)
    path = 'www/{}'.format(urlparse(url).netloc.replace('www.', ''))

    proc = Popen(['pass', 'insert', '--multiline', path], stdin=PIPE, stdout=PIPE)
    proc.communicate(data)
    proc.wait()
