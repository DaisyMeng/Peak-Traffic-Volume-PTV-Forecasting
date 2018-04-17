# Peak-Traffic-Volume-PTV-Forecasting

Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages’ traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (‘PTV’) forecasting based on the ‘PTV’ for a shop in Taiwan during 2017. 

Files
-- requirement.txt 				# python libraries needed to run the code
-- preprocessing.py				# preprocessing 
-- features.py					# form all the possible features
-- feature_selection.py			# select the most relevant features for regression model
-- regression.py				# regression
-- reduced.pckl					# preprocessed data: corrected wrong data and combined data items. It is the output of preprocessing.py, and is the input to features.py
-- feature_all.pckl				# all the possible features. It is the output of features.py, and is the input to feature_selection.py and regression.py
-- data/						# original dataset
	| -- PTV_TTV.csv			# recodes PTV in 2017
	| -- promotions.csv			# records for promoted items offered in the shop
	| -- vouchers.csv			# records for shop vouchers sent to users 
	
Instructions to run the file


