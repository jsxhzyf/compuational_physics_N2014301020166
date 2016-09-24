x='1'
d={'1':'  '*1 ,'2':'    '*2,'3':'      '*3,'4':'        '*4,'5':'          '*4,'6':'            '*4,'7':'              '*4,'8':'                '*4}
import sys
import time
times=input('Please input the times you want the name to move horiziontally')
for y in range(times):
  for x in ['1','2','3','4','5','6','7','8']:
    print d[x],'#####   ##   ##   ######'
    print d[x],'   #      # #     #      '
    print d[x],'  #        #      ###### ' 
    print d[x],' #         #      #      '
    print d[x],'#####      #      #      '    
    print('\n')  
    time.sleep(0.3)    
  sys.stderr.write("\x1b[2J\x1b[H")
