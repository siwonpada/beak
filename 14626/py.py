isbn = list(input())
isbn_int = []
star_ind = 0
for ind, i in enumerate(isbn):
    if i == '*':
        star_ind = ind
        isbn_int.append(0)
    else:
        isbn_int.append(int(i))
for i in range(10):
    isbn_int[star_ind] = i
    mod_sum = 0
    for ind, j in enumerate(isbn_int):
        if ind % 2 == 0:
            mod_sum += j
        else:
            mod_sum += j * 3
    if mod_sum % 10 == 0:
        print(i)
        break
