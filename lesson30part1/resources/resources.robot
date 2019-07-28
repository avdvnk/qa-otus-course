*** Settings ***
Resource        main_keywords.robot


*** Variables ***
${browser}          firefox
${opencart_url}     http://192.168.0.108/opencart/admin
${login}            avdvnk
${password}         108199098
${timeout}          15 seconds
${screenshot_dir}   ./reports

${db_host}          192.168.0.108
${db_api}           pymysql
${db_port}          3306
${db_user}          avdvnk1
${db_password}      108199098
${db_name}          opencart

${product_name}     TestName
${product_tag}      MetaTagTest
${product_model}    1021