def solution(pellets):
    # Turn string into int
    pellets = int(pellets)
    i = 0
    # While there are pellets
    while pellets > 1:
        # Find the bit representation and move accordingly
        if (pellets&1) == 0:
            pellets >>= 1
        # If pellets are bitwise divisible by 3 then subtract a pellet
        elif (pellets&3) == 1 or pellets == 3:
            pellets -= 1
        else:
            pellets += 1
        # Increament the number of iterations needed
        i += 1
    return i

if __name__ in '__main__':
    print(solution('13'))