#!/usr/bin/env python3
############################################################
#
# Comparison of output files
#
############################################################
import os
import difflib

def check_rst(ref_file, check_file):
    print("")
    print("Checking result...")
    print("")

    ref_file = open(ref_file)
    check_file = open(check_file)

    print("Read:", ref_file)
    print("Read:", check_file)
    print("")

    diff = difflib.Differ()

    out_diff = diff.compare(ref_file.readlines(), check_file.readlines())
    
    ans = True
    for data in out_diff :
        if data[0:1] in ['+', '-'] :
            ans = False
            print(data)

    if ans == True:
        print("Success!")
    else:
        print("Error!")

    ref_file.close()
    check_file.close()


if __name__ == "__main__":
    ref_file = "ref_rst/ode_msd_model.csv"
    check_file = "workspace/ode_msd_model.csv"
    check_rst(ref_file, check_file)