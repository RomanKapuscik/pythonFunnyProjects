import PySimpleGUI as sg


def int_to_bin(number: int, n_of_bits: int, notation_type: int) -> str:
    """Function converting a given integer to its binary representation using n number of bits.

    :param int notation_type: 1.SM (ZM), 2.1C (U1), 3.2C (U2)
    :param int number:
    :param int n_of_bits:
    :return: binary representation of a number
    :rtype: str
    """
    binary = ''
    n_of_bits -= 1
    positive = number > 0
    number = abs(number)
    while n_of_bits >= 0:
        if number >= 2**n_of_bits:
            binary += '1'
            number -= 2 ** n_of_bits
        else:
            binary += '0'
        n_of_bits -= 1
    if number > 0:
        return 'more bits needed to convert given number to binary'
    if notation_type == 1:    # ZM
        if positive:
            return '0. ' + binary
        else:
            return '1. ' + binary
    elif notation_type == 2:    # U1
        if positive:
            return '0 ' + binary
        else:
            u1 = ''
            for char in binary:
                if char == '0':
                    u1 += '1'
                else:
                    u1 += '0'
            return '1 ' + u1
    elif notation_type == 3:    # U2
        if positive:
            return '0 ' + binary
        else:
            u2 = ''
            extra = False
            for char in binary:
                if char == '0':
                    u2 += '1'
                else:
                    u2 += '0'
            u2 = u2[::-1]
            u2_final = ''
            first_iteration = True
            for char in u2:
                if char == '0' and first_iteration:
                    u2_final += '1'
                elif char == '1' and first_iteration:
                    u2_final += '0'
                    extra = True
                elif char == '0' and extra:
                    u2_final += '1'
                    extra = False
                elif char == '1' and extra:
                    u2_final += '0'
                    extra = True
                elif not first_iteration:
                    u2_final += char
                first_iteration = False
            return '1 ' + u2_final[::-1]


sg.theme('DarkAmber')

layout = [[sg.Text('Integer: '), sg.InputText(key='-IN_NUMBER-')],
          [sg.Text('Number of bites: '), sg.InputText(key='IN_BITES')],
          [sg.Button('SM'), sg.Button('1C'), sg.Button('2C')],
          [sg.Text(key='-OUTPUT-')],
          [sg.Button('Cancel')]]

window = sg.Window('INTEGER -> BINARY', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'SM':
        window['-OUTPUT-'].update(int_to_bin(int(values['-IN_NUMBER-']), int(values['IN_BITES']), 1))
    elif event == '1C':
        window['-OUTPUT-'].update(int_to_bin(int(values['-IN_NUMBER-']), int(values['IN_BITES']), 2))
    elif event == '2C':
        window['-OUTPUT-'].update(int_to_bin(int(values['-IN_NUMBER-']), int(values['IN_BITES']), 3))

window.close()
