'''
Script for quick QC. A webpage will be generated.
By Xiangzhen Kong, 20200205
'''
import os 

#vbm_dir = '../vbm/'
vbm_dir = '../vbm2/'
os.chdir(vbm_dir)
cmdstr = 'slicesdir `imglob *`'
print cmdstr
os.system(cmdstr)

