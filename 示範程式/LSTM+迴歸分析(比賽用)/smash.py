f = open('output.csv', 'r')
g = open('/Users/anthony/aiclub/Solar-Energy-Prediction/36_TestSet_SubmissionTemplate/upload(no answer).csv', 'r')
h = open('upload-all.csv', 'w')

lines = ["序號,答案\n"]

f.readline()
g.readline()

for i in range(9600):
    line = g.readline()
    val = float(f.readline())
    if(val < 0):
        val = 0
    line = line[:-1] + str(val) + "\n"
    lines.append(line)

h.writelines(lines)