import random


def draw_grid(w, h):
    grid = []

    if w <= 10 and h <= 100:

        for height in range(h):
            row = ["."] * (w - 1)
            row[random.randint(0, w - 2)] = "-"

            line = "|{}" * (w - 1) + "|"
            line = line.format(*row)

            print(line)
            grid.append(line)

        return grid
    else:

        print("Width of grid (w) must be <= 10;\n Height of grid (h) must be <=100.")


def track(number):
    """Track number from 1 to width of grid.
    Function returns track position on grid."""
    pos = (number - 1) * 2
    return pos


def grid_sort(w, h):

    grid = draw_grid(w, h)

    destination = []

    for track_num in range(1, w+1):

        pos = track_num

        for row in grid:

            if pos == 1:
                if row[track(pos)+1] == "-":
                    pos = pos + 1
                else:
                    pass

            elif pos == w:
                if row[track(pos)-1] == "-":
                    pos = pos - 1
                else:
                    pass

            else:
                if row[track(pos)+1] == "-":
                    pos = pos + 1

                elif row[track(pos)-1] == "-":
                    pos = pos - 1

        destination.append(pos)

    print(*destination, sep=" ")

    return destination


if __name__ == "__main__":
    grid_sort(5, 5)