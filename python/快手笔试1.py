# def sing_cal(equation):
#     ef = 0
#     cons = 0
#     if 'X' not in equation:
#         cons += int(equation)
#     else:
#         x_eq = equation.split('*')
#         if len(x_eq) == 1:
#             if x_eq[0][0] == '-': ef -= 1
#             else: ef += 1
#         else: ef += int(x_eq[0])
#     return ef, cons
#
# def cal(equation):
#     equation = equation.replace('-', '+-')
#     equations = equation.split('+')
#     equations = [ch for ch in equations if ch != '']
#     t_ef, t_cons = 0, 0
#     for eq in equations:
#         ef, cons = sing_cal(eq)
#         t_ef += ef
#         t_cons += cons
#     return t_ef, t_cons
#
#
# equation = input()
# equation.replace(' ', '')
# equation = equation.split('=')
# l_eq = equation[0].strip()
# r_eq = equation[1].strip()
#
# l_ef, l_cons = cal(l_eq)
# r_ef, r_cons = cal(r_eq)
#
# ef = l_ef - r_ef
# cons = r_cons-l_cons
# if ef == 0 or ef * cons <= 0 or cons % ef != 0: print(-1)
# else: print(cons//ef)

s = input()
char_idx = {}
max_len = 0
start = 0
for idx, ch in enumerate(s):
    if ch in char_idx and char_idx[ch] >= start:
        start = char_idx[ch] + 1
    char_idx[ch] = idx
    max_len = max(max_len, idx - start + 1)
print(max_len)


