'''
Script for template creating using fslvbm_2_template. 
By Xiangzhen Kong, 20200205
'''
import os 

#vbm_dir = '../vbm/'
vbm_dir = '../vbm2/'
os.chdir(vbm_dir)
cmdstr = '../script/fslvbm_3_proc_mpi' 
print cmdstr
os.system(cmdstr)

