*** Settings ***
Resource        main_keywords.robot


*** Variables ***
${browser}          firefox
${opencart_url}     http://192.168.0.108/opencart/admin
${login}            avdvnk
${password}         108199098
${timeout}          15 seconds

${input_username}   //input[@id='input-username']
${input_password}   //input[@id='input-password']
${login_button}     //button[@type='submit']
${catalog_menu}     //li[@id='menu-catalog']
${settings_btn}     //button[@id='button-setting']
${setting_title}    //h4[@class='modal-title']
${icon_profile}     //img[@id='user-profile']
${your_profile}     //i[@class='fa fa-user-circle-o fa-fw']
${extensions_menu}  //li[@id='menu-extension']
${market_place}     //li[@id='menu-extension']//li[contains(text(), Marketplace)]
${logout_btn}       //ul[@class='nav navbar-nav navbar-right'][2]
${total_orders}     //div[@class='col-lg-3 col-md-3 col-sm-6']//div[@class='tile-footer']//a
${title}            //h1