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
    #STARTS ModuloVentas3.py
    # Click #root >> text=Módulo Punto de Venta
    page.locator("#root >> text=Módulo Punto de Venta").click()
    page.wait_for_url("https://pos.implementaconbubo.com/principal")
    page.wait_for_timeout(5000)#5 SECONDS
    page.screenshot(path="Ventas2_Screenshot.png")

    # Click text=Módulo Punto de Venta Vender >> button
    page.locator("text=Módulo Punto de Venta Vender >> button").click()
    page.wait_for_url("https://pos.implementaconbubo.com/venta")
    page.wait_for_timeout(40000)#40 SECONDS
    page.screenshot(path="ModuloVentas3_Screenshot.png")

    # Click #ProdFav div >> nth=1
    page.locator("#ProdFav div").nth(1).click()

    #ModuloVentas4_AgregarProducto
    # Click [id="\32 44997"] >> nth=0
    page.locator("[id=\"\\32 44997\"]").first.click()
    # Click [id="\32 47079"] >> nth=0
    page.locator("[id=\"\\32 47079\"]").first.click()
    # Click text=PISTOLA CAL22 WALTHER ALEMANIA P22 PPQ M2 -5100301 TACTIAL NEGRA
    page.locator("text=PISTOLA CAL22 WALTHER ALEMANIA P22 PPQ M2 -5100301 TACTIAL NEGRA").click()
    # Click text=PISTOLA CAL22 BERSA ARGENTINA MATE BLUE NIKEL Y NEGRO
    page.locator("text=PISTOLA CAL22 BERSA ARGENTINA MATE BLUE NIKEL Y NEGRO").click()
    # Click [id="\32 44509"] >> nth=0
    page.locator("[id=\"\\32 44509\"]").first.click()
    # Click [id="\32 45170"] >> nth=0
    page.locator("[id=\"\\32 45170\"]").first.click()
    # Click [id="\32 44978"] >> nth=0
    page.locator("[id=\"\\32 44978\"]").first.click()
    # Click text=Pagar24,447.00 >> nth=0
    page.locator("text=Pagar24,447.00").first.click()
    # Click text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder="Escriba el nombre o nit del cliente\."]
    page.locator("text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").click()
    # Fill text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder="Escriba el nombre o nit del cliente\."]
    page.locator("text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").fill("Gabriela Calvimontes")
    page.wait_for_timeout(2000)#2 SECONDS
    # Press Enter
    page.locator("text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").press("Enter")
    page.screenshot(path="screenshots/ModuloPOSVenta6_AgregarCliente.png")
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
