'''
Script for template creating using fslvbm_2_template. 
By Xiangzhen Kong, 20200205
'''
import os 

#vbm_dir = '../vbm/'
vbm_dir = '../vbm2/'
os.chdir(vbm_dir)
#cmdstr = 'fslvbm_2_template -n' # -n option for using non-linear registration. 
cmdstr = '../script/fslvbm_2_template_mpi -n' # -n option for using non-linear registration. 
print cmdstr
os.system(cmdstr)

