
cQube Release_1.3

Prerequisites:
  To Run Selenium python scripts ,Install pycharm in your system
  Google Chrome need to be installed in the server or local machine.
  Chrome driver need to be downloaded and place this driver file in cQubeTesting-1.3/Driver folder
 
  
Steps to install the google chrome

  Open the terminal (Ctrl+Alt+t) in the ubuntu
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  sudo apt install ./google-chrome-stable_current_amd64.deb
  Check chrome brower version using command -> google-chrome -version
  	
Steps to Download the chrome driver 
Note: Based on chrome browser version need to download chrome driver 
   https://sites.google.com/a/chromium.org/chromedriver/downloads
   Unzip the chrome driver and place it in /usr/bin or /usr/local/bin.

Pycharm:
  cQubeTesting-1.3 project need to be cloned from the github to your storage i.e /home/ubuntu/Downloads
  Open project in pycharm and click on file -> Settings -> Project -> 

Note : Java jdk1.8 need to be already installed in the machine
Note:  execution of Admin console scripts , i.e  create_user.py script should provide the username and password in sendkeys.

Steps to execute the test script
	1.Open the Terminal (Ctrl+Alt+t) in the ubuntu
	2.sudo apt update
	3.sudo apt install python3-pip
	4.Execute the Requirement.txt in the terminal (Requirement.txt file present in the cQubeTesting-1.3 Folder) [mandatory]
	    pip3 install -r Requirement.txt 
	5.Fill the config.ini file (config.ini file present in the cQubeTesting-1.3 Folder).

	  [config]
	  domain= #Enter the url of the cqube application ex: https://<domainname>/ or http://<ip>:4200
	  username= #Enter the username of report viewer  
	  password= #Enter the password of report viewer
	  admin_username = #Enter the admin user name 
	  admin_password = #Enter the admin password
	  createadmin= #for creating new admin user provide name of admin
          adminpassword= # Enter password for new admin
          createviewer= #for creating new admin user provide name of reportviewer
          viewerpassword= # Enter password for new viewer
          createemission= #for creating new admin user provide name of emission user
          emissionpassword= # Enter password for new emission user	  

For Executing the Regression Test suites using pytest 
	if using pycharm 
	Open this file:  Testsuite/Regression_suite/regression_test_suite.py and right click and click on run option 
			 Adminconsole/admin_console_regression_testing.py and right click and click on run option 
	
For Execution of System testing follow the steps:
	if using pycharm 
	Open this file:  Testsuite/system_testing_suite/system_testing_suite.py and right click and click on run option 
			 Adminconsole/admin_console_system_testing.py and right click and click on run option


For Execution of smoke testing follow the steps: 
	if using pycharm 
	Open this file:  Testsuite/smokeTestsuite/smoke_testing.py and right click and click on run option 
			 Adminconsole/admin_console_smoke_testing.py and right click and click on run option 
	
VPN CONNECTION:	  
Please follow the steps for run testscripts for admin console
	  	1> open vpn based url in browser 
		   click on advanced --> open unsecured link --> login to openvpn access server  
		2> click on user-profile and starts downloading client.ovpn 
		3> open terminal with directory of client.ovpn is located
		4> check version of openvpn ,if not exist use command to install : sudo apt-get install openvpn
		5> sudo openvpn --config client.ovpn 
		6> provide author userid and password 
		7> note: dont close terminal , just open browser and navigate to cQube application 
		8> login with admin user and password , admin can access both cQube reports and admin console
	
6.To Run the Test scripts
Navigate to cQubeTesting-1.3 Directory in the terminal (ex cd /home/ubuntu/cQubeTesting-1.3)
	For Regression:
		python3 -m unittest Testsuite/Regression_suite/regression_test_suite.py
		python3 -m unittest Adminconsole/admin_console_regression_testing.py
	For System Testing:
		python3 -m unittest Testsuite/system_testing_suite/system_testing_suite.py
		python3 -m unittest Adminconsole/admin_console_system_testing.py
	For Smoke Testing:
		python3 -m unittest Testsuite/smokeTestsuite/smoke_testing.py
		python3 -m unittest Adminconsole/admin_console_smoke_testing.py


After execution of scripts , the report will be generated and present in Reports folder

















