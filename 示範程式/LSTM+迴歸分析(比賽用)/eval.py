f = open('output.csv')
f.readline()
g = open('ExampleTestData/upload.csv')
g.readline()
score = 0
for i in range(9600):
    line = f.readline()
    gline = g.readline()
    predict = float(line)
    answer = float(gline.split(',')[1])
    print(abs(predict - answer))
    score += abs(predict - answer)
print("Total score: " + str(score))
print("Average score: " + str(score / 9600))