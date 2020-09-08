from appium import webdriver
import unittest
import HtmlTestRunner

class AppiumTest(unittest.TestCase):
    dc = {
        "deviceName": "Galaxy S10e",
        "platformName": "Android",
        "appPackage": "io.selendroid.testapp",
        "appActivity": "io.selendroid.testapp.HomeScreenActivity"
    }
    def setUp(self) -> None:
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(5)

    def test_Selandroid_UserRegistration(self):
        # locate element using ID = resource-id
        self.driver.find_element_by_id("android:id/button1").click()

        # locate element using accessibilty_id = content-desc
        self.driver.find_element_by_accessibility_id("startUserRegistrationCD").click()

        # sending value in form elemnets

        # Hide onscreen keyboar
        self.driver.hide_keyboard()

        # driver.find_element_by_id()
        usename = self.driver.find_element_by_id("io.selendroid.testapp:id/inputUsername")
        usename.send_keys("s.bhowmik")
        email = self.driver.find_element_by_id("io.selendroid.testapp:id/inputEmail")
        email.send_keys("subrata@yopmail.com")
        password = self.driver.find_element_by_id("io.selendroid.testapp:id/inputPassword")
        password.send_keys("1234@asdf")
        name = self.driver.find_element_by_id("io.selendroid.testapp:id/inputName")
        name.clear()
        name.send_keys("Subrata K. Bhowmik")

        # Click on dropdown to open list.
        self.driver.find_element_by_id("io.selendroid.testapp:id/input_preferedProgrammingLanguage").click()
        programlist = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.CheckedTextView[4]').click()
        self.driver.find_element_by_id("io.selendroid.testapp:id/input_adds").click()
        self.driver.find_element_by_id("io.selendroid.testapp:id/btnRegisterUser").click()
        name_result = self.driver.find_element_by_id("io.selendroid.testapp:id/label_name_data").text
        assert "Subrata K. Bhowmik" in name_result
        print("Test Passed")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="./result/"))
