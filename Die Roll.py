n = int(input())

# remainder modulo 7
remainder = n % 7

# Minimum rolls needed to reach multiple of 7
if remainder == 0:
    print(0)
else:
    print(7 - remainder)
