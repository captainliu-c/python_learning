from contextlib import closing
from urllib.request import urlopen
import ssl

with closing(urlopen('http://www.daomubiji.org/1.html',context=ssl._create_unverified_context())) as page:
    for line in page:
        print(line)

