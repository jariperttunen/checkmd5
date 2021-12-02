## Check MD5 checksum
Clone `checkmd5.py` from GitHub:
+ git clone https://github.com/jariperttunen/checkmd5.git

Check MDF5 checksum. Give a list of directories (wildcards):
+ python checkmd5.py -d path/to/A*/  > MD5_OK.txt 2> MD5_errors.txt
  + (Directories beginning with letter A)

See also [Setup_checkmd5](Setup_checkmd5.md) to setup python3 at CSC.
