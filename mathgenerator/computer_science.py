import random
import math

def floating_point_binary_to_decimal(mantissa_length=8, exponent_length=4):
    r"""Floating Point Binary to Decimal

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | There is a floating point binary number $011100000010$ where the signed mantissa is 8 bits long and the signed exponent is 4 bits long | $011100000010 = 3.5$ |

    """
    # TODO Could do with some work ensuring the number is not too small or too big.
    mantissa = ''
    for x in range(mantissa_length):
        mantissa += str(random.randint(0,1))
    exponent = ''
    for x in range(exponent_length):
        exponent += str(random.randint(0,1))
    decimal_mantissa = int(mantissa, 2)
    if (decimal_mantissa & (1 << (mantissa_length - 1))) != 0:
        decimal_mantissa = decimal_mantissa - (1 << mantissa_length)
    decimal_exponent = int(exponent, 2)
    if (decimal_exponent & (1 << (exponent_length - 1))) != 0:
        decimal_exponent = decimal_exponent - (1 << exponent_length)
    answer = decimal_mantissa * 2**(decimal_exponent - (mantissa_length - 1))

    problem = f"There is a floating point binary number ${mantissa}{exponent}$ where the signed mantissa is {mantissa_length} bits long and the signed exponent is {exponent_length} bits long"
    solution = f'${mantissa}{exponent} = {answer}$'

    return problem, solution

def binary_addition(max_sum=256, max_addend=128):
    r"""Binary Addition

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | In binary, calculate: $101 + 110110 = $ | $111011$ |
    """
    if max_addend > max_sum:
        max_addend = max_sum
    a = random.randint(0, max_addend)
    b = random.randint(0, min((max_sum - a), max_addend))
    c = a + b

    problem = f"In base 2, ${bin(a).replace('0b', "")} + {bin(b).replace('0b', "")} =$ "
    solution = f'${bin(c).replace('0b', "")}$'
    return problem, solution

def bcd_to_decimal(max_number=10000):
    r"""Binary Coded Decimal to Integer

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Integer of Binary Coded Decimal $4 =$ | $17801$ |
    """
    n = random.randint(1000, max_number)
    binstring = ''
    while True:
        q, r = divmod(n, 10)
        nibble = bin(r).replace('0b', "")
        while len(nibble) < 4:
            nibble = '0' + nibble
        binstring = nibble + binstring
        if q == 0:
            break
        else:
            n = q

    problem = f"Integer of Binary Coded Decimal ${n} =$ "
    solution = f'${int(binstring, 2)}$'
    return problem, solution


def binary_2s_complement(maxDigits=10):
    r"""Binary 2's Complement

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | 2's complement of $1011 = $ | $101$ |
    """
    digits = random.randint(1, maxDigits)
    question = ''.join([str(random.randint(0, 1))
                        for i in range(digits)]).lstrip('0')

    answer = []
    for i in question:
        answer.append(str(int(not bool(int(i)))))

    carry = True
    j = len(answer) - 1
    while j >= 0:
        if answer[j] == '0':
            answer[j] = '1'
            carry = False
            break
        answer[j] = '0'
        j -= 1

    if j == 0 and carry is True:
        answer.insert(0, '1')

    problem = f"2's complement of ${question} = $"
    solution = ''.join(answer).lstrip('0')
    return problem, f'${solution}$'


def binary_complement_1s(maxDigits=10):
    r"""Binary Complement 1s

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $1111001 = $ | $0000110$ |
    """
    question = ''.join([
        str(random.randint(0, 1)) for _ in range(random.randint(1, maxDigits))
    ])
    answer = ''.join(["0" if digit == "1" else "1" for digit in question])

    problem = f'${question} = $'
    return problem, f'${answer}$'


def binary_to_decimal(max_dig=10):
    r"""Binary to Decimal

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $000110$ | $6$ |
    """
    problem = ''.join(
        [str(random.randint(0, 1)) for _ in range(random.randint(1, max_dig))])
    solution = f'${int(problem, 2)}$'
    return f'${problem}$', solution


def binary_to_hex(max_dig=10):
    r"""Binary to Hexidecimal

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $010101$ | $0x15$ |
    """
    problem = ''.join(
        [str(random.randint(0, 1)) for _ in range(random.randint(1, max_dig))])
    solution = f'${hex(int(problem, 2))}$'
    return f'${problem}$', solution


def decimal_to_bcd(max_number=10000):
    r"""Decimal to Binary Coded Decimal

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | BCD of Decimal Number $6575 = $ | $191015$ |
    """
    n = random.randint(1000, max_number)
    x = n
    # binstring = ''
    bcdstring = ''
    while x > 0:
        nibble = x % 16
        bcdstring = str(nibble) + bcdstring
        x >>= 4

    problem = f"BCD of Decimal Number ${n} = $"
    return problem, f'${bcdstring}$'


def decimal_to_binary(max_dec=99):
    r"""Decimal to Binary

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Binary of $4 = $ | $100$ |
    """
    a = random.randint(1, max_dec)
    b = bin(a).replace("0b", "")

    problem = f'Binary of ${a} = $'
    solution = f'${b}$'
    return problem, solution


def decimal_to_hexadeci(max_dec=1000):
    r"""Decimal to Hexadecimal

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | Hexadecimal of $410 = $ | $0x19a$ |
    """
    a = random.randint(0, max_dec)
    b = hex(a)

    problem = f"Hexadecimal of ${a} = $"
    solution = f"${b}$"
    return problem, solution


def decimal_to_octal(max_decimal=4096):
    r"""Decimal to Octal

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The decimal number $3698$ in octal is: | $0o7162$ |
    """
    x = random.randint(0, max_decimal)

    problem = f"The decimal number ${x}$ in octal is: "
    solution = f'${oct(x)}$'

    return problem, solution


def fibonacci_series(min_no=1):
    r"""Fibonacci Series

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The Fibonacci Series of the first ${n}$ numbers is ? | $0, 1, 1, 2, 3, 5, 8, 13, 21$ |
    """
    n = random.randint(min_no, 20)

    def createFibList(n):
        list = []
        for i in range(n):
            if i < 2:
                list.append(i)
            else:
                val = list[i - 1] + list[i - 2]
                list.append(val)
        return list

    fibList = createFibList(n)

    problem = "The Fibonacci Series of the first ${n}$ numbers is ?"
    solution = ', '.join(map(str, fibList))
    return problem, f'${solution}$'


def modulo_division(max_res=99, max_modulo=99):
    r"""Modulo Division

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | $43$ % $33 = $ | $10$ |
    """
    a = random.randint(0, max_modulo)
    b = random.randint(0, min(max_res, max_modulo))
    c = a % b if b != 0 else 0

    problem = f'${a}$ % ${b} = $'
    solution = f'${c}$'
    return problem, solution


def nth_fibonacci_number(max_n=100):
    r"""nth Fibonacci number

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the 85th Fibonacci number? | $259695496911123328$ |
    """
    gratio = (1 + math.sqrt(5)) / 2
    n = random.randint(1, max_n)

    problem = f"What is the {n}th Fibonacci number?"
    solution = int(
        (math.pow(gratio, n) - math.pow(-gratio, -n)) / (math.sqrt(5)))

    return problem, f'${solution}$'


def nth_tribonacci_number(min_length=1, max_length=80):
    r"""nth Tribonacci number

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | What is the 14th Tribonacci number? | $504$ |
    """

    tribDict = {0: 0, 1: 0, 2: 1}

    def recTrib(i):
        if i not in tribDict:
            tribDict[i] = recTrib(i - 1) + recTrib(i - 2) + recTrib(i - 3)
        return tribDict[i]

    n = random.randint(min_length, max_length)
    problem = f"What is the {n}th Tribonacci number?"
    solution = recTrib(n - 1)
    return problem, f'${solution}$'


def tribonacci_series(min_length=1, max_length=80):
    r"""Fibonacci Series

    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | The Tribonacci Series of the first $8$ numbers is ? | $0, 0, 1, 1, 2, 4, 7, 13$ |
    """

    tribDict = {0: 0, 1: 0, 2: 1}

    def createTribSeries(i):
        tribSeries = []
        for idx in range(i):
            if idx not in tribDict:
                tribDict[idx] = tribDict[idx - 1] + tribDict[idx - 2] + tribDict[idx - 3]
            tribSeries.append(tribDict[idx])
        return tribSeries

    n = random.randint(min_length, max_length)
    tribSeries = createTribSeries(n)
    problem = "The Tribonacci Series of the first ${n}$ numbers is ?"
    solution = ', '.join(map(str, tribSeries))
    return problem, f'${solution}$'

def lba_to_chs(max_lba=2880, sectors_per_track=18, number_of_heads=2):
    r""" Calculating the Cylinder, Head and Sector numbers for a given LBA
    | Ex. Problem | Ex. Solution |
    | --- | --- |
    | If the LBA of a block is $2243$ on a device with $18$ sectors per track and $2$ heads, what are the cylinder, head and sector numbers? | Cylinder: $62$, Head: $0$, Sector: $12$ |
    """
    lba = random.randint(0, max_lba)
    cylinder = math.floor(lba/(sectors_per_track*number_of_heads));
    t = cylinder*(sectors_per_track*number_of_heads);
    t = lba-t;
    head = math.floor(t/(sectors_per_track));
    sector = t - (head * lba) + 1;

    problem = f"If the LBA of a block is ${lba}$ on a disk with ${sectors_per_track}$ sectors per track and ${number_of_heads}$ heads, what are the cylinder, head and sector numbers?"
    solution = f"Cylinder: ${cylinder}$, Head: ${head}$, Sector: ${sector}$"
    return problem, solution
