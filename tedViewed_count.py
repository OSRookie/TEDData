import re
import requests

head = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
    'ue': 'utf-8',
}
def getViewed_count(url_ted):
    try:
        reponse=requests.get(url_ted,params=head)
        content=reponse.content
        content=content.decode('utf-8')
        viewed_count=re.findall(r'"viewed_count":(\d+)?',content)
        return viewed_count[0]
    except:
        return ""
    return ""
#浏览量
