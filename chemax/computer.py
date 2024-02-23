def simple(formula: str) -> dict:
    """
    简单的分子式解析
    不包括括号递归解析
    基础功能函数
    :param formula:
    :return:
    """
    atom_stack = []
    _in_brackets = False
    _atom_ = ''
    _atom_num_ = ''
    finger = 0
    for word in formula:
        finger += 1
        # 如果在方括号内，只能有数字
        if _in_brackets and _atom_ and word != ']':
            if not word.isdigit():
                raise ValueError(
                    f"Invalid character '{word}' in formula[{finger}]: \n'{formula}'\n{finger * ' ' + '^'}")
            _atom_ += word
            continue
        # 如果是大写字母或*，表示原子的开始
        if word.isupper() or word == "*":
            # 如果之前有原子
            if _atom_:
                atom_stack.append((_atom_, _atom_num_))
                _atom_, _atom_num_ = '', ''
            _atom_ = word
        # 如果是小写字母，表示原子的延续
        elif word.islower():
            _atom_ += word
        # 如果是数字，表示原子的数量
        elif word.isdigit():
            _atom_num_ += word
        elif word == '[':
            if not _atom_ or _atom_num_:
                raise ValueError(
                    f"Invalid character '{word}' in formula[{finger}]: \n'{formula}'\n{finger * ' ' + '^'}")
            _in_brackets = True
            _atom_ += word
        elif word == ']':
            _in_brackets = False
            _atom_ += word
        else:
            raise ValueError(f"Invalid character '{word}' in formula[{finger}]: \n'{formula}'\n{finger * ' ' + '^'}")

    if _atom_:
        atom_stack.append((_atom_, _atom_num_))

    molecule_dict = {}
    # 合并元素
    for _atom in atom_stack:
        _atom_name, _atom_num = _atom
        molecule_dict[_atom_name] = molecule_dict.get(_atom_name, 0) + (int(_atom_num) if _atom_num else 1)

    return molecule_dict


def simple_parser(formula: str) -> list:
    """
    通过递归和堆栈方式解析含括号的分子式
    返回多层嵌套列表
    :param formula:
    :return:
    """
    global_formula = formula

    def parse(_formula, finger=0):
        """
        递归解析
        :param _formula: The part of the chemical formula processed by the current function
        :param finger: The absolute starting position of the current pointer is convenient for reporting errors.
        :return:
        """
        atom_stack = []
        _in_brackets = False
        _in_square_brackets = False
        _atom_ = ''
        _atom_num_ = ''
        stack = 0
        stack_in_position = 0
        for word in _formula:
            if stack > 0:
                stack_in_position += 1
            else:
                finger += 1
            # 如果不在圆括号内，即圆括号堆栈为0，正常解析
            if stack == 0:
                # 如果在方括号内，只能有数字
                if _in_brackets and _atom_ and word != ']':
                    if not word.isdigit():
                        raise ValueError(
                            f"Invalid character '{word}' in formula[{finger}]: \n'{formula}'\n{finger * ' ' + '^'}")
                    _atom_ += word
                    continue
                # 如果是大写字母或*，表示原子的开始
                if word.isupper() or word == "*":
                    # 如果之前有原子
                    if _atom_:
                        atom_stack.append((_atom_, _atom_num_))
                        _atom_, _atom_num_ = '', ''
                    _atom_ = word
                # 如果是小写字母，表示原子的延续
                elif word.islower():
                    _atom_ += word
                # 如果是数字，表示原子的数量
                elif word.isdigit():
                    _atom_num_ += word
                # 方括号开始，其中内容为中子数，即注释同位素
                elif word == '[':
                    if not _atom_ or _atom_num_:
                        raise ValueError(
                            f"Invalid character '{word}' in formula[{finger}]: \n'{formula}'\n{finger * ' ' + '^'}")
                    _in_brackets = True
                    _atom_ += word
                # 方括号结束
                elif word == ']':
                    _in_brackets = False
                    _atom_ += word
                # 圆括号开始，堆栈开始
                elif word == '(':
                    # 先保存之前的原子
                    if _atom_:
                        atom_stack.append((_atom_, _atom_num_))
                        _atom_, _atom_num_ = '', ''
                    stack += 1
                    stack_in_position = 0
                # 堆栈等于0时，右圆括号为非法字符，无需特殊处理
                else:
                    raise ValueError(f"Unexpected character '{word}' in formula[{finger}]: \n'{global_formula}'\n{finger * ' ' + '^'}")

            else:
                # 堆栈内，只解析圆括号的堆栈
                if word == '(':
                    _atom_ += word
                    stack += 1
                elif word == ')':
                    stack -= 1
                    if stack == 0:
                        # 递归解析
                        _atom_ = parse(_atom_, finger)
                        finger += stack_in_position
                    else:
                        _atom_ += word
                else:
                    _atom_ += word

        # 循环结束，如果还有原子，保存
        if _atom_:
            atom_stack.append((_atom_, _atom_num_))
        # 循环结束，如果堆栈不为0，说明括号不匹配
        if stack != 0:
            raise ValueError(f"Unmatched parentheses in formula[{finger}]: \n'{global_formula}'\n{finger * ' ' + '^'}")
        return atom_stack
    return parse(formula)


def regular(w_formula: str) -> (int, dict):
    """
    解析电荷数
    电荷数表示法 {OH}- {O}2-
    将递归解析的多层嵌套列表转换为字典
    依然需要递归
    :param w_formula:
    :return:
    """
    e_stack = 0
    ele = ''
    formula = w_formula
    if w_formula[0] == '{' and w_formula[-1] in ['+', '-']:
        formula = ''
        e_finger = 0
        for word in w_formula[:-1]:
            e_finger += 1
            if e_stack > 1 or e_stack < 0:
                raise ValueError(f"Unmatched parentheses in formula: \n'{w_formula}'\n ^")
            if word == '{':
                e_stack += 1
            elif word == '}':
                e_stack -= 1
            elif e_stack == 0:
                # 说明已在花括号外层
                if word in '0123456789':
                    ele += word
                else:
                    raise ValueError(f"Unexpected character '{word}' in formula[{e_finger}]: \n'{w_formula}'\n{e_finger * ' ' + '^'}")
            else:
                # 说明在花括号内层
                formula += word
    if ele:
        ele = int(ele) if w_formula[-1] == '+' else -int(ele)
    elif w_formula[-1] in ['+', '-']:
        ele = 1 if w_formula[-1] == '+' else -1
    else:
        ele = 0

    result = simple_parser(formula)
    # 初始化字典
    molecule_dict = {}

    # 定义递归函数
    def parse(_result, _multiplier=1):
        """
        递归解析
        :param _result: 要解析的列表
        :param _multiplier: 列表（对应原子团）的右下角标，默认为1
        :return:
        """
        for _atom in _result:
            _atom_name, _atom_num = _atom
            _atom_num = int(_atom_num) if _atom_num else 1
            if isinstance(_atom_name, list):
                # 如果是列表，说明还有括号
                parse(_atom_name, _atom_num*_multiplier)
            else:
                # 是普通原子
                molecule_dict[_atom_name] = molecule_dict.get(_atom_name, 0) + int(_atom_num) * _multiplier
    parse(result)
    return ele, molecule_dict


if __name__ == '__main__':
    print(simple_parser('CH3(CH2)2CH3'))
    print(regular('CH3(CH2(CH2)2)2CH3'))
