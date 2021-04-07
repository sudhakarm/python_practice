if __name__ == '__main__':
    students = [['Barry', 37.21],['Aarry', 37.21], ['Herry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    students = sorted(students, key=lambda x: x[1], reverse=False)
    k = []
    second_best = 0
    for i in range(1,len(students)):
        if(students[i][1] > students[0][1]):
            if(students[i][1] != second_best and second_best != 0):
                break
            else:
                second_best = students[i][1]
                k.append(students[i][0])
    print(*sorted(k),sep = "\n") #'*' prints the chars or list items sperated by space

# or
# s = sorted(set([x[1] for x in students]))
# for name in sorted(x[0] for x in students if x[1] == s[1]):
    # print(name)
