<h1> Peak-Traffic-Volume-PTV-Forecasting</h1>

<p>Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages’ traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (PTV) forecasting based on the ‘PTV’ for a shop in Taiwan during 2017. </p>

1.Files<br>

--&nbsp;requirement.txt&emsp;&emsp;&emsp;# python libraries needed to run the code<br>
--&nbsp;preprocessing.py&emsp;&emsp;&emsp;# preprocessing <br>
--&nbsp;features.py	&emsp;&emsp;&emsp;# form all the possible features<br>
--&nbsp;feature_selection.py &emsp;&emsp;&emsp;# select the most relevant features for regression model<br>
--&nbsp;regression.py	&emsp;&emsp;&emsp;# regression<br>
--&nbsp;reduced.pckl	&emsp;&emsp;&emsp;# preprocessed data:corrected wrong data and combined data items. <br>
--&nbsp;feature_all.pckl&emsp;&emsp;&emsp;# all the possible features. <br>
--&nbsp;data/	<br>					
&emsp;&emsp;| --&nbsp;PTV_TTV.csv&emsp;&emsp;&emsp;# recodes PTV in 2017<br>
&emsp;&emsp;| --&nbsp;promotions.csv&emsp;&emsp;&emsp;# records for promoted items offered in the shop<br>
&emsp;&emsp;| --&nbsp;vouchers.csv	&emsp;&emsp;&emsp;#  records for shop vouchers sent to users <br>
	
Instructions to run the file


