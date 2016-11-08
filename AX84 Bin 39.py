import pandas	#Used to import into dataframe
import warnings	#Using this to turn off warnings
import glob		#Use Unix shell rules to find file names matching a pattern.
import Tkinter as Tk
import tkFileDialog

warnings.simplefilter("ignore") #Turns off UserWarning: Boolean Series key will be reindexed to match DataFrame index

def browse_file():

	root = Tk.Tk()
	#fname = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
	fname = tkFileDialog.askdirectory()
	return fname
	
####################################################################################
# Look through a directory and save all the csv files in a list
path = browse_file()
path += '/'
my_file = glob.glob(path + 'Format*.csv')	
####################################################################################


print '/**********************************************/'
print '/**************** Running *********************/'
print '/**********************************************/'
print ''

for entry in my_file:
	################################################################################
	#Have a problem with the path that's used in my_file.  Has / and \.  This 
	#messes up pandas read_csv.  So I strip the file name and manually add it 
	#back with the path to fix this.  I don't understand it or have the time 
	#to figure it out. 
	################################################################################
	
	file_name = entry[len(path):] 	#strip the path 
	my_path = path + file_name		#add the path back with proper formatting.
	
	my_df = pandas.read_csv(my_path)
	my_df = my_df.fillna(-9999)		#fill all empty spaces with -9999
	
	##########################################################################################
	#Go through all the files looking for SBIN = 39.  Check to see if the insertion
	#equals 8 if we had a bin 39.  This would imply that all 8 sites were testing at 
	#when the bin 39 occurred.  My theory is that bin 39 happens when we're testing 
	#less than 8 sites.  This initial screen will just check to see if 8 sites were 
	#running at the start of the test.  Ideally we'll need to see if a site failed 
	#before we got to the bin 39 test.  Makes sense to check the easy one first though
	#because if we don't get bin 39 with 8 sites activated then it supports our hypothesis.
	##########################################################################################
	
	#a = my_df.groupby([my_df['SBIN']==39, 'INSERTION'])['INSERTION'].count()
	
	#filter data on bin, x, y coordinates, count, insertion, and total tests beyond bin 39 failure #
	#b = a[['INSERTION', 'DIE_X', 'DIE_Y', 'INSERTION_COUNT','SBIN']][a['TOTAL_TESTS']>8]
	a = my_df[['INSERTION', 'DIE_X', 'DIE_Y','SBIN','TOTAL_TESTS']][my_df['TOTAL_TESTS']>357]
	
	#add a column that sums how many sites were active for each insertion.  Add this number to each insertion group
	#a = my_df.join(my_df.groupby('INSERTION')['INSERTION'].count(), on='INSERTION', rsuffix='_COUNT')
	b = a.join(a.groupby('INSERTION')['INSERTION'].count(), on='INSERTION', rsuffix='_COUNT')
	
	#filter on bin 39 and insertion count of 8
	c = b[['INSERTION', 'DIE_X', 'DIE_Y']][b['SBIN']==39][b['INSERTION_COUNT']==8]
	
	if len(c) > 0:
		print '-----------------------------------------------'
		print file_name
		print '-----------------------------------------------'
		print c
		print ''
'''	
	try:
		len(a[1])				#see if filter returned data
		print "Bin 39"
		for i in b:
			print counter, i
			if i == 8:
				print '-----------------------------------------------'
				print file_name
				print '-----------------------------------------------'
				print counter, i 
				print ''
			counter += 1
	except:
		print "No Bin 39"
'''
	
print '/**********************************************/'
print '/**************** Complete ********************/'
print '/**********************************************/'