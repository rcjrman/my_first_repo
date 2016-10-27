import pandas	#Used to import into dataframe
import warnings	#Using this to turn off warnings
import glob		#Use Unix shell rules to find file names matching a pattern.
import os

warnings.simplefilter("ignore") #runs off UserWarning: Boolean Series key will be reindexed to match DataFrame index

####################################################################################
# Look through a directory and save all the csv files in a list
path = 'C:/Users/rafael.colon/Desktop/Data/AX84/CFAR/CFAR 40076977/'
my_file = glob.glob(path + 'Format*.csv')	
####################################################################################

for entry in my_file:
	################################################################################
	#Have a problem with the path that's used in my_file.  Has / and \.  This 
	#messes up pandas read_csv.  So I strip the file name and manually add it 
	#back with the path to fix this.  I don't understand it or have the time 
	#to figure it out. 
	################################################################################
	
	file_name = entry[len(path):] 	#strip the path 
	my_path = path + file_name		#add the path back with proper formatting.
	
	print '-----------------------------------------------'
	print file_name
	print '-----------------------------------------------'
	
	my_df = pandas.read_csv(my_path)
	my_df = my_df.fillna(-9999)		#fill all empty spaces with -9999

	#Filter for the die we're looking for.
	
	a = my_df[['DIE_X','DIE_Y']]\
		[my_df['ICGM code  '] == 1]\
		[my_df['ZTC code  '] == 0]\
		[my_df['VREF code  '] == 1]\
		[my_df['OSC CLK code  '] == 0]\
		[my_df['AMP OSC code  '] == 0]\
		[my_df['AMP1 Vos  '] == 6]\
		[my_df['AMP2 Vos  '] == 2]\
		[my_df['IV_Xtalk R  '] == 18]\
		[my_df['IV Xtalk F  '] == 16]\
		[my_df['IV V Distortion  '] == 0]\
		[my_df['IV I Distortion  '] == 18]\
		[my_df['V offset  '] == 19]\
		[my_df['I offset  '] == 133]\
		[my_df['V gain  '] == 51]\
		[my_df['I gain C  '] == 1]\
		[my_df['I gain F  '] == 31]\
		[my_df['Program Rev ID  '] == 0]\
		[my_df['Spare  '] == 0]\
		[my_df['Bst 1  '] == 55]\
		[my_df['Bst Vout  '] == 3]\
		[my_df['Bst Osc  '] == 19]\
		[my_df['Bst Bias  '] == 6]\
		[my_df['Bst Trim 5  '] == 3]\
		[my_df['SAR  '] == 43]

	print a
	print '****************** END ************************'
	print ""