import FDTGui
import os
import hashlib
from collections import defaultdict
import csv

from tkinter import*


def generate_md5(fname,chunk_size = 1024):
    """ This Function takes a file name and returns md5 checksum of the file """
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        #Read the first block of the file
        chunk = f.read(chunk_size)
        #Read till the end and update the hash
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)
    #Return the hex checksum
    return hash.hexdigest()

if __name__ == "__main__":

    #The dict has a list as values
    md5_dict = defaultdict(list)
    file_types_inscope = ["ppt","pptx","pdf","txt","html","mp4","jpg","png","xls","xlsx","xml","vsd","py","json"]

    #Walk through all files and folders in the directory
    for path, dirs, files in os.walk(FDTGui.src_folder):
        print("Please Wait...Now Analyzing {}".format(path))
        for each_file in files:
            if each_file.split(".")[-1].lower() in file_types_inscope:
                #Update Path Variable for each subfolder
                file_path = os.path.join(os.path.abspath(path), each_file)

                #Check if there are files with the same checksum and append to list
                md5_dict[generate_md5(file_path)].append(file_path)

    #Identify Checksums that have more than one values(File names)
    duplicate_files = (val for key, val in md5_dict.items() if len(val)>1)

    #Write the list of duplicate files to csv file
    with open("DuplicateFiles.csv","w") as log:
        #Line terminator added for windows as it inserts blank rows as it inserts blank rows otherwise
        csv_writer = csv.writer(log, quoting =csv.QUOTE_MINIMAL, delimiter = ",", lineterminator ="\n")
        header = ["File Names"]
        csv_writer.writerow(header)

        for file_name in duplicate_files:
            csv_writer.writerow(file_name)
    print("Thank you...The Entire Process is Complete")