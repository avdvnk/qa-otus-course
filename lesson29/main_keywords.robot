*** Settings ***
Library         SeleniumLibrary  WITH NAME  Browser
Resource        resources.robot


*** Keywords ***
Open Browser To Login Page
    Browser.Open Browser                    ${opencart_url}  ${browser}

Close Browser
    Browser.Close Browser

Get Page Title
    Browser.Wait Until Page Contains Element    ${title}
    ${title_text} =  Browser.Get Text           ${title}
    [Return]  ${title_text}

Input Username
    [Arguments]  ${username}
    Browser.Input Text      ${input_username}  ${username}

Input Password
    [Arguments]  ${password}
    Browser.Input Text      ${input_password}  ${password}

Click Submit Button
    Browser.Click Button    ${login_button}

Login To Admin Mode
    [Arguments]  ${username}  ${password}
    Open Browser To Login Page
    Input Username          ${username}
    Input Password          ${password}
    Click Submit Button
    BuiltIn.Sleep           ${timeout}

Open Settings
    Browser.Click Element   ${settings_btn}

Get Settings Title
    ${text} =  Browser.Get Text  ${setting_title}
    [Return]    ${text}

Click Profile Icon
    Browser.Click Element   ${icon_profile}

Click Your Profile Link
    Browser.Click Element   ${your_profile}

Click Extensions Menu
    Browser.Click Element   ${extensions_menu}

Click Marketplace
    Browser.Click Element   ${market_place}

Click Total Orders
    Browser.Click Element   ${total_orders}