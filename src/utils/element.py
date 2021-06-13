import builtins

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exc
from selenium.webdriver.support.wait import WebDriverWait

from src.utils import logger, common


def find_element(element: tuple, timeout=60, wait=True) -> WebElement:
    """
    Find an element existing in DOM with a timeout in seconds.
    :return: WebElement if found
    :raise: NoSuchElementException if not found
    """
    driver = getattr(builtins, "driver")
    locator = element[0]
    value = element[1]
    try:
        if wait:
            return WebDriverWait(driver, timeout).until(exc.visibility_of_element_located((locator, value)))
        return driver.find_element(locator, value)
    except Exception:
        log = "Element not found with locator %s value '%s' after %d seconds" % (locator, value, timeout)
        raise NoSuchElementException(log)


def wait_element_invisible(element: tuple, timeout=60, wait=True) -> WebElement:
    """
    Find an element existing in DOM with a timeout in seconds.
    :return: WebElement if found
    :raise: NoSuchElementException if not found
    """
    driver = getattr(builtins, "driver")
    locator = element[0]
    value = element[1]
    try:
        if wait:
            return WebDriverWait(driver, timeout).until(exc.invisibility_of_element((locator, value)))
        return driver.find_element(locator, value)
    except Exception:
        log = "Element not found with locator %s value '%s' after %d seconds" % (locator, value, timeout)
        raise NoSuchElementException(log)


def find_elements_list(element: tuple, timeout=60, wait=True) -> list[WebElement]:
    """
    Find an available element list with a timeout in seconds.
    :return: WebElement if found
    :raise: NoSuchElementException if not found
    """
    driver: WebDriver = getattr(builtins, "driver")
    locator = element[0]
    value = element[1]
    try:
        if wait:
            return WebDriverWait(driver, timeout).until(exc.visibility_of_element_located((locator, value)))
        return driver.find_elements(locator, value)
    except Exception:
        log = "Element not found with locator %s value '%s' after %d seconds" % (locator, value, timeout)
        raise NoSuchElementException(log)


def send_keys(element: tuple, value: str, press_enter=False, clear=False):
    ele = find_element(element)
    if clear:
        ele.clear()
    ele.send_keys(value)
    if press_enter:
        ele.send_keys(Keys.ENTER)


def send_keys_timeout(element: tuple, value: str, *, timeout=60, press_enter=False, clear=False):
    ele = find_element(element, timeout)
    if clear:
        ele.clear()
    ele.send_keys(value)
    if press_enter:
        ele.send_keys(Keys.ENTER)


def send_keys_chord(element: tuple, value: str, press_enter=False, clear=False):
    driver: WebDriver = getattr(builtins, "driver")
    ele = find_element(element)
    if clear:
        ele.clear()
    actions = ActionChains(driver)
    actions.send_keys_to_element(ele, value)
    actions.perform()
    logger.debug(ele.text)
    common.sleep(2)


def click(element: tuple):
    find_element(element).click()


def wait_for_element_displayed(element: tuple) -> bool:
    try:
        find_element(element, wait=True)
        return True
    except NoSuchElementException:
        return False
