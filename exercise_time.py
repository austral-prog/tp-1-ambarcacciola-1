def time():
    total_segundos = 3665

    horas = total_segundos // 3600
    resto = total_segundos % 3600

    minutos = resto // 60
    segundos = resto % 60

    print(horas)
    print(minutos)
    print(segundos)
time()

