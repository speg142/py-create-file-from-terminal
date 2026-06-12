import os
import sys
import datetime

args = sys.argv[1:]
if "-d" in args and "-f" not in args:
    parent_dir = os.getcwd()
    idx = args.index("-d")
    directories = []
    for arg in args[idx + 1:]:
        directories.append(arg)
    path = os.path.join(parent_dir, *directories)
    os.makedirs(path)

elif "-f" in args and "-d" not in args:
    parent_dir = os.getcwd()
    idx = args.index("-f")
    directories = args[idx + 1]
    count = 0
    if os.path.exists(os.path.join(parent_dir, directories)):
        with open(os.path.join(parent_dir, directories), "a") as f:
            f.write("\n")
    with open(os.path.join(parent_dir, directories), "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        ask = input("Enter content line: ")
        while ask != "stop":
            count += 1
            f.write(f"{count} {ask}\n")
            ask = input("Enter content line: ")

elif "-d" in args and "-f" in args:
    parent_dir = os.getcwd()
    idx_d = args.index("-d")
    idx_f = args.index("-f")
    start = min(idx_d, idx_f)
    end = max(idx_d, idx_f)
    if idx_d < idx_f:
        directories = args[idx_d + 1 : idx_f]
    else:
        directories = args[idx_d + 1 :]
    filename = args[idx_f + 1] if idx_f + 1 < len(args) else args[idx_f - 1]
    for i in range(len(directories)):
        sub_path = os.path.join(parent_dir, *directories[:i + 1])
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)
    count = 0
    path = os.path.join(parent_dir, *directories, filename)
    if os.path.exists(path):
        with open(path, "a") as f:
            f.write("\n")
    with open(path, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        ask = input("Enter content line: ")
        while ask != "stop":
            count += 1
            f.write(f"{count} {ask}\n")
            ask = input("Enter content line: ")
