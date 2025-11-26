


## Initialize Project
first create a python virtual environment, and active it.   
projct using `$PYTHONPATH` environment variable to make sure package import correctly, please set this variable to project directory. e.g. `export PYTHONPATH=$PWD`.
```bash
python -m venv .venv
source .venv/bin/activate 
```

then, install project dependencies.  
```bash
pip install -r requirements.txt
```

for code testing, run the following command.
```bash 
bash ./test.sh
```
for packaging, run the following command.
```bash
bash ./build.sh
```
