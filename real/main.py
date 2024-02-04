import os
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileMerger
from fake_useragent import UserAgent


def main_scrap():
    ua = UserAgent()
    url = 'https://pages.cs.wisc.edu/~remzi/OSTEP/'
    response = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )
    with open('OS_book.html', 'wb') as f:
        f.write(response.content)
    
    with open("OS_book.html", "r") as file_os:
        content = BeautifulSoup(file_os, 'lxml')
        tbody = content.find_all('table')[-1]
        all_td = tbody.find_all('td')
        yellow_count = 0
        orrange_count = 0
        blue_count = 0
        green_count = 0
        tree_count = 0
        for td in all_td:
            if td.get('bgcolor') == 'yellow':
                td_ahref = td.find('a')
                if td_ahref is not None:
                    td_small = td.find('small')
                    if td_small is not None:
                        td_small = int(td_small.text)
                        if td_small <= yellow_count:
                            td_small = yellow_count + 1
                            yellow_count += 1
                        pdf = td_ahref.get('href')
                        pdf_response = requests.get('https://pages.cs.wisc.edu/~remzi/OSTEP/' + pdf)
                        with open(f'book/1intro/{td_small}{pdf}', 'wb') as f:
                            f.write(pdf_response.content)
                    else:
                        yellow_count += 1
                        pdf = td.find('a').get('href')
                        pdf_response = requests.get('https://pages.cs.wisc.edu/~remzi/OSTEP/' + pdf)
                        with open(f'book/1intro/{yellow_count}{pdf}', 'wb') as f:
                            f.write(pdf_response.content)
                else:
                    continue
            

            if td.get('bgcolor') == '#f88017':
                td_ahref = td.find('a')
                if td_ahref is not None:
                    td_small = td.find('small')
                    if td_small is not None:
                        td_small = int(td_small.text)
                        pdf = td.find('a').get('href')
                        pdf_response = requests.get('https://pages.cs.wisc.edu/~remzi/OSTEP/' + pdf)
                        with open(f'book/2virtualization/{td_small}{pdf}', 'wb') as f:
                            f.write(pdf_response.content)
                    else:
                        orrange_count += 1
                        pdf = td.find('a').get('href')
                        pdf_response = requests.get('https://pages.cs.wisc.edu/~remzi/OSTEP/' + pdf)
                        with open(f'book/2virtualization/{orrange_count}{pdf}', 'wb') as f:
                            f.write(pdf_response.content)
                else:
                    continue

            if td.get('bgcolor') == '#00aacc':
                td_ahref = td.find('a')
                if td_ahref is not None:
                    blue_count += 1
                    pdf = td.find('a').get('href')
                    pdf_response = requests.get('https://pages.cs.wisc.edu/~remzi/OSTEP/' + pdf)
                    with open(f'book/3concurrency/{blue_count}{pdf}', 'wb') as f:
                        f.write(pdf_response.content)
                else:
                    continue

            if td.get('bgcolor') == '#4CC417':
                td_ahref = td.find('a')
                if td_ahref is not None:
                    green_count += 1
                    pdf = td.find('a').get('href')
                    pdf_response = requests.get('https://pages.cs.wisc.edu/~remzi/OSTEP/' + pdf)
                    with open(f'book/4persistence/{green_count}{pdf}', 'wb') as f:
                        f.write(pdf_response.content)
                else:
                    continue

            if td.get('bgcolor') == '#3EA99F':
                td_ahref = td.find('a')
                if td_ahref is not None:
                    tree_count += 1
                    pdf = td.find('a').get('href')
                    pdf_response = requests.get('https://pages.cs.wisc.edu/~remzi/OSTEP/' + pdf)
                    with open(f'book/5security/{tree_count}{pdf}', 'wb') as f:
                        f.write(pdf_response.content)
                else:
                    continue

def union_scrap():
    rootdir = r'D:/py-projects/scrapping/scrap_book_about_cs/book/'
    merger = PdfFileMerger()
    for subdir, dirs, files in os.walk(rootdir):
        for pdf_file in files:
            merger.append(subdir + '\\' + pdf_file)
    merger.write('Operating Systems Three Easy Pieces.pdf')
    merger.close()

def main():
    main_scrap()
    union_scrap()

if __name__ == "__main__":
    main()