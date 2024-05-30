def main():
    ##Qual o tipo de horario
    kind = input(str('what kind timetable(N/M): '))

    ##Horario normal para militar
    if kind == "N":

        timetable_n = (input("timetable(:): ")).split(":")
        _type = input(str('kind(AM/PM): ')) 

        transforme_n = time_transforme_n(_type,timetable_n[0])

        print(f'{transforme_n}:{timetable_n[1]}:{timetable_n[2]}')
    ##Horario militar para o normal
    elif kind == "M":

        timetable_m = (input("timetable(:): ")).split(":")
        transforme_m = time_transforme_m(timetable_m[0])
        am_pm = tronsforme(timetable_m[0])

        print(f'{transforme_m}:{timetable_m[1]}:{timetable_m[2]} {am_pm}')
    ##Não exite essa variavel
    else:
        print(f"It doesn't exist")

def time_transforme_n(_type,timetable_n):

    ##Manhã
    if _type == "AM":
        if timetable_n == "12":
            print("00")
        elif timetable_n == "01":
            print('01')
        elif timetable_n == "02":
            print('02')
        elif timetable_n == "03":
            print('03')
        elif timetable_n == "04":
            print('04')
        elif timetable_n == "05":
            print('05')
        elif timetable_n == "06":
            print('06')
        elif timetable_n == "07":
            print('07')
        elif timetable_n == "08":
            print('08')
        elif timetable_n == "09":
            print('09')
        elif timetable_n == "10":
            print('10')
        elif timetable_n == "11":
            print('11')
    ##Tarde
    elif _type == "PM":
        if timetable_n == "12":
            print('12')
        elif timetable_n == "01":
            print('13')
        elif timetable_n == "02":
            print('14')
        elif timetable_n == "03":
            print('15')
        elif timetable_n == "04":
            print('16')
        elif timetable_n == "05":
            print('17')
        elif timetable_n == "06":
            print('18')
        elif timetable_n == "07":
            print('19')
        elif timetable_n == "08":
            print('20')
        elif timetable_n == "09":
            print('21')
        elif timetable_n == "10":
            print('22')
        elif timetable_n == "11":
            print('23')

def time_transforme_m(timetable_m):

    if timetable_m == "00":
        print("12")
    elif timetable_m == "01":
        print('01')
    elif timetable_m == "02":
        print('02')
    elif timetable_m == "03":
        print('03')
    elif timetable_m == "04":
        print('04')
    elif timetable_m == "05":
        print('05')
    elif timetable_m == "06":
        print('06')
    elif timetable_m == "07":
        print('07')
    elif timetable_m == "08":
        print('08')
    elif timetable_m == "09":
        print('09')
    elif timetable_m == "10":
        print('10')
    elif timetable_m == "11":
     print('11')
    elif timetable_m == "12":
        print('12')
    elif timetable_m == "13":
        print('01')
    elif timetable_m == "14":
        print('02')
    elif timetable_m == "15":
        print('03')
    elif timetable_m == "16":
        print('04')
    elif timetable_m == "17":
     print('05')
    elif timetable_m == "18":
        print('06')
    elif timetable_m == "19":
        print('07')
    elif timetable_m == "20":
        print('08')
    elif timetable_m == "21":
        print('09')
    elif timetable_m == "22":
        print('10')
    elif timetable_m == "23":
     print('11')

def tronsforme(timetable_m):
    if int(timetable_m) >= 00 and int(timetable_m) <= 11:
        print('AM')
    else:
        print('PM')

main()