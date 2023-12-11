from random import shuffle


def read_sudoku(path: str) -> list[list[str]]:
    """ Прочитать Судоку из указанного файла """
    file = open(path)
    return [list(file.readline().rstrip()) for i in range(0, 9)]


def display(grid: list[list[str]]) -> None:
    """Вывод Судоку"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(grid[i][j], end=" ")
        print()


def group(values: list[int | str], n: int) -> list[list[int | str]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    groups = []
    for i in range(0, n):
        groups.append([])
        for j in range(0, n):
            groups[-1].append(values[i * n + j])
    return groups


def get_row(grid: list[list[str]], pos: tuple[int, int]) -> list[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]
    pass


def get_col(grid: list[list[str]], pos: tuple[int, int]) -> list[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    col = []
    for i in range(0, len(grid)):
        col.append(grid[i][pos[1]])
    return col


def get_block(grid: list[list[str]], pos: tuple[int, int]) -> list[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    ind = (pos[0] // 3) * 3 + (pos[1] // 3)
    block = []
    for i in range(ind // 3 * 3, (ind // 3 + 1) * 3):
        for j in range(ind % 3 * 3, (ind % 3 + 1) * 3):
            block.append(grid[i][j])
    return block


def find_empty_positions(grid: list[list[str]]) -> tuple[int, int]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '.':
                return i, j
    return -1, -1


def find_possible_values(grid: list[list[str]], pos: tuple[int, int]) -> set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    values = []
    for j in range(1, 10):
        i = str(j)
        if (i not in get_row(grid, pos) and i not in get_col(grid, pos)
                and i not in get_block(grid, pos)):
            values.append(str(i))
    return set(values)


def solve(grid: list[list[str]]) -> list[list[str]]:
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    def in_solve(grid: list[list[str]]) -> bool:
        for i in range(0, 9):
            for j in range(0, 9):
                if grid[i][j] == '.':
                    for num in range(1, 10):
                        number = str(num)
                        if not (number in get_row(grid, (i, j)) or number in
                                get_col(grid, (i, j)) or number
                                in get_block(grid, (i, j))):
                            grid[i][j] = str(number)
                            if in_solve(grid):
                                return True
                            else:
                                grid[i][j] = '.'
                    return False
        return True

    in_solve(grid)
    return grid


def check_solution(solution: list[list[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False
    >>> grid = read_sudoku('puzzle1.txt')
    >>> check_solution(solve(grid))
    True
    >>> bad_solution = [['1', '2', '3', '4', '5', '6', '7', '8', '9'] for val in range(0, 9)]
    >>> check_solution(bad_solution)
    False
    """
    for i in range(0, len(solution)):
        for j in range(0, len(solution[i])):
            if solution[i][j] == '.':
                return False
            else:
                copy_grid = []
                for ind_i in solution:
                    copy_line = []
                    for ind_j in ind_i:
                        copy_line.append(ind_j)
                    copy_grid.append(copy_line)
                copy_grid[i][j] = '.'
                if (solution[i][j] in get_row(copy_grid, (i, j)) or solution[i][j] in
                        get_col(copy_grid, (i, j)) or solution[i][j]
                        in get_block(copy_grid, (i, j))):
                    return False
    return True


def generate_sudoku(n: int) -> list[list[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = solve([list('.' * 9) for val in range(9)])
    pos = []
    for i in range(0, 9):
        for j in range(0, 9):
            pos.append((i, j))
    shuffle(pos)
    if n > 81:
        n = 81
    for i in range(0, 81 - n):
        grid[pos[i][0]][pos[i][1]] = '.'
    return grid


if __name__ == "__main__":
    for path in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt', 'bad_puzzle.txt']:
        if not check_solution(solve(read_sudoku(path))):
            print(f'Puzzle {path} can\'t be solved')
        else:
            print(f'Puzzle {path}:')
            display(solve(read_sudoku(path)))
