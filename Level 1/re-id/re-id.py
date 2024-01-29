def get_pi_string(index):
    # Start with first prime number
    poss_str = '2'
    prime_list = [2]

    # Evaluate every number until you get the length needed
    x_start = 3
    # Length of prime string increases until the string is longer than the input by at least 5
    while len(poss_str)<index+5:
        # If number being evaluated can be divided by any prime number break
        for i in prime_list:
            if (x_start % i) == 0:
                break
        # If number is prime append to string and to prime list
        else:
            poss_str += str(x_start)
            prime_list.append(x_start)
        x_start +=1

    return poss_str

def solution(index):
    #Get prime string
    poss_str = get_pi_string(index)
    # Return string id
    id_str = poss_str[index:index+5]

    return id_str

if __name__ in '__main__':
    result = solution(10)
    print(result)