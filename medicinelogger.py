import time,os

file = 'C:\\Users\\Timothy\\Desktop\\medicine_log.txt'
medhistory = []
def write(st):
    mode='w+'
    if os.path.isfile: mode='a+'
    with open(file,mode) as f:
        f.write(st+'\n')
def gethour():
    return(int(time.strftime('%H')))
def readandprintfile():
    global medhistory
    if not os.path.isfile(file):
        print('will create new medicine log \n')
        return()
    with open(file,'r') as f:
        medhistory=f.read()
        print(medhistory)



medschedule = {
    'proprananol':  (0,24),
    'escitalopram': (7,16),
    'hydroxizine':  (20,4)
    }

defaultmedicine = None

for i,c in medschedule.items():
    hr=gethour()
    
    if hr > c[0] or hr < c[1]:
        defaultmedicine=i

readandprintfile()

#if last med taken was one hydroxizine, next med will be hydroxizine x2
medhistory=medhistory.split('\n')
print('last med,',medhistory[-2].split(' ')[0],'\n')
if medhistory[-2].split(' ')[0] == 'hydroxizine' and medhistory[-2].split(' ')[1] != 'x2':
    defaultmedicine='hydroxizine x2'


print('default medicine: ',defaultmedicine)
medicine=defaultmedicine
i = input('enter name of medicine to log, enter nothing for default: ')

if len(i) > 2:
    medicine=i

logtext=medicine + ' ' + time.asctime()
write(logtext)
print('\n'+logtext)
