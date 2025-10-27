import os

root = "./dir"  
level1 = {}
level2 ={}

for root_dir, dirs, files in os.walk(root):
    parts = root_dir.split(os.sep)
    if len(parts) >= 4:
        l1 = parts[2]
        l2 = parts[3]
        key = (l1,l2)
        if files:
            if key not in level1:
                level1[key] = []
                
            for f in files:
                path = os.path.join(root_dir, f)
                rel = os.path.relpath(path, root)
                level1[key].append((l2, rel))
print("pirveli magaliti: ")
for k in list(level1.keys())[:2]:
    print(k, "->", level1[k][:1], "...")

for outer, files in level1.items():
    inner = {}
    for l2name, rel_path in files:
        filename = os.path.basename(rel_path)
        name_without = os.path.splitext(filename)[0]
        key2 =(l2name, name_without)
        nums = set()
        try:
            with open(os.path.join(root, rel_path), "r") as f:
                for line in f:
                    s = line.strip()
                    if len(s) == 9 and s.isdigit():
                        nums.add(int(s))
        except:
            continue
        inner[key2] = nums
        if inner:
            level2[outer] = inner

print("meore magaliti: ")
for k in list(level2.keys())[:1]:
    print(k, "->", list(level2[k].items())[:1])

max_len = 0
max_keys = []

for out, inn in level2.items():
    for k, vals in inn.items():
        if len(vals) > max_len:
            max_len = len(vals)
            max_keys = [(out, k)]
        elif len(vals) == max_len and len(vals) > 0:
            max_keys.append((out, k))

print(" yvelaze meti ricxvebis mqone faili: ")
if max_len > 0:
    print("ricxvebis raodenoba: ", max_len)
    for o,i in max_keys:
        print(o, i)
else:
    print("9 nishna ricxvebi ve moidzebna")

def shiddze_iyopa(num):
    s = str(num)
    if len(s) != 9:
        return False
    total = 0
    for i in range(9):
        if i % 3 != 0:
            total += int(s[i])
        return total % 7 == 0

print("funqciis testi: ")
print("123456789: ", shiddze_iyopa(123456789))
print("177777777: ", shiddze_iyopa(177777777))


best = 0
best_keys = []
for out, inn in level2.items():
    for k, vals in inn.items():
        cnt = 0
        for n in vals:
            if shiddze_iyopa(n):
                cnt += 1
        if cnt > best:
            best = cnt
            best_keys = [(out, k)]
        elif cnt == best and cnt > 0:
            best_keys.append(out, k)

print("yvelaze meti shesabamisi ricxvebis faili: ")
if best > 0:
    print("shesabamisi ricxvebis raodenoba: ", best)
    for o , i in best_keys:
        print(o, i)
else:
    print("SHesabamisi ricxvi ver moidzebna")