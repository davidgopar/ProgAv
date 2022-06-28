'''Tarea 9'''
# Gopar Morales David
# Progra. Av.
# tarea 9

import re

# 1. Extraer el nombre de un archivo de una trayectoria del sistema de archivos
# P. ej. "$HOME/proyecto1/modulo5/programa3.py" -> "programa3.py"

a = re.match('.*/(.*)', "$HOME/proyecto1/modulo5/programa3.py")
print(a.group(1))


# --------------------------------------------------------------


# 2. Escribir la función date_in_spanish. Use re.sub para sustituir los nombres
# de los meses.
def date_in_spanish(date):
    """
    Translates a string date to spanish. That is, all references to months
    abbreviations like 'Jan', 'Feb', 'Mar' and so on are changed to 'Ene',
    'Feb', 'Mar', respectively.

    Parameters
    ----------
    date : str
        Date to be translated.

    Returns
    ------
        str
        The translated base_date.

    Examples
    --------
    >>> date_in_spanish("23-Apr-2021")
    23-Abr-2021
    >>> date_in_spanish("Dec-24-2020")
    Dic-24-2020
    """

    aux = re.match(r'(\d{2})-(\D{3})-(\d{4})', date)  # DD-MM-YYYY
    if aux:
        if aux.group(2) == 'Jan':
            date = re.sub('Jan', 'Ene', date)
        elif aux.group(2) == 'Apr':
            date = re.sub('Apr', 'Abr', date)
        elif aux.group(2) == 'Aug':
            date = re.sub('Aug', 'Ago', date)
        elif aux.group(2) == 'Dec':
            date = re.sub('Dec', 'Dic', date)
        return date

    # se asumirá que entonces el formato de fecha es MM-DD-YYYY
    aux = re.match(r'(\D{3})-(\d{2})-(\d{4})', date)
    if aux.group(1) == 'Jan':
        date = re.sub('Jan', 'Ene', date)
    elif aux.group(1) == 'Apr':
        date = re.sub('Apr', 'Abr', date)
    elif aux.group(1) == 'Aug':
        date = re.sub('Aug', 'Ago', date)
    elif aux.group(1) == 'Dec':
        date = re.sub('Dec', 'Dic', date)
    return date


print(date_in_spanish('Feb-11-2020'))


# -------------------------------------------------------------------


# 3. Escribir la siguiente función
# def from_standard_equity_option_convention(code: str) -> dict:
#  """
#   Transform a standard equity option convention code to record representation.
#
#   Parameters
#   ----------
#   code : str
#       Standard equity option convention code (see
#       https://en.wikipedia.org/wiki/Option_naming_convention).
#
#   Returns
#   -------
#       dict
#       A dictionary containing:
#       'symbol': Symbol name
#       'expire': Option expiration base_date
#       'right': Put (P) or Call (C).
#       'strike': Option strike
#
#   Examples:
#   >>> from_standard_equity_option_convention('YHOO150416C00030000')
#    {'symbol': 'YHOO', 'expire': '20150416', 'right': 'C', 'strike': 30.0}
#	"""

def from_standard_equity_option_convention(code):
    """
    Transform a standard equity option convention code to record representation.

    Parameters
    ----------
    code : str
        Standard equity option convention code (see
        https://en.wikipedia.org/wiki/Option_naming_convention).

    Returns
    -------
        dict
        A dictionary containing:
        'symbol': Symbol name
        'expire': Option expiration base_date
        'right': Put (P) or Call (C).
        'strike': Option strike

    Examples:
    >>> from_standard_equity_option_convention('YHOO150416C00030000')
    {'symbol': 'YHOO', 'expire': '20150416', 'right': 'C', 'strike': 30.0}
    """
    val = re.match(r'(\D{1,6})(\d{6})(\D)(\d{5})(\d{3})', code)

    diccionario = {}
    diccionario['symbol'] = val.group(1)
    diccionario['expire'] = '20' + val.group(2)
    diccionario['right'] = val.group(3)
    diccionario['strike'] = float(val.group(4) + '.' + val.group(5))

    return diccionario


print(from_standard_equity_option_convention('YHOO150416C00030000'))

# -------------------------------------------------------------------

# 4. Explique con palabras qué hace la siguiente instrucción
# symbols_str = re.sub(r"'", "''", str(symbols))

# Solución: Donde vea ' lo va a sustituir por '',
# por ejemplo, a'a, lo cambia por a''a
# lalsks'asks se cambia por lalsks''asks
#


# --------------------------------------------------------------------


# 5. Escriba una cadena 'account' apropiada para que se ejecute la instrucción print
# if re.match(r'DU[0-9]{7}', account):
#    print("Account: ", account)

account = 'DU1234567'
if re.match(r'DU[0-9]{7}', account):
    print("Account: ", account)

# -------------------------------------------------------


# 6
# Escriba la expresión regular de manera más sintética pero preservando la funcionalidad.
# if re.match('^([0-9][0-9][0-9][0-9][0-9][0-9])$', text):
#    LOGGER.info("Correct OTP format: %s.", text)


# Solución:
# if re.match('^([0-9]{6})$', text):
#    LOGGER.info("Correct OTP format: %s.", text)

# if re.match('^(\d{6})$', text):
#    LOGGER.info("Correct OTP format: %s.", text)


# ------------------------------------------------------------


# 7. ¿Cuál es el valor de 'reg_exp' que hace funcionar el código siguiente?
# if re.match(reg_exp, text) is None:
#    error_message = \
#        "Try again, your answer does not correspond to a comma " + \
#       "separated integers list. Type something like '1, 2, 3' " + \
#       "without the apostrophes."

# Solución
# reg_exp='([0-9]+(,\s[0-9]+)*)*$' este considera espacios y la posible lista vacía
# reg_exp='[0-9]+(,[0-9]+)*$'       no considera espacios entre las comas ni la lista vacía

# Ejemplo

if re.match(r'[0-9]+(,[0-9]+)*$', '1111, 2'):
    print(re.match(r'[0-9]+[,[0-9]+]*$', '1111,2'))


# Nota,otra manera es ocupar re.fullmatch
# if re.fullmatch('[0-9]+(,[0-9]+)*', '1111,2'):
#	print(re.fullmatch('[0-9]+[,[0-9]+]*', '1111,2'))
# pues re.match() = Looks for a regex match at the beginning of a string
#     re.fullmatch() =	Looks for a regex match on an entire string


# ---------------------------------------------------


# 8. Programar el método siguiente.
# def collect_commission_adjustment(data):

def collect_commission_adjustment(data):
    """
    Retrieve a commision adjustment record from the section "Commission
    Adjustments" in one Interactive Brokers activity report.

    PARAMETERS
    ----------
    data : list[]
        Line from the activity report in the "Commission Adjustment" section
        in list format. That is, each element in the list is a comma
        separated item from the line.

    RETURNS
    -------
        dict
        Containing the open position information in dictionary format.

    Examples
    --------
    >>> collect_commission_adjustment(['Commission Adjustments', 'Data', 'USD',
    ... '2021-04-23',
    ... 'Commission Computed After Trade Reported (C     210430C00069000)',
    ... '-1.0906123', '\\n'])
    {'end_date': '20210423', 'symbol': 'C', 'expire': '20210430', \
'right': 'C', 'strike': 69.0, 'sectype': 'OPT', 'amount': -1.0906123}
    >>> collect_commission_adjustment(
    ... ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
    ... 'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n'])
    {'end_date': '20210219', 'symbol': 'ALB', 'sectype': 'STK', \
'amount': -0.4097}
    >>> collect_commission_adjustment(
    ... ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
    ... 'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n'])
    {'end_date': '20210219', 'symbol': 'ALB', 'sectype': 'STK', \
'amount': -0.4097}
    """
    diccionario = {}
    diccionario['end_date'] = re.sub('-', '', data[3])

    aux = re.match(r'Commission Computed After Trade Reported'
                   r' \(([A-Z]+)\s*(\d{6})(\D+)(\d{5})(\d{3})\)', data[4])
    if aux:

        diccionario['symbol'] = aux.group(1)
        diccionario['expire'] = '20' + aux.group(2)
        diccionario['right'] = aux.group(3)
        diccionario['strike'] = float(aux.group(4) + '.' + aux.group(5))
        diccionario['sectype'] = 'OPT'
    else:

        diccionario['symbol'] = re.match(r'Commission Computed After Trade '
                                         r'Reported \(([A-Z]+).*\)', data[4]).group(1)
        diccionario['sectype'] = 'STK'
    diccionario['amount'] = data[5]

    return diccionario


print(collect_commission_adjustment(['Commission Adjustments', 'Data', 'USD',
                                     '2021-04-23',
                                     'Commission Computed After Trade Reported'
                                     ' (C     210430C00069000)',
                                     '-1.0906123', '\\n']))


# ---------------------------------------------------------


# 9. De dos ejemplos de uso del siguiente método. En el primero el método debe
# regresar un número de punto flotante y en el segundo np.nan

#def banxico_value(tag, data):
#    """
#    Get data values from Banxico portals.
#
#   Parameters
#   ----------
#   tag : str
#       Internal tag name of the variable to retrieve.
#   data : str
#       Html page to locate the tag value.
#
#   Returns
#   --------
#       float
#       The associated tag value.
#   """
#   float_nt = "[^0-9-]*([-]*[0-9]+.[0-9]+)[^0-9]"
#   try:
#       res = float(re.search(tag + float_nt, data).group(1))
#   except AttributeError:
#       res = np.nan
#   return res

# Solución:
#	Un ejemplo de que nos regrese un número de punto flotante sería
#	que primero coincida con data = tag + 'a-1231/123a'
#	donde el grupo que nos regresaría es '1231/123'
#	y se haría res = float('1231/123')

#	El caso en que no entra sería por ejemplo en que data =
#	tag + 'abcd'


# -------------------------------------------------------------


# 10. Describa en palabras qué hace el siguiente código.
# col_sel = list(
#        map(
#           lambda s: s if re.match("[Ii][Mm][Ff][0-9]+", s) else None,
#           dat_df.columns,
#        ))
# col_sel = [c for c in col_sel if c is not None]


# Solución:
#	En un principio se crea una función en que a cada elemento de dat_df.columns
#	se le asigna el mismo si coincide con '[Ii][Mm][Ff][0-9]+', y en caso de no coincidir
#	se le asigna None. Posteriormente con estos se crea la lista col_sel y el el último
#	renglón se dejan solo los elementos que no sean None, y todos los que sean None se
#	ya no aparecen.
