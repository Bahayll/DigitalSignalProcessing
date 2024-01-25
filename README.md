--------- MATLAB ve PYTHON kullanarak kayan ortalama algoritması ile bir işaretin gürültüden arındırılması -----------

1- Gürültüsüz orijinal bir sinüs işareti tanımlayın.  
𝑥(𝑡) = 𝐴𝑠𝑖𝑛(2𝜋𝑓𝑡) 
Parametre tanımlama kuralları: 
-öğrenci no: 210401008 olsun 
-𝐴 = öğrenci no’daki rakamlar toplamı (Genlik) 
-𝑓 = 1000 Hz, 2000 Hz, 5000 Hz için üç farklı sinyal örnekleme; (Örnekleme frekansı) 
-0 ≤ 𝑡 ≤ 𝑟𝑜𝑢𝑛𝑑(öğ𝑟𝑒𝑛𝑐𝑖 𝑛𝑜 𝑖𝑙𝑘 𝑟𝑎𝑘𝑎𝑚+𝑠𝑜𝑛 𝑟𝑎𝑘𝑎𝑚2) 

2- Orijinal işarete Random toplamsal gürültü ekleyin. 
Random toplamsal gürültü genliği= öğrenci no’daki rakamlar toplamı/rakam sayısı

3- Üç noktalı kayan ortalama algoritması ile gürültüyü gideren algoritmayı yazın ve kodu çalıştırın. 

4-  Kayan Ortalama Algoritması Parametreleri ile ayarlanabilir Pencere boyutu (üç noktalı kayan ortalama gibi düşünerek) kullanarak gürültüyü gideren algoritmayı yazın ve kodu çalıştırın.
%pencere_boyutu1=öğrenci no’daki sıfırdan farklı rakamların çarpımı (mod10) %pencere_boyutu2=öğrenci no’daki sıfırdan farklı rakamların çarpımı (mod100) Sonuçlar 10’dan ve 100’den küçük ise çıkan sayıyı pencere boyutu olarak atayın.

5- Sonuçlar 5 farklı grafik başlığı altında (orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret, farklı renkli ve üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma) 
tek pencerede alt alta bu sıra ile sunulacak. Yani grafikler 1 sütun 5 satır şeklinde yukarıdaki sırada ekrana basılacak. Her pencere farklı alt projeler için ayrı ayrı isimlendirilecek ve sunulacak.
Örneğin f=1000 Hz için bir pencerede 5 grafik olacak, 5000 Hz için ayrı bir pencerede 5 grafik olacak. Yine benzer şekilde f=1000 Hz için üç-noktalı kayan ortalama algoritması başka bir pencerede, ayarlanabilir pencere boyutu1 için başka bir pencerede, pencere boyutu2
bir diğer pencere sunulacak.  6- SNR (Signal-to-Noise Ratio - İşaret-Gürültü Oranı) ve RMSE (Root Mean Square Error - Kök Ortalama Kare Hata) metrikleri sayısal ve kantitatif metriklerdir. İşaret işleme ve sinyal analizi alanlarında kullanılan bu metrikler, 
işaretin kalitesini ve gürültü seviyesini değerlendirmek için kullanılır. SNR ve RMSE metrikleri kullanarak gürültülü ve gürültüden arındırılmış işaretlerin kantitatif analizlerini yapınız, değişimi (iyileşme/kötüleşme) sayısal veriler kullanarak tartışınız 
ve raporlayınız. 

6- Proje çıktıları şu şekilde özetlenebilir: 
𝑓 = 1000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (Üç noktalı kayan ortalama algoritması ile), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 2000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (Üç noktalı kayan ortalama algoritması ile), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 5000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (Üç noktalı kayan ortalama algoritması ile), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 1000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (ayarlanabilir pencere boyutu1 için), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 2000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (ayarlanabilir pencere boyutu1 için), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 5000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (ayarlanabilir pencere boyutu1 için), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 1000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (ayarlanabilir pencere boyutu2 için), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 2000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (ayarlanabilir pencere boyutu2 için), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = 5000 Hz için tek pencerede orijinal işaret, gürültü işareti, gürültülü işaret, gürültüden arındırılmış işaret (ayarlanabilir pencere boyutu2 için), üst üste gürültülü işaret ve gürültüden arındırılmış işaret-aynı pencerede karşılaştırma 
𝑓 = …..için (1000, 2000 veya 5000 Hz’den birini seçiniz) tek pencerede gürültülü işaret ile gürültüden arındırılmış işareti (bu üçünden bir yöntemi seçiniz: Üç noktalı kayan ortalama algoritması ile veya ayarlanabilir pencere boyutu1 için veya
ayarlanabilir pencere boyutu2 için) SNR ve RMSE ile karşılaştırınız, çok kısaca grafiğin yanına yorum yazınız.



![Figure 1 26 01 2024 00_01_49](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/28e57712-885e-430b-91a2-4e121d45f7ba)

![Figure 2 26 01 2024 00_02_06](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/294b50c5-5996-4547-b078-0f6ca55f042a)

![Figure 3 26 01 2024 00_02_16](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/7f5bc192-e551-4a2a-93c1-72a3b7c4313f)

![Figure 4 26 01 2024 00_02_25](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/1317b02d-2f28-4516-bcde-47bcddcec8c3)

![Figure 5 26 01 2024 00_02_33](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/d2912f5d-68f4-41ab-a17a-f9e4fd45c5b8)

![Figure 6 26 01 2024 00_02_38](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/eed01482-2846-4a9b-96ab-576aa26397f4)

![Figure 7 26 01 2024 00_02_46](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/8fe4aa56-0760-4b7a-a3e8-05311143ecd7)

![Figure 8 26 01 2024 00_02_53](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/e76810c7-d91c-4c36-9825-5441c849b364)

![Figure 9 26 01 2024 00_03_02](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/c387f131-ae4d-4c6d-9140-dd0a524ba8a9)

![Figure 10 26 01 2024 00_03_10](https://github.com/Bahayll/DigitalSignalProcessing/assets/120746431/0fb1515f-c555-4b1e-8f23-03cc6c44b3c8)










