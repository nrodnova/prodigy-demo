export PRODIGY_PORT=8082
export PRODIGY_ALLOWED_SESSIONS=natalia,llm,test

export PRODIGY_CONFIG_OVERRIDES='{"feed_overlap": false}'

prodigy review summarization-dataset-reviewed summarization-dataset-annotated --view-id choice --auto-accept

# This will start a session at http://localhost:8082?session=natalia

