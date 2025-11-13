# Prodigy Demo

## Set up instructions

### Codespaces

Get Prodigy license # and save it in a secret `PRODIGY_LICENSE`

After that, open the code space.

To check installation, type in the terminal window:

```
prodigy stats
```
You should get something like this:

```
============================== ✨  Prodigy Stats ==============================

Version          1.18.3                        
License Type     Prodigy Personal              
Location         /home/vscode/.local/lib/python3.12/site-packages/prodigy
Prodigy Home     /home/vscode/.prodigy         
Platform         Linux-6.8.0-1030-azure-x86_64-with-glibc2.31
Python Version   3.12.11                       
spaCy Version    3.8.8                         
Database Name    SQLite                        
Database Id      sqlite                        
Total Datasets   0                             
Total Sessions   0                          
```

### Local

To install prodigy, run:

```
export PRODIGY_LICENSE="XXXXXXX" # enter your license

# Set up and activate virtual environment of your choice
# pyenv virtualenv prodigy-demo
# pyenv activate prodigy-demo

# Install Prodigy and necessary packages
pip install 'prodigy' -f https://${PRODIGY_LICENSE}@download.prodi.gy
pip install -r requirements.txt 
```

## Repository Structure

* `Prodigy Demo.ipynb` contains all code and instructions how to start prodigy sections. You will need terminal to run prodigy
* `annottaion-projects` directory contains so-called Prodigy projects. A project is a set of files and start script necessary to run a single annotation task. For each task, `cd` into a project directory and run `start.sh`. For several projects, there are alternative Prodigy session start scripts that demonstrate different approaches to the same task.
* `data` directory contains all datasets used in `Prodigy Demo.ipynb`

```
├── annotation-projects 
│   ├── resume-ner
│   │   ├── annotation-guidelines.html
│   │   ├── prodigy.json
│   │   └── start.sh
│   ├── resume-partitioning
│   │   ├── annotation-guidelines.html
│   │   ├── prodigy.json
│   │   ├── start-spans.sh
│   │   └── start.sh
│   ├── summarization-binary
│   │   ├── my-choice-binary.py
│   │   ├── prodigy.json
│   │   └── start.sh
│   └── summarization-choices
│       ├── my-choice.py
│       ├── prodigy.json
│       ├── start-review.sh
│       └── start.sh
├── data
│   ├── hf-summarization-dataset.csv
│   ├── news-headlines.jsonl
│   ├── resume-dataset.csv
│   ├── resume-ner-dataset-annotated.jsonl
│   ├── resume-ner-dataset.jsonl
│   ├── resume-partitioning-dataset-annotated.jsonl
│   ├── resume-partitioning-dataset.jsonl
│   ├── summarization-dataset-binary.jsonl
│   └── summarization-dataset-choices.jsonl
├── Prodigy Demo.ipynb
├── README.md
├── requirements.txt
```
## Prodigy Resources

* Website: https://prodi.gy/
* Documentation: https://prodi.gy/docs (really good and detailed)
* Live demo: https://demo.prodi.gy/

