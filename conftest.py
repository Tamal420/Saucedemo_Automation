"""Shared pytest configuration and hooks for the test suite."""

import os

import pytest

SCREENSHOT_DIR = "screenshots"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically capture a screenshot whenever a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")
