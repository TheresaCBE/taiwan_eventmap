import requests , json
from urllib.request import urlretrieve
from lxml import etree #xpath
import pandas as pd
################################################################
def MapInfo():
    MapInfo = Maptemp(db,df,cctvY,cctvX,cctvURL)
    return MapInfo
class Maptemp:
    def __init__(self,db,df,cctvY,cctvX,cctvURL):
        self.db = db
        self.df = df
        self.cctvY = cctvY
        self.cctvX = cctvX
        self.cctvURL = cctvURL
    def evt_db(self):
        return db
    def evt_df(self):
        return df
    def cctv_Y(self):
        return cctvY
    def cctv_X(self):
        return cctvX
    def cctv_URL(self):
        return cctvURL
def getevt(): 
        #db,df#
        global db,df
        eventapiurl = "https://od.moi.gov.tw/MOI/v1/pbs"
        response = requests.get(eventapiurl)
        if response.status_code == 200:
            db = json.loads(response.content)
            #格式化
            df = pd.DataFrame.from_dict(db) 
        elif response.status_code == 404:
            return "Unknown Resourse"
def getscctv():
    #cctvY,cctvX,cctvURL#
    global cctvY,cctvX,cctvURL
    cctvapiurl = "https://tisvcloud.freeway.gov.tw/history/motc20/CCTV.xml"
    requests.packages.urllib3.disable_warnings() #不顯示格式警告
    response1 = requests.get(cctvapiurl, verify=False)
    if response1.status_code == 200:
        urlretrieve(cctvapiurl,"./resources/CCTV.xml") #讀網頁內檔案 .xml
    else:
        return "檢查權限或暫時離線"
    treedata = etree.parse("./resources/CCTV.xml")
    root = treedata.getroot()
    cctvY,cctvX,cctvURL=[],[],[]
    try:
        for i in root[3]:
            cctv_temp=[]
            for j in i:
                cctv_temp.append(j.text)    
            cctvY.append(cctv_temp[5])
            cctvX.append(cctv_temp[6])
            cctvURL.append(cctv_temp[3])
    except:
        return "沒讀到XML"
getevt(),getscctv()

