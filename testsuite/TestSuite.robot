*** Settings ***
Library    os
Resource    ${EXECDIR}/resources/Keyword.robot
Variables  ${EXECDIR}/config/Config_Test.py
Library  ${EXECDIR}/libraries/Initial_Context_Setup_Request.py

*** Test Cases ***
Test Case: Initial Context Setup
    Context Setup validation