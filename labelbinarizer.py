# code to create the dataset 

# importing the libraries 
import pandas as pd 

# creating the dictionary 
dictionary = {'OUTLOOK': ['Rainy', 'Rainy', 
						'Overcast', 'Sunny', 
						'Sunny', 'Sunny', 
						'Overcast', 'Rainy', 
						'Rainy', 'Sunny', 
						'Rainy', 'Overcast', 
						'Overcast', 'Sunny'], 
			'TEMPERATURE': ['Hot', 'Hot', 'Hot', 
							'Mild', 'Cool', 
							'Cool', 'Cool', 
							'Mild', 'Cool', 
							'Mild', 'Mild', 
							'Mild', 'Hot', 'Mild'], 
			'HUMIDITY': ['High', 'High', 'High', 
						'High', 'Normal', 'Normal', 
						'Normal', 'High', 'Normal', 
						'Normal', 'Normal', 'High', 
						'Normal', 'High'], 
			'WINDY': ['No', 'Yes', 'No', 'No', 'No', 
						'Yes', 'Yes', 'No', 'No', 
						'No', 'Yes', 'Yes', 'No', 
						'Yes']} 

# converting the dictionary to DataFrame 
df = pd.DataFrame(dictionary) 

display(df) 

# importing the libraries 
from sklearn.preprocessing import LabelBinarizer 

# creating a copy of the 
# original data frame 
df1 = df.copy() 

# creating an object 
# of the LabelBinarizer 
label_binarizer = LabelBinarizer() 

# fitting the column 
# TEMPERATURE to LabelBinarizer 
label_binarizer_output = label_binarizer.fit_transform( df1['TEMPERATURE']) 

# creating a data frame from the object 
result_df = pd.DataFrame(label_binarizer_output, 
						columns = label_binarizer.classes_) 

display(result_df) 
