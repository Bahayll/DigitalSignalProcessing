function [rmse_gurultulu, rmse_arindirilmis_gurultu] = RMSE_Hesapla(orjinal_sinyal, gurultulu_sinyal, gurultuden_arindirilmis_sinyal)
    hata_gurultulu = orjinal_sinyal - gurultulu_sinyal;
    hata_arindirilmis_gurultu = orjinal_sinyal - gurultuden_arindirilmis_sinyal;

    mse_gurultulu = mean(hata_gurultulu.^2);
    mse_arindirilmis_gurultu = mean(hata_arindirilmis_gurultu.^2);

    rmse_gurultulu = sqrt(mse_gurultulu);
    rmse_arindirilmis_gurultu = sqrt(mse_arindirilmis_gurultu);
end
