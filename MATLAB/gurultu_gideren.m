function gurultusuz_sinyal = gurultu_gideren(sinyal, pencere_boyutu)
    sinyal_uzunlugu = length(sinyal);
    gurultusuz_sinyal = zeros(1, sinyal_uzunlugu);
%Bir döngü içinde her eleman için şu adımları uygulamamız gereklidir.
%1-baslangic_indeksi ve bitis_indeksi, pencerenin başlangıç ve bitiş indekslerini tutacak. Bu, pencerenin sinyalin kenarlarına kadar taşmamasını sağlar.
%2-Belirtilen indekslere sahip pencere, pencere adlı bir alt dizi olarak alınır.
%3-Pencerenin ortalaması hesaplanır ve gürültüsüz sinyalin ilgili indeksine atanarak gürültü pencere boyutuna göre giderilmiş olur.
    for i = 1:sinyal_uzunlugu
        baslangic_indeksi = max(1, i - floor(pencere_boyutu / 2));
        bitis_indeksi = min(sinyal_uzunlugu, i + floor(pencere_boyutu / 2));

        pencere = sinyal(baslangic_indeksi:bitis_indeksi);
        gurultusuz_sinyal(i) = mean(pencere);
    end
end