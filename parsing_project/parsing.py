import requests
from bs4 import BeautifulSoup
import csv

def write(data):
    with open('easy.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages_ul = soup.find('div', class_="vm-pagination vm-pagination-bottom").find('ul')
    total_pages = soup.find('span', class_='vm-page-counter'
    ).text.split()[-1]
    return total_pages

def get_page_data(html):
    soup =BeautifulSoup(html, 'lxml')
    product_list = soup.find_all('div', class_='row')
    for i in product_list:
        title = i.find('span', class_='prouct_name').find('a').text
        price = i.find('span', class_='price').text
        image = 'https://enter.kg' + i.find('img').get('src')
        write([title, price, image])
        

def main():
    with open('easy.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['title','price','image'])
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    pages = '/results,'
    html = get_html(url)
    pages_num = get_total_pages(html)
    
    for page in range(1,int(pages_num)+1):
        print(page)
        if page == 1:
        
            page_url =url
        else:
            page_url = url + f'{pages}{(page-1)*100+1}-{(page-1)*100}'
        print(page_url)
        html = get_html(page_url)
        get_page_data(html)
    

main()