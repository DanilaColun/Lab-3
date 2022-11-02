# var 2, asthma, survival sur_points = 10

stuffs = {
    'в': (3, 25),
    'п': (2, 15),
    'б': (2, 15),
    'а': (2, 20),
    'и': (1, 5),
    'н': (1, 15),
    'т': (3, 20),
    'о': (1, 25),
    'ф': (1, 15),
    'д': (1, 10),
    'к': (2, 20),
    'р': (2, 20)
}

# survival points for my variant without the items
sur_points = -sum(v for _, v in stuffs.values()) + 10


def get_space(sd, max_w):
    items = list(sd.items())
    # empty array
    V = [[([], sur_points) for _ in range(max_w + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for j in range(1, max_w + 1):

            item = items[i - 1]
            n, w, v = item[0], item[1][0], item[1][1]

            if w > j:
                V[i][j] = V[i - 1][j]
            else:
                V[i][j] = max(V[i - 1][j], (V[i - 1][j - w][0] + [n], V[i - 1][j - w][1] + v * 2), key=lambda x: x[1])
    return V


mem_table = get_space(stuffs, 9)  # fulfilling the table
ok = list(mem_table[-1][-1])  # the optimal solution of last table
if 'и' not in ok[0]:  # looking if the inhalator not in the backpack
    replace_item = min(list(filter(lambda i: stuffs[i][0] == 1, ok[0])), key=lambda i: stuffs[i][1])
    ok[1] = ok[1] - stuffs[replace_item][1] * 2 + stuffs['и'][1] * 2
    ok[0].remove(replace_item)
    ok[0].append('и')

# sorting out the backpack
ok[0].sort(key=lambda i: stuffs[i][0], reverse=True)

# forming the index for the backpack, so that the first items will be the biggest
index, range1, range2 = [], list(range(len(ok[0]) // 2 + 1)), list(range(-1, -len(ok[0]) // 2, -1))
for i in range(max(len(range1), len(range2))):
    try:
        index.append(range1[i])
    except IndexError:
        pass
    try:
        index.append(range2[i])
    except IndexError:
        pass

backpack = []
for i in index:
    item = ok[0][i]
    if stuffs[item][0] == 3:
        backpack.extend([item] * 3)
    elif stuffs[item][0] == 2:
        backpack.extend([item] * 2)
    elif stuffs[item][0] == 1:
        backpack.extend([item])

print("Optimal backpack composition:" + "\n")
print(''.join([f'[{backpack[i]}],' if i % 3 != 2 else f'[{backpack[i]}]\n' for i in range(len(backpack))]))
print('Surviving points:', ok[1])

if ok[1] > 0:
    print("He is going to survive.")
else:
    print("He isn't going to survive.")
