# List of allowed annotators
export PRODIGY_ALLOWED_SESSIONS=natalia,llm,test

# Port to start prodigy on. Default: 8080
export PRODIGY_PORT=8082

# prodigy recipe-name annotated-dataset-name input-file-name -F file-with-custom-recipe
python -m prodigy my-choice text-summarization ../../data/summarization-dataset-choices.jsonl -F my-choice.py

# This will start a session at http://localhost:8082?session=natalia