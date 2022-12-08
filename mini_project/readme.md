


## 1 introduction

## 2 deployment

### 2.1 conda install

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

### 2.2 environment setup

conda update conda
conda create -n 655mini python=3.9
y
conda activate 655mini

pip install -r requirement.txt

### 2.3 run app.py

python app.py