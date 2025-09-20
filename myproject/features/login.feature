Feature: Django Admin Login

  Scenario: Successful login and navigation
    Given the Django admin login page is open
    When the user logs in with "Nanz" and "Nanz@123"
    And the user clicks on "Audit reports"
    Then the audit report list should be displayed