<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Pratima Paudel(pp235)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2022 4:02:22 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/pp235" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you&#39;re working in an up to date branch</p>
<ul>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b M4-Simple-Calc</code></li>
</ul>
<p>This will likely be started in class.</p>
<p>Steps:</p>
<ol>
<li>Create a new Folder called M4</li>
<li>Create a new file called MyCalc.py inside this folder</li>
<li>Create a MyCalc Class</li>
<li>Define basic addition / subtraction / multiplication / division functions<ol>
<li>These functions should update an internal variable as a running total/value called <code>ans</code></li>
<li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero)</li>
<li>Since you&#39;ll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li>
</ol>
</li>
<li>Define a &quot;main&quot; logic to run when the program runs</li>
<li>This logic should ask for user input<ol>
<li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol>
<li>This will do an immediate calculation, print it, and store the answer in the <code>ans</code> variable</li>
</ol>
</li>
<li>Alternatively, the input can be <code>ans</code>, any valid math operator, any valid number (i.e., <code>ans</code> * 2)<ol>
<li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the <code>ans</code> variable</li>
</ol>
</li>
</ol>
</li>
<li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass<ol>
<li>Test number-add-number</li>
<li>Test ans-add-number</li>
<li>Test number-sub-number</li>
<li>Test ans-sum-number</li>
<li>Test number-mult-number</li>
<li>Test ans-mult-number</li>
<li>Test number-div-number</li>
<li>Test ans-div-number</li>
</ol>
</li>
<li>Create a new file called m4_submission.md inside the M4 folder</li>
<li>Fill out the below deliverables</li>
<li>Generate the markdown and paste it into the m4_submission.md</li>
<li><code>git add .</code></li>
<li><code>git commit -m &quot;adding m4 hw&quot;</code></li>
<li><code>git push origin M4-Simple-Calc</code></li>
<li>Create a pull request M4-Simple-Calc to dev</li>
<li>Create a pull request dev to prod (after the previous one is merged)</li>
<li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li>
<li>Submit this link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862067-6c0581b0-38fe-42d8-a7f0-cb387e14e8f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the screenshot of add function with my ucid=pp235<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862154-abc01030-2c5e-4356-bf9b-a6897b9e529f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the screenshot of substruction function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862211-c191da95-9078-4126-99d7-6fda58df72a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of multiplication function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862270-5d1339dd-069c-4598-94a2-56e001fc8212.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of division function.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of passing number-add-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862644-fe54de5d-a05f-4209-842a-1aac216fb24c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the screen shot for test cases of addition.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of passing ans-add-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862753-0afacc62-e13e-4820-8556-19acabba0b98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the test cases  for addition cached from previous case with<br>passing answers.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of passing number-sub-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862882-a09b2947-3656-45ed-9e18-a1a997796f1f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the screenshot of test cases for subtraction.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of passing ans-sub-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154862944-6314b1fd-e782-4cad-848b-eebfd91f4438.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the test cases  for subtraction cached from previous case with<br>passing answers.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot of passing number-mult-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154863726-04325dda-b15a-47e8-911f-6188a1ce4f64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the screenshot of test cases for subtraction with multiple values.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot of passing ans-multi-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154863752-3ef04203-0d39-4282-a4ab-3ecd19572354.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the screenshot of test cases for multiplication with multiple values.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshot of passing number-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154863545-a0f7e43a-fe5c-4e16-9d5d-8d8f86ccd87b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the screenshot of test cases for division with multiple values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshot of passing ans-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/154863580-7ffd3ff1-eb53-4f58-9164-7599f5e9e5a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This the screenshot of test cases for division with multiple values with passing<br>answers<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I learned about different functions like add, subtraction, multiplication, and division and a<br>little bit learned how to build a calculator. <br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p> It checks for a specific response to a particular set of inputs.<br>In my homework, I test the codes for the calculator which was given<br>by Professor. I also learned that the process of writing a test case<br>can also help reveal errors or defects within the system. <br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/commit/b1b54dbe989e01f62e4fe490e536ecd2e9160e0a">https://github.com/githubPratima/webdev/commit/b1b54dbe989e01f62e4fe490e536ecd2e9160e0a</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/pp235" target="_blank">Grading</a></td></tr></table>