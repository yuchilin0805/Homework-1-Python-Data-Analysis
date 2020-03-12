# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107033134.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
      #print(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.



answer=[]
target_data=[]
def findmax(id_num):
   biggest=-9999
   for point in data:
      if point['station_id']==id_num:
         floatdata=float(point['TEMP'])
         if floatdata>biggest:
            biggest=floatdata
   return biggest

def putanswer(ss):
   sec=findmax(ss)
   if sec==-99 or sec==-999:
      answer=[ss,'None']
   else: 
      answer=[ss,findmax(ss)]
   target_data.append(answer)

putanswer('C0A880')
putanswer('C0F9A0')
putanswer('C0G640')
putanswer('C0R190')
putanswer('C0X260')


#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)

#========================================