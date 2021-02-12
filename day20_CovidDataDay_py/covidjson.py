import requests
 

response = requests.get("https://data.covid19.go.id/public/api/update.json")
api = response.json()
positif = f'{api["update"]["penambahan"]["jumlah_positif"]:,}'
meninggal = f'{api["update"]["penambahan"]["jumlah_meninggal"]:,}'
sembuh = f'{api["update"]["penambahan"]["jumlah_sembuh"]:,}'
s = positif+" Positive \n"+meninggal+" Death \n"+sembuh+" People Cure \n\n" + "Last Update From Indonesia daily indonesia: " + api["update"]["penambahan"]["created"]
  
print(s)