function toplam = rakamlar_topla(liste)
    toplam = 0;
    for i = 1:length(liste)
        toplam = toplam + liste(i);
    end
end