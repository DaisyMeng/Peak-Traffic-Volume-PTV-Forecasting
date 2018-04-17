# Peak-Traffic-Volume-PTV-Forecasting

<p>Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages’ traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (‘PTV’) forecasting based on the ‘PTV’ for a shop in Taiwan during 2017. </p>

Files
<pre>
-- requirement.txt    		# python libraries needed to run the code<br>
-- preprocessing.py		# preprocessing <br>
-- features.py			# form all the possible features<br>
-- feature_selection.py 	# select the most relevant features for regression model<br>
-- regression.py		# regression<br>
-- reduced.pckl			# preprocessed data:   corrected wrong data and combined data items. It is the output of preprocessing.py, and is the input to features.py<br>
-- feature_all.pckl		# all the possible features. It is the output of features.py, and is the input to 	feature_selection.py and regression.py<br>
-- data/ <br>
	| -- PTV_TTV.csv			# recodes PTV in 2017<br />
	| -- promotions.csv			# records for promoted items offered in the shop<br>
	| -- vouchers.csv			# records for shop vouchers sent to users <br>
</pre>

Instructions to run the file


