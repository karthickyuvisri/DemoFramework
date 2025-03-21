from selenium.webdriver.support.events import AbstractEventListener


class Listener(AbstractEventListener):
    def before_navigate_to(self, url: str, driver) -> None:
        print(f"Navigating to {url}")

    def before_close(self, driver) -> None:
        print("closing browser")

    def after_close(self, driver) -> None:
        print("Browser Closed")

    def before_change_value_of(self, element, driver) -> None:
        print(f"Before changing value {dir(element)}")

    # def after_change_value_of(self, element, driver) -> None:
    #     print(f"After changing value {element}")

