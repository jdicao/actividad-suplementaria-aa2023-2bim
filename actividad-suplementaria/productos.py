# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from base_datos import conn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpProductos = QtWidgets.QGroupBox(self.centralwidget)
        self.grpProductos.setGeometry(QtCore.QRect(10, 10, 881, 80))
        self.grpProductos.setAutoFillBackground(True)
        self.grpProductos.setObjectName("grpProductos")
        self.label = QtWidgets.QLabel(self.grpProductos)
        self.label.setGeometry(QtCore.QRect(10, 30, 33, 16))
        self.label.setObjectName("label")
        self.txtCodigo = QtWidgets.QLineEdit(self.grpProductos)
        self.txtCodigo.setGeometry(QtCore.QRect(48, 30, 94, 20))
        self.txtCodigo.setObjectName("txtCodigo")
        self.label_2 = QtWidgets.QLabel(self.grpProductos)
        self.label_2.setGeometry(QtCore.QRect(161, 30, 54, 16))
        self.label_2.setObjectName("label_2")
        self.txtDescripcion = QtWidgets.QLineEdit(self.grpProductos)
        self.txtDescripcion.setGeometry(QtCore.QRect(220, 30, 251, 20))
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.label_3 = QtWidgets.QLabel(self.grpProductos)
        self.label_3.setGeometry(QtCore.QRect(483, 30, 70, 16))
        self.label_3.setObjectName("label_3")
        self.cboUnidad = QtWidgets.QComboBox(self.grpProductos)
        self.cboUnidad.setGeometry(QtCore.QRect(558, 30, 69, 20))
        self.cboUnidad.setObjectName("cboUnidad")
        # Añadir unidades de media al QComboBox
        unidades = ["Unidad", "Kilos", "Metros"]
        self.cboUnidad.addItems(unidades)

        self.label_4 = QtWidgets.QLabel(self.grpProductos)
        self.label_4.setGeometry(QtCore.QRect(632, 30, 43, 16))
        self.label_4.setObjectName("label_4")
        self.txtCantidad = QtWidgets.QLineEdit(self.grpProductos)
        self.txtCantidad.setGeometry(QtCore.QRect(680, 30, 51, 20))
        self.txtCantidad.setObjectName("txtCantidad")
        self.btnGuardar = QtWidgets.QPushButton(self.grpProductos)
        self.btnGuardar.setGeometry(QtCore.QRect(760, 20, 75, 41))
        self.btnGuardar.setObjectName("btnGuardar")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 881, 441))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.lstProductos = QtWidgets.QTableWidget(self.groupBox)
        self.lstProductos.setGeometry(QtCore.QRect(10, 50, 861, 381))
        self.lstProductos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lstProductos.setObjectName("lstProductos")
        self.lstProductos.setColumnCount(0)
        self.lstProductos.setRowCount(0)
        self.btnActualizar = QtWidgets.QPushButton(self.groupBox)
        self.btnActualizar.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnActualizar.setObjectName("btnActualizar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # guardar
        self.crear_base()
        self.obtener_informacion()
        self.btnGuardar.clicked.connect(self.guardar_informacion)
        self.btnActualizar.clicked.connect(self.obtener_informacion)
        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grpProductos.setTitle(_translate("MainWindow", "Datos del producto"))
        self.label.setText(_translate("MainWindow", "Código"))
        self.label_2.setText(_translate("MainWindow", "Descripción"))
        self.label_3.setText(_translate("MainWindow", "Unidad Medida"))
        self.label_4.setText(_translate("MainWindow", "Cantidad"))
        self.btnGuardar.setText(_translate("MainWindow", "Ingresar"))
        self.groupBox.setTitle(_translate("MainWindow", "Productos ingresados"))
        self.btnActualizar.setText(_translate("MainWindow", "Actualizar"))

    def crear_base(self):
        cursor = conn.cursor()
        cadena_sql = 'CREATE TABLE Producto (codigo TEXT, descripcion TEXT, unidad_medida TEXT, cantidad INTEGER)'
        try:
            cursor.execute(cadena_sql)
        except:
            pass
        cursor.close()

    def guardar_informacion(self):

        codigo = str(self.txtCodigo.text())
        descripcion = str(self.txtDescripcion.text())
        try:
            unidad_medida = str(self.cboUnidad.currentText())
        except:
            unidad_medida
        try:
            cantidad = int(self.txtCantidad.text())
        except:
            cantidad = 0

        #validar que todos los campos se llenen
        if codigo == "" or descripcion == "" or cantidad == 0 or unidad_medida == "":
            # Crear una instancia de QMessageBox
            message_box = QMessageBox(MainWindow)
            # Establecer el título del cuadro de diálogo
            message_box.setWindowTitle('Validacion')
            # Establecer el texto del mensaje
            message_box.setText('Ingrese todos los campos requeridos!')

            # Agregar botones personalizados (opcional)
            message_box.addButton('Aceptar', QMessageBox.YesRole)
            # Mostrar el cuadro de diálogo de mensaje
            result = message_box.exec_()
        else :
            cursor = conn.cursor()
            cadena_sql = """INSERT INTO Producto (codigo, descripcion, unidad_medida, cantidad) VALUES ('%s', '%s', '%s', %d);""" % \
            (codigo, descripcion, unidad_medida, cantidad)
            print(cadena_sql)
            # ejecutar el SQL
            cursor.execute(cadena_sql)
            # confirmar los cambios
            conn.commit()
            cursor.close()
            #limpiar los campor
            self.txtCodigo.setText('')
            self.txtDescripcion.setText('')
            self.cboUnidad.setCurrentIndex(0)
            self.txtCantidad.setText('')
            #recuperar los registros
            self.obtener_informacion()    

    def obtener_informacion(self):
        cursor = conn.cursor()
        cadena_consulta_sql = "SELECT * from Producto"
        cursor.execute(cadena_consulta_sql)
        informacion = cursor.fetchall()
        database_table_column_count = 4
        self.lstProductos.setColumnCount(database_table_column_count)
        #cabecera de las columnas
        cabecera = ['Codigo', 'Descripcion', 'Unidad Medida','Cantidad']
        self.lstProductos.setHorizontalHeaderLabels(cabecera)

        numero_filas = len(informacion)
        self.lstProductos.setRowCount(numero_filas)
        for j in range(numero_filas):
            valor = informacion[j]
            for i in range(0, len(valor)):
                elemento = valor[i]
                elemento = str(elemento)
                nuevo_registro = QtWidgets.QTableWidgetItem(elemento)
                self.lstProductos.setItem(j, i, nuevo_registro)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Registro de Productos')
    MainWindow.show()
    sys.exit(app.exec_())
