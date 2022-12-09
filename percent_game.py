# D I S C L A I M E R :

# THE FILE WAS MADE (and all is in one file) USING TOOLS I COULD ACTUALLY USE AFTER 3 MONTHS OF LEARNING PYTHON,
# SO IT IS NOT EVEN CLOSE TO ANY `OPTIMAL CLEAN CODE`.

# It's ONLY A DRAFT of my `game for learning Python` where player should guess the percentage of one given number
# from another given number.
# Algorithm of scoring is based on:
# 1) how close was guess (polynomial approximation to the graph I draw myself);
# 2) were random given numbers `hard` to make a guess or no (trigonometric interpolation in MathCad
# to the graph I draw myself).
# The result of each game is writen in an updated txt file.


import random
import math
import statistics


def in_only(x, y):
    while True:
        print(x)
        try:
            y = int(input(y))
            break
        except ValueError:
            continue
    return y


def f_polyn_interpol(x):
    result = (8.3595605*10**(-6))*x**7-(4.1522711*10**(-4))*x**6+0.0080581*x**5-0.0774653*x**4+0.3778528*x**3-1.0476877*x**2-2.3740946*x+100.0220083
    return result


def f_trig_interpol(x):
    result = a0 + a1 * math.cos(x * w) + b1*math.sin(x * w) + \
             a2 * math.cos(2 * x * w) + b2 * math.sin(2 * x * w) + a3 * math.cos(3 * x * w) + \
             b3 * math.sin(3 * x * w) + a4 * math.cos(4 * x * w) + b4 * math.sin(4 * x * w) + \
             a5 * math.cos(5 * x * w) + b5 * math.sin(5 * x * w) + a6 * math.cos(6 * x * w) + \
             b6 * math.sin(6 * x * w) + a7 * math.cos(7 * x * w) + b7 * math.sin(7 * x * w) + \
             a8 * math.cos(8 * x * w) + b8 * math.sin(8 * x * w)
    return result


def f_norm_trig_interpol(x):
    result_1 = (f_trig_interpol(x) + 100) / med_special
    if result_1 >= 1:
        result_2 = 1
    else:
        result_2 = result_1
    return result_2


w = 0.05916
a0 = 27.51
a1 = -10.03
a2 = -7.871
a3 = -3.552
a4 = -4.062
a5 = 2.043
a6 = -1.657
a7 = -0.9555
a8 = -1.426
b1 = 1.86
b2 = 3.026
b3 = 2.18
b4 = 3.664
b5 = -2.668
b6 = 3.262
b7 = 3.245
b8 = 13.81

med_special = 129.96667818282




qty_of_rounds = in_only("How many rounds will you play?: ", "")


for i in range(1, qty_of_rounds + 1):
    ran_for_highest = range(1051, 9999)
    ran_for_part = range(1, 10000)
    li_for_highest = list(ran_for_highest)
    li_for_part = list(ran_for_part)
    exclude_set_highest = li_for_highest[(1250-1051)::250]
    legal_li_for_highest = [x for x in li_for_highest if x not in exclude_set_highest]
    highest = random.choice(legal_li_for_highest)
    exclude_set_part = [i for i in li_for_part if i > highest or (i * 10 == highest) or ((abs(highest - i) / highest) <= 0.005)]
    legal_li_for_part = [j for j in li_for_part if j not in exclude_set_part]
    part = random.choice(legal_li_for_part)
    print(highest)
    print(part)
    guessed_percent = in_only(f"ROUND-{i}. Guess a %: ", "")
    real_percent = int((part / highest) * 100 + 0.5)
    result_simple = abs(guessed_percent - real_percent)
    result_complex = 0
    locals()['real_percent'+str(i)] = real_percent
    locals()['guessed_percent'+str(i)] = guessed_percent
    locals()['result_simple'+str(i)] = result_simple
    if result_simple <= 15:
        result_complex = f_polyn_interpol(result_simple) * f_norm_trig_interpol(real_percent)
    else:
        result_complex_1 = -0.5
    result_complex_int = int(result_complex + 0.5)
    locals()['result_complex_int'+str(i)] = result_complex_int
    points_ceiling = int(f_polyn_interpol(0) * f_norm_trig_interpol(real_percent) + 0.5)
    locals()['points_ceiling'+str(i)] = points_ceiling
    print(f"Right answer is --{real_percent}-- %")
    print(f"You were wrong by --{result_simple}-- percentage points")
    print(f"You've scored --{result_complex_int}-- points")
    print(f"The maximum possible number of points you could score was --{points_ceiling}-- points")
    print("")

total_points = sum(list([eval("result_complex_int"+str(i)) for i in range(1, qty_of_rounds + 1)]))
average_points = float(statistics.mean(list([eval("result_complex_int"+str(i)) for i in range(1, qty_of_rounds + 1)])))
average_points_ceiling = float(statistics.mean(list([eval("points_ceiling"+str(i)) for i in range(1, qty_of_rounds + 1)])))
guessing_accuracy = int((average_points / average_points_ceiling) * 100 + 0.5)

print(f"In total, you've scored --{total_points}-- points in --{qty_of_rounds}-- rounds")
print(f"On average, you scored --{average_points}-- points per game...")
print(f"...out of --{average_points_ceiling}-- maximum possible")
print(f"GUESSING ACCURACY IS --{guessing_accuracy}-- %")
with open("game_results.txt", "a") as game_results:
    for j in range(1, qty_of_rounds + 1):
        print(f'Real\t{eval("real_percent"+str(j))}\tGuessed\t{eval("guessed_percent"+str(j))}')
        game_results.write(f'Real\t{eval("real_percent"+str(j))}\tGuessed\t{eval("guessed_percent"+str(j))}\n')
