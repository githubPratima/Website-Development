<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Pratima Paudel(pp235)</td></tr>
<tr><td> <em>Generated: </em> 5/13/2022 3:05:32 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone1-deliverable/grade/pp235" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Checkout Milestone1 branch</li>
<li>Create a milestone1.md file in your Project folder</li>
<li>Fill in the deliverable items</li>
<li>Ensure your images display correctly in the sample markdown at the bottom</li>
<li>Save the submission items</li>
<li>Copy/paste the markdown from the &quot;Copy markdown to clipboard link&quot;</li>
<li>Paste the code into the milestone1.md file</li>
<li>Git add/commit/push the md file to Milestone1</li>
<li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li>
<li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol>
<li>Make sure everything looks ok</li>
</ol>
</li>
<li>Make a pull request from dev to prod (resolve any conflicts) <ol>
<li>Make sure everything looks ok on the deploy service</li>
</ol>
</li>
<li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li>
</ol>
<p>Note: Make sure all provided links work as they&#39;re likely to be visited during testing/validation of this assignment</p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168127849-d328b187-66da-4bbd-a9f6-df4a7e70cc62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passport not matching while logging in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168125937-44254ca6-7a3a-44c7-81dd-c41c6af5efe7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data base of entering the email ids. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>I created the registration form for the user(admin/forms.py)  data required() to make<br>sure the user fills all the requirements and others are like length validator<br>to check the min/max length, equalTo is to check email if two fields<br>contain same data. In register.html there is an alert message in the jinja<br>template which flash the wrong message if the user types the wrong email,<br>wrong username, and wrong password.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="//I could not deploy my website in google cloud.">I could not deploy my website in google cloud.</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168128205-6d00d85d-900a-48a4-8dfa-e0cb661cc9d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username and email doesnot exsit error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168129037-b1f8df3e-57b7-4727-8ae7-d12ca28c4a01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>In url.py file/@pp route login decorator, I create a flash method in f<br>string which is used to generate messages(you are logged in) in the flask.<br>It creates the message and renders the messages to the next request in<br>HTML templates<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168129281-13e00254-4195-4e71-be7f-435accd20873.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successful logout<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168129679-e035f6f4-a817-4a42-987a-624d58f315fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is the page so nothing happens, i mean it does get click<br>anything unless and user doesnot logged. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>In url.py file/@pp route logout decorator, I create a flash method in f<br>string which is used to generate messages(logout is successful) in the flask. It<br>creates the message and renders the messages to the next request in HTML<br>templates<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168159779-c8754e32-ccd1-46ce-aa6f-9893ae20ee84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>if logoout users try to add the phone in cart there is no<br>option is seen. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page (a test/dummy page is fine)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>could not add anything for this feature<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168185310-c28fd7f7-1c7a-45be-9a9d-b877de7a81f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user databases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168185310-c28fd7f7-1c7a-45be-9a9d-b877de7a81f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>userroles called admin databses<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>@login_required is the decorator in my url.py which works for login-protected pages. This<br>will prevent a user that is not logged in from visiting the route.<br>If user is not logged in, the user will get redirected to the<br>login page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>@login_required is the decorator in my url.py which works for login-protected pages.I have<br>to define the function add users and generalize the roles.  for this<br>user must logged if not logged they are redirected to the user_unauthrized page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168181820-ff99cff2-bf08-495b-887a-f6cc3d8f712b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>my webiste looks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>I added my CSS style sheet in the static field. CSS is about<br>colors, alignment, fonts and margins, tables, and padding. Also, it gives structure to<br>the header area, formating the header area and background color, centering the body<br>content, I copied CSS from getbootstrap.com In my CSS file. CSS is also<br>including about the background color and the transition of a header of the<br>site. Also the size of products length width and height etc.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168183626-ac54e3b3-c5e0-470f-b24c-6e58ccd0d2d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it gives username and email does not, <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>I created the registration form for the user(admin/forms.py)  data required() to make<br>sure the user fills all the requirements and others are like length validator<br>to check the min/max length, equalTo is to check email if two fields<br>contain same data. In register.html there is an alert message in the jinja<br>template which flash the wrong message if the user types the wrong email,<br>wrong username, and wrong password.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168184010-5e354aa8-81b7-4f16-a44c-d28870293a65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this is the screen shot for user <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168184148-523288ab-19a6-4cd2-88f3-5c405856ae34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The profile page for user (Pratima)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>I have created a route called @ update username in url.py which is<br>working to update for a profile of the user.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168133292-ddb042bb-62e5-4966-b6eb-16e183a61ea3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The profile page of user called( pratima)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98135375/168133812-935a3282-3666-4edb-b781-a800e9b3095c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user can change the password.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em>  <br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/githubPratima/webdev/pull/52">https://github.com/githubPratima/webdev/pull/52</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone1-deliverable/grade/pp235" target="_blank">Grading</a></td></tr></table>