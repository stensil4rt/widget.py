from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
ui = uic.loadUi("form.ui")
ui.setWindowTitle("KalGUI")


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

chislo1 =""
chislo2 =""
ravno = ""
glob1 = ""
glob2 = ""
glob3 = ""
znak = ""

def button(vvod):
    global glob1
    global glob2
    global glob3
    global a

    vvod = int(vvod)

    ui.line.setText(glob1 + str(vvod))
    a[vvod] = ui.line.text()

    ui.label.setText(glob2 + str(vvod))
    glob2 = ui.label.text()

    print(a[vvod])
    print(glob2)

    glob1 = a[vvod]

def znak (znak_vvod):
    global glob1
    global glob2
    global chislo1
    global chislo2
    global znak


    chislo1 = glob1
    glob1 = ""
    ui.line.setText(znak_vvod)
    znak = znak_vvod

    ui.label.setText(glob2 + znak_vvod)
    glob2 = ui.label.text()

    print(znak)


def ravno():
    global chislo1
    global chislo2
    global ravno
    global znak

    chislo2 = glob1

    if znak == "+":
        ravno = int(chislo1) + int(chislo2)
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)
    if znak == "-":
        ravno = int(chislo1) - int(chislo2)
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)

    if znak == "/":
        ravno = int(chislo1) / int(chislo2)
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)

    if znak == "*":
        ravno = int(chislo1) * int(chislo2)
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)

def stiranie():
    global chislo1
    global chislo2
    global glob1
    global glob2
    global g_odin
    global g_dva
    global znak

    chislo1 = ""
    chislo2 = ""
    glob1 = ""
    glob2 = ""
    g_odin = ""
    g_dva = ""
    znak = ""
    ui.line.setText("0")
    ui.label.setText("0")

ui.b_0.clicked.connect(lambda: button(0))
ui.b_1.clicked.connect(lambda: button(1))
ui.b_2.clicked.connect(lambda: button(2))
ui.b_3.clicked.connect(lambda: button(3))
ui.b_4.clicked.connect(lambda: button(4))
ui.b_5.clicked.connect(lambda: button(5))
ui.b_6.clicked.connect(lambda: button(6))
ui.b_7.clicked.connect(lambda: button(7))
ui.b_8.clicked.connect(lambda: button(8))
ui.b_9.clicked.connect(lambda: button(9))
ui.b_p.clicked.connect(lambda: znak("+"))
ui.b_m.clicked.connect(lambda: znak("-"))
ui.b_u.clicked.connect(lambda: znak("*"))
ui.b_d.clicked.connect(lambda: znak("/"))
ui.b_r.clicked.connect(ravno)
ui.b_ce.clicked.connect(stiranie)

ui.show()
app.exec()
