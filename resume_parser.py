import pdfplumber


def extract_resume_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


resume_text = extract_resume_text("data/General CV Template.pdf")

print(resume_text)