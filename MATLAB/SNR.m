function snr = SNR(sinyal, gurultu)
    sin_gucu = sinyal.^2;
    gurultu_gucu = gurultu.^2;
    snr = 10 * log10(sin_gucu ./ gurultu_gucu);
end