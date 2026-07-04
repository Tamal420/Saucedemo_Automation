# SauceDemo Checkout Automation

Automated end-to-end tests for the checkout flow on [saucedemo.com](https://www.saucedemo.com), built with **Python** and **Playwright**.

## What is covered


| Test     | File                              | Description                                                                |
| -------- | --------------------------------- | -------------------------------------------------------------------------- |
| Positive | `tests/test_checkout_flow.py`     | Login → add product to cart → checkout → verify order confirmation         |
| Negative | `tests/test_checkout_negative.py` | Checkout is correctly blocked when a required field (Last Name) is missing |




## Project structure

```
saucedemo-automation/
├── pages/                      
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_checkout_flow.py      
│   └── test_checkout_negative.py   
├── conftest.py                 
├── pytest.ini
├── requirements.txt

```

The suite follows the **Page Object Model**: each page of the app has its own class holding its locators and actions.Tests interact with the application through page objects and perform assertions on the expected results, keeping test logic separate from page interactions.

## Setup

**Prerequisites:** Python 3.9+ installed.

1. Clone the repository and open it in VS Code:
  ```bash
   git clone <your-repo-url>
   cd saucedemo-automation
  ```
2. Create and activate a virtual environment:
  ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
  ```
3. Install dependencies:
  ```bash
   pip install -r requirements.txt
  ```
4. Install the Playwright browser binaries (one-time step):
  ```bash
   python -m playwright install
  ```



## How to run the tests

Run the full suite (headless, default browser is Chromium):

```bash
pytest
```

Run with the browser visible, useful while debugging:

```bash
pytest --headed
```

Run only the positive scenario:

```bash
pytest tests/test_checkout_flow.py
```

Run only the negative scenario:

```bash
pytest tests/test_checkout_negative.py
```

Run with a specific browser:

```bash
pytest --browser firefox
```

If a test fails, a screenshot is automatically saved to the `screenshots/` folder — see `conftest.py`.

## Notes on test data

Login credentials and the product name are defined as constants at the top of each test file. SauceDemo is a public demo app with fixed, publicly known test accounts (e.g. `standard_user` / `secret_sauce`), so no `.env` file or secrets management is required for this project.