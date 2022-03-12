from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
ui = uic.loadUi("form.ui")
ui.setWindowTitle("KalGUI")

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chislo = ['', '', '', '']
ravno = ""
glob = ['', '', '', '']
znak = ""

def button(vvod):
    global glob
    global a

    vvod = int(vvod)

    ui.line.setText(glob[1] + str(vvod))
    a[vvod] = ui.line.text()

    ui.label.setText(glob[2] + str(vvod))
    glob[2] = ui.label.text()

    print(a[vvod])
    print(glob[2])

    glob[1] = a[vvod]

def znak_f (znak_vvod):

    global glob
    global chislo
    global znak

    chislo[1] = glob[1]
    glob[1] = ""
    ui.line.setText(znak_vvod)
    znak = znak_vvod

    ui.label.setText(glob[2] + znak_vvod)
    glob[2] = ui.label.text()

    print(znak)

def ravno():
    global chislo
    global ravno
    global znak

    chislo[2] = glob[1]

    if znak == "+":
        ravno = int(chislo[1]) + int(chislo[2])
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)

    if znak == "-":
        ravno = int(chislo[1]) - int(chislo[2])
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)

    if znak == "/":
        ravno = int(chislo[1]) / int(chislo[2])
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)

    if znak == "*":
        ravno = int(chislo[1]) * int(chislo[2])
        ravno = str(ravno)
        ui.line.setText(ravno)
        print(ravno)

def stiranie():
    global chislo
    global glob
    global znak

    chislo[1] = ""
    chislo[2] = ""
    glob[1] = ""
    glob[2] = ""
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
ui.b_p.clicked.connect(lambda: znak_f("+"))
ui.b_m.clicked.connect(lambda: znak_f("-"))
ui.b_u.clicked.connect(lambda: znak_f("*"))
ui.b_d.clicked.connect(lambda: znak_f("/"))
ui.b_r.clicked.connect(ravno)
ui.b_ce.clicked.connect(stiranie)

ui.show()
app.exec()