<table><tr><td> <em>Assignment: </em> Mini Project 2_Advanced Calculator</td></tr>
<tr><td> <em>Student: </em> Pratima Paudel(pp235)</td></tr>
<tr><td> <em>Generated: </em> 3/17/2022 5:34:00 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/pp235" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Prepare your workspace</p>
<ol>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b MP2-AdvCalc</code></li>
</ol>
<p>In this project, you&#39;ll decorate or extend one of the given MyCalc samples (do not edit MyCalc directly).
For every added calculation you&#39;ll need to provide a positive and negative test case.
<strong>Note:</strong> negative test cases will throw and capture exceptions to generate a positive test case
Negative test cases test for invalid input and/or invalid operations. These test cases will be via csv files as well 
(just like the changes to addition, subtraction, multiplication, division, square, and square root)</p>
<p>HINT 1: You can generate a normal distribution of random distribution of numbers with excel to use for your data:  Here (<a href="http://howtoexcel.org/statistics/normal-distribution/">http://howtoexcel.org/statistics/normal-distribution/</a>)</p>
<p>HINT 2: You can create another excel file that contains the answers to your calculations that you can use in your unit tests.</p>
<p><strong>Your program needs to additionally calculate the following:</strong></p>
<ol>
<li>Square</li>
<li>Square Root</li>
<li>Pick 5 from below<ul>
<li>Population Mean</li>
<li>Median</li>
<li>Mode</li>
<li>Population Standard Deviation</li>
<li>Variance of population proportion</li>
<li>Z-Score</li>
<li>Standardized score</li>
<li>Population Correlation Coefficient</li>
<li>Confidence Interval</li>
<li>Population Variance</li>
<li>P Value</li>
<li>Proportion</li>
<li>Sample Mean</li>
<li>Sample Standard Deviation</li>
<li>Variance of sample proportion</li>
</ul>
</li>
</ol>
<ul>
<li>You&#39;ll update your previous test cases to read from csv files for the input and output values.</li>
<li>Use the below csv files for your existing test cases of addition, subtraction, multiplication, and division.
As well as testing the new square and square root modifications.</li>
</ul>
<p><strong>Note</strong>: You may need to view the data via the &quot;Raw&quot; button on the gist.
<a href="https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe">https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe</a> </p>
<p>Once done do the following:</p>
<ol>
<li>Git add all changes (including the test case csv files)</li>
<li>Git commit with relevant messages</li>
<li>Git push origin MP2-AdvCalc</li>
<li>Create a Pull Request on Github to dev (keep it open)</li>
<li>Fill out the details here</li>
<li>Save and Generate the markdown (any changes require this step to be repeated)</li>
<li>Paste the content into a <code>mp2_submission.md</code> file</li>
<li>Git add/commit/push the submission file change</li>
<li>Complete the pull request merge</li>
<li>Create a new pull request from dev to prod and complete it</li>
<li>Navigate to prod branch&#39;s <code>mp2_submission.md</code> file and paste the direct link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Added Functionality: Square </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158062023-ab7845b3-8526-41fb-b5cb-70747995066d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of square function.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158062801-fc0ff0a0-d340-4a34-8e6d-6e13012cb7ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of output of square in terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158062433-50b34137-cbe0-41f3-9011-b1798a594417.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of testing the square.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158062987-00524856-1921-4b7b-884c-52dfd711f274.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the additional screen of passed results.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Added Functionality: Square Root </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158063277-7e392f51-6fe9-43b8-8712-a7e06734f166.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of square root functionality.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158063323-4295b6cf-05bc-4253-b62b-c213e3f2bf69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of output of square root in terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158063387-b2b5932a-5130-4721-adef-b75ae03da343.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of testing the square root.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158063890-204093cb-e422-42a0-a0d7-608d1784daec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the additional screen of passed results.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Choice 1 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>I choose sample mean and its syntax name is smean in my codes.<br>It is an average of a set of data. The sample mean can<br>be used to calculate the central tendency.<br>Also, the sample mean is used while<br>calculating the standard deviation and the variance of a data set. <br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158064194-49252e2c-c28d-48e0-b5df-b8e5ff500cdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of sample mean functionality.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158064263-b974a13e-6227-4774-9383-6fe8c466419a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of output of sample mean pycharm terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158064649-8fb237ba-8187-4629-abf6-3c4abbeb36fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is for both positive and negative codes.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158064803-5c5fe20a-8239-4e40-a292-ff05a2205832.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passed result for testing positive test of smean.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158064918-1bf821a2-8465-4ff1-920b-d0eb8b5394ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>codes for combined test case.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158065004-42418355-27a4-4006-8004-0058bead8c4c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Its passed test cases  for both where negative is also included. <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Choice 2 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p> The median value is the number that is in the middle, with<br>the same amount of numbers below and above. The purpose of median in<br>math is to give us an idea of where the center value is<br>located in a dataset.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158065316-b3e0e4ce-c2b5-4108-ba96-755c3a2b6e58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screen shot of median function. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158065405-a9b14175-e660-4f9a-af64-83ac338fc790.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of output of median in pycharm terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158068932-12aba18e-b6ae-4e84-af05-758db79ba440.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the codes for both.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158069054-f6f2d785-d8db-4c8d-88f1-0e0d0fd08e17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>execution of test passing positive result.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158069077-be352284-fcc8-4a50-aa72-34a469a63a3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>codes for negative as well as positive included.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158069130-543f79fe-049b-42c4-914e-600e20d08073.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing negative test execution<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Choice 3 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Standard deviation is a statistical measurement that looks at how far a group<br>of numbers is from the mean. The purpose of standard deviation is it<br>tells us how spread out the data is. In my codes, i am<br>using sstd_dev as the syntax.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158066458-def2d207-7ed1-499d-b063-e2e4fbbc85c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screen shot of standard deviation codes.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158066564-d790e5bf-3d53-4769-99b6-2a9f337ea079.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of output of standard deviation in pycharm terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158066763-0da89101-7e6c-4fe8-91f9-438257c165fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Included both codes but name  is given in test files.  #<br>i did this because i used method 1 where both positive test and<br>negative test cases code is written in same function.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158066913-ef74d4d4-ff14-44b6-9cb2-fd97befa8fab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>result in terminal passing positive test case for standard deviation.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158066763-0da89101-7e6c-4fe8-91f9-438257c165fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>codes for negative  test cases also included positve,<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158066947-b54b1c3a-8795-45dd-8333-f01bfee90d3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>result of passing negative test cases including positive also.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Choice 4 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p> I am choosing the sample variance and its syntax in my codes<br>is svariance. The sample variance measures the degree to which the numbers in<br>a list are spread out.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158067277-dc11979f-3ecf-462c-82b2-bb2640b491b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot for the codes of sample variance.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158067347-d70d3f0d-c2fe-41d0-806e-3ef8bf683850.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of output of sample variance in pycharm terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158069397-2a407994-ceec-4c49-b8b7-717e2fd21ea8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screen shot of codes included both.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158069481-5a015de2-b8df-4979-a19b-799f6229a884.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screen shot of passed positive test cases excution <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158069546-5ea9809d-dc91-4135-8beb-f906d59422c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The codes for both.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158069578-c720fa10-cfc5-40c1-a476-55a717c7a5d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The passing testing result of negative test cases as well as positive.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Choice 5 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Now I choose the mode. It is used to find out the value<br>that appears most frequently in a data set. Also, A set of data<br>may have one mode, more than one mode, or no mode at all.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158068209-e996e9d8-7be1-4937-9ffc-624f923bc657.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot for mode.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158068244-28c01c2c-e3d2-44cb-b6cb-6cefbcc73a8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>result for one mode in pycharm terminal.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158068292-a6016c1c-6a51-4e95-b1e4-b44adc63ff6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>result of two mode in pycharm terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158070824-690be4eb-a9e8-4004-863d-575b029cc58c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>postive test cases passing result.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158070994-a38000af-a7a4-4359-992b-95e4518abb74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>codes for both <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158071039-802307e9-238c-453d-a893-c3f158b0b9d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing result of negative test cases included positve also.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/158070994-a38000af-a7a4-4359-992b-95e4518abb74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>codes for both<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Mention any difficulties and how you overcame them or what you learned during this mini project.</td></tr>
<tr><td> <em>Response:</em> <p>I faced a lot of difficulties while doing this project since I am<br>new to coding. Also, the mode was quite confusing. Professor helped me a<br>lot and also I searched codes from the internet.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Pull Request Link(s) for this project</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/26">https://github.com/githubPratima/webdev/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/pp235" target="_blank">Grading</a></td></tr></table>