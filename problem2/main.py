def draw_xyz(N):
    pattern = ""
    letters = ['Y', 'Z', 'X']
    for i in range(N):
        line = ""
        for j in range(N):
            line += letters[(i + j) % 3] + " "
        pattern += line.strip() + "\n"
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """