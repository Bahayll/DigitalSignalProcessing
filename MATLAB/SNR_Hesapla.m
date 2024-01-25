function [snr_gurultulu, snr_arindirilmis_gurultu] = SNR_Hesapla(orjinal_sinyal, gurultulu_sinyal, gurultuden_arindirilmis_sinyal)
    gurultulu = gurultulu_sinyal - orjinal_sinyal;
    arindirilmis_gurultu = gurultuden_arindirilmis_sinyal - orjinal_sinyal;

    snr_gurultulu = 10 * log10(sum(orjinal_sinyal.^2) / sum(gurultulu.^2));
    snr_arindirilmis_gurultu = 10 * log10(sum(orjinal_sinyal.^2) / sum(arindirilmis_gurultu.^2));
end
