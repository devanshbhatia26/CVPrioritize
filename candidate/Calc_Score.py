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
            job_desc = jd[i]
            p_skills = [' '+i.lower()+' ' for i in job_desc["fields"]["primary_skills"].split(',')]
            s_skills = [' '+i.lower()+' ' for i in job_desc["fields"]["secondary_skills"].split(',')]
            t_skills = [' '+i.lower()+' ' for i in job_desc["fields"]["tertiary_skills"].split(',')]
            skills = resume.skills
            skill_score = 0
            count = 1
            for i in range(len(skills)):
                if skills[i].lower() in p_skills:
                    count = count+1
                    skill_score = skill_score + 10
                if skills[i].lower() in s_skills:
                    count = count+1
                    skill_score = skill_score + 9
                if skills[i].lower() in t_skills:
                    count = count + 1
                    skill_score = skill_score + 8
            skill_score = float(skill_score) / count
            

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

            Qualifications = {"Ug": ["b.e", "b.tech","btech", "bba", "bca", "b.a", "b.arch", "bsc", "b.sc", "b.com", "bcom"], "Pg": ["ms", "m.s", "mba", "m.tech", "mtech", "mcs", "mca", "m.sc", "msc", "m.com", "mcom"], "Assc": [" a.s ", "a.a", "a.a.s", "a.a.t"], "Others": ["others", "phd", "doctorate"]}

            qualification = resume.qualification
            qual_score = 0
            mand_qual = [i.lower() for i in job_desc["fields"]["mand_qualification"].split(',')]
            if job_desc["fields"]["opt_qualification"] is not None :
                opt_qual = [i.lower() for i in job_desc["fields"]["opt_qualification"].split(',')]
            else:
                opt_qual = []

            for i in range(len(qualification)):
                if qualification[i].lower() in mand_qual :
                    qual_score = qual_score + 10
                    continue
                if qualification[i].lower() in opt_qual:
                    qual_score = qual_score+ 9
                elif qualification[i].lower() in Qualifications["Pg"]:
                    qual_score = qual_score + 8
                elif (qualification[i].lower() in Qualifications["Ug"]) or (qualification[i].lower() in Qualifications["Assc"]):
                    qual_score = qual_score + 7
                else:
                    qual_score = qual_score + 5
            print(qual_score)

            qual_score = (qual_score / len(qualification))

            Total_Score = (10 * (skill_score) + 9 * (exp_score) + 8 * (qual_score))/(2.7)
            print(Total_Score)
    
            job=JobPost.objects.get(pk=job_desc['pk'])

            Application.objects.create(score = Total_Score, candidateid = resume, jobid = job)




    



