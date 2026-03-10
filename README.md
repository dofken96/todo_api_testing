How to run allure report

1. install java 8 version and set to Path as variable
2. install Scoop. 


Run this in cdm: 

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

scoop install allure

Then check allure version: allure --version

3. Run and store tests results in a folder

pytest --alluredir=allure-results

4. To the Allure report run:

allure serve allure-results



How to check Allure report result in GitHub

1. Navigate to the "Upload Allure HTML report" step
2. Download the Artifact
3. Extract the folder anywhere you want
4. Run PowerShell from the extracted folder
5. Execute the command: allure open.


