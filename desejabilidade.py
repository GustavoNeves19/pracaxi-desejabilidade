def desejabilidade_global(abts, tpc, tf,
                          L_abts=5.5209, T_abts=118.70,
                          L_tpc=0.0400, T_tpc=0.8600,
                          L_tf=0.005439, T_tf=0.054651,
                          s=1):
    def d_ind(y, L, T):
        if y < L:
            return 0
        elif L <= y <= T:
            return ((y - L) / (T - L)) ** s
        else:
            return 1

    d_abts = d_ind(abts, L_abts, T_abts)
    d_tpc = d_ind(tpc, L_tpc, T_tpc)
    d_tf = d_ind(tf, L_tf, T_tf)
    D = (d_abts * d_tpc * d_tf) ** (1/3)
    return D, d_abts, d_tpc, d_tf
