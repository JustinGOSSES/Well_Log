"""
Justin Gosses
python 2.7
2015-10-08
LASIO test - import and print logs from las file
"""
#import lasio and read the trial las as an object
import lasio
import numpy as np
import math
l = lasio.read("Test_1b.las")
# # print all curves, will print all curve information
from pprint import pprint
pprint(l.curves)

#print curves bu only mnemonic, units, values, and description
for curve in l.curves:
    print("%s\t[%s]\t%s\t%s" % (
                                curve.mnemonic, curve.unit, curve.value, curve.descr))
    
    

def bottom_of_data_all_curves(well):
    """
    finds lowest position in each curve that has data that is not NAN.
    """
    for aa_curve in list(well.curves):
        a_curve = aa_curve.mnemonic
        #print a_curve,"a_curve"
        x = -1
        #print well[a_curve][x]
        while math.isnan(well[a_curve][x]):
            x -= 1
        else:
            last_data = x
            trial_depth = well["DEPT"][x]
            print x,"=value at last non-NaN ",trial_depth, "= bottom of curve: ", a_curve

print bottom_of_data_all_curves(l)        
        
def top_of_data_all_curves(well):
    """
    finds highest position in each curve that has data that is not NAN.
    """
    for aa_curve in list(well.curves):
        a_curve = aa_curve.mnemonic
        #print a_curve,"a_curve"
        x = 0
        #print well[a_curve][x]
        while math.isnan(well[a_curve][x]):
            x += 1
        else:
            last_data = x
            trial_depth = well["DEPT"][x]
            print x,"=value at last non-NaN ",trial_depth, "= top of curve: ", a_curve       

print top_of_data_all_curves(l)
