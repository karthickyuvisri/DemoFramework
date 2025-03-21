from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver: webdriver.Chrome, wait_time: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def open_url(self, url: str):
        """Opens a URL in the browser."""
        self.driver.get(url)

    def get_element(self, locator):
        """Finds and returns a web element."""
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """Finds and returns a list of web elements."""
        return self.driver.find_elements(*locator)

    def wait_for_element_visible(self, locator):
        """Waits until an element is visible and returns it."""
        print(locator)
        return self.wait.until(EC.visibility_of_element_located((locator)))

    def wait_for_element_clickable(self, locator):
        """Waits until an element is clickable and returns it."""
        return self.wait.until(EC.element_to_be_clickable((locator)))

    def wait_for_element_present(self, locator):
        """Waits until an element is present in the DOM and returns it."""
        return self.wait.until(EC.presence_of_element_located((locator)))

    def click_element(self, locator):
        """Clicks on a web element."""
        element = self.wait_for_element_clickable(locator)
        element.click()

    def enter_text(self, locator, text: str, clear_first=True):
        """Enters text into a text field."""
        element = self.wait_for_element_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def press_key(self, key: str):
        """Presses a keyboard key."""
        ActionChains(self.driver).send_keys(key).perform()

    def hover_over_element(self, locator):
        """Hovers over a web element."""
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_dropdown_by_text(self, locator, text: str):
        """Selects a dropdown option by visible text."""
        select = Select(self.wait_for_element_visible(locator))
        select.select_by_visible_text(text)

    def select_dropdown_by_value(self, locator, option_value: str):
        """Selects a dropdown option by value."""
        select = Select(self.wait_for_element_visible(locator))
        select.select_by_value(option_value)

    def select_dropdown_by_index(self, locator, index: int):
        """Selects a dropdown option by index."""
        select = Select(self.wait_for_element_visible(locator))
        select.select_by_index(index)

    def get_selected_option(self, locator):
        """Returns the currently selected option in a dropdown."""
        select = Select(self.wait_for_element_visible(locator))
        return select.first_selected_option.text

    def get_page_title(self):
        """Returns the page title."""
        return self.driver.title

    def refresh_page(self):
        """Refreshes the current page."""
        self.driver.refresh()

    def go_back(self):
        """Navigates back in the browser history."""
        self.driver.back()

    def go_forward(self):
        """Navigates forward in the browser history."""
        self.driver.forward()

    def accept_alert(self):
        """Accepts an alert pop-up."""
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """Dismisses an alert pop-up."""
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        """Gets text from an alert pop-up."""
        return self.driver.switch_to.alert.text

    def switch_to_frame(self, locator):
        """Switches to an iframe."""
        frame = self.wait_for_element_present(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """Switches back to the default content from an iframe."""
        self.driver.switch_to.default_content()

    def scroll_into_view(self, locator):
        """Scrolls to an element in the viewport."""
        element = self.wait_for_element_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def take_screenshot(self, file_path: str):
        """Takes a screenshot of the current page."""
        self.driver.save_screenshot(file_path)

    def close_browser(self):
        """Closes the browser window."""
        self.driver.quit()
