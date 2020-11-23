import requests
from bs4 import BeautifulSoup
from tedDescription import getDescription
from tedRecorded_at import getRecorded_at
from tedTag import getTag
from tedViewed_count import getViewed_count
head = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
    'ue': 'utf-8',
}

def get_TED(url, count):
    page_part = url.split('=')
    #z=0
    for i in range(1, count+1):
        url_ted = page_part[0] + '=' + str(i) + '&sort=popular'
        response = requests.get(url_ted,params=head)
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')
        talks_list = bs.find_all('div', attrs={'class': 'media__message'})

        for j in range(len(talks_list)):
            #z+=1
            ted_a = talks_list[j].find_all('a', attrs={'class': 'ga-link', 'data-ga-context': 'talks'})
            ted_url = 'https://www.ted.com' + ted_a[0]['href']
            #print(z)
            print("TED演讲标题：" + ted_a[0].text)
            print("TED演讲者身份："+getDescription(ted_url))
            print("发布日期："+getRecorded_at(ted_url))
            print("浏览量："+getViewed_count(ted_url))
            print("相关标签："+getTag(ted_url)+"\n")

if __name__ == '__main__':
    url = 'https://www.ted.com/talks?page=1&sort=popular'
    count = int(input("请输入要下载的页数（一页36个TED）："))
    get_TED(url, count)
