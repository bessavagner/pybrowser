# Changelog

<!--next-version-placeholder-->

## v0.1.0 (17/10/2022)

- First release of `thatscraper`!

## v1.0.0

- Aditional docstrings.
- More type hints.
- Added:
    - WeDriverWait as callbacks to pollin2.poll.
    - WeDriverWait to 'send' like methods.
    - more Keys.
    - Apadtations to `webdriver.execute_script`:
        - `Crawler.run_script`: Execute Javascript code given a string.
        - `Crawler.query_selector`: Assing 'value' to value attribute of the
                                            first element found with 'selector'.
        - `Crawler.to_selector`: Assing 'value' to 'attribute' of the
                                 first element found with 'selector'.
    - Attribute `quit_on_falure`: when set to False, when
      methods fails driver won't quit. Can be set in constructor.
- Changed:
  - `Crawler.get_items` to `Crawler.items_of`.
  - Replaced `polling2.poll` for `selenium.webdriver.support.ui.WebDriverWait` as wait method.
- Removed dependencies:
  - `polling2`.