import spacy
from app.services.skills_db import SKILLS

nlp = spacy.load("en_core_web_sm")


def extract_skills(text: str) -> list[str]:
    text_lower = text.lower()
    found_skills = set()

    for skill in SKILLS:
        if skill in text_lower:
            found_skills.add(skill)

    return sorted(found_skills)


def extract_experience_sentences(text: str) -> list[str]:
    doc = nlp(text)
    experience_sentences = []

    keywords = ["experience", "worked", "years", "developer", "engineer"]

    for sent in doc.sents:
        if any(keyword in sent.text.lower() for keyword in keywords):
            experience_sentences.append(sent.text.strip())

    return experience_sentences
