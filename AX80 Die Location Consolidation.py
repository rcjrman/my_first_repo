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
        print file_name
    
	my_path = path + file_name		#add the path back with proper formatting.
	
	my_df = pandas.read_csv(my_path)  
	my_df = my_df.fillna(-9999)		#fill all empty spaces with -9999
    
	#Filter for the die we're looking for.
	
	a = my_df[['DIE_X','DIE_Y']]\
		[my_df['IVFE_TEST_0_Readback'] == 0]\
		[my_df['TEST_BIAS_3_Readback'] == 8]\
		[my_df['TEST_OSC_TRIM_Readback'] == 126]\
		[my_df['TEST_SPK_2_Readback'] == 7]\
		[my_df['TEST_SPK_OFFSET_TRIM_Readback'] == 6]\
		[my_df['TEST_BOOST_1_Readback'] == 128]\
		[my_df['TEST_BOOST_2_Readback'] == 16]\
		[my_df['TEST_BOOST_3_Readback'] == 185]\
		[my_df['TEST_BOOST_4_Readback'] == 7]\
		[my_df['TEST_BOOST_5_Readback'] == 6]\
		[my_df['TEST_BOOST_6_Readback'] == 16]\
		[my_df['TEST_BOOST_7_Readback'] == 26]\
		[my_df['TEST_BOOST_9_Readback'] == 15]\
		[my_df['TEST_BOOST_10_Readback'] == 39]\
		[my_df['TEST_BIAS_ICGM_TRIM_Readback'] == 2]\
		[my_df['TEST_BIAS_BANDGAP_TRIM_Readback'] == 0]\
		[my_df['TEST_IV_FE_I_TRIMF_Readback'] == 2]\
		[my_df['TEST_IV_FE_I_TRIMC_Readback'] == 20]\
		[my_df['TEST_IV_FE_I_TRIM_Readback'] == 1]\
		[my_df['TEST_IVADC_XTALK_COEFFICIENT_OTP_Readback'] == 83]\
		[my_df['TEST_IVADC_TEMP_COEFFICIENT_A_OTP_Readback'] == 11]\
		[my_df['TEST_IVADC_TEMP_COEFFICIENT_B_OTP_Readback'] == 0]\
		[my_df['TEST_MEAS_ADC_GAIN_TRIM_Readback'] == 1]\
		[my_df['TEST_MEAS_ADC_OFFSET_TRIM_Readback'] == 0]\
		[my_df['TEST_MEAS_ADC_TEMP_TRIM_Readback'] == 2]\
		[my_df['X_COORDINATE_LSB_Readback'] == 98]\
		[my_df['X_COORDINATE_MSB_Readback'] == 1]\
		[my_df['Y_COORDINATE_LSB_Readback'] == 26]\
		[my_df['Y_COORDINATE_MSB_Readback'] == 0]\
		[my_df['WAFER_NUMBER_LSB_Readback'] == 4]\
		[my_df['WAFER_NUMBER_MSB_Readback'] == 0]\
		[my_df['PART_NUMBER_LSB_Readback'] == 28]\
		[my_df['PART_NUMBER_MSB_Readback'] == 0]
		
	if len(a) != 0:	
		print '-----------------------------------------------'
		print file_name
		print '-----------------------------------------------'
		print a
		print ''
		
print '/**********************************************/'
print '/**************** Complete ********************/'
print '/**********************************************/'