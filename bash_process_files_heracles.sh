#!/bin/bash

clear
echo "Starting script"
cd /home/iwsatlas1/fior/anaconda2/bin/data_mpp
echo "Processing file 1"
python process_csv_beam_v4_heracles.py 10cm_1e6_400GeV_Rb10minus7_beam_cut1_5mm_nt_B4_g.csv
echo "Processing file 2"
python process_csv_beam_v4_heracles.py 10cm_1e6_400GeV_Rb10minus6_beam_cut1_5mm_nt_B4_g.csv
echo "Processing file 3"
python process_csv_beam_v4_heracles.py 10cm_1e6_400GeV_Rb10minus5_beam_cut1_5mm_nt_B4_g.csv
echo "Processing file 4"
python process_csv_beam_v4_heracles.py 10cm_1e6_400GeV_Rb10minus4_beam_cut1_5mm_nt_B4_g.csv
echo "Finished"