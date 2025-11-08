# Prodigy Demo

## Set up (In Codespaces)

Get Prodigy license # and save it in a secret `PRODIGY_LICENSE`

To check installation, type in terminal window:

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

## Set up (local)

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