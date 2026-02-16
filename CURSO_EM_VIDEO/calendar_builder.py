import calendar

text_cal = calendar.TextCalendar(firstweekday=0)

year = int(input('\nAno: '))
width = int(input('Largura: '))
# width = 2
print(f'\033[32m{text_cal.formatyear(year, width)}\033[m')