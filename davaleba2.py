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