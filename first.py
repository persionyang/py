#分支语句中代码块的缩进
score = 54
pass_score = 60
if score > pass_score:
    gpoint = 1 + (score - pass_score) / 10
    print("学分绩点为", gpoint)
    print("通过考试")
else:
    print("学分绩点为0")
    print("未通过考试")