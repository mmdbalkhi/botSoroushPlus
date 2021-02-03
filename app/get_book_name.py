#!/env/bin/python3
"""Module get_book_name"""
from bs4 import BeautifulSoup
from requests import get


def get_book_name(search_mark):
    """get book name at googdread"""

    good_reads = f'https://www.goodreads.com/search?q={search_mark}'

    data = get(good_reads).content
    soup = BeautifulSoup(data, features="html5lib")

    loopnum = 0
    names = ''
    for name in soup.select('.bookTitle span'):

        newname = str(name).replace("</span>", "")
        newname = str(newname).replace(
            """<span aria-level="4" itemprop="name" role="heading">""", "")
        loopnum += 1

        names += f"{loopnum}- {newname}\n\n"
        if loopnum == 10:  # TODO: loopnum is hardCode
            break
    return "این کتاب ها را یافتیم!\n\n"+names
