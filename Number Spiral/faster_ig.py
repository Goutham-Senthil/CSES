import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    t = int(next(it))
    out = []

    for _ in range(t):
        y = int(next(it)); x = int(next(it))
        if y >= x:
            if y % 2 == 0:
                out.append(str(y * y - x + 1))
            else:
                out.append(str((y - 1) * (y - 1) + x))
        else:
            if x % 2 == 1:
                out.append(str(x * x - y + 1))
            else:
                out.append(str((x - 1) * (x - 1) + y))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()