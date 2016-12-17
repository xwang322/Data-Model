from bs4 import BeautifulSoup

html = """<html><head></head><body><h1>Hamlet</h1><ul class="cast"><li>Hamlet</li><li>Polonius</li><li>Ophelia</li><li>Claudius</li></ul></body></html"""
html1 = """Coaxial Cable Type RG6/U Shielding 1 Foil 1 Braid Conductor Size 18 AWG Impedance 75 Ohms Spool Length 1000 Feet Nominal Outside Diameter 0.270 Inch Capacitance per Feet 17.3 pF Jacket Type PVC Black Suitable For RF Signal Transmission And Master Antenna Television Systems MATV CATV LANs<br><b>Features</b><ul><li>Capacitance (pF/Ft) : 16.2</li><li>Color : Black</li><li>Conductor Size (AWG) : 18</li><li>Nominal Outside Dia. (In.) : 0.263</li><li>Spool/Coil Length (Ft.) : 1000</li><li>Cable Type : RG6/U</li><li>Impedance (Ohms) : 75</li><li>Jacket Type : PVC</li><li>Shielding : 100% Flexfoil 60% Aluminum Braid</li></ul>"""
soup = BeautifulSoup(html1, "lxml")
for ul in soup.find_all('ul'):
    if "cast" in ul.get('class', []):
        for item in ul.find_all('li'):
            print(item.get_text(), end=", ")