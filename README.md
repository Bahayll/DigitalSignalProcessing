----------------------------------------------------------- MATLAB ve PYTHON kullanarak kayan ortalama algoritması ile bir işaretin gürültüden arındırılması ---------------------------------------------------------------------------

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



