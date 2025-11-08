# List of allowed annotators
export PRODIGY_ALLOWED_SESSIONS=natalia,llm,test

# Port to start prodigy on. Default: 8080
export PRODIGY_PORT=8082

#       recipe-name annotated-dataset-name  spacy model  input-file-name                              NER labels                         
prodigy ner.manual resume-ner               blank:en    ../../data/resume-ner-dataset.jsonl --label FIRST_NAME,MIDDLE_NAME,LAST_NAME,LINKEDIN,EMAIL,PHONE,CITY,STATE,1ST_WORK_YEAR,1ST_STUDY_YEAR

# This will start a session at http://localhost:8082?session=natalia