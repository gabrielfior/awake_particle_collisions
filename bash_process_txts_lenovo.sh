#!/bin/bash

clear
echo "Starting script"
#cd /home/iwsatlas1/fior/anaconda2/bin/data_mpp
echo "Processing file 1"
python read_txt_export_csv.py '/media/gabriel/UNTITLED/beam/' '10cm_1e6_400GeV_Rb10minus7_beam_cut1_5mm_nt_B4_g_proc.txt'
echo "Processing file 2"
python read_txt_export_csv.py '/media/gabriel/UNTITLED/beam/' '10cm_1e6_400GeV_Rb10minus6_beam_cut1_5mm_nt_B4_g_proc.txt'
echo "Processing file 3"
python read_txt_export_csv.py '/media/gabriel/UNTITLED/beam/' '10cm_1e6_400GeV_Rb10minus5_beam_cut1_5mm_nt_B4_g_proc.txt'
echo "Processing file 4"
python read_txt_export_csv.py '/media/gabriel/UNTITLED/beam/' '10cm_1e4_400GeV_Rb10minus4_beam_cut1_5mm_nt_B4_g_proc.txt'
echo "Finished"