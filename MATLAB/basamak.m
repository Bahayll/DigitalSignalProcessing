function basamak_sayisi = basamak(number)
    if number == 0
        basamak_sayisi = 1;  % Sıfırın bir basamağı vardır
    else
        basamak_sayisi = 0;
        while (number >= 1)
            basamak_sayisi = basamak_sayisi + 1;
            number = floor(number / 10);
        end
    end
end