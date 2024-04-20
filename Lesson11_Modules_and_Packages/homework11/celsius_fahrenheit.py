temperature_value = int(input('Enter temperature value: '))
temperature_units = input('Select input temperature units: \n1)Celsius degrees (\u00B0C) '
                          '\n2)Fahrenheit (\u00B0F) \n(enter the corresponding number(1 or 2):')


def temperature_conversion(temperature_value: int, temperature_units: str) -> int:
    if temperature_units == '1':
        result = int(32 + (temperature_value * 9 / 5))
        input_temperature_unit = '\u00B0C'
        output_temperature_unit = '\u00B0F'
    elif temperature_units == '2':
        result = int((temperature_value - 32) * (5 / 9))
        input_temperature_unit = '\u00B0F'
        output_temperature_unit = '\u00B0C'
    else:
        raise ValueError('Invalid value entered.')
    return result, input_temperature_unit, output_temperature_unit


result, input_temperature_unit, output_temperature_unit = temperature_conversion(temperature_value, temperature_units)
print(f'Result of converting {temperature_value} {input_temperature_unit} is {result} {output_temperature_unit}.')
