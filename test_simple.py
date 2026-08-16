"""
简单的Python测试代码
"""

def add(a, b):
    """两个数相加"""
    return a + b


def subtract(a, b):
    """两个数相减"""
    return a - b


def multiply(a, b):
    """两个数相乘"""
    return a * b


def divide(a, b):
    """两个数相除"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


# 测试函数
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("✓ add测试通过")


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0
    print("✓ subtract测试通过")


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    print("✓ multiply测试通过")


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(1, 2) == 0.5
    print("✓ divide测试通过")


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "应该抛出异常"
    except ValueError as e:
        assert str(e) == "除数不能为0"
        print("✓ divide异常测试通过")


if __name__ == "__main__":
    print("开始运行测试...\n")
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("\n✅ 所有测试通过！")
