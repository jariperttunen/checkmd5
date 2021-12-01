import sys
import argparse
import glob
import hashlib
import pathlib
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--dir",dest="d",type=str,required=True,help="Directory names (wild card)")
    args = parser.parse_args()

    ls = glob.glob(args.d)
    for dir_name in ls:
        print(dir_name)
        #Collect files and make the dictionary {file_name:[md5_value]}
        file_ls = glob.glob(dir_name+'/*.gz')
        md5_ls = glob.glob(dir_name+'/MD5.txt')
        df =  pd.read_csv(md5_ls[0],delim_whitespace=True,header = None)
        md5_dict = df.set_index(1).T.to_dict(orient='list')
        #Go through the files and calculate MD5 values, compare to MD5 dictionary values
        for file_name in file_ls:
            md5file = hashlib.md5()
            md5file.update(open(file_name,"rb").read())
            md5hash = md5file.hexdigest()
            p = pathlib.Path(file_name)
            #Note the key is file name only and hash value is in the list, 
            MDF5file_hash = md5_dict[p.name][0]
            if MDF5file_hash != md5hash:
                print("File:", file_name, "MDF5 file hash:", MDF5file_hash, "!=", md5hash,file = sys.stderr)
            else:
                print("File:", file_name, "MD5 file hash OK")

