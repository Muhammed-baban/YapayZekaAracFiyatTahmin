import os

dataCar={'Marka':[],
    'Seri':[],
    'Yıl':[],
    'Kasa Tipi':[],
    'Yakit Tipi':[],
    'Vites Tipi':[],
    'Paket':[],
    'Km':[],
    'Tramer':[]
    ,'Fiyat':[]}

for path in os.listdir():

    if path != 'dataClear.py':
        for file in os.listdir(path+'/'):
            if file=='desktop.ini':
                pass
            else:
                with open(path+'/'+str(file),'r',encoding='utf-8') as f:
                    carInfo = list(f)
                    marka = carInfo[carInfo.index('Marka:\n')+1]
                    model = carInfo[carInfo.index('Seri:\n')+1]
                    year = carInfo[carInfo.index('Yıl:\n')+1]
                    kasaTipi = carInfo[carInfo.index('Kasa Tipi:\n')+1]
                    yakiTipi = carInfo[carInfo.index('Yakıt Tipi:\n')+1]
                    vitesTipi = carInfo[carInfo.index('Vites Tipi:\n')+1]
                    paket = carInfo[carInfo.index('Model:\n')+1]
                    km = carInfo[carInfo.index('Kilometre:\n')+1]
                    degisen = carInfo[carInfo.index('Boya-değişen:\n')+1]
                    tramer = carInfo[carInfo.index('ARAÇ BİLGİLERİ\n')-1]
                    fiyat =carInfo[carInfo.index('İlan No:\n')-2]
                    if degisen == 'Belirtilmemiş\n':

                        sagArkaCamurluk = 'Belirtilmemiş'
                        arkaKaput = 'Belirtilmemiş'
                        solArkaCamurluk = 'Belirtilmemiş'
                        sagArkaKapı = 'Belirtilmemiş'
                        sagOnKapi = 'Belirtilmemiş'
                        tavan = 'Belirtilmemiş'
                        solArkaKapi = 'Belirtilmemiş'
                        solOnKapi = 'Belirtilmemiş'
                        sagOnCamurluk = 'Belirtilmemiş'
                        motorKaput = 'Belirtilmemiş'
                        solOnCamurluk = 'Belirtilmemiş'
                        onTampon = 'Belirtilmemiş'
                        arkaTampon = 'Belirtilmemiş'

                    elif degisen == 'Tamamı orjinal\n':
                        sagArkaCamurluk = 'Orjinal1'
                        arkaKaput = 'Orjinal1'
                        solArkaCamurluk = 'Orjinal1'
                        sagArkaKapı = 'Orjinal1'
                        sagOnKapi = 'Orjinal1'
                        tavan = 'Orjinal1'
                        solArkaKapi = 'Orjinal1'
                        solOnKapi = 'Orjinal1'
                        sagOnCamurluk = 'Orjinal1'
                        motorKaput = 'Orjinal1'
                        solOnCamurluk = 'Orjinal1'
                        onTampon = 'Orjinal1'
                        arkaTampon = 'Orjinal1'

                    else:
                        try:
                            sagArkaCamurluk = carInfo[carInfo.index('Sağ Arka Çamurluk:  \n')+1]
                            arkaKaput = carInfo[carInfo.index('Arka Kaput:  \n')+1]
                            solArkaCamurluk = [carInfo.index('Sol Arka Çamurluk:  \n')+1]
                            sagArkaKapı = carInfo[carInfo.index('Sağ Arka Kapı:  \n')+1]
                            sagOnKapi = carInfo[carInfo.index('Sağ Ön Kapı:  \n')+1]
                            tavan = carInfo[carInfo.index('Tavan:  \n')+1]
                            solArkaKapi = carInfo[carInfo.index('Sol Arka Kapı:  \n')+1]
                            solOnKapi = carInfo[carInfo.index('Sol Ön Kapı:  \n')+1]
                            sagOnCamurluk = carInfo[carInfo.index('Sağ Ön Çamurluk:  \n')+1]
                            motorKaput = carInfo[carInfo.index('Motor Kaputu:  \n')+1]
                            solOnCamurluk = carInfo[carInfo.index('Sol Ön Çamurluk:  \n')+1]
                            onTampon = carInfo[carInfo.index('Ön Tampon:  \n')+1]
                            arkaTampon = carInfo[carInfo.index('Arka Tampon:  \n')+1]
                        except:
                            pass
                        
                    if tramer == 'Değişmiş\n':

                        tramer = 'Belirtilmemiş'

                    elif tramer == 'Detaylı bilgi almak için satıcı ile iletişime geçebilirsiniz.\n':
                        tramer = 'Belirtilmemiş'

                    elif tramer == 'Tramer tutarı belirtilmemiş\n':
                        tramer == 'Belirtilmemiş'

                    elif tramer == 'Tramer tutarı yok\n':
                        tramer = '0'

                    dataCar['Marka'].append(marka)
                    dataCar['Seri'].append(model)
                    dataCar['Yıl'].append(year)
                    dataCar['Kasa Tipi'].append(kasaTipi)
                    dataCar['Vites Tipi'].append(vitesTipi)
                    dataCar['Yakit Tipi'].append(yakiTipi)
                    dataCar['Km'].append(km)
                    dataCar['Paket'].append(paket)
                    dataCar['Tramer'].append(tramer)
                    dataCar['Fiyat'].append(fiyat)

                    f.close()
        
    import pandas as pd

dataFrame = pd.DataFrame(data=dataCar)
dataFrame = dataFrame.transpose()
dataFrame = (dataFrame.T)
dataFrame.to_excel('Master.xlsx')