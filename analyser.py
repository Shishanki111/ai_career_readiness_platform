from resume_parser import extract_resume_text

skills = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "fastapi",
    "django",
    "flask",
    "rest api",
    "llm",
    "nlp",
    "generative ai",
    "git",
    "github",
    "docker",
    "mongodb",
    "mysql",
    "power bi",
    "tableau",
    "excel",
]


def read_job_description(file_path):
    with open(file_path, "r") as file:
        return file.read()


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills


jd_text = read_job_description("job_description.txt")

jd_skills = extract_skills(jd_text)

print("Skills found in Job Description:")
print(jd_skills)



resume_text = extract_resume_text("data/General CV Template.pdf")

resume_skills = extract_skills(resume_text)

print("Skills found in Resume:")
print(resume_skills)

matching_skills = []

missing_skills = []

for skill in jd_skills:
    if skill in resume_skills:
        matching_skills.append(skill)
    else:
        missing_skills.append(skill)

print("\nMatching Skills:")
print(matching_skills)

print("\nMissing Skills:")
print(missing_skills)


# Calculate Resume Match Score
match_score = (len(matching_skills) / len(jd_skills)) * 100

print("\nResume Match Score:")
print(round(match_score, 2), "%")