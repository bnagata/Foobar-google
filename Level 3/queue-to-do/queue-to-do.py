def xor(start, end):
    #Fast approach based on xor reduction
    #if start is even
    if(start%2==0):
        redux_list = [end, 1, end+1, 0]
    #if start is odd
    else:
        redux_list= [start, start^end, start-1, (start-1)^end]
    return redux_list[(end-start)%4]

def solution(start, length):
    result=0
    for i in range(0, length):
        # Find the xor of each line in box
        result ^= xor(start, start+(length-i)-1)
        start += length
    return result

if __name__ in '__main__':
    result = solution(17,4)
    print(result)