*** Settings ***
Documentation       Simple tests for adding and removed products
Resource            ./resources/resources.robot
Test Setup  Default Setup  ${login}  ${password}  ${db_api}  ${db_name}  ${db_user}  ${db_password}  ${db_host}  ${db_port}
Test Teardown  Default Teardown


*** Test Cases ***
Add product
    Click Catalog
    Click Products
    Click Add Product
    Input Product Name      ${product_name}
    Input Product Tag       ${product_tag}
    Click Data Tab
    Input Product Model     ${product_model}
    Click Save Button
    Exist Product In Db     ${product_model}

Delete Product
    ${product_count} =  Get Product Count
    Click Catalog
    Click Products
    Select Product          ${product_model}
    Click Remove Button
    Confirm Remove
    ${new_count} =  Get Product Count
    should be true  ${product_count} > ${new_count}
