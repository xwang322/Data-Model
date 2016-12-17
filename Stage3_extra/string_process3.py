from py_stringmatching import simfunctions, tokenizers
import re
def string_process3(line):
    line_new = re.sub(r'[],[()]', '', line)
    line_temp = re.sub(r'\<.*?\>', ' ', line_new)
    line_temp2 = line_temp.replace('&nbsp;', ' ')
    line_temp3 = re.sub(r'&#x\w\w\w\w;', ' ', line_temp2)
    line_tmp = tokenizers.whitespace(line_temp3)
    for each in line_tmp:
        if(each == '-'):
            line_tmp.remove(each)
            continue
        if(each == '/'):
            line_tmp.remove(each)
            continue
        if(each == ':'):
            line_tmp.remove(each)
            continue
        if(each == '.'):
            line_tmp.remove(each)
            continue
        if(each == '&'):
            line_tmp.remove(each)
            continue
        if('*' in each):
            each_tmp = re.sub(r'\*+', '',each)
            each_tmp.strip();
            line_tmp[line_tmp.index(each)] = each_tmp
            continue
        if(each[len(each)-1] == ':'):
            line_tmp[line_tmp.index(each)] = each[:-1]
            continue
        if(each[len(each)-1] == '.'):
            line_tmp[line_tmp.index(each)] = each[:-1]
            continue
    #print(line_tmp)
    #print(set(line_tmp))	
    return line_tmp;
a = "RCA style Keystone Jack- Coupler type (female connectors on the front and back). For use with Keystone panels or wall plates. *Monoprice continually strives to improve its product line to bring our customers the best products available. Therefore changes may be made to listed specifications without prior notice. Item received may not match photo or specs shown.&#xFFFD; &#xFFFD;*The color indicated can vary in tone and/or hue between production runs and manufacturing facilities.&#xFFFD; The color of this item may not be an exact match to any other product even if they are indicated as being the same color whether sold by Monoprice or any other vendor.&#xFFFD; Individual pieces may also vary very slightly in color from each other." 
b = "<!-- CNET Content -->The Lexmark 250-Sheet Drawer supports A4, A5, JIS B5, Letter, Legal, Executive, Folio, Oficio and Statement sizes. Paper (16 to 24 lb., 60 to 90 gsm) and paper labels may be used from this drawer. It also includes a 250-Sheet Tray.<br><br><h3 id=detailspecs>Specifications</h3><span class=font_size3bold>General</span><br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Product Type: &nbsp;Media drawer and tray<br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Total Media Capacity: &nbsp;250 sheets in 1 tray(s)<br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Media Type: &nbsp;Labels, plain paper<br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Media Sizes: &nbsp;Letter A Size (8.5 in x 11 in), Legal (8.5 in x 14 in), Executive (7.25 in x 10.5 in), A4 (8.25 in x 11.7 in), A5 (5.83 in x 8.25 in), Folio (8.5 in x 13 in), JIS B5 (7.17 in x 10.12 in), Statement (5.5 in x 8.5 in), Oficio (8.5 in x 13.5 in)<br><br><span class=font_size3bold>Compatibility Information</span><br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Designed For: &nbsp;Lexmark E260, 260d, 260dn, 360d, 360dn, 460dn, 460dtn, 460dw Lexmark X264dn<br><!-- END CNET Content -->"
c = "<!-- CNET Content -->The Lexmark W840 2000-Sheet Dual Input supports up to 2000 sheets of 20lb or 75gsm plain paper in A4 A5 JIS-B5 executive and letter sizes as 850 sheets and 1150 sheets side by side. Paper and card stock may be used with the Dual Input.<br><br><h3 id=detailspecs>Specifications</h3><span class=font_size3bold>General</span><br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Product Type: &nbsp;Media drawer and tray<br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Total Media Capacity: &nbsp;2000 sheets in 2 tray(s)<br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Media Type: &nbsp;Plain paper cards<br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Media Sizes: &nbsp;Letter A Size (8.5 in x 11 in) Executive (7.25 in x 10.5 in) A4 (8.25 in x 11.7 in) A5 (5.83 in x 8.25 in) JIS B5 (7.17 in x 10.12 in)<br><br><span class=font_size3bold>Miscellaneous</span><br>&nbsp;<img align=absmiddle src=http://images.highspeedbackbone.net/main/gfx-blkbullet.jpg>&nbsp;&nbsp;Features: &nbsp;Wheels<br><!-- END CNET Content -->"
d = "<b><U>Technical Information</U><BR></b><br><b>Connectivity Technology:</b> Wired<br><b>Sound Mode:</b> Stereo<br><b>Features:</b> Adjustable Headband<br><br><b><U>Earpiece</U><BR></b><br><b>Earpiece Design:</b> Over-the-head<br><b>Earpiece Controls:</b> Volume<br><br><b><U>Physical Characteristics</U><BR></b><br><b>Printed Design/Pattern/Texture:</b> Swampy<br><br><b><U>Miscellaneous</U><BR></b><br><b>Certifications & Standards:</b> <p>CE</p>"
e = "A High Speed HDMI Cable is the best way to ensure that you have the ability to pass all the signals authorized in the latest HDMI feature specification.<br><br>Ferrite Cores are small magnetic blocks wrapped around the end of a cable. They are used to suppress EMI/RFI electronic noise on the cable by absorbing the unwanted high frequencies and dissipating them as very low-level heat. This is the simplest and cheapest form of electronic noise reduction and is most effective on small gauge cabling, which is inherently more susceptible to electronic noise interference than thicker cables.<br><br><b>This cable supports the following HDMI features:</b><br><br>* 1080p Resolution<br>* HDMI Ethernet Channel<br>* Audio Return Channel<br>* 3D<br>* 4K<br>* Deep Color<br>* x.v.Color<br>* High Definition Audio<br><br><br>*** 30-day easy returns. No restocking fee. Free lifetime technical support. Limited lifetime warranty. ***"
f = "Rating 194 Degrees (F Application) For Indoor Use Standards UL<br><b>Features</b><ul><li>Application : For Indoor Use</li><li>Color : White</li><li>Gauge/Conductor : 14/3 with Ground</li><li>Item : Nonmetallic Building Cable</li><li>Max. Amps : 15</li><li>Max. Voltage : 600</li><li>Nominal Outside Dia. (In.) : 0.307</li><li>Number of Conductors : 3 with Ground</li><li>Spool/Coil Length (Ft.) : 100</li><li>Temp. Range (F) : 194</li><li>Type : Nonmetallic</li><li>Wire Size : 14 AWG</li><li>Cable Type : NM-B</li><li>Description/Special Features : For Indoor Use</li><li>Jacket Color : White</li><li>Jacket Type : PVC</li><li>Spool Length : 100 ft.</li><li>Voltage : 600V</li><li>Jacket Material : PVC</li><li>Standards : UL</li><li>Conductor : THHN</li><li>Temp. Rating : 194 Degrees F</li><li>Nominal Outside Dia. : 0.307</li><li>Stranded / Solid : Solid</li></ul>"
g = 'lexmark 18c0031 - 18c0533 photo ink cartridge<br><br>produces stunning prints with bold, crisp details. uses an advanced formula that resists smudging, streaking, and fading. stays clog-free throughout the life of the cartridge. this cartridge generates optimum print quality. device types: inkjet printer; oem/compatible: oem; page-yield: 130; supply type: ink.<br><b>what it is and why you need it</b><br><br><ul><li>oem ink cartridge for lexmark color jetprinter x5250, 5270, z816.<li>stunning prints with bold, crisp details.<li>advanced formula.<li>stays clog-free.<li>optimum print quality.</ul>'
string_process3(g)