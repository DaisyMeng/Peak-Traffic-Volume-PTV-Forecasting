<h1>Peak Traffic Volume Forecasting</h1>
<p>Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages&rsquo; traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (PTV) forecasting based on the &lsquo;PTV&rsquo; for a shop in Taiwan during 2017.</p>
<div>
<h4><a id="user-content-1-files" class="anchor" href="https://github.com/DaisyMeng/Peak-Traffic-Volume-PTV-Forecasting/blob/master/README.md#1-files" aria-hidden="true"></a>1. Files</h4>
<p>-- Peak_Volume_Traffic_Forecasting_Report.pdf&nbsp;&nbsp;<span style="color: #808080;"># Detail steps and explaination for this solution</span><br />--&nbsp;preprocessing.py&nbsp;&nbsp;<span style="color: #808080;"># preprocessing&nbsp;</span><br />--&nbsp;features.py&nbsp;&nbsp;<span style="color: #808080;"># form all the possible features</span><br />--&nbsp;feature_selection.py&nbsp;&nbsp;<span style="color: #808080;"># select the most rel<a style="color: #808080;" href="https://camo.githubusercontent.com/c4d4a89e11aba00b4246317a934d33da7baf2d8f/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f30716a6c69746b6c3179326269376f2f72656772657373696f6e253230726573756c742e706e673f646c3d30" target="_blank" rel="noopener"><img src="https://camo.githubusercontent.com/c4d4a89e11aba00b4246317a934d33da7baf2d8f/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f30716a6c69746b6c3179326269376f2f72656772657373696f6e253230726573756c742e706e673f646c3d30" alt="" data-canonical-src="https://www.dropbox.com/s/0qjlitkl1y2bi7o/regression%20result.png?dl=0" /></a>evant features for regression model</span><br />--&nbsp;regression.py&nbsp;&nbsp;<span style="color: #808080;"># regression</span><br />--&nbsp;reduced.pckl&nbsp;&nbsp;<span style="color: #808080;"># preprocessed data:corrected wrong data and combined data items.&nbsp;</span><br />--&nbsp;feature_all.pckl <span style="color: #808080;"># all the possible features.</span>&nbsp;<br />--&nbsp;data/&nbsp;<br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;PTV_TTV.csv&nbsp;&nbsp;<span style="color: #808080;"># recodes PTV in 2017</span><br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;promotions.csv&nbsp;&nbsp;<span style="color: #808080;"># records for promoted items offered in the shop</span><br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;vouchers.csv&nbsp;&nbsp;<span style="color: #808080;"># records for shop vouchers sent to users</span></p>
<h4><a id="user-content-2-instructions-to-run-the-file" class="anchor" href="https://github.com/DaisyMeng/Peak-Traffic-Volume-PTV-Forecasting/blob/master/README.md#2-instructions-to-run-the-file" aria-hidden="true"></a>2. Instructions to run the file</h4>
<ul>
<li>requirements: sklearn,pickle,numpy,matplotlib,pandas,datetime</li>
<li>preprocessing:
<ul>
<li>run preprocessing.py: correct wrong data, and combine some items. (inputs are&nbsp;PTV_TTV.csv,&nbsp;promotions.csv,vouchers.csv. outputs is&nbsp;reduced.pckl)</li>
<li>run features.py: find all the possible features. (input is reduced.pckl. output is feature_all.pckl)</li>
<li>feature_selection: find the features for regression</li>
</ul>
</li>
<li>regression: run regression.py. (input is feature_all.pckl)</li>
</ul>
<h4><a id="user-content-3-model-descriptions" class="anchor" href="https://github.com/DaisyMeng/Peak-Traffic-Volume-PTV-Forecasting/blob/master/README.md#3-model-descriptions" aria-hidden="true"></a>3. Model Descriptions</h4>
<ol>
<li>Preprocessing
<ul>
<li>promotions.csv: reset nagetive discount percent to zero.</li>
<li>voucher.csv: if 'end_time'&lt;'start_time', delete the item</li>
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
<li>Linear Regressor-- trend prediction</li>
<li>Extra-Tree Regressor and&nbsp;Polynomial Regressor -- detrended PTV prediction</li>
</ul>
</li>
</ol>
<h4>4. Result</h4>
<p>With 10-fold cross validation, the following figure shows the predicted 'PTV' and the true 'PTV'. The mean squared error of the prediction is 3.98e7</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://github.com/DaisyMeng/Peak-Traffic-Volume-PTV-Forecasting/blob/master/image/regression%20result.png" width="Infinity" /></p>
</div>
