import folium
from folium.plugins import MarkerCluster
from resources.mapdef import MapInfo
db = MapInfo().evt_db()
df = MapInfo().evt_df()
cY,cX,cUrl= MapInfo().cctv_Y() , MapInfo().cctv_X() , MapInfo().cctv_URL()
fmap = folium.Map(location=[25.05561, 121.32844],zoom_start=10,minZoom=8) #預設南投竹山
def displayenvMap(): #純事件地圖
    for i in range(len(db)): 
        mapy , mapx = df.loc[i,"y1"],df.loc[i,"x1"]
        evtIcon = folium.CustomIcon('./resources/logo.png',icon_size = (30, 30),icon_anchor = (15, 30)) 
        try:
            folium.Marker(location=[mapy , mapx],icon=evtIcon,popup=df.loc[i,"comment"]+"時間："+df.loc[i,"modDttm"]).add_to(fmap)
        except:
            return "error format"
def displayenvR():
    marker_cluster = MarkerCluster().add_to(fmap)
    for i in range(len(db)): 
        mapy , mapx = df.loc[i,"y1"],df.loc[i,"x1"]
        evtIcon = folium.CustomIcon('./resources/logo.png',icon_size = (30, 30),icon_anchor = (15, 30)) 
        try:
            folium.Marker(location=[mapy , mapx],icon=evtIcon,popup=df.loc[i,"comment"]+"時間："+df.loc[i,"modDttm"]).add_to(marker_cluster)
        except:
            return "error format"
    fmap.add_child(marker_cluster)
def displaycamera():
    for j in range(len(cUrl)):
        fmap.add_child(folium.Marker(location=[cX[j] , cY[j]],popup=cUrl[j],icon=folium.Icon(color="green", icon="ok-sign")))
################################################################
displayenvR()
displaycamera()
fmap.save("map.htm")