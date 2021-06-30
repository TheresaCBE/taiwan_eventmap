import requests , json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
eventapiurl = "https://od.moi.gov.tw/MOI/v1/pbs"
################################################################
response = requests.get(eventapiurl) 
if response.status_code == 200:
    db = json.loads(response.content)
    df = pd.DataFrame.from_dict(db) 
elif response.status_code == 404:
    print("Unknown Resourse")
################
def htimect(aHRpbWVjdA=[]):
    objtimectls=[]
    for k in rdtype:
        timectls=[]
        for i in range(24):
            timect=0
            for j in range(len(db)):
                if i <= 9:
                    ic = "0"+str(i)
                    if k==df["roadtype"][j] and ic == df["happentime"][j][0:2]:
                        timect+=1  
                elif i > 9:
                    if k==df["roadtype"][j] and str(i) == df["happentime"][j][0:2]:
                        timect+=1
            timectls.append(timect)
        objtimectls.append(timectls)
    return objtimectls
def print_line():
    colorls = ["k","lightcoral","sienna","orange","y","lawngreen","g","c","dodgerblue","slategray","b","darkviolet","red","hotpink"]
    ################
    printfont = FontProperties(fname='./resources/DejaVuSansDisplay.ttf', size=40)
    plt.rc('font', family='DFKai-SB', size=12)
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
    for i in range(len(rdtype)):
        plt.plot(timels,Htimect[i],'o--',color = colorls[i], label=rdtype[i],markerfacecolor='none') 
    plt.title("近三日警廣通報道路事件統計", size=26)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=20)
    plt.xlabel("時間", fontsize=30, labelpad = 15)
    plt.ylabel("事件數", fontsize=30, labelpad = 20)
    plt.legend(loc = "best", fontsize=20)
    # 畫出圖片
    return plt.show()
################################################################
rdtype = pd.unique(["{}".format(i) for i in df["roadtype"]]).tolist() #圖類別
timels = ["{}點整".format(i) for i in range(24)] #底時間
Htimect = htimect(rdtype) #數據
