'''
This script is for preparing img files fot running FSL VBM processing. 
By Xiangzhen Kong, 20200205
'''
import os
import glob
import numpy as np

dat_dir = '../sMRI/'
#vbm_dir = '../vbm'
vbm_dir = '../vbm2'
if not os.path.exists(vbm_dir):
    os.mkdir(vbm_dir)
# Note that several problem subjects in problema_subid_visualQC.txt were removed manually. 

template_list = []
img_list = []

subj_dir_list = glob.glob(os.path.join(dat_dir, 'BIG'+'[0-9]'*4))
for subj_dir in subj_dir_list:
    print subj_dir
    scan_dir_list = glob.glob(os.path.join(subj_dir, '[0-9]'*1))
    scan_dir_list.sort()
    for i, scan_dir in enumerate(scan_dir_list):
        scan_img_list = glob.glob(os.path.join(scan_dir, '*.nii'))
        scan_img_list.sort()
        img_list.append(os.path.basename(scan_img_list[0]))
        if i==0:
            template_list.append(os.path.basename(scan_img_list[0]))
            
        for scan_img in scan_img_list:
            out_img_name = os.path.basename(scan_img)
            out_img_file = os.path.join(vbm_dir, out_img_name)
            if not os.path.exists(out_img_file):
                #cmdstr = 'ln -s ' + scan_img + ' ' + out_img_file
                #cmdstr = 'fsl_sub -q single15.q fslreorient2std ' + scan_img + ' ' + out_img_file
                cmdstr = 'fsl_sub -q single.q orientLAS ' + scan_img + ' ' + out_img_file
                print cmdstr
                os.system(cmdstr)
            else:
                print 'Already existed', scan_img
                #exit(-1)

np.savetxt('img_list.txt', img_list, fmt='%s')
np.savetxt('template_list', template_list, fmt='%s')
print 'Finished!'

