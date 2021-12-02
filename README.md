## Check MD5 checksum
Clone *checkmd5* from GitHub:

    git clone https://github.com/jariperttunen/checkmd5.git

Setup python3 at CSC:

    module load python-env/2019.3

Check MD5 checksum. Give a list of directories (wildcards):

    python checkmd5/checkmd5.py -d /path/to/A*/  > MD5_OK.txt 2> MD5_errors.txt
 
 In the example directories beginning with letter *A* are explored.

