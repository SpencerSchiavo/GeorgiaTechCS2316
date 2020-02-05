# Spencer Schiavo
# 903125926
# sschiavo3

import sys
import csv
import json

class Candidate:

    def __init__(self, ident, name, gpa, cs2316grade, technical, behavioral):

        self.ident = ident
        self.name = name
        self.gpa = gpa
        self.cs2316grade = cs2316grade
        self.technical = technical
        self.behavioral = behavioral

    def __repr__(self):

        return f"{self.ident} - {self.name}"

    def __gt__(self, other):

        gradeLetter = self.cs2316grade
        gradeNum1 = 0
        if gradeLetter != '':
            if gradeLetter == 'A':
                gradeNum1 = 4
            elif gradeLetter == 'B':
                gradeNum1 = 3
            elif gradeLetter == 'C':
                gradeNum1 = 2
            elif gradeLetter == 'D':
                gradeNum1 = 1
        gradeLetter = other.cs2316grade
        gradeNum2 = 0
        if gradeLetter != '':
            if gradeLetter == 'A':
                gradeNum2 = 4
            elif gradeLetter == 'B':
                gradeNum2 = 3
            elif gradeLetter == 'C':
                gradeNum2 = 2
            elif gradeLetter == 'D':
                gradeNum2 = 1
        compositeSelf = gradeNum1 + self.gpa + self.technical + self.behavioral
        compositeOther = gradeNum2 + other.gpa + other.technical + other.behavioral
        if compositeSelf > compositeOther:
            return True
        else:
            return False







def rank_composite(candidates):

    new_candidates1 = candidates
    return bubble_sort(new_candidates1)









def rank_academics(candidates):

    new_candidates2 = candidates
    for cand in new_candidates2:
        cand.technical = 0
        cand.behavioral = 0
    return bubble_sort(new_candidates2)






def rank_technical(candidates):

    new_candidates3 = candidates
    for cand in new_candidates3:
        cand.cs2316grade = 'F'
        cand.gpa = 0
        cand.behavioral = 0


    return bubble_sort(new_candidates3)






def rank_behavioral (candidates):

    new_candidates4 = candidates
    for cand in new_candidates4:
        cand.cs2316grade = 'F'
        cand.gpa = 0
        cand.technical = 0
    return bubble_sort(new_candidates4)



def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i+1] > seq[i]:
                seq[i+1], seq[i] = seq[i], seq[i+1]
                changed = True
    return seq

if __name__ == "__main__":

    cands = []
    list_c = []
    file = json.load(open(sys.argv[2]))
    for line in open(sys.argv[1]):                                          # Fill in with sys.argv[2]
        line = line.split(',')
        cands.append(line)
    for x in range(1,len(cands)):
        temp_el = ''
        cands[x][0] = cands[x][0][1:]                                           # Remove apostrophe at beginning
        cands[x][1] = cands[x][1][1:len(cands[x][1]) - 1]
        temp_cand = cands[x]
        end = len(temp_cand)-1
        last_el = temp_cand[end]
        if last_el == '\n':
            cands[x] = cands[x][0:end]
        elif last_el[len(last_el)-1] == '\n':
            cands[x][end] = cands[x][end][0]

    for x in range(1,len(cands)):
        ident = cands[x][2]
        name = cands[x][0] + ', ' + cands[x][1]
        gpa = float(cands[x][5])
        cs2316grade = cands[x][len(cands[x])-1] if len(cands[x])>=7 else ''
        technical = file[cands[x][2]][0]
        behavioral = file[cands[x][2]][1]
        c = Candidate(ident, name, gpa, cs2316grade, technical, behavioral)
        list_c.append(c)

    if len(sys.argv)<4:
        new_list = rank_composite(list_c)
    else:
        if sys.argv[3]=='composite':
            new_list = rank_composite(list_c)
        if sys.argv[3]=='academics':
            new_list = rank_academics(list_c)
        elif sys.argv[3]=='technical':
            new_list = rank_technical(list_c)
        elif sys.argv[3]=='behavioral':
            new_list = rank_behavioral(list_c)
    print('id' + ' ' + 'name'  + ' ' + 'gpa' + '  ' + 'cs2316grade' + '   ' + 'technical' + '   ' + 'behavioral')
    for cand in new_list:
        print(cand.ident + '  ' + cand.name + '  ' + str(cand.gpa) + '  ' + cand.cs2316grade + '  ' + str(cand.technical) + '  ' + str(cand.behavioral))

























