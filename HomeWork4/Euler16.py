# 2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2**1000?


class MyNumber:
    def __init__(self, power):
        self.value = 2 ** power

    digits_sum = 0

    def count_digits_sum(self):
        for i in str(self.value):
            self.digits_sum += int(i)
        return self.digits_sum


num = MyNumber(1000)
print(num.count_digits_sum())
