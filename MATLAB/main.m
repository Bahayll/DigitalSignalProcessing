function [] = main()

sayi = input('Lütfen Öğrenci Numaranızı Giriniz: ');
 disp(['Girilen sayı: ' num2str(sayi)]);
  

    basamak_sayisi = basamak(sayi);
disp(['Basamak Sayısı: ' num2str(basamak_sayisi)]);


   
    rakamlar = rakam(sayi); % Rakamları listeye attık 
disp(['Rakam Listesi: ' num2str(rakamlar)]);

    A = rakamlar_topla(rakamlar) % Genlik

disp(['Orjinal Sinyal Genliği: ' num2str(A)]);

   RTGG = A/basamak_sayisi %Random Toplamsal Gürültü Genliği

  disp(['Random Toplamsal Gürültü Genliği: ' num2str(RTGG)]);
 
  frekanslar = [1000, 2000, 5000];

  % zaman aralığı oluşturalım 𝑟𝑜𝑢𝑛𝑑(öğ𝑟𝑒𝑛𝑐𝑖 𝑛𝑜(ilk rakam + son rakam )/2)
  t_aralik = round((rakamlar(1) + rakamlar(end)) / 2);
  t = linspace(0, t_aralik, 1000);

 % Gürültüsüz orijinal sinüs sinyalleri tanımı - x(t)
 sinus1 = A * sin(2 * pi * frekanslar(1) * t);
 sinus2 = A * sin(2 * pi * frekanslar(2) * t);
 sinus3 = A * sin(2 * pi * frekanslar(3) * t);

 % Orijinal işarete Random toplamsal gürültü ekleyelim.
 gurultu = RTGG * randn(size(t));

 gurultulu1= sinus1 + gurultu
 gurultulu2= sinus2 + gurultu
 gurultulu3= sinus3 + gurultu

 gurultusuz1 = gurultu_gideren(gurultulu1,3)
 gurultusuz2 = gurultu_gideren(gurultulu2,3)
 gurultusuz3 = gurultu_gideren(gurultulu3,3)

 % Pencere boyutları için 0 dan farklı rakamlar_çarpımı gereklidir
rakamlar_carpimi = 1;
for i = rakamlar
    if i ~= 0
        rakamlar_carpimi = rakamlar_carpimi * i;
    end
end

% fprintf('Rakamlar Çarpımı: %d\n', rakamlar_carpimi);

pencere_boyutu1 = 0;
pencere_boyutu2 = 0;

if (mod(rakamlar_carpimi, 10) < 10)
    pencere_boyutu1 = mod(rakamlar_carpimi, 10);
else
    fprintf('Pencere_boyutu1 10''dan büyüktür!!!\n');
end

if (mod(rakamlar_carpimi, 100) < 100)
    pencere_boyutu2 = mod(rakamlar_carpimi, 100);
else
    fprintf('Pencere_boyutu2 100''den büyüktür!!!\n');
end

%pencere boyutu 1 - 2 için gürültüsüzü sinyaller
pencere1_1 =gurultu_gideren(gurultulu1, pencere_boyutu1) %1000 hz 
pencere1_2 =gurultu_gideren(gurultulu2, pencere_boyutu1) %2000 hz 
pencere1_3 =gurultu_gideren(gurultulu3, pencere_boyutu1) %5000 hz 


pencere2_1 =gurultu_gideren(gurultulu1, pencere_boyutu2) %1000 hz 
pencere2_2 =gurultu_gideren(gurultulu2, pencere_boyutu2) %2000 hz 
pencere2_3 =gurultu_gideren(gurultulu3, pencere_boyutu2) %5000 hz 

% Zaman aralıklarını güncelleyelim
gurultusuz_t = t(1:length(gurultusuz1));
gurultusuz_pencere1_t = t(1:length(pencere1_1));
gurultusuz_pencere2_t = t(1:length(pencere2_1));



% --------------------------   RAPOR İÇİN SNR HESAPLA   ---------------------------------------
%---------------------------          1000 Hz           ---------------------------------------

fprintf('------------------------------  SNR DEĞERLERİ ------------------------------------------\n');
[gurultulu_SNR, ucnoktali_gurultusuz_SNR] = SNR_Hesapla(sinus1, gurultulu1, gurultusuz1);
[gurultulu_SNR, p1_gurultusuz_SNR] = SNR_Hesapla(sinus1, gurultulu1, pencere1_1);
[gurultulu_SNR, p2_gurultusuz_SNR] = SNR_Hesapla(sinus1, gurultulu1, pencere2_1);

fprintf('1000 Hz Gürültülü sinyalin SNR değeri = %f\n', gurultulu_SNR);
fprintf('1000 Hz 3 noktalı kayan ortalamanın SNR değeri = %f\n', ucnoktali_gurultusuz_SNR);
fprintf('1000 Hz Pencere boyutu 1''in SNR değeri = %f\n', p1_gurultusuz_SNR);
fprintf('1000 Hz Pencere boyutu 2''nin SNR değeri = %f\n', p2_gurultusuz_SNR);

%---------------------------          2000 Hz           ---------------------------------------

[gurultulu_SNR, ucnoktali_gurultusuz_SNR] = SNR_Hesapla(sinus2, gurultulu2, gurultusuz2);
[gurultulu_SNR, p1_gurultusuz_SNR] = SNR_Hesapla(sinus2, gurultulu2, pencere1_2);
[gurultulu_SNR, p2_gurultusuz_SNR] = SNR_Hesapla(sinus2, gurultulu2, pencere2_2);

fprintf('2000 Hz Gürültülü sinyalin SNR değeri = %f\n', gurultulu_SNR);
fprintf('2000 Hz 3 noktalı kayan ortalamanın SNR değeri = %f\n', ucnoktali_gurultusuz_SNR);
fprintf('2000 Hz Pencere boyutu 1''in SNR değeri = %f\n', p1_gurultusuz_SNR);
fprintf('2000 Hz Pencere boyutu 2''nin SNR değeri = %f\n', p2_gurultusuz_SNR);

%---------------------------          5000 Hz           ---------------------------------------

[gurultulu_SNR, ucnoktali_gurultusuz_SNR] = SNR_Hesapla(sinus3, gurultulu3, gurultusuz3);
[gurultulu_SNR, p1_gurultusuz_SNR] = SNR_Hesapla(sinus3, gurultulu3, pencere1_3);
[gurultulu_SNR, p2_gurultusuz_SNR] = SNR_Hesapla(sinus3, gurultulu3, pencere2_3);

fprintf('5000 Hz Gürültülü sinyalin SNR değeri = %f\n', gurultulu_SNR);
fprintf('5000 Hz 3 noktalı kayan ortalamanın SNR değeri = %f\n', ucnoktali_gurultusuz_SNR);
fprintf('5000 Hz Pencere boyutu 1''in SNR değeri = %f\n', p1_gurultusuz_SNR);
fprintf('5000 Hz Pencere boyutu 2''nin SNR değeri = %f\n', p2_gurultusuz_SNR);

fprintf(' \n');

% --------------------------   RAPOR İÇİN RMSE HESAPLA   ---------------------------------------
%---------------------------          1000 Hz           ---------------------------------------

fprintf('------------------------------  RMSE DEĞERLERİ ------------------------------------------\n');
[gurultulu_RMSE, ucnoktali_gurultusuz_RMSE] = RMSE_Hesapla(sinus1, gurultulu1, gurultusuz1);
[gurultulu_RMSE, p1_gurultusuz_RMSE] = RMSE_Hesapla(sinus1, gurultulu1, pencere1_1);
[gurultulu_RMSE, p2_gurultusuz_RMSE] = RMSE_Hesapla(sinus1, gurultulu1, pencere2_1);

fprintf('1000 Hz Gürültülü sinyalin RMSE değeri = %f\n', gurultulu_RMSE);
fprintf('1000 Hz 3 noktalı kayan ortalamanın RMSE değeri = %f\n', ucnoktali_gurultusuz_RMSE);
fprintf('1000 Hz Pencere boyutu 1''in RMSE değeri = %f\n', p1_gurultusuz_RMSE);
fprintf('1000 Hz Pencere boyutu 2''nin RMSE değeri = %f\n', p2_gurultusuz_RMSE);

%---------------------------          2000 Hz           ---------------------------------------

[gurultulu_RMSE, ucnoktali_gurultusuz_RMSE] = RMSE_Hesapla(sinus2, gurultulu2, gurultusuz2);
[gurultulu_RMSE, p1_gurultusuz_RMSE] = RMSE_Hesapla(sinus2, gurultulu2, pencere1_2);
[gurultulu_RMSE, p2_gurultusuz_RMSE] = RMSE_Hesapla(sinus2, gurultulu2, pencere2_2);

fprintf('2000 Hz Gürültülü sinyalin RMSE değeri = %f\n', gurultulu_RMSE);
fprintf('2000 Hz 3 noktalı kayan ortalamanın RMSE değeri = %f\n', ucnoktali_gurultusuz_RMSE);
fprintf('2000 Hz Pencere boyutu 1''in RMSE değeri = %f\n', p1_gurultusuz_RMSE);
fprintf('2000 Hz Pencere boyutu 2''nin RMSE değeri = %f\n', p2_gurultusuz_RMSE);

%---------------------------          5000 Hz           ---------------------------------------

[gurultulu_RMSE, ucnoktali_gurultusuz_RMSE] = RMSE_Hesapla(sinus3, gurultulu3, gurultusuz3);
[gurultulu_RMSE, p1_gurultusuz_RMSE] = RMSE_Hesapla(sinus3, gurultulu3, pencere1_3);
[gurultulu_RMSE, p2_gurultusuz_RMSE] = RMSE_Hesapla(sinus3, gurultulu3, pencere2_3);

fprintf('5000 Hz Gürültülü sinyalin RMSE değeri = %f\n', gurultulu_RMSE);
fprintf('5000 Hz 3 noktalı kayan ortalamanın RMSE değeri = %f\n', ucnoktali_gurultusuz_RMSE);
fprintf('5000 Hz Pencere boyutu 1''in RMSE değeri = %f\n', p1_gurultusuz_RMSE);
fprintf('5000 Hz Pencere boyutu 2''nin RMSE değeri = %f\n', p2_gurultusuz_RMSE);



%  ---------------------- GÖRSELLEŞTİRME --------------------------------

% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
% ---------------------- 1000 Hz -----------------------------
figure;
sgtitle('3 Noktalı 1000 Hz ', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus1, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu1, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_t, gurultusuz1, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu1, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_t, gurultusuz1, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;

% ---------------------- 2000 Hz -----------------------------
% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('3 Noktalı 2000 Hz ', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus2, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu2, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_t, gurultusuz2, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu2, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_t, gurultusuz2, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;


% ---------------------- 5000 Hz -----------------------------
% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('3 Noktalı 5000 Hz ', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus3, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu3, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_t, gurultusuz3, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu3, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_t, gurultusuz3, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;

% ---------------------- Pencere Boyutu 1 -----------------------------
% -------------------------- 1000 Hz ----------------------------------

% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('Pencere Boyutu 1 - 1000 Hz', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus1, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu1, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_pencere1_t, pencere1_1, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu1, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_pencere1_t, pencere1_1, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;

% -------------------------- 2000 Hz ----------------------------------

% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('Pencere Boyutu 1 - 2000 Hz', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus2, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu2, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_pencere1_t, pencere1_2, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu2, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_pencere1_t, pencere1_2, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;

% -------------------------- 5000 Hz ----------------------------------

% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('Pencere Boyutu 1 - 5000 Hz', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus3, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu3, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_pencere1_t, pencere1_3, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu3, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_pencere1_t, pencere1_3, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;
% ---------------------- Pencere Boyutu 1 -----------------------------
% -------------------------- 1000 Hz ----------------------------------

% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('Pencere Boyutu 2 - 1000 Hz', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus1, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu1, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_pencere2_t, pencere2_1, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu1, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_pencere2_t, pencere2_1, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;


% -------------------------- 2000 Hz ----------------------------------


% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('Pencere Boyutu 2 - 2000 Hz', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus2, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu2, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_pencere2_t, pencere2_2, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu2, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_pencere2_t, pencere2_2, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;


% -------------------------- 5000 Hz ----------------------------------


% 5 satır 1 sütündan oluşan bir alt grafik düzenine sahip bir figür oluşturalım
figure;
sgtitle('Pencere Boyutu 2 - 5000 Hz', 'FontSize', 20, 'HorizontalAlignment', 'center');

subplot(5, 1, 1);
plot(t, sinus3, 'Color', 'black', 'LineWidth', 5);
title('Orjinal İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 2);
plot(t, gurultu, 'Color', 'red', 'LineWidth', 5);
title('Gürültü İşareti');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 3);
plot(t, gurultulu3, 'Color', '#800080', 'LineWidth', 5);
title('Gürültülü İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 4);
plot(gurultusuz_pencere2_t, pencere2_3, 'Color', 'green', 'LineWidth', 5);
title('Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');

subplot(5, 1, 5);
plot(t, gurultulu3, 'Color', 'black', 'LineWidth', 5, 'DisplayName', 'Gürültülü İşaret');
hold on;
plot(gurultusuz_pencere2_t, pencere2_3, 'Color', '#FFA500', 'LineWidth', 5, 'DisplayName', 'Gürültüden Arındırılmış İşaret');
title('Gürültülü İşaret ve Gürültüden Arındırılmış İşaret');
xlabel('t(sn)');
ylabel('x(t)');
hold off;


snr1 = zeros(1, length(gurultulu3));
snr2 = zeros(1, length(pencere2_3));

rmse1 = RMSE(gurultulu3, gurultu);
rmse2 = RMSE(pencere2_3, gurultu(32:end));

for i = 1:length(gurultulu3)
    snr1(i) = SNR(gurultulu3(i), gurultu(i));
end

for i = 1:length(pencere2_3)
    snr2(i) = SNR(pencere2_3(i), gurultu(i));
end


% ----------------------- SNR - RMSE - GÖRSELLEŞTİRME -------------------


% Subplotları oluştur
figure;
sgtitle('Pencere Boyutu 2 - 3 Noktalı - SNR Karşılaştırma - 5000 Hz');
axs(1) = subplot(3, 1, 1);
axs(2) = subplot(3, 1, 2);
axs(3) = subplot(3, 1, 3);




% SNR Grafiği
plot(axs(1), t, snr1, 'k', 'LineWidth', 5);
title(axs(1), '3 Noktalı - 5000 Hz');
xlabel(axs(1), 't(sn)');
ylabel(axs(1), 'dB(desibel)');

% SNR2 Grafiği
plot(axs(2), gurultusuz_pencere2_t, snr2, 'r', 'LineWidth', 5);
title(axs(2), 'Pencere 2 - 5000 Hz');
xlabel(axs(2), 't(sn)');
ylabel(axs(2), 'dB(desibel)');

% Eksenleri ayarla
linkaxes(axs(3), 'x');
annotation('textbox', [0.1, 0.15, 0.8, 0.15], ...
    'String', {'SNR,istenilen bir sinyalin arka plandaki gürültü seviyesiyle karşılaştıran bir ölçüdür.',...
                '0 dB den büyük bir rakam gürültüden fazla sinyal olduğunu gösterir.SNR değerinin',...
                'yüksek olması, sinyal-gürültü oranının yüksek olduğunu ve istenen sinyalin belirgin olduğunu', ...
                'gösterir. Hesaplamalara göre 5000Hz için Üç noktalı kayan ortalama ile sinyal daha belirgindir.'}, ...
    'FitBoxToText', 'on', 'BackgroundColor', 'white', 'EdgeColor', 'none', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle', 'FontSize', 10, 'Color', 'blue');
set(axs(3), 'Visible', 'off');  % Ekseni kapatmak için

% RMSE Bar'ları oluştur
figure;
axs(3)=subplot(3,1,3);
subplot(3, 1, [1, 2]);
bars1 = bar(1, rmse1, 0.2, 'FaceColor', 'black');
hold on;
bars2 = bar(2, rmse2, 0.2, 'FaceColor', 'red');

% Eksen etiketlerini ve başlıkları ayarla
xticks([1, 2]);
xticklabels({'RMSE 3 Noktalı 5000 Hz', 'RMSE Pencere 2 5000 Hz'});
xlabel('RMSE Karşılaştırma');
ylabel('RMSE DEĞERİ');
title('3 Noktalı - Pencere2 - RMSE Karşılaştırması - 5000 Hz');

% Bar'ların üzerine değerleri ekleyin
text(0.92  , bars1(1).YData -3.5, sprintf('%.2f', bars1(1).YData), 'Color', 'red', 'FontWeight', 'bold');
text(2 -0.08, bars2(1).YData -3.5, sprintf('%.2f', bars2(1).YData), 'Color', 'black', 'FontWeight', 'bold');

linkaxes(axs(3), 'x');
annotation('textbox', [0.1, 0.15, 0.8, 0.15], ...
    'String', {'RMSE değerinin düşük olması, orjinal sinyal ile gürültüden arındırılmış sinyal arasındaki ', ...
               'farkın küçük olduğunu ve sinyalin doğru bir şekilde gürültüden arındıldığını gösterir.',...
               'Karşılaştırma, hangi sinyalin daha iyi gürültüden arındırılmış olduğunu değerlendirmemize ',...
               'olanak tanır. Bu sebeple pencere boyutu 2 kullanarak oluşturduğumuz sinyal daha doğru,',...
               'güvenilirdir ve sinyali daha iyi bir oranda gürültüden arındırmıştır.'}, ...
    'FitBoxToText', 'on', 'BackgroundColor', 'white', 'EdgeColor', 'none', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle', 'FontSize', 10, 'Color', 'blue');
set(axs(3), 'Visible', 'off');  % Ekseni kapatmak için

hold off;

legend;


end