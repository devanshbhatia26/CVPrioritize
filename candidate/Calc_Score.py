import json
from itertools import chain
from .models import Candidate, Application
from Recruiter_HM.models import JobPost
from Recruiter_HM.views import match
from taggit.models import Tag

def score_calculation(resume):
    jd = json.loads(match())

    for i in range(len(jd)):
        if jd[i]['fields']['status'] == 3:
            print(jd[i])
            print(resume)
            job_desc = jd[i]
            p_skills = [i.lower().strip() for i in job_desc["fields"]["primary_skills"].split(',')]
            if job_desc["fields"]["secondary_skills"] is None:
                job_desc["fields"]["secondary_skills"] = []
            else:
                s_skills = [i.lower().strip() for i in job_desc["fields"]["secondary_skills"].split(',')]
            
            if job_desc["fields"]["tertiary_skills"] is None:
                job_desc["fields"]["tertiary_skills"]
            else:
                t_skills = [i.lower().strip() for i in job_desc["fields"]["tertiary_skills"].split(',')]

            skills = [i.lower().strip() for i in resume.skills.split(',')]
            skill_score = 0
            count = 0
            for i in range(len(skills)):
                if skills[i] in p_skills:
                    count = count+1
                    skill_score = skill_score + 10
                if skills[i] in s_skills:
                    count = count+1
                    skill_score = skill_score + 9
                if skills[i] in t_skills:
                    count = count + 1
                    skill_score = skill_score + 8
            print(skill_score)
            skill_score = float(skill_score) / count
            print(skill_score)
            

            exprnc = ['0-2','3-5','6-8','9-12','13-15','15+']
            exp = job_desc["fields"]["overall_experience"]
            flag = True
            exp_score = 0
            for i in range(6):
                if resume.experience == exprnc[i]:
                    if exprnc[i] == exp:
                        flag = False
                        exp_score = exp_score + 10
                        continue
                    elif flag:
                        exp_score = exp_score + 5 + i
                    else:
                        exp_score = exp_score + (10 - i)
            print(exp_score)

            Qualifications = {"Ug": ["b.e", "b.tech","btech", "bba", "bca", "b.a", "b.arch", "bsc", "b.sc", "b.com", "bcom"], "Pg": ["ms", "m.s", "mba", "m.tech", "mtech", "mcs", "mca", "m.sc", "msc", "m.com", "mcom"], "Assc": ["a.s", "a.a", "a.a.s", "a.a.t"], "Others": ["others", "phd", "doctorate"]}

            qualification = [ i.lower().strip() for i in resume.qualification.split(',')]
            qual_score = 0
            qual = [i.lower().strip() for i in job_desc["fields"]["qualification"].split(',')]
            if job_desc["fields"]["additional_qualification"] is not None :
                add_qual = [i.lower().strip() for i in job_desc["fields"]["additional_qualification"].split(',')]
            else:
                add_qual = []
            qualification = clean_items(qualification)
            mand_qual = clean_items(mand_qual)
            opt_qual = clean_items(opt_qual)

            for i in range(len(qualification)):
                if qualification[i] in mand_qual :
                    qual_score = qual_score + 10
                    continue
                if qualification[i] in opt_qual:
                    qual_score = qual_score+ 9
                elif qualification[i] in Qualifications["Pg"]:
                    qual_score = qual_score + 6
                elif (qualification[i] in Qualifications["Ug"]) or (qualification[i].lower() in Qualifications["Assc"]):
                    qual_score = qual_score + 5
                else:
                    qual_score = qual_score + 3
            print(qual_score)

            qual_score = (qual_score / len(qualification))

            Total_Score = round(((10 * (skill_score) + 9 * (exp_score) + 8 * (qual_score))/(2.7)), 2)
            print(Total_Score)
    
            job=JobPost.objects.get(pk=job_desc['pk'])

            Application.objects.create(score = Total_Score, candidateid = resume, jobid = job)


def clean_items(qualification):
    lists = []
    if len(qualification) !=0:
        for i in range(len(qualification)):
            qual = qualification[i].split('.')
            lists.append(''.join(qual))
    return lists
    
    




    



