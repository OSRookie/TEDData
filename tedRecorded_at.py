import ast
import re
import requests

head = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
    'ue': 'utf-8',
}
def getRecorded_at(url_ted):
    try:
        response = requests.get(url_ted,params=head,timeout=30)
        content=response.content
        content=content.decode('utf-8')
        #print(response.text)
        recorded_at=re.findall(r'"recorded_at":\".*?\"',content)
        dict_test=ast.literal_eval("{"+recorded_at[0]+"}")
        return dict_test['recorded_at']
    except:
        return ""
    return ""
#演讲者演讲日期
