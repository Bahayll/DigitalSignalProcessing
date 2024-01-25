function rakamlar = rakam(number)
    rakamlar = []; % Initialize an empty array
    
    liste_boyutu = basamak(number);

    for i = 1:liste_boyutu
        rakamlar = [rakamlar, mod(number, 10)]; 
        number = floor(number / 10);
    end

    rakamlar = fliplr(rakamlar); 
end

