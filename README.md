<h1> Peak-Traffic-Volume-PTV-Forecasting</h1>

<p>Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages’ traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (PTV) forecasting based on the ‘PTV’ for a shop in Taiwan during 2017. </p>

1.Files<br>

--&nbsp;requirement.txt&emsp;&emsp;# python libraries needed to run the code<br>
-- preprocessing.py	&emsp;&emsp;	# preprocessing <br>
-- features.py	&emsp;&emsp;# form all the possible features<br>

-- feature_selection.py &emsp;&emsp;	# select the most relevant features for regression model<br>

-- regression.py	&emsp;&emsp;# regression
-- reduced.pckl	&emsp;&emsp;# preprocessed data:corrected wrong data and combined data items. It is the output of preprocessing.py, and is the input to features.py
-- feature_all.pckl&emsp;&emsp;# all the possible features. It is the output of features.py, and is the input to feature_selection.py and regression.py
-- data/						# original dataset
	| -- PTV_TTV.csv			# recodes PTV in 2017
	| -- promotions.csv			# records for promoted items offered in the shop
	| -- vouchers.csv			# records for shop vouchers sent to users 
	
Instructions to run the file


