<table><tr><td> <em>Assignment: </em> Mini Project 3 - Flask AdvCalc</td></tr>
<tr><td> <em>Student: </em> Pratima Paudel(pp235)</td></tr>
<tr><td> <em>Generated: </em> 5/2/2022 11:05:29 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/pp235" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Create a new branch called MP3-Flask-AdvCalc</li>
<li>Add the ability to load a basic csv file of mixed sets of data/equations for add/sub/div/mult</li>
<li>Add UI support for your 5 stats functions from MP2 (buttons on the screen that trigger the equation) The user should be able to enter data and run each of your stats functions as expected</li>
<li>Add the ability to load an advanced csv file of fixed data/equations for the 5 stats functions (or load in 5 different files separately)</li>
<li>Give the ability for the user to delete a single history item of theirs</li>
<li>Give the ability for the user to delete all of their history (this should not affect any other user&#39;s history)</li>
<li>Add test cases to <ol>
<li>Register a user</li>
<li>Login the user</li>
<li>To run a calc function for the user and record/create a SimpleHistory (verify this gets created with proper data)</li>
<li>Make sure the User and SimpleHistory data get deleted after the test phase</li>
</ol>
</li>
<li>Fill in the below deliverables (make sure screenshots load properly)</li>
<li>Create an mp3_submission.md file in your project/app folder</li>
<li>Paste the generated markdown into this file</li>
<li>git add/commit/push to MP3-Flask-AdvCalc</li>
<li>Merge to dev</li>
<li>Merge dev to prod</li>
<li>Find the mp3_submission.md in the prod branch on github</li>
<li>Submit the direct link to that file to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Basic CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the mixed csv data of add/sub/mult/div</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166346317-0a2d5757-e594-4282-9958-fbed2b2a0bcd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the csv file for add/sub/mult/div<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the history after uploading the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166346463-67b69f45-831d-459b-893f-d57dc8616435.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><img src="https://user-images.githubusercontent.com/98135375/166386514-cb926739-1f2f-4332-b94d-f10b2771e416.png" alt="image"><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166346521-8ba46cdf-22ad-4277-afaa-8c06a332419a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the codes for uploading the csv file. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the csv is processed and the data is sent to the calculator</td></tr>
<tr><td> <em>Response:</em> <p>In calc folder(views.py) a decorator called my calc.route is created with upload_csv function.<br>This route is working for uploading the CSV, the first file is uploaded<br>if it works it is printed the uploaded file passes information to work<br>in the original working MyCalc.py and gives the result. <br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Adv Calc Functions </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the new Advanced buttons on the UI</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166389786-effb6b85-7fbd-4574-81ea-85de45d61ab5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot of advanced buttton with mean, median, mode, standard deviation, variation<br></p>
</td></tr>
<tr><td><img width="768px" src="![image](https://user-images.githubusercontent.com/98135375/166389981-6c220b7e-8962-4978-8dc2-a269328e02ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is the code in html file which is the design for buttons.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history of each 5 advanced function being ran</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166390825-c29bcaef-2ca6-4642-af3f-0bcd9a2bc49f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>history after uploading the advance csv file.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166390887-4c75a1f5-e406-4527-90af-bae736140b26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of uploading the csv with calculation of advance functions.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>In view.py the decorator mycalc. route with function upload_csv():  is working for<br>advanced CSV file. For my project same route is working for both advance<br>and simple functions of uploading CSV.  The original MyCalc.py in the calc<br>folder is doing a collection of nums(in_nums) then it pops out the first<br>row with(mean, median, mode) and then calculates the for a remaining list and<br>gives the result.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Advanced CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of mixed advanced csv data (or separate csv files if you wish)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166390961-45543678-75b6-494a-a940-8c528399ea48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of csv file of advance functions.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history the csv file execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166391135-4f8f8515-d1d8-48ac-b8ac-cb2b4d67481b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is the result in apprun in terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="![image](https://user-images.githubusercontent.com/98135375/166391221-bdefd423-32e3-4907-8dc2-e34b76f2a638.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is the history in googlecloud<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>MyClac.py does all the calculations, views.py is handling those calculations logic for reading<br>and processing information from websites and mycalc.html does the design of the page.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> History Management </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of deleting a single history item</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166391522-33acfb78-7125-4719-aceb-d5e95e97a78f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the screen shot before deleting single history. I will delete first<br>history from here.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166391903-d3247ae1-15b1-477d-8737-40d19134b76a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot is after deleting the first few histories. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot showing the history being cleared (all of it for this user)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166392156-47737753-0e19-4188-85b5-e0e2c90fdf1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after history being deleted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show that the history is still present for other users (that task 2 didn't delete it for other users)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166392201-ec29a43c-102e-479c-9572-885f85225de5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>history is still present<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain how you implemented single delete of the history</td></tr>
<tr><td> <em>Response:</em> <p>For deleting history also need to create a route,  also have to<br>pass in a specific blog post id so we know which one to<br>delete. then created functiuon called (delete_single_history)    passed id, and look<br>into in database and grab that id and we can delete it.. So<br>after grabbing the single id no that is passed when we click the<br>delete button<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain how you implemented deleting all of the logged in user's history</td></tr>
<tr><td> <em>Response:</em> <p>For deleting the whole history, again need to create a route,  first<br>history is collected and a history id is needed.  Also, have to<br>pass in the post id so we know which one to delete. then<br>created function called (def delete():    passed id, and look into<br>in database and grab that id and we can delete it.. So after<br>grabbing the single id no that is passed when we click the delete<br>button.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot the test case code to register a test user via pytest</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166393151-9b5e86da-d7c8-4641-8c3a-e05f56ad62c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is the pytest for addtion<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot the passing test case from pytest for task 1</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/166396505-e5a7c7af-80a2-4d02-80e1-ad7eaa14b7e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is screenshot of one of the function divide of task 1.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot the test case code for logging in the test user via pytest</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot the passing test case from pytest for task 3</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot the test case code for recording a SimpleHistory for the test user (should be a valid generation from the calculator)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot the passing test case from pytest for task 5</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain the flow/process of these new test cases that pass the test user around</td></tr>
<tr><td> <em>Response:</em> <p>The process of the new test cases is to check if each module<br>is working properly or not,I have not done testcases for all of the<br>tasks.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add a link to your deployed app </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add the link here to the hosted instance</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://flask-pp1-gg6uefp37a-uc.a.run.app/mycalc/ ">https://flask-pp1-gg6uefp37a-uc.a.run.app/mycalc/ </a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/43">https://github.com/githubPratima/webdev/pull/43</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/pp235" target="_blank">Grading</a></td></tr></table>