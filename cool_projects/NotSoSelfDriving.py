cases = int(input())
outputs = []
for caseNum in range(cases):
    ask = input()
    new_ask = ask.split(':')
    V = float(new_ask[0])
    X = float(new_ask[1])
    if (0 < V <= 200) and (1 <= X <= 400):
        if X / V <= 1:
            outputs.append("SWERVE")
        elif X / V <= 5:
            outputs.append("BRAKE")
        else:
            outputs.append("SAFE")
    else:
        outputs.append("SAFE")
for value in outputs:
    print(value)
