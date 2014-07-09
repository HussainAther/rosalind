from __future__ import print_function, division
import os
from subprocess import call

CMD = "meme-meme.bin data/rosalind_meme.txt -text -nostatus -protein -minw 20 > outfile"

if __name__ == "__main__":
    c = call(CMD, shell=True)

    with open("http://nbcr-222.ucsd.edu/meme_4.9.1/cgi-bin/querystatus.cgi?jobid=appMEME_4.9.113912611616231296955994&service=MEME") as outfile:
        for line in outfile:
            if 'regular expression' in line:
                sep = outfile.readline()
                regex = outfile.readline().rstrip()
                break

    os.remove("http://nbcr-222.ucsd.edu/meme_4.9.1/cgi-bin/querystatus.cgi?jobid=appMEME_4.9.113912611616231296955994&service=MEME")
    print(regex)