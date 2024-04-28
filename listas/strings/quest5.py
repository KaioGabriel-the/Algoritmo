def month_in_full(month):
    if month == '01':
        return str('January')
    elif month == '02':
        return str('February')
    elif month == '03':
        return str('March')
    elif month == '04':
        return str('April')
    elif month == '05':
        return str('May')
    elif month == '06':
        return str('June')
    elif month == '07':
        return str('July')
    elif month == '08':
        return str ('August')
    elif month == '09':
        return str('September')
    elif month == '10':
        return str('October')
    elif month == '11':
        return str('November')
    elif month == '12':
        return str('December')


def main():

    date = str(input('Ex:DD/MM/AAAA --> '))
    break_date = date.split("/")
    month = month_in_full(break_date[1])

    print(f'{month} {break_date[0]},{break_date[2]}')

main()
