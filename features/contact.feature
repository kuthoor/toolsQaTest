Feature: Contact Form

  Scenario: Fill contact form
    Given I am on the toolsqa Site
    Then I should be able to contact toolsqa with the following information
    Then I should be able to enter name "j.blogger"
    Then I should be able to enter email "j.Blogger@toolsqa.com"
    Then I should be able to enter message "please contact me I want to find out more"

  Scenario: Fail to submit partial filled form
    Given I am on the toolsqa Site
    Then I should be able to contact toolsqa with the following information
    Then I should be able to enter name "j.blogger"
    Then I should be able to enter email "j.Blogger@toolsqa.com"
    Then I should be able to enter message "please contact me I want to find out more"
    And I should not be able to submit

  Scenario: Email validation
    Given I am on the toolsqa Site
    Then I should be able to contact toolsqa with the following information
    Then I should be able to enter name "j.blogger"
    Then I should be able to enter email "j.Blogger"
    Then I should be able to enter message "please contact me I want to find out more"
    Then I should not be able to submit
    And Email validation should fail

  Scenario: Phone validation
    Given I am on the toolsqa Site
    Then I should be able to contact toolsqa with the following information
    Then I should be able to enter name "j.blogger"
    Then I should be able to enter email "j.Blogger@toolsqa.com"
    Then I should be able to enter mobile "qwerty"
    Then I should be able to enter message "please contact me I want to find out more"
    Then I should not be able to submit
    And Phone validation should fail

  Scenario: Submit without error
    Given I am on the toolsqa Site
    Then I should be able to contact toolsqa with the following information
    Then I should be able to enter name "j.blogger"
    Then I should be able to enter email "j.Blogger@toolsqa.com"
    Then I should be able to enter mobile "123456"
    Then I should be able to enter city "London"
    Then I should be able to enter country "UK"
    Then I should be able to enter company "Foo"
    Then I should be able to enter message "please contact me I want to find out more"
    And I should be able to submit without error