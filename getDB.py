import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

class getDataBase:
    def __init__(self, size, start, end):
        self.size = size
        self.start = start
        self.end = end

    def getData(self):
        headers = {'Content-type': 'application/json'}
        pload = {}
        r = requests.post('',json= pload,headers=headers)
        listOfDatas = []
        for data in r.json()['hits']['hits']:
            datas = {
                'id' : data['_id'],
                'content' : BeautifulSoup(data['_source']['content'],"html.parser").get_text(),
                'link' : data['_source']['link'],
                'created_at' : data['_source']['created_at'],
                'sumber' : data['_source']['source']
            }
            listOfDatas.append(datas)
        df = pd.DataFrame(listOfDatas)
        return df
        # print(cleansingContent.cleasing(Data=df).cleansingData())

# getDataBase(10,1606755600000,1607619599000).getData()