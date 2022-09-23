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
    page.screenshot(path="screenshots/Ventas2.png")

    # Click text=Módulo Punto de Venta Vender >> button
    page.locator("text=Módulo Punto de Venta Vender >> button").click()
    page.wait_for_url("https://pos.implementaconbubo.com/venta")
    page.wait_for_timeout(40000)#40 SECONDS
    page.screenshot(path="screenshots/ModuloVentas3.png")

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
    page.wait_for_timeout(3000)#5 SECONDS
    page.screenshot(path="screenshots/ModuloVentas4.png")
    # Click text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder="Escriba el nombre o nit del cliente\."]
    page.locator("text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").click()
    # Fill text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder="Escriba el nombre o nit del cliente\."]
    page.locator("text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").fill("Gabriela Calvimontes")
    page.wait_for_timeout(2000)#2 SECONDS
    # Press Enter
    page.locator("text=Cliente: Empleado:Vendedor genérico / casa matriz 890 >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").press("Enter")
    #---------------------Bug!-------------------------#
    page.screenshot(path="screenshots/ModuloPOSVenta5.png")
    
    # Click text=¿Método de pago secundario?SiNo >> span >> nth=4
    page.locator("text=¿Método de pago secundario?SiNo >> span").nth(4).click()
    # Click span:nth-child(2) > .k-dropdown-wrap > .k-select > .k-icon
    page.locator("span:nth-child(2) > .k-dropdown-wrap > .k-select > .k-icon").click()
    # Click text=+200 >> nth=0
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()
    page.locator("text=+200").first.click()

     # Click text=Boliviano >> nth=1
    page.locator("text=Boliviano").nth(1).click()
    # Click text=Dólar
    page.locator("text=Dólar").click()
   
    # Click text=Monto secundarioMoneda de pagoDólar >> [placeholder="Escriba el monto"]
    page.locator("text=Monto secundarioMoneda de pagoDólar >> [placeholder=\"Escriba el monto\"]").click()
    # Fill text=Monto secundarioMoneda de pagoDólar >> [placeholder="Escriba el monto"]
    page.locator("text=Monto secundarioMoneda de pagoDólar >> [placeholder=\"Escriba el monto\"]").fill("2903.00")
    
    # Click text=Cambio 2.35:
    page.locator("text=2.35").click()
    page.screenshot(path="screenshots/ModuloPOS7.png")
     
    #STARTS ModuloPosVenta8_FinalizarVentas.py

    # Click text=Finalizar venta
    page.locator("text=Finalizar venta").click()
    expect(page.locator(".status")).to_have_text("COMPRA REALIZADA CON EXITO")
    #---------------Bug--------------#
    page.wait_for_timeout(3000)#3 SECONDS
    page.screenshot(path="screenshots/ModuloPOS8.png")
    # Click text=3.40
    

    # EXPECT Message  
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
