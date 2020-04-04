# ABC049C - 白昼夢

S = input()

while True:
    if S[0:5] == "dream":
        if S == "dream": # この単語がdream、次の単語は存在しない
            S = ""
        elif S == "dreamer": # この単語がdreamer、次の単語は存在しない
            S = ""
        elif S[5:8] == "dre": # この単語がdream、次の単語はdreamかdreamer
            S = S[5:]
        elif S[5:8] == "era": # この単語がdream、次の単語はeraseかeraser
            S = S[5:]
        elif S[5:8] == "erd": # この単語がdreamer、次の単語はdreamかdreamer
            S = S[7:]
        elif S[5:8] == "ere": # この単語がdreamer、次の単語はeraseかeraser
            S = S[7:]
    elif S[0:5] == "erase":
        if S == "erase": # この単語がerase、次の単語は存在しない
            S = ""
        elif S == "eraser": # この単語がeraser、次の単語は存在しない
            S = ""
        elif S[5:8] == "dre": # この単語がerase、次の単語はdreamかdreamer
            S = S[5:]
        elif S[5:8] == "era": # この単語がerase、次の単語はeraseかeraser
            S = S[5:]
        elif S[5:8] == "rdr": # この単語がeraser、次の単語はdreamかdreamer
            S = S[6:]
        elif S[5:8] == "rer": # この単語がeraser、次の単語はeraseかeraser
            S = S[6:]
    elif S == "":
        print("YES")
        break
    else:
        print("NO")
        break
