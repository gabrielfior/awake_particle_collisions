# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:35:46 2016

@author: gabrielfior
"""
import os
import json
import csv
import numpy as np
import matplotlib.pyplot as plt

#file1 = "/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/proton_Rb_300MeV_10mm.out"
file1 = "/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/output_300MeV_verbose3.out"
with open(file1) as f:
    x = f.readlines()



starts=[]
ends=[]
#Get start and end of runs
for i in range(len(x)):
    if 'starts.' in x[i] and 'Event' in x[i]:
        starts.append(i)
    elif '--> End of event' in x[i]:
        ends.append(i)

 
#Get tracking information
tracks=[]
for i in range(len(x)):
    if 'G4Track Information' in x[i]:
        tracks.append(i)


#Need to get begin and end of track
#Clean start and end of events
tracks_list=[]
cross_end = False
event_num = 0
event_num2 = 0
line_step_detail = '        StepPoint Information               PreStep            PostStep\n'

#tracks.append(len(x))

tracks.append(ends[-1])
all_steps=[]
#for i in range(len(tracks)-1):
for i in range(1):
    
    item_list=[]
    steps_list=[]

    
    
    #print i
    item = x[tracks[i]:tracks[i+1]]
    #print item

    
        
    #cleaning
    for j in range(len(item)):
        if '--->' in item[j]:
            item = item[:j]
            event_num = event_num+1
            break
        
    for j in range(len(item)):
        if '#Step#' in item[j] or 'Step#' in item[j]:
            steps_list.append(j)
    
    #Divide into steps
    steps_list.append(len(item))
    for iii in range(len(steps_list)-1):
        item3 = item[steps_list[iii]:steps_list[iii+1]]    
        item_list.append(item3)
        

    #Process each step
    #1 - See if it is last event
    
    for ii,jj in enumerate(item_list):
        step_store={}
        flag_post = False #for else iteration
        if len(jj) > 10:#regular step
            #Loop inside step0
            for iii,o in enumerate(jj):
                
                if 'Step#' in o:
                    #Get X,Y,Z,kinE,nextVol,ProcName
                    g= jj[iii+1]
                    step_store['step_number'] = np.double(filter(None,g.split(' '))[0])
                    step_store['position_x'] = np.double(filter(None,g.split(' '))[1])
                    step_store['position_y'] = np.double(filter(None,g.split(' '))[2])
                    step_store['position_z'] = np.double(filter(None,g.split(' '))[3])
                    step_store['kinetic_energy'] = np.double(filter(None,g.split(' '))[4])
                    step_store['next_vol']= filter(None,g.split(' '))[-2]
                    step_store['dE']= filter(None,g.split(' '))[5]          
                
                
                elif 'Step Length' in o:
                    bb = filter(None,o.split(' '))[-1]
                    step_store['step_length']=np.double(bb[:bb.index('\n')]) 

                elif 'Energy Deposit' in o:
                    bb = filter(None,o.split(' '))[-1]
                    step_store['energy_deposit']=np.double(bb[:bb.index('\n')]) 
                
                
                elif 'Momentum Direct - x' in o:
                    try:
                        step_store['mom_dir_x']=np.double(filter(None,o.split(' '))[-2])                
                    except ValueError:
                        step_store['mom_dir_x']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])

                elif 'Momentum Direct - y' in o:
                    try:
                        step_store['mom_dir_y']=np.double(filter(None,o.split(' '))[-2])                
                    except ValueError:
                        step_store['mom_dir_y']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])

                elif 'Momentum Direct - z' in o:
                    try:
                        step_store['mom_dir_z']=np.double(filter(None,o.split(' '))[-2])                
                    except ValueError:
                        step_store['mom_dir_z']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])
                elif 'Momentum - x' in o:
                    try:
                        step_store['mom_x']=np.double(filter(None,o.split(' '))[-2])                
                    except ValueError:
                        step_store['mom_x']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])

                elif 'Momentum - y' in o:
                    try:
                        step_store['mom_y']=np.double(filter(None,o.split(' '))[-2])                
                    except ValueError:
                        #2 minus case
                        #print 'oi'
                        a = filter(None,o.split(' '))[-1]
                        if a.count('-')==2:
                            step_store['mom_y'] = np.double(a.split('-')[1])*-1
                                                        
                        else:
                            #print 'here'
                            step_store['mom_y']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])
                        
                elif 'Momentum - z' in o:
                    try:
                        step_store['mom_z']=np.double(filter(None,o.split(' '))[-2])                
                    except ValueError:
                        step_store['mom_z']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])

                elif 'Total Energy' in o:
                    try:
                        step_store['total_energy']=np.double(filter(None,o.split(':')[1].split(' '))[0])    
                    except ValueError:
                        step_store['total_energy']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])
                                               
                    
                elif 'Velocity' in o:
                    step_store['velocity']=np.double(filter(None,o.split(' '))[-2])

                elif 'Process defined Step' in o:
                    step_store['process_defined_step']=filter(None,o.split(' '))[-2]
                elif 'List of secondaries generated' in o:
                    step_store['list_secs_gener']=int(o[o.index('=')+1:o.index('\n')])
                if 'PostStepDoIt' in o:
                    break
                    
        #step_store={}
                #all_steps.append(step_store)        
        
        else: #Last step, get data from right column
             #print 'entered else'

             
             for iii,o in enumerate(jj):
                
                if '#Step#' in o:
                    #Get X,Y,Z,kinE,nextVol,ProcName
                    g= jj[iii+1]
                    step_store['step_number'] = np.double(filter(None,g.split(' '))[0])
                    step_store['position_x'] = np.double(filter(None,g.split(' '))[1])
                    step_store['position_y'] = np.double(filter(None,g.split(' '))[2])
                    step_store['position_z'] = np.double(filter(None,g.split(' '))[3])
                    step_store['kinetic_energy'] = np.double(filter(None,g.split(' '))[4])
                    step_store['next_vol']= filter(None,g.split(' '))[-2]
                    step_store['dE']= filter(None,g.split(' '))[5]                    
                #Get previous step
                
             g1 = item_list[ii-1] #get last item and process column on the right                
          
             for iii,o in enumerate(g1):
                 
                #Get second part of g1 (after PostStepdoIt)

                if 'PostStepDoIt' in o:
                    flag_post = True
                
                if flag_post:                 
                     
                    if 'Step Length' in o:
                        bb = filter(None,o.split(' '))[-1]
                        step_store['step_length']=np.double(bb[:bb.index('\n')]) 
    
                    elif 'Deposit' in o:
    
                        bb = filter(None,o.split(' '))[-1]
                        step_store['energy_deposit']=np.double(bb[:bb.index('\n')]) 
                    
    
                    elif 'Momentum Direct - x' in o:
                        try:
                            #print 'try'
                            step_store['mom_dir_x']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                            #print ' except'
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                #print 'if2'
                                step_store['mom_dir_x'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'else2'
                                #print 'here'
                                step_store['mom_dir_x']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[2].replace('\n','')[:8])
                                
    
                    elif 'Momentum Direct - y' in o:
                        try:
                            #print 'try'
                            step_store['mom_dir_y']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                        
                            #print ' except'
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                #print 'if2'
                                step_store['mom_dir_y'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'else2'
                                #print 'here'
                                step_store['mom_dir_y']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[2].replace('\n','')[:8])
                     
                   
                    
                    elif 'Momentum Direct - z' in o:
                        try:
                            #print 'try'
                            step_store['mom_dir_z']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                            #print ' except'
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                #print 'if2'
                                step_store['mom_dir_z'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'else2'
                                #print 'here'
                                step_store['mom_dir_z']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[2].replace('\n','')[:8])
                    
    
                    
                    elif 'Momentum - x' in o:
                        try:
                            #print 'try'
                            step_store['mom_x']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                            #print ' except'
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                #print 'if2'
                                step_store['mom_x'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'else2'
                                #print 'here'
                                step_store['mom_x']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[2].replace('\n','')[:8])
                    
    
                    elif 'Momentum - y' in o:
                        try:
                            step_store['mom_y']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                step_store['mom_y'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'here'
                                step_store['mom_y']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])
                            
                    elif 'Momentum - z' in o:
                        try:
                            step_store['mom_z']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                step_store['mom_z'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'here'
                                step_store['mom_z']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])
                            
    
                    elif 'Total Energy' in o:
                        try:
                            step_store['total_energy']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                step_store['total_energy'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'here'
                                step_store['total_energy']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])
                            
                        
                    elif 'Velocity' in o:
                        try:
                            step_store['velocity']=np.double(filter(None,o.split(' '))[-1])                
                        except ValueError:
                            #2 minus case
                            #print 'oi'
                            a = filter(None,o.split(' '))[-1]
                            if a.count('-')==2:
                                step_store['velocity'] = np.double(a.split('-')[1])*-1
                                                            
                            else:
                                #print 'here'
                                step_store['velocity']=np.double(filter(None,o.split(':')[1].split(' '))[0].split('.')[0] + '.'+ filter(None,o.split(':')[1].split(' '))[0].split('.')[1][:8])
                            
    
                    elif 'Process defined Step' in o:
                        step_store['process_defined_step']=filter(None,o.split(' '))[-1]
                    elif 'List of secondaries generated' in o:
                        step_store['list_secs_gener']=np.NaN #no secondaries defined
                    if 'PostStepDoIt' in o:
                        #break
                        pass
                     
        
        all_steps.append(step_store)                
    #Check for this line for detailed step info

        
    '''
    #Process line
    item2=[]
    headers=[]        
    b1_list=[]
    for ii in item:

        #print ii
        
        if 'G4Track' in ii:

            #print ii
            a = ii.strip().split(',')   
            for b in a:
                #print b
                headers.append(b[b.index('=')+1:].strip())           
    
        elif 'G4Track' not in ii and '*' not in ii and len(ii)>1 and 'X(mm)' not in ii:# and ii[:2] != "\n" and 'Step' not in ii:
                
            b1 = filter(None,ii.split(' '))  
            b1_list.append(b1)                       
            
            #item2.append(b1)

    for b2 in b1_list:
        tracks_list.append({'event_num':event_num2,
                                    'particle_name':headers[0],
                                    'track_id':headers[1],
                                    'parent_id':headers[2],
                                'step_num':b2[0],
                                'X(mm)':b2[1],
                                'Y(mm)':b2[2],
                                'Z(mm)':b2[3],
                                'KinE(MeV)':b2[4],
                                'dE(MeV)':b2[5],
                                'StepLeng':b2[6],
                                'TrackLeng':b2[7],
                                'NextVolume':b2[8],
                                'ProcName':b2[9].replace('\n',''),
                            })

    #tracks_list.append({'event:num':event_num2,
    #                    'item':item2,
    #                   })
    event_num2 = event_num



#Write CSV
#x = json.loads(x)

f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(tracks_list[0].keys())

for xx in tracks_list:
    list_values = []
    for i,j in xx.iteritems():
        list_values.append(j)

    f.writerow(list_values)


'''
