function rmse = RMSE(sinyal, gurultu)
    % İki diziyi de aynı uzunluğa getirelim
    min_len = min(length(sinyal), length(gurultu));
    sinyal = sinyal(1:min_len);
    gurultu = gurultu(1:min_len);
    
    rmse = sqrt(mean((sinyal - gurultu).^2));
end
