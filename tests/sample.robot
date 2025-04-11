*** Settings ***
Resource               ../resources/common.resource
Suite Setup            OpenBrowser                 about:blank                 chrome
Suite Teardown         CloseAllBrowsers

*** Test Cases ***
First Test
    [Documentation]
    [Tags]
    ${response}=       Get Content
    Log To Console     Get response: ${response}                 # [] for the first run

    ${dict}=           Create Dictionary           id=1                        name=foo           age=13
    ${list}=           Create List
    Append To List     ${list}                     ${dict}

    ${response}=       Create Content              ${list}                     # {"created":1}
    Log To Console     Create response: ${response}

    ${response}=       Get Content
    Log To Console     Get response: ${response}                 # [{"id":"1","name":"foo","age":"13"}]


Another Test
    [Documentation]
    [Tags]
    ${response}=       Get Content
    Log To Console     Get response: ${response}                 # [{"id":"1","name":"foo","age":"13"}]

    ${dict}=           Create Dictionary           id=1                        name=bar           age=15
    ${response}=  Update Content  column_name=id  value=1  data=${dict}
    Log To Console     Patch response: ${response}                 # {'updated': 1}

    ${response}=       Get Content
    Log To Console     Get response: ${response}                 # [{"id":"1","name":"bar","age":"15"}]

    ${response}=       Delete Content  column_name=id  value=1
    Log To Console     Delete response: ${response}
