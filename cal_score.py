import json
jd = {"qualification": ["MBA", 'MS', ' B.Tech'], "P_skill": ['python'], "S_skill": ['java'], "T_skill": ['SQL'], "experience": ['2-5']}

file2 = open("C:\Users\Sampath\PycharmProjects\HireEasy\cvscan-master\cand_details.txt","r")
res = file2.read()
resume = json.loads(res)

p_skills = jd["P_skill"]
s_skills = jd["S_skill"]
t_skills = jd["T_skill"]
skills = resume["skills"]
skill_score = 0
for i in range(len(skills)):
    if skills[i] in p_skills:
        skill_score = skill_score + 10
    if skills[i] in s_skills:
        skill_score = skill_score + 9
    if skills[i] in t_skills:
        skill_score = skill_score + 8

exp = jd["experience"]
flag = True
exp_score = 0
for i in range(8):
    if resume["experience"] in exp:
        flag = False
        exp_score = exp_score + 10
        continue
    elif flag:
        exp_score = exp_score + 3 + i
    else:
        exp_score = exp_score + (10-i)

Qualifications = {"Ug":["B.E", "B.Tech", "BBA", "BCA", "B.A", "B.Arch", "BSc", "B.Sc", "B.Com", "BCom", "Diploma"], "Pg":["MS", "MBA", "M.Tech", "MCS", "MCA", "M.Sc", "Msc", "M.Com", "MCom"], "Assc":["A.S", "A.A", "A.A.S", "A.A.T"], "Others":["others","PHD", "Doctorate"]}
qualification = resume["qualifications"]

qual_score = 0

for i in range(len(qualification)):
    if qualification[i] in jd["mand_qualification"]:
        qual_score = qual_score + 10
    elif qualification[i] in jd["opt_qualification"]:
        qual_score = qual_score + 9
    elif qualification[i] in Qualifications["Pg"]:
        qual_score = qual_score + 8
    elif (qualification[i] in Qualifications["Ug"])or (qualification[i] in Qualifications["Assc"]):
        qual_score = qual_score + 7
    else:
        qual_score = qual_score + 5

Total_Score = 10*(skill_score) + 9*(exp_score) + 8*(qual_score)



