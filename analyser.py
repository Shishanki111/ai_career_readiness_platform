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