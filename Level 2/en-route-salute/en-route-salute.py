import re
def solution(hallway):
    # Find every index location of those walking right and left
    walk_right = [m.start() for m in re.finditer('>', hallway)]
    walk_left = [n.start() for n in re.finditer('<', hallway)]

    # For every bunny walking right count how many are after that are walking left and increase count by 2
    salutes = 0
    for right in walk_right:
        for left in walk_left:
            if right<left:
                salutes +=2

    return salutes

if __name__ in '__main__':
    salutes = solution("<<>><")
    print(salutes)