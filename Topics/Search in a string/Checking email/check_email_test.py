import pytest
from main import check_email


@pytest.mark.parametrize("email, expected", [("this@.example.com", "False"), ("this@e.xamplecom", "True"), ("this@example.com", "True"), ("this@ example.com", "False"), ("thisexample.com", "False"), ("this.ulvi@example.com", "True"), ("My e-mail is: this@example.com", "False"), ("this.@example.com", "False"), ("this@example", "False")])
def test_check_email(email, expected):
    assert check_email(email) == expected


if __name__ == '__main__':
    unittest.main()
