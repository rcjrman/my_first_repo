import csv  #Use to import csv files
import glob	#Use Unix shell rules to find file names matching a pattern.
import Tkinter as Tk
import tkFileDialog

####################################################################################
# This takes a CSV file that's been converted from an STDF file and formats it into
# a table.  It does this by stripping out the leading header information and leaving
# behind only the test headings and data.
####################################################################################

def browse_file():

	root = Tk.Tk()
	#fname = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
	fname = tkFileDialog.askdirectory()
	return fname
	
####################################################################################
# Look through a directory and save all the csv files in a list
path = browse_file()
path += '/'
my_file = glob.glob(path + '*.csv')	
####################################################################################
	
for entry in my_file:
	
	with open(entry, 'rb') as f_in:
	
		reader_in = csv.reader(f_in, skipinitialspace = True) #skipinitialspace makes sure it imports number only.  Otherwise can import as a string.
		
		output_file = 'Formatted_'+entry[len(path):] #strip the path and rename the file with 'Formatted_' 
		
		with open(path + output_file, 'wb') as f_out:		
			writer_in = csv.writer(f_out)
			insertion_index = 0								#set the insertion to zero at start of file
			test_time = 0									#set the test time to zero at start of file
			for row in reader_in:				
				if len(row) != 0: 							#check if it's an empty line
					if row[0] == 'Parameter':				#if it's the header row 
						row.append('INSERTION')				#add column for insertion
						writer_in.writerows([row])			#need [] otherwise it prints by character.	
					
					if row[0][:3] == 'PID':
						if insertion_index == 0:			#indicates start of file
							insertion_index += 1			#increase it to first insertion.
							row.append(insertion_index)		#add the insertion to this row.
							test_time = row[6]				#assign test to start the indexing
						
						elif row[6] == test_time:			#see if new row has same test time (same insertion)
							row.append(insertion_index)		#add insertion index
						else:
							insertion_index += 1			#increase insertion index
							row.append(insertion_index)		#add insertion index
							test_time = row[6]				#assign test to start the indexing
							
						writer_in.writerows([row])			#need [] otherwise it prints by character.			
		f_out.closed
	f_in.closed

