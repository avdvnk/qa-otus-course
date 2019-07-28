*** Settings ***
Documentation       Include all libraries and main keywords
Resource            resources.robot
Resource            db_keywords.robot
Library             AdminPage.py  WITH NAME  AdminPage


*** Keywords ***
Default Setup
    [Arguments]  ${login}  ${password}  ${db_api}  ${db_name}  ${db_user}  ${db_pass}  ${db_host}  ${db_port}
    AdminPage.Set Browser               ${browser}
    AdminPage.Open Page                 ${opencart_url}
    AdminPage.Input Username            ${login}
    AdminPage.Input Password            ${password}
    AdminPage.Click Submit Button
    Get Db Connection  ${db_api}  ${db_name}  ${db_user}  ${db_pass}  ${db_host}  ${db_port}

Default Teardown
    AdminPage.Close Browser
    Close Db Connection