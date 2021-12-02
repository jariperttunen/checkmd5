## Check MD5 checksum
Clone `checkmd5.py` from GitHub:
+ git clone https://github.com/jariperttunen/checkmd5.git

Setup python3 at CSC and create *md5* python virtual environment
+ module load python-env/2019.3
+ python -m venv md5

Activate the virtual environment and install pandas
+ source md5/bin/activate
+ pip install --upgrade pip
+ pip install pandas

Check MDF5 checksum. Give a list of directories (wildcards):
+ python checkmd5.py -d path/to/A*/  > MD5_OK.txt 2> MD5_errors.txt
  + (Directories beginning with letter A)

