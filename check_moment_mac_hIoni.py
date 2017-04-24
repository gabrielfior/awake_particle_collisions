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
import re
import aux_funcs_verbose as aux


write_flag=False

#file1 = "/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/proton_Rb_300MeV_10mm.out"
#file1 = "/Users/gabrielfior/OneDrive/Master Thesis/Share_Ubuntu/output_300MeV_verbose3.out"
file1 = '/Users/gabrielfior/data_mpp2_data/test_hioni/'
#file1 = '/media/gabriel/6CA49654A496211E/B4-build/divide/'

proc_name=[]
edep=[]
pre_kin_energy=[]
pos_kin_energy=[]
list_step_lines=[]



list_files = os.listdir(file1)
for iii in list_files:
    if '.csv' in iii:
	os.remove(file1+iii)

for iii in list_files:
    if iii[-4:]=='.dat' or iii[-4:]=='.csv':
        list_files.remove(iii)
# Filter dat files out, run again


os.chdir(file1)
rest=[]
list_files.sort()
list1=[]
list1.append(list_files[0])
list1.append(list_files[1])

rest=[]

count_particle = 0

for i in list_files:
    if i == 'csvfiles':
	list_files.remove(i)

for file0 in list_files:

    print 'reading file: ' + str(file0)

    with open(file0) as f:
        x = f.readlines()
    
    x = rest+x
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
    
    tracks.append(len(x))
    all_steps=[]
    curr_step=0
    curr_step_new=0
    cleaning=False
    
    
    
    #Update rest
    rest = x[tracks[-2]:tracks[-1]]
    
    for i in range(len(tracks)-2):
    
    #for i in range(100):
        #write on temp file
        with open('log_check_moment.dat','w') as f:
            f.write('reading file '+file0+' / reading track # ' + str(i) + '\n')
        
        
        #print 'particle # ' + str(i)    
        
        item_list=[]
        steps_list=[]
    
        
        
        #print i
        item = x[tracks[i]:tracks[i+1]]
        
        #print item
    
        for j in range(len(item)): 
            if 'G4Track' in item[j] and 'Particle' in item[j]:
                data1 = filter(None,item[j].split(' '))
                track_id = data1[9].replace(',','')
                parent_id = int(data1[-1].replace('/n',''))
                particle_name = data1[5].replace(',','')
                count_particle = count_particle+1

            elif 'End of event' in item[j]:
                print 'if on top'
                print j,item[j]
                curr_step_new=curr_step_new + 1
                print 'current step: ' + str(curr_step) +',curr_step_new:'+str(curr_step_new)
            
        #cleaning
        if cleaning:
            print 'cleaning'
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
            
            #print jj        
            
            if len(jj) > 30:#regular step
                item_to_retrieve = jj
                #Loop inside step0
                step_store = aux.get_data_from_step_line(jj,step_store)
                #print 'step store after get data from line'
                #print step_store
                for iii,o in enumerate(jj):
                    
                
                
                    if '#Step#' in o or 'Step#' in o: 
                        #proc_name.append(jj[iii+1])
                        proc_name.append(filter(None,jj[iii+1].split(' '))[-1].replace('\n',''))
                        #edep.append(jj[iii+12])
                        edep.append(np.double(filter(None,jj[iii+12].split(':'))[-1]))
                        step_store['edep'] =  np.double(filter(None,jj[iii+12].split(':'))[-1])                       
                        #pre_kin_energy.append(np.double(filter(None,jj[iii+29].split(' '))[-2]))
                        pre_kin_energy.append(aux.check_momentum(jj[iii+29],'first'))                        
                        step_store['pre_kin_en'] =  aux.check_momentum(jj[iii+29],'first')                                               
                        pos_kin_energy.append(aux.check_momentum(jj[iii+29],'second'))
                        step_store['pos_kin_en'] = aux.check_momentum(jj[iii+29],'second')
                    
        		  #elif 'Energy Deposit' in o:
                   #   step_store['energy_deposit'] = np.double(filter(None,o.split(':'))[-1])

                    '''
                    elif 'Momentum Direct - z' in o:
                        step_store['mom_dir_z'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_z'])
               
                    elif 'Momentum Direct - x' in o:
                        step_store['mom_dir_x'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_x'])
                        
                    elif 'Momentum Direct - y' in o:
                        step_store['mom_dir_y'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Momentum - z' in o:
                        step_store['mom_z'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Momentum - x' in o:
                        step_store['mom_x'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Momentum - y' in o:
                        step_store['mom_y'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_y'])
                                        
                    elif 'Total Energy' in o:
                        step_store['total_energy'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Velocity' in o:
                        step_store['velocity'] = aux.check_momentum(o,'first')
                        #print 'store:' + str(step_store['mom_y'])
                    '''
                        
            else:
                
                #Loop inside last step
                #Get normal data          
                step_store = aux.get_data_from_step_line(jj,step_store)
                #pass
                for iii,o in enumerate(item_list[ii-1]):
                
                    '''
                    step_store['energy_deposit'] = 0.0
                    if 'Momentum Direct - z' in o:
                        step_store['mom_dir_z'] = aux.check_momentum(o,'second')
                        print 'store:' + str(step_store['mom_dir_z'])

                    elif 'Momentum Direct - x' in o:
                        step_store['mom_dir_x'] = aux.check_momentum(o,'second')
                        print 'store:' + str(step_store['mom_dir_x'])
                        
                    elif 'Momentum Direct - y' in o:
                        step_store['mom_dir_y'] = aux.check_momentum(o,'second')
                        print 'store:' + str(step_store['mom_dir_y'])
                        
                    elif 'Momentum - z' in o:
                        step_store['mom_z'] = aux.check_momentum(o,'second')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Momentum - x' in o:
                        step_store['mom_x'] = aux.check_momentum(o,'second')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Momentum - y' in o:
                        step_store['mom_y'] = aux.check_momentum(o,'second')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Total Energy' in o:
                        step_store['total_energy'] = aux.check_momentum(o,'second')
                        #print 'store:' + str(step_store['mom_y'])
    
                    elif 'Velocity' in o:
                        step_store['velocity'] = aux.check_momentum(o,'second')
                        #print 'store:' + str(step_store['mom_y'])
    
                    '''
    
                #####end of else####
    	    
	    #Include particle name, track id
	    step_store['track_id'] = track_id
            step_store['parent_id'] = parent_id
            step_store['particle_name'] = particle_name
            step_store['count_particle'] = count_particle
            
            #step_store['edep'] =  np.NaN
            #step_store['pre_kin_en'] =  np.NaN
            #step_store['pos_kin_en'] = np.NaN
                                
            

	    all_steps.append(step_store)
    
    
            curr_step = curr_step_new
        
        event_num2 = event_num
    

    #write csv for each file
    #Write CSV
    #x = json.loads(x)
    
    if write_flag:
        with open(file1+'csvfiles/'+file0+'_csvfile.csv', 'w') as outfile:
            f = csv.writer(outfile)
        
        # Write CSV Header, If you dont need that, remove this line
            f.writerow(all_steps[0].keys())
            
            for xx in all_steps:
                list_values = []
                for i,j in xx.iteritems():
                    list_values.append(j)
            
                f.writerow(list_values)
        
        print 'csv file generated'

