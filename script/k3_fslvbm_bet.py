'''
Script for brain extraction using fslvbm_1_bet. A new subfolder struc will be created. 
fslvbm_1_bet copy all images to the new folder struc. Run this after k2 is finished.
By Xiangzhen Kong, 20200205
'''
import os 

#vbm_dir = '../vbm/'
vbm_dir = '../vbm2/'
os.chdir(vbm_dir)
cmdstr = 'fslvbm_1_bet -N' # -N for T1 images with a lost of neck. 
print cmdstr
os.system(cmdstr)

