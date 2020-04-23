import folium, pandas as pd
from folium.plugins import MarkerCluster
pdf = pd.read_json('https://tinyurl.com/covid19-github')
pdf = pdf[pdf.data==pdf.data.max()]
pdf = pdf[pdf.totale_casi>0]

centroid = pdf.describe()[['lat','long']].loc['50%'].values
fm = folium.Map(location=centroid, zoom_start=6, tiles='stamentoner',
                width=800, height=600)
mc = MarkerCluster()
for row in pdf.itertuples():
  mc.add_child(folium.Marker(location=[row.lat,row.long],
               popup=row.denominazione_provincia))
mc.add_to(fm)
fm
