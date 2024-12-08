# Generated by Selenium IDE
import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_test_data():
    with open("level1/EditStudentName/input_editStudentName.json", "r", encoding="utf-8") as file:
        return json.load(file)


class TestEditStudentName:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        yield
        self.driver.quit()

    @pytest.mark.parametrize("test_data", load_test_data())
    def test_eSN(self, test_data):
        last_name = test_data["last_name"]
        first_name = test_data["first_name"]
        error_lastname = test_data["error_lastname"]
        error_firstname = test_data["error_firstname"]

        try:
            self.driver.get("https://school.moodledemo.net/?lang=vi")
            self.driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
            self.driver.find_element(By.ID, "username").send_keys("student")
            self.driver.find_element(By.ID, "password").send_keys("moodle2024")
            self.driver.find_element(By.ID, "loginbtn").click()


            self.driver.find_element(By.ID, "user-menu-toggle").click()
            self.driver.find_element(By.LINK_TEXT, "Hồ sơ").click()
            self.driver.find_element(By.LINK_TEXT, "Sửa hồ sơ cá nhân").click()


            self.driver.find_element(By.ID, "id_firstname").clear()
            self.driver.find_element(By.ID, "id_firstname").send_keys(first_name)
            self.driver.find_element(By.ID, "id_lastname").clear()
            self.driver.find_element(By.ID, "id_lastname").send_keys(last_name)
            self.driver.find_element(By.ID, "id_submitbutton").click()


            if first_name == "":
                firstname_error = self.driver.find_element(By.ID, "id_error_firstname").text
                assert firstname_error == error_firstname, f"Error in 'firstname': Expected '{error_firstname}', Got '{firstname_error}'"
            if last_name == "":
                lastname_error = self.driver.find_element(By.ID, "id_error_lastname").text
                assert lastname_error == error_lastname, f"Error in 'lastname': Expected '{error_lastname}', Got '{lastname_error}'"
            if first_name != "" and last_name != "":
                full_name = self.driver.find_element(By.CSS_SELECTOR, ".h2").text
                expected_name = f"{first_name} {last_name}"
                assert full_name == expected_name, f"Full name mismatch: Expected '{expected_name}', Got '{full_name}'"

        except AssertionError as e:
            pytest.fail(f"Test failed for first_name='{first_name}', last_name='{last_name}': {str(e)}", pytrace=False)

        except Exception as e:
            pytest.fail(f"Unexpected error: {str(e)}", pytrace=False)

        finally:
            try:
                self.driver.find_element(By.CSS_SELECTOR, ".avatar").click()
                self.driver.find_element(By.LINK_TEXT, "Thoát").click()
            except:
                print("Could not log out properly.")
