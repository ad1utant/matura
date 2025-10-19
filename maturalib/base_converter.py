def convert_number(number: str, from_base: int, to_base: int) -> str:
    # Checking bases range
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        raise ValueError("Bases should be between 2 and 36.")

    # Converting input number to decimal
    decimal = int(number, from_base)

    # Converting decimal number to target base
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal == 0:
        return "0"

    result = ""
    while decimal > 0:
        result = digits[decimal % to_base] + result
        decimal //= to_base

    return result