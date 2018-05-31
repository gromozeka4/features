@tags @Read_Socket
Feature: Read_Socket

    Background: Pre-condition
        Given Start My Server

    Scenario: 1. Read socket with default settings successfully
        Given Server address 'localhost'
        And Server port '4444'
        And Output file '.\output.out'
        When Start client
        Then There is some data in output file

    Scenario: 2. No arguments passed
        When No arguments entered
        Then Help is displayed

    Scenario: 3. Listening wrong host
        Given Server address '0.0.0.0'
        And Server port '4444'
        And Output file '.\output.out'
        When Start client
        Then Error appears '10049'

    Scenario: 4. Listening wrong port
        Given Server address 'localhost'
        And Server port '12312'
        And Output file '.\output.out'
        When Start client
        Then Error appears '10061'