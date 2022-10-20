row1 = ['11', '21', '31']
row2 = ['12', '22', '32']
row3 = ['13', '23', '33']

grid = [row1, row2, row3]


def game():
    xo = input("Enter X or O:")
    pos = int(input("Enter coordinates:"))
    input1 = pos % 10
    input2 = pos // 10
    grid[input1 - 1][input2 - 1] = xo


print(f"Grid coordinates:\n{row1}\n{row2}\n{row3}")
while True:
    game()
    print(f"{row1}\n{row2}\n{row3}")
    if grid[0][0] == grid[1][0] == grid[1][0] == grid[2][0]:
        print(f"{grid[0][0]} wins!")
        quit()
    elif grid[0][1] == grid[1][1] == grid[1][1] == grid[2][1]:
        print(f"{grid[0][1]} wins!")
        quit()
    elif grid[0][2] == grid[1][2] == grid[1][2] == grid[2][2]:
        print(f"{grid[0][2]} wins!")
        quit()
    elif grid[0][0] == grid[0][1] == grid[0][1] == grid[0][2]:
        print(f"{grid[0][0]} wins!")
        quit()
    elif grid[1][0] == grid[1][1] == grid[1][1] == grid[1][2]:
        print(f"{grid[1][0]} wins!")
        quit()
    elif grid[2][0] == grid[2][1] == grid[2][1] == grid[2][2]:
        print(f"{grid[2][0]} wins!")
        quit()
    elif grid[0][0] == grid[1][1] == grid[1][1] == grid[2][2]:
        print(f"{grid[0][0]} wins!")
        quit()
    elif grid[0][2] == grid[1][1] == grid[1][1] == grid[2][0]:
        print(f"{grid[0][2]} wins!")
        quit()
