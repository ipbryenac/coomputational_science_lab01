from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 110
#surface area of a cylinder =  (2 * pi * r^2 + 2 * pi * r * h )
# Cylinder Multiplier (2 * r * (r + h))
# dimensions:
r = 3
h = 12
multiplier = Decimal(2) * Decimal(r) * (Decimal(r) + Decimal(h)) # = 90: initial area without the pi

# 2. The 100-digit Pi for reference
pi_full = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

def filter(digits):
    # TRUNCATE: 
    pi_str = format(pi_full, 'f')
    dot_idx = pi_str.find('.')
    pi_trunc = Decimal(pi_str[:dot_idx + digits + 1])
    
    # ROUND: Use the quantize method to round properly
    rounding_rule = Decimal('1.' + '0' * digits)
    pi_round = pi_full.quantize(rounding_rule) # handles the rounding of the digit of the targeted precision.
    
    # Calculate Surface Areas 
    sa_trunc = pi_trunc * multiplier 
    sa_round = pi_round * multiplier
    diff = sa_round - sa_trunc #difference
    
    print(f"--- Precision: {digits} decimal places ---\n")
    print(f"Truncated Pi: {pi_trunc}")
    print(f"Rounded Pi:   {pi_round}")
    print(f"SA from the truncated pi: {sa_trunc} cm^2")
    print(f"SA from the rounded pi: {sa_round} cm^2")
    print(f"SA Difference: {format(diff, 'f')} cm^2\n")

# digits
filter(20) # in rounding, no difference here since the 21st digit is 2 and is less than 5, therefore the 20th digit remains the same; it's like truncated still.
filter(40)
filter(60)
filter(100)# similar here in rounding, the 101st digit is less than 5; therefore the the 100 digit remains the same. So no difference with truncating.
