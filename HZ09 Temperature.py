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
	#Go through all the files looking for ADC_Temp_Post = -29 (returned 0)
	##########################################################################################
	if len(my_df.columns) > 600:
		c = my_df[['DIE_X', 'DIE_Y']][my_df['ADC_Temp_Post  ']==-29]
	
		if len(c) != 0:
			print '-----------------------------------------------'
			print file_name
			print '-----------------------------------------------'
			print c
			print ''
	
print '/**********************************************/'
print '/**************** Complete ********************/'
print '/**********************************************/'