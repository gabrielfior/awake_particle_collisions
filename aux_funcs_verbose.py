# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 01:01:09 2016

@author: gabrielfior
"""
import os
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
import re
import aux_funcs_verbose as aux


def check_momentum(o,first_or_second='first'):
    import re
    import numpy as np
    
    if first_or_second == 'first':
    
        print 'entrei moment direct x'
        print o
        #b=o
        try:
            a = filter(None,o.split(' '))[-2]
            print len(a)
            list1 = [m.start() for m in re.finditer('\.', a)]
            if a[0].strip()=='-':                        
                    sign= -1.0
            else:
                    sign = 1.0
            print sign
                
            print list1
            #print '1 item:' + str(a[:list1[len(list1)-1]])
            #print '2 item:' + str(a[list1[len(list1)-1]:-1])
            var1=np.double(filter(None,o.split(' '))[-2])  
            print  'ok' + str(var1)
        except ValueError:
            print 'entrei valor error'
            a = o.split(' ')[-1]
            list1 = [m.start() for m in re.finditer('\.', a)]
            print '1 item:' + str(a[:list1[len(list1)-1]])
            print '2 item:' + str(a[list1[len(list1)-1]:-1])
            print 'my item' + str(a[list1[len(list1)-1]-2])
            sign2 = 1.0                        
            if a[list1[len(list1)-1]-2] == '-':
                sign2 = -1.0
            var1=sign2*np.double(a[:list1[len(list1)-1]].replace('-',''))  
            #print 'try ok'
            print 'step_store is ' + str(var1)

    if first_or_second=='second':
        
        print 'entrei moment direct x'
        print o
        #b=o
        try:
            a = filter(None,o.split(' '))[-2]
            print len(a)
            list1 = [m.start() for m in re.finditer('\.', a)]
            if a[0].strip()=='-':                        
                    sign= -1.0
            else:
                    sign = 1.0
            print sign
                
            print list1
            #print '1 item:' + str(a[:list1[len(list1)-1]])
            #print '2 item:' + str(a[list1[len(list1)-1]:-1])
            var1=np.double(filter(None,o.split(' '))[-1])  
            print  'ok' + str(var1)
        except ValueError:
            print 'entrei valor error'
            a = o.split(' ')[-1]
            list1 = [m.start() for m in re.finditer('\.', a)]
            print '1 item:' + str(a[:list1[len(list1)-1]])
            print '2 item:' + str(a[list1[len(list1)-1]:-1])
            print 'my item' + str(a[list1[len(list1)-1]-2])
            sign2 = 1.0                        
            if a[list1[len(list1)-1]-2] == '-':
                sign2 = -1.0
            var1=sign2*np.double(a[list1[len(list1)-1]:-1].replace('-',''))  
            #print 'try ok'
            print 'step_store is ' + str(var1)    

    return var1
    
    
def write_txt(count1,list_to_write,folder1):
    
    with open(folder1+str(count1)+'.out','w') as outfile:
        for item in list_to_write:
            outfile.write('%s\n' % item)


def get_data_from_step_line(jj, step_store):
    
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
            step_store['dE']= np.double(filter(None,g.split(' '))[5])
            step_store['process_name']= filter(None,g.split(' '))[-1].replace('\n','')
            
            

    return step_store

def return_full_sframe(dir1):

    list_files1 = os.listdir(dir1)
    print dir1+list_files1[0]
    sf = graphlab.SFrame.read_csv(dir1+list_files1[0])

    for ii in list_files1[1:]:
        #print ii
        
        #read SFrame
        temp = graphlab.SFrame.read_csv(dir1+ii)
        print temp.num_rows()
        sf=sf.append(temp)
        print sf.num_rows()            
            
    return sf
    
def ce(E):

    mc2 = 938*1e6
    
    #E=mc2/(1−v2/c2)1/2.
    #return E
    c = 3*1e8 #m/s
    v = np.sqrt(1. - ((mc2/E)*(mc2/E))) * c    
    m0 = 1.6726 *1e-27
    
    #p = np.sqrt((E*E - (m0*c*m0*c*c*c)) / (c*c) )   
    #v = np.sqrt(p / (m0*m0) + (p/(c*c)) )
    
    beta = v/c
    gamma = 1./np.sqrt(1 - ((v*v)/(c*c)))
    
    return beta, gamma