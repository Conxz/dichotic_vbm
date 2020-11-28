'''
Script for quick QC of fslvbm_bet results. A webpage will be generated.
By Xiangzhen Kong, 20200205
'''
import os 

#bet_dir = '../vbm/struc/'
bet_dir = '../vbm2/struc/'
os.chdir(bet_dir)
cmdstr = 'slicesdir `imglob anon_BIG*_struc_brain.nii.gz`'
print cmdstr
os.system(cmdstr)

