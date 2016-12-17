from py_stringmatching import simfunctions, tokenizers
import re
import json

def JsonLongDescription(line):
    feature = []
    ul = re.findall(r'<ul>.*</ul>', line)
    ul = ''.join(ul)
    ul1 = ul.replace('<ul>','')
    ul2 = ul1.replace('</ul>','')
    li = ul2.replace('<li>', '  ')
    li = li.replace('</li>','  ')
    li_items = li.split('  ')
    for each in li_items:
        each1 = re.sub(r'<b>','', each)
        each2 = re.sub(r'</b>','', each1)
        #print(each2)
        each3 = re.sub(r'&quot','',each2)
        each4 = each3.strip()
        #print(each4)
        if ':' in each4:
            feature.append(each4)
    #print(feature)
    return feature


a = "Coaxial Cable Type RG6/U Shielding 1 Foil 1 Braid Conductor Size 18 AWG Impedance 75 Ohms Spool Length 1000 Feet Nominal Outside Diameter 0.270 Inch Capacitance per Feet 17.3 pF Jacket Type PVC Black Suitable For RF Signal Transmission And Master Antenna Television Systems MATV CATV LANs<br><b>Features</b><ul><li>Capacitance (pF/Ft) : 16.2</li><li>Color : Black</li><li>Conductor Size (AWG) : 18</li><li>Nominal Outside Dia. (In.) : 0.263</li><li>Spool/Coil Length (Ft.) : 1000</li><li>Cable Type : RG6/U</li><li>Impedance (Ohms) : 75</li><li>Jacket Type : PVC</li><li>Shielding : 100% Flexfoil 60% Aluminum Braid</li></ul>"
b = "The Cables To Go 43060 250ft RG6/U Dual Shield In-Wall Coaxial Cable is ideal for antenna, cable television and satellite installations. The Cables To Go 43060 250ft RG6/U Dual Shield In-Wall Coaxial Cable has an 18 AWG copper clad steel center conductor surrounded by a foam polyethylene dielectric. A bonded aluminum foil and 60% aluminum braid provide 100% shield coverage. The Cables To Go 43060 250ft RG6/U Dual Shield In-Wall Coaxial Cable can be used for CL1, CL2, CM, CMX and CMG installations. Swept tested to 3 GHz to ensure performance at applicable frequencies. To help you keep track of cable used, the cable jacket is sequentially marked every two feet."
c = "VeraLite is the simplest, most affordable way to start making your smart home smart and creating powerful new possibilities for yourself and your family.Compact but armed with plenty of brains and muscle, the VeraLite smart controller instantly turns a home or apartment into a personal assistant for your busy life.It makes possible all kinds of conveniences and savings that youll appreciate from day one, and come to love more and more over time as you start to see all the things it can do for you.VeraLite is the gateway to all these benefits:  EASY HOME SECURITY Keep watch over your home! VeraLite manages cameras, controls door locks and alerts you to activity when needed. Youll always know that everyones ok.  REDUCTIONS IN ENERGY BILLS VeraLite lets you see and control household energy consumption and tailor it for savings every month, automatically or by remote control.   IMPORTANT ALERTS Wouldnt you love to get an email or text that the kids got home s"
d = "Featuring slick design and a built-in battery pack VeraLites setup -- both to your network and to the devices you want to control -- is fast and convenient. It gives you virtually unlimited options for controlling individual devices and also devices that have been grouped together in a room or as part of a unified control scene. Getting VeraLite up and going is dead simple. Just plug it into an open port in your Wi-Fi router and in less than a minute youve got a complete home control station ready to roll."
e = "<ul><li><b>Product Material:</b> Nylon</li><li><b>Product Weight:</b> 2 lbs.</li><li><b>Laptop Compartment Dimensions:</b> 14.5&quot; x 12&quot; x 2.5&quot;</li><li>You need your notebook computer safely secure and easily accessible.</li><li>One storage compartment keeps your files.</li><li>Organizer pocket provides added storage for miscellaneous items.</li><li>This compact design provides a no muss, no fuss solution for the light traveler.</li></ul>"
f = "UMX1183<br/>Features:<ul><li>Notebook case</li><li>Outside pocket with mobile phone compartment</li><li>Fits iPad netbooks or other tablet PC up to 10.2</li><li>Inside accessory pocket</li><li>Inside soft padded safety compartment</li><li>Messenger bag style sling with adjustable velcro strap</li></ul><br/>     Dimensions:<ul><li>Dimensions: 9.25 Depth x 2.5 Width x 11 Height</li></ul><br/>"
g = "<br><b>Spellbinders M-Bossabilities Folders, Music:</b><ul><li>Each folder measures 7-1/2 x 5-1/4 and has design sizes of 7 x 5<li>This package contains one embossing folder<li>Deign: Music<li>Imported</ul>"
#JsonLongDescription(g)