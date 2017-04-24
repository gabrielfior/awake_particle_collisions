#!/bin/bash
#this is a comment-the first line sets bash as the shell script
cd /Users/gabrielfior/data_mpp2;
python ./process_csv_beam_v4.py /Volumes/UNTITLED/beam/10cm_1e6_400GeV_Rb10minus4_beam_cut1_5mm_nt_B4_g.csv;
python ./process_csv_beam_v4.py /Volumes/UNTITLED/beam/10cm_1e6_400GeV_Rb10minus5_beam_cut1_5mm_nt_B4_g.csv;
python ./process_csv_beam_v4.py /Volumes/UNTITLED/beam/10cm_1e6_400GeV_Rb10minus6_beam_cut1_5mm_nt_B4_g.csv;
python ./process_csv_beam_v4.py /Volumes/UNTITLED/beam/10cm_1e6_400GeV_Rb10minus7_beam_cut1_5mm_nt_B4_g.csv;
exit;