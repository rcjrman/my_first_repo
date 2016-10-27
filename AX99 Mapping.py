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

	#Filter for the die we're looking for.
	
	a = my_df[['DIE_X','DIE_Y']]\
		[my_df['PTAT_Code  '] == 31]\
		[my_df['GM_Code  '] == 1]\
		[my_df['SD_Code  '] == 3]\
		[my_df['ZTC_Code  '] == 31]\
		[my_df['BG_Code  '] == 54]\
		[my_df['BST_Gain_Code  '] == 0]\
		[my_df['BST_VOS_Code  '] == 0]\
		[my_df['BAT_Gain_Code  '] == 0]\
		[my_df['BAT_VOS_Code  '] == 0]\
		[my_df['OSC_Code  '] == 0]\
		[my_df['I_Gain_Coarse_Code  '] == 20]\
		[my_df['I_Gain_Fine_Code  '] == 30]\
		[my_df['V_REF_Code  '] == 5]\
		[my_df['IV_Correct_Code  '] == 0]\
		[my_df['V_THD_Code  '] == 0]\
		[my_df['I_THD_Code  '] == 19]\
		[my_df['Spkr_VOS_Code  '] == 1]\
		[my_df['IV_Half_I_Code  '] == 0]\
		[my_df['BCNTIV_Code  '] == 0]\
		[my_df['VOS_D_Code  '] == 4]\
		[my_df['IV_XtalkCoarse_Code  '] == 0]\
		[my_df['IV_XtalkFine_Code  '] == 19]\
		[my_df['BOOST_ZC_Code  '] == 0]\
		[my_df['BOOST_REF_Code  '] == 1]\
		[my_df['Ilim_Gain_Code  '] == 3]\
		[my_df['PreampOffsetAnalogMode  '] == 36]\
		[my_df['Ilim_Offset_Code  '] == 60]\
		[my_df['ALCEN_Option  '] == 1]\
		[my_df['REV_ID_ILIM_Code  '] == 0]

	if len(a) != 0:	
		print '-----------------------------------------------'
		print file_name
		print '-----------------------------------------------'
		print a
		print ''
		
print '/**********************************************/'
print '/**************** Complete ********************/'
print '/**********************************************/'