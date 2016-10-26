import csv
import glob

#bogus edit to experiment with github
my_path = 'c:/Users/rafael.colon/Desktop/Data/Python/My_input.csv'
with open(my_path, 'rb') as f_in:
	# don't seem to need the delimiter = ',', but still separates characters in output file
	reader_in = csv.reader(f_in, skipinitialspace = True) #skipinitialspace makes sure it inports number only.  Otherwise can import as a string.
	
	#for i in xrange(71):
	#	reader_in.next()
	with open('My_output.csv', 'wb') as f_out:		
		writer_in = csv.writer(f_out)
		for row in reader_in:
			#print row
			if len(row) != 0: #check if it's an empty line
				if row[0][:3] == 'PID' or row[0] == 'Parameter':
					writer_in.writerows([row])			#need [] otherwise it prints by character.			
	f_out.closed
f_in.closed


'''
import glob
for filename in glob.glob('*.csv'):
	#do something
'''

'''for row in reader:
    for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = 0
                print x
'''				