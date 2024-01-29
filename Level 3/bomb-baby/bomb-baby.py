def solution(m,f):
    #turn inputs into ints
    m = int(m)
    f = int(f)

    cycles = 0

    #While m and f are > 1
    while True:
        if m<1 or f<1:
            return 'impossible'
        if m == 1 and f == 1:
            return str(cycles)
        
        # Same process if f>m just names are backwards
        if m>f:
            # Find the how much bigger m is than f
            factor_m = int(m/f)-1
            # Decrease m by the factor of f (helps with time execution)
            if f!=m and factor_m!=0:
                m = m - factor_m*f
            # Else just decrease by f
            else:
                m -= f
                factor_m = 1
            # Increase the number of cycles by the factor of f
            cycles += factor_m
        else:

            factor_f = int(f/m)-1
            if m != f and factor_f!=0:
                f = f - factor_f*m
            else:
                f -= m
                factor_f =1
            cycles += factor_f

if __name__ in '__main__':
    cycles = solution('2','4')
    print(cycles)