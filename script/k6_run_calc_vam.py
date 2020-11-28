import os
import numpy as np 
import glob

vbm_dir = '../vbm2/struc/'

vbm_file = '_GM_to_template_GM_mod_sm255.nii.gz'

mask_file = 'template_GM_thr03_bin_clean_sym_atlas'

asym_dir = os.path.join(vbm_dir, 'asym')
if not os.path.exists(asym_dir):
    os.mkdir(asym_dir)
sge_log_dir = os.path.join(asym_dir, 'sge_logs')
if not os.path.exists(sge_log_dir):
    os.mkdir(sge_log_dir)

mod_sm255_list = glob.glob(os.path.join(vbm_dir, '*'+vbm_file))
for mod_sm255 in mod_sm255_list:
    SID = os.path.basename(mod_sm255)[5:14]
    SID_vbm_file = os.path.basename(mod_sm255)
    print SID
    run_sge_str = 'fsl_sub -q single.q -l ' + sge_log_dir
    cmd_str = run_sge_str + ' ./calc_vam ' + SID_vbm_file + ' ' + mask_file + ' ' + vbm_dir + ' ' + asym_dir
    print cmd_str
    os.system(cmd_str)

