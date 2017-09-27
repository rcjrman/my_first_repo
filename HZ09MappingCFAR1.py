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
		[my_df['IVFE_TEST_0_Readback  -1 <> IVFE_TEST_0_Readback'] == 1]\
		[my_df['DAC_Test_1_Readback  -1 <> DAC_Test_1_Readback'] == 8]\
		[my_df['TEST_BIAS_0_Readback  -1 <> TEST_BIAS_0_Readback'] == 0]\
		[my_df['TEST_OSC_TRIM_Readback  -1 <> TEST_OSC_TRIM_Readback'] == 5]\
		[my_df['TEST_SPK_2_Readback  -1 <> TEST_SPK_2_Readback'] == 39]\
		[my_df['TEST_SPK_OFFSET_TRIM_Readback  -1 <> TEST_SPK_OFFSET_TRIM_Readback'] == 17]\
		[my_df['TEST_BOOST_1_Readback  -1 <> TEST_BOOST_1_Readback'] == 0]\
		[my_df['TEST_BOOST_2_Readback  -1 <> TEST_BOOST_2_Readback'] == 17]\
		[my_df['TEST_BOOST_3_Readback  -1 <> TEST_BOOST_3_Readback'] == 131]\
		[my_df['TEST_BOOST_4_Readback  -1 <> TEST_BOOST_4_Readback'] == 127]\
		[my_df['TEST_BOOST_5_Readback  -1 <> TEST_BOOST_5_Readback'] == 0]\
		[my_df['TEST_BOOST_6_Readback  -1 <> TEST_BOOST_6_Readback'] == 10]\
		[my_df['TEST_BOOST_7_Readback  -1 <> TEST_BOOST_7_Readback'] == 0]\
		[my_df['TEST_BOOST_9_Readback  -1 <> TEST_BOOST_9_Readback'] == 204]\
		[my_df['TEST_BOOST_10_Readback  -1 <> TEST_BOOST_10_Readback'] == 32]\
		[my_df['TEST_BIAS_ICGM_TRIM_Readback  -1 <> TEST_BIAS_ICGM_TRIM_Readback'] == 0]\
		[my_df['TEST_BIAS_BANDGAP_TRIM_Readback  -1 <> TEST_BIAS_BANDGAP_TRIM_Readback'] == 63]\
		[my_df['TEST_IV_FE_I_TRIMF_Readback  -1 <> TEST_IV_FE_I_TRIMF_Readback'] == 3]\
		[my_df['TEST_IV_FE_I_TRIMC_Readback  -1 <> TEST_IV_FE_I_TRIMC_Readback'] == 18]\
		[my_df['TEST_IV_FE_I_TRIM_Readback  -1 <> TEST_IV_FE_I_TRIM_Readback'] == 1]\
		[my_df['TEST_IVADC_XTALK_COEFFICIENT_OTP_Readback  -1 <> TEST_IVADC_XTALK_COEFFICIENT_OTP_Readback'] == 2]\
		[my_df['TEST_IVADC_TEMP_COEFFICIENT_A_OTP_Readback  -1 <> TEST_IVADC_TEMP_COEFFICIENT_A_OTP_Readback'] == 15]\
		[my_df['TEST_IVADC_TEMP_COEFFICIENT_B_OTP_Readback  -1 <> TEST_IVADC_TEMP_COEFFICIENT_B_OTP_Readback'] == 0]\
		[my_df['TEST_MEAS_ADC_GAIN_TRIM_Readback  -1 <> TEST_MEAS_ADC_GAIN_TRIM_Readback'] == 1]\
		[my_df['TEST_MEAS_ADC_OFFSET_TRIM_Readback  -1 <> TEST_MEAS_ADC_OFFSET_TRIM_Readback'] == 14]\
		[my_df['TEST_MEAS_ADC_TEMP_TRIM_Readback  -1 <> TEST_MEAS_ADC_TEMP_TRIM_Readback'] == 12]\
		[my_df['X_COORDINATE_LSB_Readback  -1 <> X_COORDINATE_LSB_Readback'] == 0]\
		[my_df['X_COORDINATE_MSB_Readback  -1 <> X_COORDINATE_MSB_Readback'] == 0]\
		[my_df['Y_COORDINATE_LSB_Readback  -1 <> Y_COORDINATE_LSB_Readback'] == 0]\
		[my_df['Y_COORDINATE_MSB_Readback  -1 <> Y_COORDINATE_MSB_Readback'] == 0]\
		[my_df['WAFER_NUMBER_LSB_Readback  -1 <> WAFER_NUMBER_LSB_Readback'] == 0]\
		[my_df['WAFER_NUMBER_MSB_Readback  -1 <> WAFER_NUMBER_MSB_Readback'] == 0]\
		[my_df['PART_NUMBER_LSB_Readback  -1 <> PART_NUMBER_LSB_Readback'] == 23]\
		[my_df['PART_NUMBER_MSB_Readback  -1 <> PART_NUMBER_MSB_Readback'] == 0]
		
	if len(a) != 0:	
		print '-----------------------------------------------'
		print file_name
		print '-----------------------------------------------'
		print a
		print ''
		
print '/**********************************************/'
print '/**************** Complete ********************/'
print '/**********************************************/'