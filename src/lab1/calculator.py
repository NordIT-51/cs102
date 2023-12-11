possible_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
possible_sign = ['+', '-', '*', '/']
SPECIAL_MARK = 'SPEC_MARK'


class MathClass:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index


def solve(math_str):
    math_str = math_str.strip()
    if math_str[0] not in possible_num or math_str[-1] not in possible_num:
        print('Incorrect expression!')
        return
    num = []
    steps = []
    priority_steps = []
    current_step = ''
    ind = 0
    for c in math_str:
        if c in possible_num or c == '.':
            current_step += c
        elif c in possible_sign:
            if len(current_step) == 0:
                print('Incorrect expression!')
                return
            if current_step[0] == '.' or current_step[-1] == '.':
                print('Incorrect expression!')
                return
            if current_step.count('.') > 1:
                print('Incorrect expression!')
                return
            num.append(MathClass(float(current_step), ind))
            current_step = ''
            if c == '+' or c == '-':
                steps.append(MathClass(c, ind))
            else:
                priority_steps.append(MathClass(c, ind))
            ind += 1
        else:
            print('Incorrect expression!')
            return
    if current_step:
        if current_step[0] == '.' or current_step[-1] == '.':
            print('Incorrect expression!')
            return
        if current_step.count('.') > 1:
            print('Incorrect expression!')
            return
        num.append(MathClass(float(current_step), ind))

    for step in priority_steps:
        elem1 = num[step.index]
        elem2 = None
        i = step.index + 1
        while i < len(num):
            if num[i].obj == SPECIAL_MARK:
                i += 1
            else:
                elem2 = num[i]
                break
        if step.obj == '*':
            num[elem2.index].obj = elem1.obj * elem2.obj
            num[elem1.index].obj = SPECIAL_MARK
        if step.obj == '/':
            try:
                num[elem2.index].obj = elem1.obj / elem2.obj
            except ZeroDivisionError as _ex:
                print('Incorrect expression!')
                return
            num[elem1.index].obj = SPECIAL_MARK
    for step in steps:
        elem1 = num[step.index]
        elem2 = None
        i = step.index + 1
        while i < len(num):
            if num[i].obj == SPECIAL_MARK:
                i += 1
            else:
                elem2 = num[i]
                break
        if step.obj == '+':
            num[elem2.index].obj = elem1.obj + elem2.obj
            num[elem1.index].obj = SPECIAL_MARK
        if step.obj == '-':
            num[elem2.index].obj = elem1.obj - elem2.obj
            num[elem1.index].obj = SPECIAL_MARK
    return num[-1].obj


if __name__ == '__main__':
    while True:
        problem = str(input())
        s = solve(problem)
        if s is None:
            pass
        elif s == int(s):
            print(int(s))
        else:
            print(s)