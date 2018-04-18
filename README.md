<p>&nbsp;</p>
<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
<h1 class="vicinity rich-diff-level-zero">Peak Traffic Volume Forecasting</h1>
<p class="vicinity rich-diff-level-zero">Predicting traffic volume of shop webpages is important for providing a better online shopping experience, as webpages&rsquo; traffic volume may surge to an extremely high level during big promotion events. This project focuses on Peak Traffic Volume (PTV) forecasting based on the &lsquo;PTV&rsquo; for a shop in Taiwan during 2017.</p>
<div class="expandable unchanged js-expandable rich-diff-level-zero">
<h4 class="unchanged rich-diff-level-one">1.Files</h4>
<p class="unchanged rich-diff-level-one">--&nbsp;requirement.txt&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp; # python libraries needed to run the code<br />--&nbsp;preprocessing.py&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp; # preprocessing&nbsp;<br />--&nbsp;features.py&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; &nbsp; &nbsp; &nbsp;# form all the possible features<br />--&nbsp;feature_selection.py &emsp;&emsp;&emsp;# select the most relevant features for regression model<br />--&nbsp;regression.py &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; # regression<br />--&nbsp;reduced.pckl &nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; # preprocessed data:corrected wrong data and combined&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;data items.&nbsp;<br />--&nbsp;feature_all.pckl&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;# all the possible features.&nbsp;<br />--&nbsp;data/ <br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;PTV_TTV.csv&nbsp;&nbsp;&emsp;&nbsp; &nbsp; # recodes PTV in 2017<br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;promotions.csv&emsp;&nbsp; # records for promoted items offered in the shop<br />&emsp;&emsp;&nbsp; &nbsp; | --&nbsp;vouchers.csv&nbsp;&emsp;&nbsp; &nbsp; # records for shop vouchers sent to users</p>
<p class="unchanged rich-diff-level-one">-- report.pdf&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # Detail steps and&nbsp;</p>
<h4 class="unchanged rich-diff-level-one">2.Instructions to run the file</h4>
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
</div>