*** Settings ***
Documentation       Login tests
Library             resources/MyLib.py
Resource            resources/resources.robot


*** Test Cases ***
Test Admin Login
    AdminPage.Set Webdriver         ${browser}
    AdminPage.Open Opencart             ${opencart_url}
    AdminPage.Input Username            ${login}
    AdminPage.Input Password            ${password}
    AdminPage.Click Submit Button
    AdminPage.Check Admin Dashboard
    [Teardown]  AdminPage.Close Browser

Test Customer Login
    CustomerPage.Set WebDriver         ${browser}
    CustomerPage.Open Opencart         ${opencart_url}
    CustomerPage.Check Dashboard Page
    [Teardown]  CustomerPage.Close Browser
