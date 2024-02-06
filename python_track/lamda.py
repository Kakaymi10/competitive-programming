if __name__ == '__main__':
    N = int(input())
    ans = []
    commands = {
        'insert': lambda instr: ans.insert(int(instr[1]), int(instr[2])),
        'print': lambda _: print(ans),
        'remove': lambda instr: ans.remove(int(instr[1])),
        'append': lambda instr: ans.append(int(instr[1])),
        'sort': lambda _: ans.sort(),
        'pop': lambda _: ans.pop(),
        'reverse': lambda _: ans.reverse()
    }

    for _ in range(N):
        instr = input().split()
        command = instr[0]
        commands[command](instr)
