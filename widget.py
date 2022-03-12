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
g_nol = ""
g_odin = ""
g_dva = ""
g_tri = ""
g_hetire = ""
g_pyat = ""
g_shest = ""
g_sem = ""
g_vosem = ""
g_devyat = ""
znak = ""

def vvod_cifre():
    ui.label.setText

def nol(a0):
    global glob1
    global glob2
    global glob3
    global a

    ui.line.setText(glob1 + "0")
    a[0] = ui.line.text()

    ui.label.setText(glob2 + "0")
    glob2 = ui.label.text()

    print(a[0])
    print(glob2)

    glob1 = a[0]

def odin(a1):
    global glob1
    global glob2
    global glob3
    global a

    ui.line.setText(glob1 + "1")
    a[1] = ui.line.text()

    ui.label.setText(glob2 + "1")
    a[1] = ui.label.text()

    print(g_odin)
    print(a[1])
    print(glob2)

    glob1 = a[1]

def dva(a2):
    global glob1
    global glob2
    global a

    ui.line.setText(glob1 + "2")
    a[2] = ui.line.text()

    ui.label.setText(glob2 + "2")
    glob2 = ui.label.text()

    print(a[2])

    glob1 = a[2]

def tri(a3):
    global glob1
    global glob2
    global g_tru

    ui.line.setText(glob1 + "3")
    g_tri = ui.line.text()

    ui.label.setText(glob2 + "3")
    glob2 = ui.label.text()

    print(g_tri)

    glob1 = g_tri

def hetire(a4):
    global glob1
    global glob2
    global g_hetire

    ui.line.setText(glob1 + "4")
    g_hetire = ui.line.text()

    ui.label.setText(glob2 + "4")
    glob2 = ui.label.text()

    print(g_hetire)

    glob1 = g_hetire

def pyat(a5):
    global glob1
    global glob2
    global g_pyat

    ui.line.setText(glob1 + "5")
    g_pyat = ui.line.text()

    ui.label.setText(glob2 + "5")
    glob2 = ui.label.text()

    print(g_pyat)

    glob1 = g_pyat

def shest(a6):
    global glob1
    global glob2
    global g_shest

    ui.line.setText(glob1 + "6")
    g_shest = ui.line.text()

    ui.label.setText(glob2 + "6")
    glob2 = ui.label.text()

    print(g_shest)

    glob1 = g_shest

def sem(a7):
    global glob1
    global glob2
    global g_sem

    ui.line.setText(glob1 + "7")
    g_sem = ui.line.text()

    ui.label.setText(glob2 + "7")
    glob2 = ui.label.text()

    print(g_sem)

    glob1 = g_sem

def vosem(a8):
    global glob1
    global glob2
    global g_vosem

    ui.line.setText(glob1 + "8")
    g_vosem = ui.line.text()

    ui.label.setText(glob2 + "8")
    glob2 = ui.label.text()

    print(g_vosem)

    glob1 = g_vosem

def devyat(a9):
    global glob1
    global glob2
    global g_devyat

    ui.line.setText(glob1 + "9")
    g_devyat = ui.line.text()

    ui.label.setText(glob2 + "9")
    glob2 = ui.label.text()

    print(g_devyat)

    glob1 = g_devyat

def plus(text):
    global glob1
    global glob2
    global chislo1
    global chislo2
    global znak

    if (znak == '+'):
        chislo2 = glob1
        glob1 = ""
        slozhenie()
        znak = ""
    else:
        chislo1 = glob1
        glob1 = ""
        ui.line.setText('+')
        znak = '+'
   #     ui.label.setText(chislo1 + "+")

        ui.label.setText(glob2 + "+")
        glob2 = ui.label.text()

        print(znak)

def minus(text):
    global glob1
    global glob2
    global chislo1
    global chislo2
    global znak

    if (znak == '-'):
        chislo2 = glob1
        glob1 = ""
        vichitanie()
        znak = ""
    else:
        chislo1 = glob1
        glob1 = ""
        ui.line.setText('-')
        znak = '-'
   #     ui.label.setText(chislo1 + "+")

        ui.label.setText(glob2 + "-")
        glob2 = ui.label.text()

        print(znak)

def umnozh(text):
    global glob1
    global glob2
    global chislo1
    global chislo2
    global znak

    if (znak == '*'):
        chislo2 = glob1
        glob1 = ""
        vichitanie()
        znak = ""
    else:
        chislo1 = glob1
        glob1 = ""
        ui.line.setText('*')
        znak = '*'
   #     ui.label.setText(chislo1 + "+")

        ui.label.setText(glob2 + "*")
        glob2 = ui.label.text()

        print(znak)

def delit(text):
    global glob1
    global glob2
    global chislo1
    global chislo2
    global znak

    if (znak == '/'):
        chislo2 = glob1
        glob1 = ""
        vichitanie()
        znak = ""
    else:
        chislo1 = glob1
        glob1 = ""
        ui.line.setText('/')
        znak = '/'
   #     ui.label.setText(chislo1 + "/")

        ui.label.setText(glob2 + "/")
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

def slozhenie():
    global chislo1
    global chislo2
    global ravno

    ravno = int(chislo1) + int(chislo2)
    ravno = str(ravno)
    ui.line.setText(ravno)
    print(ravno)

def vichitanie():
    global chislo1
    global chislo2
    global ravno

    ravno = int(chislo1) - int(chislo2)
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

ui.b_0.clicked.connect(nol)
ui.b_1.clicked.connect(odin)
ui.b_2.clicked.connect(dva)
ui.b_3.clicked.connect(tri)
ui.b_4.clicked.connect(hetire)
ui.b_5.clicked.connect(pyat)
ui.b_6.clicked.connect(shest)
ui.b_7.clicked.connect(sem)
ui.b_8.clicked.connect(vosem)
ui.b_9.clicked.connect(devyat)
ui.b_p.clicked.connect(plus)
ui.b_m.clicked.connect(minus)
ui.b_u.clicked.connect(umnozh)
ui.b_d.clicked.connect(delit)
ui.b_r.clicked.connect(ravno)
ui.b_ce.clicked.connect(stiranie)

ui.show()
app.exec()
