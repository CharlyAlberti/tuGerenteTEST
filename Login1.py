from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    #STARTS Login1.py

    # Go to https://auth.implementaconbubo.com/login
    page.goto("https://auth.implementaconbubo.com/login")

    # Click [placeholder="Correo Electrónico"]
    page.locator("[placeholder=\"Correo Electrónico\"]").click()

    # Fill [placeholder="Correo Electrónico"]
    page.locator("[placeholder=\"Correo Electrónico\"]").fill("tugastro@tugerente.com")

    # Click [placeholder="Contraseña"]
    page.locator("[placeholder=\"Contraseña\"]").click()

    # Fill [placeholder="Contraseña"]
    page.locator("[placeholder=\"Contraseña\"]").fill("TuGerente_2019!")

    # Press Enter
    page.locator("[placeholder=\"Contraseña\"]").press("Enter")
    page.wait_for_url("https://erp.implementaconbubo.com/principal")
    page.wait_for_timeout(5000)#5 SECONDS
    page.screenshot(path="Login1_Screenshot.png")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
