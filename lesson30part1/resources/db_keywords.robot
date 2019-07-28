*** Settings ***
Documentation       Keywords for operating with database
Library             DatabaseLibrary  WITH NAME  DB
Library             String


*** Keywords ***
Get Db Connection
    [Arguments]  ${db_api}  ${db_name}  ${db_user}  ${db_pass}  ${db_host}  ${db_port}
    DB.Connect To Database      ${db_api}  ${db_name}  ${db_user}  ${db_pass}  ${db_host}  ${db_port}

Exist Product In DB
    [Arguments]  ${product_model}
    ${sql_query} =  Format String   SELECT product_id FROM oc_product WHERE model = '{}';       ${product_model}
    DB.Row Count Is Equal To X      ${sql_query}  1

Close Db Connection
    DB.Disconnect From Database

Get Product Count
    ${sql_query} =  convert to string  SELECT COUNT(product_id) FROM oc_product;
    @{result} =  DB.Query  ${sql_query}
    [Return]  ${result[0][0]}