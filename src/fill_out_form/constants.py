"""Every URL, locator, text and timing value of the lecture, defined once.

@file constants.py
@brief Every URL, locator, text and timing value of the lecture, defined once.

The locator strategies are the plain strings that Selenium's `By` class holds
(`By.LINK_TEXT == "link text"`); a unit test guards that they stay equal, so
the application layer does not need to import Selenium.
"""

# --- Pages -----------------------------------------------------------------
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"
FORM_URL = "https://secure-retreat-92358.herokuapp.com/"

# --- Locator strategies (equal to selenium.webdriver.common.by.By) ----------
BY_LINK_TEXT = "link text"
BY_NAME = "name"
BY_CSS_SELECTOR = "css selector"

# --- Lecture step 1: click a link by its text -------------------------------
LINK_TEXT_CONTENT_PORTALS = "Content portals"

# --- Lecture step 2: type into an input and send a special key --------------
SEARCH_INPUT_NAME = "search"
SEARCH_TERM = "Python"
KEY_ENTER = ""  # selenium.webdriver.common.keys.Keys.ENTER

# --- Lecture step 3: fill out the form (challenge) --------------------------
FIRST_NAME_SELECTOR = "input[name='fName']"
LAST_NAME_SELECTOR = "input[name='lName']"
EMAIL_SELECTOR = "input[name='email']"
SIGN_UP_BUTTON_SELECTOR = "form button"
DEFAULT_FIRST_NAME = "Jane"
DEFAULT_LAST_NAME = "Doe"
DEFAULT_EMAIL = "jane.doe@example.com"

# --- Browser ----------------------------------------------------------------
PAUSE_SECONDS = 2.0
WINDOW_SIZE = "1280,900"
CHROME_BINARY_ENV = "CHROME_BIN"
HEADLESS_ARGUMENTS = (
    "--headless=new",
    "--no-sandbox",
    "--disable-dev-shm-usage",
)

# --- Screenshots (one per lecture step) ---------------------------------------
SCREENSHOT_STEP_1 = "step-1-click-link.png"
SCREENSHOT_STEP_2 = "step-2-search.png"
SCREENSHOT_STEP_3_FILLED = "step-3-form-filled.png"
SCREENSHOT_STEP_3_SIGNED_UP = "step-3-form-signed-up.png"
