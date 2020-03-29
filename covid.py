import requests
import bs4

negara = input("Masukkan nama negara: ")

def covid_19(country):
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    index = -1
    data = soup.select('tr td')
    for i in range (len(data)):
        if data [i].text.lower()==country.lower():
            index = i
            break
    
    for i in range(7):
        if i== 0:
            print("\nNegara: "+str(data[i+index].text))
        elif i==1:
            print("\nJumlah Kasus: "+str(data[i+index].text))
        elif i == 2:
            if data[i+index].text == '':
                print("Kasus baru: 0")
            else:
                print("Kasus baru: "+str(data[i+index].text))
        elif i == 3:
            print("Total kematian: "+str(data[i+index].text))
        elif i == 4:
            if data[i+index].text == '':
                print("Kematian baru: 0")
            else:
                print("Kematian baru: "+str(data[i+index].text))
        elif i == 5:
            print("Sembuh: "+str(data[i+index].text))
        elif i == 6:
            print("Kasus yang sedang aktif: "+str(data[i+index].text),end='\n\n')
covid_19(negara)