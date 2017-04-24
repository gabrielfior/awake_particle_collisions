import os
import pandas
import numpy
import datetime
import matplotlib.pyplot as plt

agenda = pandas.read_csv('/Users/gabrielfior/Downloads/Dados/odontoway_csv/tbagenda.csv',
                            header=0)
pac = pandas.read_csv('/Users/gabrielfior/Downloads/Dados/odontoway_csv/tbpaciente.csv',
                            header=0)
                            
#Find 10 most ocurrent
a = agenda.idpaciente.value_counts()

count=0
for i,j in a.iteritems():
    count+=1
    print i,j

    b = pac[pac.idPaciente==int(i)]
    print b.Nome + " " + b.Sobrenome
    if count>=10:
        break
    
#Get all visits of 1 patient
#patient 63
    
pat63 = agenda[agenda.idpaciente==63]
pat63['date1']=pandas.to_datetime(pat63.Data)
pat63 = pat63.sort_values(by='date1')


pat63['dA'] =  pat63['date1'].shift(-1) - pat63['date1']
pat63.dA=pat63.dA.fillna(1)
pat63.dA = pandas.to_timedelta(pat63.dA,unit='d').astype('timedelta64[D]')

f1 = plt.figure(2)
plt.title('Tempo entre consultas - paciente id 63 - A.C.K.M')
plt.xlabel('Dias')
plt.ylabel('# de ocorrencias')
pat63.dA.hist(bins=40)
plt.show()