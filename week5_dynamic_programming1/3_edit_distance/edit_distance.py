# Uses python3

def edit_distance(s, t):
    D = []
    for i in range(len(s) + 1):
        D.append([i])
    for j in range(1, len(t) + 1):
        D[0].append(j)
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            if s[i - 1] == t[j - 1]:
                D[i].append(min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1]))
            else:
                D[i].append(min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + 1))
    return D[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
