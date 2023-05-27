import os.path
from lxml import etree
import requests


def create_file(file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)


url = "https://wenku.baidu.com/view/4203ad749989680203d8ce2f0066f5335b81677f.html?fr=income12-doc-search&_wkts_=1685077927424&wkQuery=python%E7%BC%96%E7%A8%8Bppt"
url = "https://wenku.baidu.com/view/4dce7cdca4e9856a561252d380eb6294dc8822bd.html?fr=income2-doc-search&_wkts_=1685113445279&wkQuery=python%E7%BC%96%E7%A8%8Bppt"
resp = requests.get(url)
text = resp.text
html = etree.HTML(text)
img_list = html.xpath('//div[@class="mod flow-ppt-mod"]/div/div/img')

file_path = "./documents/"
create_file(file_path)

cnt = 1
for i in img_list:
    try:
        img_url = i.xpath('./@src')[0]
    except:
        img_url = i.xpath('./@data-src')[0]

    file_name = f'{file_path}page_{cnt}.jpg'
    print(file_name, img_url)

    resp = requests.get(img_url)
    with open(file_name, 'wb') as f:
        f.write(resp.content)

    cnt += 1
