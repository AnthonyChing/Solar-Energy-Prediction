f = open("test-dates.txt", "w")
g = open(r"36_TestSet_SubmissionTemplate/upload(no answer).csv", "r")

g.readline()

days = 200
lines = []

for day in range(days):
    line = g.readline()
    lines.append(line[4:8] + " " + line[-4:-2] + "\n")
    for _ in range(47):
        g.readline()

f.writelines(lines)