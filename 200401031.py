import math
import time
import numpy as np
import matplotlib.pyplot as plt



ogrenci_no=int(input("Ogrenci numaranızı giriniz : "))
rakamlar =[] #öğrenci numarasındaki rakamları birler basamağından sırayla buraya atacağız 

def rakam(number):
   
    liste_boyutu = basamak(number)

    for i in range(liste_boyutu):
        rakamlar.append(int(number % 10))
        number //= 10

    return rakamlar[::-1] 

# öğrenci numarasının rakamlarının tutulduğu liste için basamak sayısı lazım
def basamak(number):
    if number == 0:
        return 1  # Sıfırın bir basamağı vardır
    basamak = 0
    while (number >= 1):
        basamak += 1
        number //= 10

    return basamak

# Genlik için öğrenci numarasının rakamlarını toplayan fonksiyon
def rakamları_topla(liste):
    toplam=0
    for i in range(len(liste)):
        toplam+=liste[i]


    return toplam

# Denemeler
#print("Sayının basamağı: ",basamak(ogrenci_no))
#print("Sayının basamağı: ",len(rakamlar))
#print("Sayının rakamları ters liste:", rakam(ogrenci_no))
#print("Sayının  rakamları normal liste:", rakamlar)

#print("Sayının rakamlar toplamo: ",rakamları_topla(rakamlar))
#print("rakamlar[0]", rakamlar[0])
#print("rakamlar[8]:", rakamlar[8])


rakam(ogrenci_no)# rakamları listeye atıyoruz
A = rakamları_topla(rakamlar) #GENLİk
RTGG=rakamları_topla(rakamlar)/len(rakamlar) #Random toplamsal gürültü genliği

#print("",A)
#print("",RTGG)
frekanslar= [1000, 2000, 5000]

#zaman aralığı oluşturalım 𝑟𝑜𝑢𝑛𝑑(öğ𝑟𝑒𝑛𝑐𝑖 𝑛𝑜(ilk rakam + son rakam )/2)

t_aralık = round((rakamlar[0]+rakamlar[len(rakamlar)-1])/2)
t=np.linspace(0, t_aralık, 1000)  #(rakamlar[8]+rakamlar[0])/2

# Gürültüsüz orijinal sinüs sinyalleri tanımı - x(t)
sinüs1=A * np.sin(2 * np.pi * frekanslar[0] * t)
sinüs2=A * np.sin(2 * np.pi * frekanslar[1] * t)
sinüs3=A * np.sin(2 * np.pi * frekanslar[2] * t)

# Orijinal işarete Random toplamsal gürültü ekleyelim.
gurultu = np.random.normal(0, RTGG, len(t))

#orjinal işaretlerin gürültülü sinyalini oluşturalım.
gurultulu1= sinüs1 + gurultu
gurultulu2= sinüs2 + gurultu
gurultulu3= sinüs3 + gurultu
"""

def gürültü_gideren(sinyal, pencere_boyutu):
    # Zero-pad the signal
    sinyal_padded = np.pad(sinyal, (pencere_boyutu // 2, pencere_boyutu // 2), mode='constant')

    # Convolve with the window
    gürültüsüz = np.convolve(sinyal_padded, np.ones(pencere_boyutu) / pencere_boyutu, mode='valid')
    return gürültüsüz

"""
"""
def gürültü_gideren(signal, window_size):
    N = len(signal)  # Sinyalin uzunluğu
    gurultusuz = [0] * N  # Temizlenmiş sinyali saklamak için bir dizi oluşturun

    for i in range(N):
        # Kayan ortalama hesaplama
        if i <= window_size:
            gurultusuz[i] = sum(signal[0:i + 1]) / (i + 1)
        else:
            gurultusuz[i] = sum(signal[i - window_size + 1:i + 1]) / window_size

    return gurultusuz

# Üç noktalı kayan ortalama algoritması ile gürültüyü gideren algoritma
def gürültü_gideren(sinyal,pencere_boyutu):   
    gürültüsüz = np.convolve(sinyal, np.ones(pencere_boyutu)/pencere_boyutu, mode='valid')
    return gürültüsüz
"""
#yukardaki yorum satırına aldığımız gürültü giderme algoritması ile pencere 2 de istediğimizi elde edemedik çünkü sinyal çıkartması yaptığında uzunluk farkı ortaya çıkıyordu
#Aşağıdaki algoritmada her elamanın üzerinde dönerek her bir elemanın etrafında bir pencere oluşturmalıyız ve bu pencerenin ortalaması, temizlenmiş sinyalin o konumdaki değeri olarak atamamız gereklidir.. 
#Yani bir sinyalin üzerindeki lokal ortalamayı hesaplayarak  bu şekilde gürültüyü azaltmaya çalışacağız. 

def gürültü_gideren(sinyal, pencere_boyutu):
    sinyal_uzunlugu = len(sinyal)
    gürültüsüz_sinyal = np.zeros(sinyal_uzunlugu) # elemanları atmak için dizi oluşturduk.
#Bir döngü içinde her eleman için şu adımları uygulamamız gereklidir.
#1-baslangic_indeksi ve bitis_indeksi, pencerenin başlangıç ve bitiş indekslerini tutacak. Bu, pencerenin sinyalin kenarlarına kadar taşmamasını sağlar.
#2-Belirtilen indekslere sahip pencere, pencere adlı bir alt dizi olarak alınır.
#3-Pencerenin ortalaması hesaplanır ve gürültüsüz sinyalin ilgili indeksine atanarak gürültü pencere boyutuna göre giderilmiş olur.
    for i in range(sinyal_uzunlugu):
        baslangic_indeksi = max(0, i - pencere_boyutu // 2)
        bitis_indeksi = min(sinyal_uzunlugu, i + pencere_boyutu // 2 + 1)

        pencere = sinyal[baslangic_indeksi:bitis_indeksi]
        gürültüsüz_sinyal[i] = np.mean(pencere)

    return gürültüsüz_sinyal



gurultusuz1 = gürültü_gideren(gurultulu1,3)
gurultusuz2 = gürültü_gideren(gurultulu2,3)
gurultusuz3 = gürültü_gideren(gurultulu3,3)

# Pencere boyutları için 0 dan farklı rakamlar_çarpımı gereklidir
rakamlar_carpimi = 1
for i in rakamlar:
    if(i!=0):
        rakamlar_carpimi = rakamlar_carpimi * i

#print("Rakamlar Çarpımı:", rakamlar_carpimi)
pencere_boyutu1=0
pencere_boyutu2=0
if (rakamlar_carpimi%10 <10) :
    pencere_boyutu1=rakamlar_carpimi%10
else:
    
    print("Pencere_boyutu1 10'dan büyüktür!!!")

if(rakamlar_carpimi%100 < 100):
    pencere_boyutu2=rakamlar_carpimi%100

else:
    print("Pencere_boyutu2 100'den büyüktür!!!")    

#pencere boyutu 1 - 2 için gürültüsüzü sinyaller
pencere1_1 =gürültü_gideren(gurultulu1, pencere_boyutu1) #1000 hz 
pencere1_2 =gürültü_gideren(gurultulu2, pencere_boyutu1) #2000 hz 
pencere1_3 =gürültü_gideren(gurultulu3, pencere_boyutu1) #5000 hz 


pencere2_1 =gürültü_gideren(gurultulu1, pencere_boyutu2) #1000 hz 
pencere2_2 =gürültü_gideren(gurultulu2, pencere_boyutu2) #2000 hz 
pencere2_3 =gürültü_gideren(gurultulu3, pencere_boyutu2) #5000 hz 


#Zaman aralıklarını güncelleyelim
gürültüsüz_t = t[:len(gurultusuz1)]
gürültüsüz_pencere1_t= t[:len(pencere1_1)]
gürültüsüz_pencere2_t = t [:len(pencere2_1)]


#-------------------------------------------- RAPOR İÇİN RMSE VE SNR HESAPLAMA -----------------------------------------

def SNR_Hesapla(orjinal_sinyal, gürültülü_sinyal, gürültüden_arındırılmış_sinyal):
    gürültülü= gürültülü_sinyal - orjinal_sinyal
    arındırılmış_gürültü = gürültüden_arındırılmış_sinyal - orjinal_sinyal

    snr_gürültülü = 10 * np.log10(np.sum(orjinal_sinyal**2) / np.sum(gürültülü**2))
    snr_arındırılmış_gürültü= 10 * np.log10(np.sum(orjinal_sinyal**2) / np.sum(arındırılmış_gürültü**2))

    return snr_gürültülü, snr_arındırılmış_gürültü

def RMSE_Hesapla(orjinal_sinyal, gürültülü_sinyal, gürültüden_arındırılmış_sinyal):
    error_noisy = orjinal_sinyal - gürültülü_sinyal
    error_smoothed = orjinal_sinyal - gürültüden_arındırılmış_sinyal
   #mse 'nin karekökü rmse yapar rmse mse ye göre daha anlamlıdır.
    mse_noisy = np.mean(error_noisy**2)
    mse_smoothed = np.mean(error_smoothed**2)

    rmse_gürültülü = np.sqrt(mse_noisy)
    rmse_gürültüden_arındırılmış= np.sqrt(mse_smoothed)

    return rmse_gürültülü, rmse_gürültüden_arındırılmış

# --------------------------   RAPOR İÇİN SNR HESAPLA   ---------------------------------------

#---------------------------          1000 Hz           ---------------------------------------

print("------------------------------  SNR DEĞERLERİ ------------------------------------------")
gürültülü_SNR, ücnoktalı_gürültüsüz_SNR = SNR_Hesapla(sinüs1, gurultulu1, gurultusuz1)
gürültülü_SNR,p1_gürültüsüz_SNR = SNR_Hesapla(sinüs1, gurultulu1, pencere1_1)
gürültülü_SNR,p2_gürültüsüz_SNR = SNR_Hesapla(sinüs1, gurultulu1, pencere2_1)

print("1000 Hz Gürültülü sinyalin SNR değeri = ",gürültülü_SNR)
print("1000 Hz 3 noktalı kayan ortalamanın SNR değeri = ",ücnoktalı_gürültüsüz_SNR)
print("1000 Hz Pencere boyutu 1'in SNR değeri = ",p1_gürültüsüz_SNR)
print("1000 Hz Pencere boyutu 2'nin SNR değeri = ",p2_gürültüsüz_SNR)

#---------------------------          2000 Hz           ---------------------------------------

gürültülü_SNR,ücnoktalı_gürültüsüz_SNR = SNR_Hesapla(sinüs2, gurultulu2, gurultusuz2)
gürültülü_SNR,p1_gürültüsüz_SNR = SNR_Hesapla(sinüs2, gurultulu2, pencere1_2)
gürültülü_SNR,p2_gürültüsüz_SNR = SNR_Hesapla(sinüs2, gurultulu2, pencere2_2)

print("2000 Hz Gürültülü sinyalin SNR değeri = ",gürültülü_SNR)
print("2000 Hz 3 noktalı kayan ortalamanın SNR değeri = ",ücnoktalı_gürültüsüz_SNR)
print("2000 Hz Pencere boyutu 1'in SNR değeri = ",p1_gürültüsüz_SNR)
print("2000 Hz Pencere boyutu 2'nin SNR değeri = ",p2_gürültüsüz_SNR)

#---------------------------          5000 Hz           ---------------------------------------

gürültülü_SNR,ücnoktalı_gürültüsüz_SNR = SNR_Hesapla(sinüs3, gurultulu3, gurultusuz3)
gürültülü_SNR,p1_gürültüsüz_SNR = SNR_Hesapla(sinüs3, gurultulu3, pencere1_3)
gürültülü_SNR,p2_gürültüsüz_SNR = SNR_Hesapla(sinüs3, gurultulu3, pencere2_3)

print("5000 Hz Gürültülü sinyalin SNR değeri = ",gürültülü_SNR)
print("5000 Hz 3 noktalı kayan ortalamanın SNR değeri = ",ücnoktalı_gürültüsüz_SNR)
print("5000 Hz Pencere boyutu 1'in SNR değeri = ",p1_gürültüsüz_SNR)
print("5000 Hz Pencere boyutu 2'nin SNR değeri = ",p2_gürültüsüz_SNR)

print(" ")

# --------------------------   RAPOR İÇİN RMSE HESAPLA   ---------------------------------------

#---------------------------          1000 Hz           ---------------------------------------

print("------------------------------  RMSE DEĞERLERİ ------------------------------------------")
gürültülü_RMSE,ücnoktalı_gürültüsüz_RMSE = RMSE_Hesapla(sinüs1, gurultulu1, gurultusuz1)
gürültülü_RMSE,p1_gürültüsüz_RMSE = RMSE_Hesapla(sinüs1, gurultulu1, pencere1_1)
gürültülü_RMSE,p2_gürültüsüz_RMSE = RMSE_Hesapla(sinüs1, gurultulu1, pencere2_1)

print("1000 Hz Gürültülü sinyalin RMSE değeri = ",gürültülü_RMSE)
print("1000 Hz 3 noktalı kayan ortalamanın RMSE değeri = ",ücnoktalı_gürültüsüz_RMSE)
print("1000 Hz Pencere boyutu 1'in RMSE değeri = ",p1_gürültüsüz_RMSE)
print("1000 Hz Pencere boyutu 2'nin RMSE değeri = ",p2_gürültüsüz_RMSE)

#---------------------------          2000 Hz           ---------------------------------------

gürültülü_RMSE,ücnoktalı_gürültüsüz_RMSE = RMSE_Hesapla(sinüs2, gurultulu2, gurultusuz2)
gürültülü_RMSE,p1_gürültüsüz_RMSE = RMSE_Hesapla(sinüs2, gurultulu2, pencere1_2)
gürültülü_RMSE,p2_gürültüsüz_RMSE = RMSE_Hesapla(sinüs2, gurultulu2, pencere2_2)

print("2000 Hz Gürültülü sinyalin RMSE değeri = ",gürültülü_RMSE)
print("2000 Hz 3 noktalı kayan ortalamanın RMSE değeri = ",ücnoktalı_gürültüsüz_RMSE)
print("2000 Hz Pencere boyutu 1'in RMSE değeri = ",p1_gürültüsüz_RMSE)
print("2000 Hz Pencere boyutu 2'nin RMSE değeri = ",p2_gürültüsüz_RMSE)

#---------------------------          5000 Hz           ---------------------------------------

gürültülü_RMSE,ücnoktalı_gürültüsüz_RMSE = RMSE_Hesapla(sinüs3, gurultulu3, gurultusuz3)
gürültülü_RMSE,p1_gürültüsüz_RMSE = RMSE_Hesapla(sinüs3, gurultulu3, pencere1_3)
gürültülü_RMSE,p2_gürültüsüz_RMSE = RMSE_Hesapla(sinüs3, gurultulu3, pencere2_3)

print("5000 Hz Gürültülü sinyalin RMSE değeri = ",gürültülü_RMSE)
print("5000 Hz 3 noktalı kayan ortalamanın RMSE değeri = ",ücnoktalı_gürültüsüz_RMSE)
print("5000 Hz Pencere boyutu 1'in RMSE değeri = ",p1_gürültüsüz_RMSE)
print("5000 Hz Pencere boyutu 2'nin RMSE değeri = ",p2_gürültüsüz_RMSE)


#----------------------------  GÖRSELLEŞTİRME ----------------------------




#                                1000 Hz
# 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True) 

fig.suptitle('3 Noktalı 1000 Hz ', fontsize=20, ha='center')

axs[0].plot(t,sinüs1,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu1,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_t,gurultusuz1,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu1,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_t,gurultusuz1,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')



#                                2000 Hz
# 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True) 

fig.suptitle('3 Noktalı 2000 Hz ', fontsize=20, ha='center')

axs[0].plot(t,sinüs2,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu2,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_t,gurultusuz2,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu2,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_t,gurultusuz2,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')




#                                5000 Hz                  
# 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True) 

fig.suptitle('3 Noktalı 5000 Hz ', fontsize=20, ha='center')

axs[0].plot(t,sinüs3,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu3,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_t,gurultusuz3,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu3,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_t,gurultusuz3,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')



#                             Pencere Boyutu 1
#                                1000 Hz                  
# 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True)
fig.suptitle('Pencere Boyutu 1 - 1000 Hz', fontsize=20)

axs[0].plot(t,sinüs1,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu1,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_pencere1_t,pencere1_1,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu1,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_pencere1_t,pencere1_1,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')


#                                2000 Hz
# 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True)
fig.suptitle('Pencere Boyutu 1 - 2000 Hz', fontsize=20)

axs[0].plot(t,sinüs2,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu2,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_pencere1_t,pencere1_2,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu2,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_pencere1_t,pencere1_2,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')

#                                5000 Hz
# 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True)
fig.suptitle('Pencere Boyutu 1 - 5000 Hz', fontsize=20)

axs[0].plot(t,sinüs3,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu3,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_pencere1_t,pencere1_3,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu3,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_pencere1_t,pencere1_3,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')



#                                Pencere Boyutu 2
#                                    1000 Hz
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True)
fig.suptitle('Pencere Boyutu 2 - 1000 Hz', fontsize=20)

axs[0].plot(t,sinüs1,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu1,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_pencere2_t,pencere2_1,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu1,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_pencere2_t,pencere2_1,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')



#                                    2000 Hz
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True)
fig.suptitle('Pencere Boyutu 2 - 2000 Hz', fontsize=20)

axs[0].plot(t,sinüs2,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu2,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_pencere2_t,pencere2_2,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu2,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_pencere2_t,pencere2_2,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')


#                                    5000 Hz
fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True)
fig.suptitle('Pencere Boyutu 2 - 5000 Hz', fontsize=20)

axs[0].plot(t,sinüs3,color="black",linewidth = 5)
axs[0].set_title('Orjinal İşaret')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('x(t)')

axs[1].plot(t,gurultu,color="red",linewidth = 5)
axs[1].set_title('Gürültü İşareti')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('x(t)')


axs[2].plot(t,gurultulu3,color="#800080",linewidth = 5)
axs[2].set_title('Gürültülü İşaret')
axs[2].set_xlabel('t(sn)')
axs[2].set_ylabel('x(t)')

axs[3].plot(gürültüsüz_pencere2_t,pencere2_3,color="green",linewidth = 5)
axs[3].set_title('Gürültüden Arındırılmış İşaret')
axs[3].set_xlabel('t(sn)')
axs[3].set_ylabel('x(t)')

axs[4].plot(t,gurultulu3,color="black",linewidth = 5,label="Gürültülü İşaret")
axs[4].plot(gürültüsüz_pencere2_t,pencere2_3,color="#FFA500",linewidth = 5,label="Gürültüden Arındırılmış İşaret")
axs[4].set_title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret')
axs[4].set_xlabel('t(sn)')
axs[4].set_ylabel('x(t)')

# --------------------------------------------- SNR RMSE KARŞILAŞTIRMA ------------------------------------------------------------------------------------------------

# İşaret Gürültü Oranı
def SNR(sinyal, gürültü):
    sin_gücü = sinyal**2
    gürültü_gücü =gürültü**2
    snr = 10 * np.log10(sin_gücü / gürültü_gücü)
    return snr

# Kök ortalama kare hatası
def RMSE(sinyal, gürültü):
    # İki diziyi de aynı uzunluğa getirelim
    min_len = min(len(sinyal), len(gürültü))
    sinyal = sinyal[:min_len]
    gürültü = gürültü[:min_len]
    
    return np.sqrt(np.mean((sinyal - gürültü)**2))



rmse1 = RMSE(gurultulu3,gurultu)
rmse2 = RMSE(pencere2_3,gurultu[31:])
snr1 = []
snr2 = []
for i in range(len(gurultulu3)):
    snr1.append(SNR(gurultulu3[i], gurultu[i]))

for i in range(len(pencere2_3)):
    snr2.append(SNR(pencere2_3[i], gurultu[i]))

# ----------------------- SNR - RMSE - GÖRSELLEŞTİRME -------------------

fig, axs = plt.subplots(5, 1, figsize=(8,8),constrained_layout=True)
fig.suptitle('Pencere Boyutu 2 - 3  Noktalı - SNR Karşılaştırma - 5000 Hz', fontsize=16)

axs[0].plot(t,snr1,color="black",linewidth = 5)
axs[0].set_title('3 nokta - 5000 Hz')
axs[0].set_xlabel('t(sn)')
axs[0].set_ylabel('dB(desibel)')

axs[1].plot(gürültüsüz_pencere2_t,snr2,color="red",linewidth = 5)
axs[1].set_title('Pencere 2 - 5000 Hz')
axs[1].set_xlabel('t(sn)')
axs[1].set_ylabel('dB(desibel)')

axs[2].text(0.5, 0.5, 'SNR,istenilen bir sinyalin arka plandaki gürültü seviyesiyle karşılaştıran bir ölçüdür.0 dB den\nbüyük bir rakam gürültüden fazla sinyal olduğunu gösterir.SNR değerinin yüksek olması,\nsinyal-gürültü oranının yüksek olduğunu ve istenen sinyalin belirgin olduğunu gösterir.\nHesaplamalara göre 5000Hz için Üç noktalı kayan ortalama ile sinyal daha belirgindir.',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7),
            horizontalalignment='center', verticalalignment='center', fontsize=12, color='blue')
axs[2].axis('off')  # Eksenleri kapatmak için

bars1=axs[3].bar("RMSE \n 3 Noktalı 5000 Hz",rmse1,width=0.2,color="black")
bars2= axs[3].bar("RMSE \n Pencere 2 5000 Hz",rmse2,width=0.2,color="red")
axs[3].set_title('3 Noktalı - Pencere2 - RMSE Karşılaştırması - 5000 Hz')
axs[3].set_xlabel('RMSE Karşılatırma')
axs[3].set_ylabel('RMSE DEĞERİ')
# Bar'ların üzerine değerleri ekleyelim.
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
        axs[3].text(i - 0.03 , bar1.get_height() - 4.5, f"{bar1.get_height():.2f}", color="red", fontweight="bold")
        axs[3].text(i + 0.97, bar2.get_height() - 4.5, f"{bar2.get_height():.2f}", color="black", fontweight="bold")

axs[4].text(0.5, 0.5, 'RMSE değerinin düşük olması, orjinal sinyal ile gürültüden arındırılmış sinyal arasındaki farkın\nküçük olduğunu ve sinyalin yüksek oranda gürültüden arındırıldığını gösterir. Karşılaştırma,\nhangi sinyalin daha iyi gürültüden arındırılmış olduğunu değerlendirmemize olanak tanır.\nBu sebeple pencere boyutu 2 kullanarak oluşturduğumuz sinyal daha doğru,\ngüvenilirdir ve sinyali daha iyi oranda gürültüden arındırmıştır.',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7),
            horizontalalignment='center', verticalalignment='center', fontsize=12, color='blue')
axs[4].axis('off')  # Eksenleri kapatmak için
 
plt.legend()

plt.show()


