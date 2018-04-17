<h1> Peak-Traffic-Volume-PTV-Forecasting</h1>

<p>Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages’ traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (PTV) forecasting based on the ‘PTV’ for a shop in Taiwan during 2017. </p>

1.Files<br>

--&nbsp;requirement.txt&emsp;&emsp;# python libraries needed to run the code<br>
--&nbsp;preprocessing.py	&emsp;&emsp;	# preprocessing <br>
--&nbsp;features.py	&emsp;&emsp;# form all the possible features<br>
--&nbsp;feature_selection.py &emsp;&emsp;	# select the most relevant features for regression model<br>
--&nbsp;regression.py	&emsp;&emsp;# regression<br>
--&nbsp;reduced.pckl	&emsp;&emsp;# preprocessed data:corrected wrong data and combined data items. It is the output of preprocessing.py, and is the input to features.py<br>
--&nbsp;feature_all.pckl&emsp;&emsp;# all the possible features. It is the output of features.py, and is the input to feature_selection.py and regression.py<br>
--&nbsp;data/	<br>					
	| --&nbsp;PTV_TTV.csv&emsp;&emsp;# recodes PTV in 2017<br>
	| --&nbsp;promotions.csv&emsp;&emsp;# records for promoted items offered in the shop<br>
	| --&nbsp;vouchers.csv	&emsp;&emsp;#  records for shop vouchers sent to users <br>
	
Instructions to run the file


