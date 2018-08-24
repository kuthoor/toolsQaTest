This is a sample test to test the contact form of toolsQA.com web site

BDD tests are developed in Python and works on Chrome.

Software required.
 - Python (2.7.14)
 The following modules should be installed using pip
 - nose (1.3.7) (pip install nose==1.3.7)
 - behave (1.2.6) (pip install behave==1.2.6)
 - selenium (3.14.0) pip install selenium==3.14.0)
 - Install Chrome  browser
 - Download selenium chrome driver (https://chromedriver.storage.googleapis.com/index.html?path=2.41/)
   Once downloaded and extracted, go to browser.py file and modify this line (number 7) and
   add correct path where chromedriver is stored in your machine
       driver = webdriver.Chrome('<path>/chromedriver.exe')

Clone this repo to your local directory

To run the test
 1. change directory to the root of this test i.e toolsQaTest
 2. execute command behave.exe and you should see an output as follows
     Failing scenarios:
     features/contact.feature:27  Phone validation

     0 features passed, 1 failed, 0 skipped
     4 scenarios passed, 1 failed, 0 skipped
     34 steps passed, 1 failed, 1 skipped, 0 undefined
     Took 1m6.796s

This test suite has 5 test cases
 1. Fill contact form (checks if user is able to navigate to contact form and fill in the details)
 2. Fail to submit partial filled form (user should not submit partially filled form)
 3. Email validation (Form should validate email format)
 4. Phone validation (form should validate phone number format)
 5. Submit without error (user should be able to submit the form when all the details are filles in)

Further test scenarios:
 - Validate form by filling it partially and omitting fields.
 - Check if the submit form was successfully received at other end with all the information
 - Check if the fields are cleared once submitted
 - Check if user is unable to submit same information multiple times by pressing the Send button

Test result:
 All except Phone validation test cases failed, this is a bug where the form is not validating the phone number.
 Another observation is that user is able to submit the form even if the msaage text box is empty.

Highlights:
 This is a modular approach and will help in rapid test case creation. We can add more modules per web page for example
 testimonial page so that it can be tested.

Improvements:
 - I could refactor lot of test steps as they are repeated.
 - Test it with other browsers (IE and Firefox)

Bugs:
 Mentioned in test result