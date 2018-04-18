<p>&nbsp;</p>
<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
<h1 class="vicinity rich-diff-level-zero">Peak Traffic Volume Forecasting</h1>
<p class="vicinity rich-diff-level-zero">Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages&rsquo; traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (PTV) forecasting based on the &lsquo;PTV&rsquo; for a shop in Taiwan during 2017.</p>
<div class="expandable unchanged js-expandable rich-diff-level-zero">
<h4 class="unchanged rich-diff-level-one">1. Files</h4>
<p class="unchanged rich-diff-level-one">-- Peak_Volume_Traffic_Forecasting_Report.pdf&nbsp; # Detail steps and explaination for this solution<br />--&nbsp;preprocessing.py&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# preprocessing&nbsp;<br />--&nbsp;features.py&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # form all the possible features<br />--&nbsp;feature_selection.py &emsp;&emsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# select the most rel<img src="https://www.dropbox.com/s/0qjlitkl1y2bi7o/regression%20result.png?dl=0" alt="" />evant features for regression model<br />--&nbsp;regression.py &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# regression<br />--&nbsp;reduced.pckl &nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# preprocessed data:corrected wrong data and combined data items.&nbsp;<br />--&nbsp;feature_all.pckl&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# all the possible features.&nbsp;<br />--&nbsp;data/ <br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;PTV_TTV.csv&nbsp;&nbsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # recodes PTV in 2017<br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;promotions.csv&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # records for promoted items offered in the shop<br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;vouchers.csv&nbsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # records for shop vouchers sent to users</p>
<h4 class="unchanged rich-diff-level-one">2. Instructions to run the file</h4>
<ul>
<li>requirements:sklearn,pickle,numpy,matplotlib,pandas,datetime</li>
<li>preprocessing:
<ul>
<li>run preprocessing.py: correct wrong data, and combine some items. (inputs are&nbsp;PTV_TTV.csv,&nbsp;promotions.csv,vouchers.csv. outputs is&nbsp;reduced.pckl)</li>
<li>run features.py: find all the possible features. (input is reduced.pckl. output is feature_all.pckl)</li>
<li>feature_selection: find the features for regression</li>
</ul>
</li>
<li>regression: run regression.py. (input is feature_all.pckl)</li>
</ul>
<h4>3. Model Descriptions</h4>
<ol style="list-style-type: lower-alpha;">
<li>Preprocessing
<ul>
<li><span class="fontstyle0">promotions.csv: reset nagetive discount percent to zero.</span></li>
<li><span class="fontstyle0"> voucher.csv: if 'end_time'&lt;'start_time', delete the item<br /> </span></li>
</ul>
</li>
<li>feature selection
<ul>
<li>find all possible features including public holidays, sale season, day of the week, day of the month, number of promoted items,average promotion discount, average promotion price, average promotion rebate, number of vouchers, average voucher discount, average voucher value, average min price, etc.</li>
<li>10-fold cross validation to select the features</li>
</ul>
</li>
<li>regression model (10-fold cross validation to select parameters)
<ul>
<li><span class="fontstyle0">Linear Regressor</span><span class="fontstyle2">-- trend prediction</span></li>
<li><span class="fontstyle0">Extra-Tree Regressor and</span><span class="fontstyle3">&nbsp;</span><span class="fontstyle0">Polynomial Regressor -- detrended PTV prediction</span></li>
</ul>
</li>
</ol>
</div>
