shift_roman = { '4': ['IV', 'XL', 'CD'], '9': ['IX', 'XC', 'CM']}
shift_numbers = dict(IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
arabic_numbers = [1000, 500, 100, 50, 10, 5, 1]
roman_numbers = ['M', 'D', 'C', 'L', 'X', 'V', 'I']


def to_roman(number):
    output = ''
    for i in arabic_numbers:
        d = number % i
        c = number // i
        if c >= 1:
            output += roman_numbers[arabic_numbers.index(i)] * c
            number = d
        numb = str(d)
        if numb[0] in shift_roman:
            output += shift_roman[numb[0]][len(numb) - 1]
            if len(numb) == 1:
                break
            number = int(numb[1:])
            continue
    return output


def to_arabic(number):
    output_number = 0
    while len(number) != 0:
        numb = number[:2]
        if len(number) >= 2 and numb in shift_numbers.keys():
            output_number += shift_numbers.get(numb)
            number = number[2:]
        else:
            output_number += int(arabic_numbers[roman_numbers.index(number[:1])])
            number = number[1:]
    return output_number


print('Sum is:', to_roman(to_arabic(input('First: ')) + to_arabic(input('Second: '))))

