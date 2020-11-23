import ast
import re
import requests

head = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
    'ue': 'utf-8',
}
def getTag(url_ted):
    try:
        response = requests.get(url_ted,params=head,timeout=30)
        content=response.content
        content=content.decode('utf-8')
        tag=re.findall(r'"tag":\".*?\"',content)
        dict_test=ast.literal_eval("{"+tag[0]+"}")
        return dict_test['tag']
    except:
        return ""
    return ""
#相关标签
