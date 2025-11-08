# List of allowed annotators
export PRODIGY_ALLOWED_SESSIONS=natalia,llm,test

# Port to start prodigy on. Default: 8080
export PRODIGY_PORT=8082

#       recipe-name annotated-dataset-name  spacy model  input-file-name                              NER labels                         
prodigy ner.manual resume-partitioning      blank:en    ../../data/resume-partitioning-dataset.jsonl --label PERSONAL_INFO,SUMMARY,EXPERIENCE,EDUCATION,SKILLS,CERTIFICATIONS,PROJECTS,AWARDS,PUBLICATIONS,LANGUAGES,OTHER

# This will start a session at http://localhost:8082?session=natalia