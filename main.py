import os
import hashlib
from collections import defaultdict
import csv

"Given a folder, this tool walks through it and creates a list of all duplicate files"
"the md5 checksum for each file determines duplicates"

src_folder = "../../"