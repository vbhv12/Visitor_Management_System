### Visitor Management System

Three types of user :<br/>
1.admin<br/>
2.Entryperson<br/>
3.user(host)<br/>

Admin : Admin can register host,visitor,event and admin can do create update and delete operation on host,vistor,event.<br/>
Entryperson : Will be having the responsibility of entering the visitor coming to visit and he/she can enter the purpose of their visit.And also have the responsibility to enter the event visitor is coming to attend. <br/>
user(host): Host will be given a user name and password to login. It will be issued by admin.Host can create event,update event,delete event and see his account.And also update account.<br/>

# Local setup for this project
<p>Clone this repository and run the following commands to install requirements:</p>
<pre><code>git clone https://github.com/KavachNetworks/Visitor_management.git<br/></code></pre>
<p>Go to Visitor_management file</p>
<pre><code>cd Visitor_management<br/></code></pre>
<pre><code>pip install -r requirements.txt<br/></code></pre>
<h3>1. Go to visitor_manage_system file and run following commands : </h3>
<pre><code>cd visitor_manage_system</code></pre>
<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python manage.py migrate</code></pre>
<pre><code>python manage.py createsuperuser</code></pre>
<p>create super user name,email,password,confirm password then run following commands:</p>
<pre><code>python manage.py runserver</code></pre>
<h3>2. go to url "127.0.0.1/admin" and login, Then create group in Groups</h3>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2013-39-57.png"  width="400" height="250">
<h3>2. Create three group admin,entryperson,host</h3>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2013-42-45.png"  width="400" height="250">
<br/>
<h3>3. Create credentials for admin</h3>
<p>create it in Users</p>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-45.png"  width="400" height="250">
 <h3>and check the  checkbox of superuser and chosen groups as admin</h3>
 <img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-55.png"  width="400" height="250">
 <br/>
 <h3>4. Create credentials for entryperson. create it in Users </h3>
<img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-07.png"  width="400" height="250">
 <h3>and check checkbox staff status and chosen groups as entryperson</h3>
 <img src="https://github.com/KavachNetworks/Visitor_management/blob/master/support%20image/Screenshot%20from%202020-08-11%2015-21-21.png"  width="400" height="250">
 <br/>
 <h3>There is a mail service to send  password reset so need to add email id and password in visitor_manage_system/visitor_manage_system/settings.py at last <br>EMAIL_HOST_USER =''
<br>EMAIL_HOST_PASSWORD ='' 
 </h3>
 <p>If it is not add reset password will not work.</p>
 <h3>5 .Now be in the folder where manage.py is present and run command as</h3>
<pre><code>python manage.py runserver</code></pre>
<p>By default it will be login as superuser. Just logout on top right and try to login as admin username and password which you created during superuser login</p>
<p> Copy and paste the url in browser or type "127.0.0.1:8000" in browser</p>
