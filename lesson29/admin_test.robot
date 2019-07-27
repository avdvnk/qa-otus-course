*** Settings ***
Documentation       Simple tests for admin interface
Library             SeleniumLibrary  WITH NAME  Browser
Resource            resources.robot

*** Test Cases ***
Valid login
    [Tags]  build
    [Setup]  Open Browser To Login Page
    Input Username          ${login}
    Input Password          ${password}
    Click Submit Button
    BuiltIn.Sleep           ${timeout}
    ${title} =  Get Page Title
    should be equal  ${title}  Dashboard
    [Teardown]  Close Browser

Open Settings
    [Setup]  Login To Admin Mode  ${login}  ${password}
    Open Settings
    ${title} =  Get Settings Title
    should be equal  ${title}   Developer Settings
    [Teardown]  Close Browser

Open Profile Page
    [Setup]  Login To Admin Mode  ${login}  ${password}
    Click Profile Icon
    Click Your Profile Link
    ${title} =  Get Page Title
    should be equal  ${title}  Profile
    [Teardown]  Close Browser

Open Marketplace
    [Tags]  build
    [Setup]  Login To Admin Mode  ${login}  ${password}
    Click Extensions Menu
    Click Marketplace
    BuiltIn.Sleep   ${timeout}
    ${title} =  Get Page Title
    should be equal  ${title}  Extension Marketplace
    [Teardown]  Close Browser

Open Total Orders
    [Setup]  Login To Admin Mode  ${login}  ${password}
    Click Total Orders
    ${title} =  Get Page Title
    should be equal  ${title}  Orders
    [Teardown]  Close Browser