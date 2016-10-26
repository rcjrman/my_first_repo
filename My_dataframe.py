import pandas
import warnings

warnings.simplefilter("ignore") #runs off UserWarning: Boolean Series key will be reindexed to match DataFrame index

my_df = pandas.read_csv('My_output.csv')
my_df = my_df.fillna(-9999)
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
