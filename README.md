# dagger
Provisioning tool.


snowflake email:
dagger100002@gmail.com
dagger100002

TODO:

odin:


services:
* create_update
    - change username
    - email
    - manager items

* access
    - data model
    
* birthright
    - create_update rule
    - delete rule


* ideas for the future when you get there:
    - have an aggregation agent that reads kafka and confirms provisioning and deprovisioning
    - you will need a scheduled full load aggregation to clean up the data
    - i think the way to do provisioning and deprovisioning is make an agent and have it call other services to make decisions on where it should provision
    -  
    - for provisioning this would do something like: recieve brithright acess from provision topic, get current accounts, get current access assigned to accounts, make the decision of what should be newly provisioned through brightright (only compare what was prov through birthright, not r and a),... 
    - continued: ...create the accounts (in snowflake too), create the access (in snowflake too), remove access not needed (mark for delete in snowflake too), remove accounts not needed (mark for delete in snowflake too), send message to aggregate and confirm
    -  
    - for deprovisioning this would do something like: recieve message from deprovision topic, get current accounts, get current access assigned to accounts, remove access not needed (mark for delete in snowflake too), remove accounts not needed (mark for delete in snowflake too), send message to aggregate and confirm

