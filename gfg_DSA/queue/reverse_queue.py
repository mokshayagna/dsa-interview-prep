q = [5, 10, 15, 20, 25]
def rev(q):
    if len(q) == 0:
        return
    x = q.pop(0)
    rev(q)
    q.append(x)
def main():
    print(f"Original queue: {q}")
    rev(q)
    print(f"Reversed queue: {q}")
if __name__ == "__main__":
    main()