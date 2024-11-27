#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Ohsawa Takuma 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import sys

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n and n > 1:
            factors.append(n)
            break
    return factors

if len(sys.argv) > 2:
    print("エラー: 引数は一つだけ指定してください。")
else:
    try:
        if len(sys.argv) == 2:

            num = int(sys.argv[1])
        else:

            num = int(input("自然数を入力してください: "))

        if num < 2:
            print("2以上の自然数を入力してください。")
        else:

            factors = prime_factors(num)
            print(f"{num} の素因数分解: {' × '.join(map(str, factors))}")
    except ValueError:
        print("無効な入力です。数値を入力してください。")

