def codificar(x_real, minimo, maximo):
    return 2 * (x_real - minimo) / (maximo - minimo) - 1

def modelo_abts(x):
    tempo, etanol, razao = x
    razao_etanol = razao * etanol
    return (
        23.6431 + 11.6008 * tempo**2 + 21.4325 * etanol +
        13.7585 * etanol**2 - 14.5911 * razao_etanol
    )

def modelo_tpc(x):
    tempo, etanol, razao = x
    razao_etanol = razao * etanol
    return (
        0.1722 + 0.0847 * tempo**2 + 0.1578 * etanol +
        0.0990 * etanol**2 - 0.1084 * razao_etanol
    )

def modelo_tf(x):
    _, _, razao = x
    return 0.0114 - 0.0082 * razao + 0.0063 * razao**2
