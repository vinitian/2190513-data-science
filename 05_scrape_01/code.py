from bs4 import BeautifulSoup
from bs4.element import Tag

def Q1(file_path): # DO NOT modify this line
    with open(file_path) as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")

    alldays = soup.select('div.bud-day-col')
    wanphra = [0,0,0,0,0,0,0]
    for element in alldays:
        date = str(element.string)
        if 'จันทร์' in date:
            wanphra[0] += 1
        if 'อังคาร' in date:
            wanphra[1] += 1
        if 'พุธ' in date:
            wanphra[2] += 1
        if 'พฤหัสบดี' in date:
            wanphra[3] += 1
        if 'ศุกร์' in date:
            wanphra[4] += 1
        if 'เสาร์' in date:
            wanphra[5] += 1
        if 'อาทิตย์' in date:
            wanphra[6] += 1
          
    return wanphra
                          


def Q2(file_path): # DO NOT modify this line
    with open(file_path) as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")

    visakha = soup.find('a', attrs={'title':"วันวิสาขบูชา"})
    date = visakha.parent.parent.div.string
    return date


exec(input().strip()) # do not delete this line
# print(Q1("webpage.html"))

