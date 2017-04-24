import numpy as np
import pandas as pd
import datetime

# Read file
filename = '/home/iwsatlas1/fior/10cm_1e6_400GeV_Rb10minus4_beam_cut1_5mm_nt_B4_g.csv'
columns_new3 = ['trackId','parentId','volumeName','particleName','stepNumber',
                                               'posX','posY','posZ','perp','kineeticEnergyDiff',
                                               'edepStep','kineticEnergyPostStep','processName',
                                'mompreX','mompreY','mompreZ','momposX','momposY','momposZ','stepLength']#,'ParticleId']

t0 = datetime.datetime.now()
df = pd.read_csv(filename,
                 skiprows=24,header=None,#nrows=1e3,#17*1e6
                 names=columns_new3,
                 index_col=None
                )


print 'elapsed: '+str(datetime.datetime.now()-t0)

df['index_col'] = df.index

#number event lines, make zip from (line_number,event_num)

array_indexes = (df[df.volumeName=='event'].index)
#volumeName=='event'
array_event_numbers = range(1,len(array_indexes)+1)
zip_array = zip(array_indexes,array_event_numbers)


def calculate_particle_id(row):
    for i in range(len(zip_array)-1):
        if row['index_col']>zip_array[i][0] and row['index_col']<zip_array[i+1][0]:
            return zip_array[i][1]
            break
        elif row['index_col']<zip_array[i][0]:
            return 0
            break

t0 = datetime.datetime.now()
print 'started: '+ str(t0)
df['particleIdNew'] = df.apply(calculate_particle_id,axis=1)
print 'ended, elapsed : '+str(datetime.datetime.now()-t0)

#drop event rows
df = df[df.volumeName != 'event']

#export csv
df.to_csv(filename[:-4]+'_proc.csv',header=False,index=False)