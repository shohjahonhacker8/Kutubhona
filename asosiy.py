from datetime import date

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QHeaderView, QMessageBox
from my_library2 import Ui_Form
from db_manager import DbManager


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.setWindowIcon(QIcon(":/img/rasmlar/book_5_24dp_EA3323_FILL0_wght400_GRAD0_opsz24.png"))
        self.chap_kichik_menu.setVisible(False)
        self.btn_asosiy_sahifa.click()
        self.db = DbManager()

        # kitoblar bo'limi
        self.btn_menu_kitoblar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_menu_kitoblar2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.kitob_orqaga.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        # talabalar bo'limi
        self.btn_menu_talabalar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_menu_talabalar2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.talaba_orqaga.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.talaba_kiritish.clicked.connect(self.talabani_kirit)
        self.talaba_ochirish.clicked.connect(self.talabani_ochir)
        self.tbl_talabalar.itemSelectionChanged.connect(self.talabani_tanlaganda)
        self.talaba_ozgartirish.clicked.connect(self.talabani_ozgartir)

        self.kurslarni_yukla()
        self.talabalarni_yukla()
        self.kitoblarni_yukla()
        self.kitob_kiritish.clicked.connect(self.kitobni_kirit)
        self.tableWidget.itemSelectionChanged.connect(self.kitobni_tanlaganda)
        self.kitob_ozgartirish.clicked.connect(self.kitobni_ozgartir)
        self.kitob_ochirish.clicked.connect(self.kitobni_ochir)

        # KITOB BERISH BO'LIMI
        self.btn_menu_olingan_kitoblar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_menu_olingan_kitoblar2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_orqaga_kitob_berish.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.edt_talaba_qidirish.textChanged.connect(lambda: self.talabani_yuklash())
        self.tbl_talaba_qidirish.itemSelectionChanged.connect(self.talabani_tanla)
        self.edt_kitob_qidirish.textChanged.connect(lambda: self.kitobni_yuklash())
        self.tbl_kitob_qidirish.itemSelectionChanged.connect(self.kitobni_tanla)

        self.dt_olinadigan.setDate(date.today())
        self.dt_olinadigan.dateChanged.connect(self.beriladigan_sanani_ozgartir)
        self.beriladigan_sanani_ozgartir()

        self.btn_kitob_berish.clicked.connect(self.kitob_berish)

        self.talabani_yuklash()
        self.kitobni_yuklash()
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    # KURSLAR BO'LIMI
    def kurslarni_yukla(self):
        self.talaba_kursi.clear()
        rows = self.db.kurs()
        for row in rows:
            self.talaba_kursi.addItem(row[1], row[0])

    # KITOBLAR BO'LIMI
    def kitoblarni_yukla(self):
        USTUN_NOMLARI = ["id", "Nomi", "Muallifi", "Soni"]
        rows = self.db.kitoblar()
        self.tableWidget.setColumnCount(len(USTUN_NOMLARI))
        self.tableWidget.setHorizontalHeaderLabels(USTUN_NOMLARI)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnHidden(0, True)

        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 50)

        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)

        for index, row in enumerate(rows):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(row[3])))

    def kitobni_kirit(self):
        nomi = self.kirit_kitob_nomi.text()
        muallifi = self.kirit_kitob_muallifi.text()
        soni = int(self.kirit_kitob_soni.text())
        id_ = self.db.kitob_kirit(nomi, muallifi, soni)
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(id_)))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(str(nomi)))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(muallifi)))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(soni)))

    def kitobni_tanlaganda(self):
        row = self.tableWidget.currentRow()
        id_ = int(self.tableWidget.item(row, 0).text())
        nomi = self.tableWidget.item(row, 1).text()
        muallifi = self.tableWidget.item(row, 2).text()
        soni = int(self.tableWidget.item(row, 3).text())
        self.kirit_kitob_nomi.setText(nomi)
        self.kirit_kitob_muallifi.setText(muallifi)
        self.kirit_kitob_soni.setText(str(soni))
        self.db.kitob_yangila(id_, nomi, muallifi, soni)

    def kitobni_ozgartir(self):
        row = self.tableWidget.currentRow()
        id_ = int(self.tableWidget.item(row, 0).text())
        nomi = self.kirit_kitob_nomi.text()
        muallifi = self.kirit_kitob_muallifi.text()
        soni = self.kirit_kitob_soni.text()

        self.tableWidget.setItem(row, 1, QTableWidgetItem(str(nomi)))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(muallifi)))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(str(soni)))

    def kitobni_ochir(self):
        row = self.tableWidget.currentRow()
        id_ = int(self.tableWidget.item(row, 0).text())
        self.db.kitob_ochir(id_)

        self.tableWidget.removeRow(row)

    # TALABALAR BO'LIMI
    def talabalarni_yukla(self):
        USTUN_NOMLARI2 = ["id", "Ismi", "Yo'nalishi", "kurs_id"]
        rows = self.db.talabalar()
        self.tbl_talabalar.setColumnCount(len(USTUN_NOMLARI2))
        self.tbl_talabalar.setHorizontalHeaderLabels(USTUN_NOMLARI2)
        self.tbl_talabalar.setRowCount(len(rows))
        self.tbl_talabalar.setColumnHidden(0, True)
        self.tbl_talabalar.setColumnHidden(3, True)

        self.tbl_talabalar.setColumnWidth(0, 50)
        self.tbl_talabalar.setColumnWidth(1, 200)
        self.tbl_talabalar.setColumnWidth(2, 200)
        self.tbl_talabalar.setColumnWidth(3, 50)

        self.tbl_talabalar.setSelectionBehavior(QTableWidget.SelectRows)

        for index, row in enumerate(rows):
            self.tbl_talabalar.setItem(index, 0, QTableWidgetItem(str(row[0])))
            self.tbl_talabalar.setItem(index, 1, QTableWidgetItem(str(row[1])))
            self.tbl_talabalar.setItem(index, 2, QTableWidgetItem(str(row[2])))
            self.tbl_talabalar.setItem(index, 3, QTableWidgetItem(str(row[3])))

    def talabani_kirit(self):
        nomi = self.kirit_talaba_ismi.text()
        kurs_id = self.talaba_kursi.currentData()
        kurs_nomi = self.talaba_kursi.currentText()
        talaba_id = self.db.talaba_kirit(nomi, kurs_id)

        self.tbl_talabalar.insertRow(0)
        self.tbl_talabalar.setItem(0, 0, QTableWidgetItem(str(talaba_id)))
        self.tbl_talabalar.setItem(0, 1, QTableWidgetItem(str(nomi)))
        self.tbl_talabalar.setItem(0, 2, QTableWidgetItem(str(kurs_nomi)))
        self.tbl_talabalar.setItem(0, 3, QTableWidgetItem(str(kurs_id)))

    def talabani_tanlaganda(self):
        row = self.tbl_talabalar.currentRow()
        talaba_id = int(self.tbl_talabalar.item(row, 0).text())
        nomi = self.tbl_talabalar.item(row, 1).text()
        kurs_nomi = self.tbl_talabalar.item(row, 2).text()
        kursd_id = int(self.tbl_talabalar.item(row, 3).text())

        self.kirit_talaba_ismi.setText(nomi)
        self.set_talaba_kursi(kursd_id)

    def set_talaba_kursi(self, kurs_id):
        for index in range(self.talaba_kursi.count()):
            id_ = self.talaba_kursi.itemData(index)
            if id_ == kurs_id:
                self.talaba_kursi.setCurrentIndex(index)
                break

    def talabani_ochir(self):
        row_list = [item.row() for item in self.tbl_talabalar.selectedItems()]
        row_list = set(row_list)

        if row_list:
            response = QMessageBox.question(self, "Savol", "Haqiqatdan ham o'chirmoqchimisiz?",
                                            QMessageBox.Yes | QMessageBox.No)
            if response == QMessageBox.Yes:
                for row in sorted(row_list, reverse=True):
                    talaba_id = self.tbl_talabalar.item(row, 0).text()
                    self.db.talaba_ochir(talaba_id)
                    self.tbl_talabalar.removeRow(row)

    def talabani_ozgartir(self):
        row = self.tbl_talabalar.currentRow()
        talaba_id = int(self.tbl_talabalar.item(row, 0).text())
        talaba_ismi = self.kirit_talaba_ismi.text()
        kurs_id = self.talaba_kursi.currentData()
        kurs_nomi = self.talaba_kursi.currentText()

        self.db.talaba_yangila(talaba_id, talaba_ismi, kurs_id)

        self.tbl_talabalar.setItem(row, 1, QTableWidgetItem(str(talaba_ismi)))
        self.tbl_talabalar.setItem(row, 2, QTableWidgetItem(str(kurs_nomi)))
        self.tbl_talabalar.setItem(row, 3, QTableWidgetItem(str(kurs_id)))

    # Kitob berish

    def talabani_yuklash(self):
        keyword = self.edt_talaba_qidirish.text()
        self.tbl_talaba_qidirish.clear()
        rows = self.db.talabalarni_top(keyword)
        COLUMNS = ["id", "Talaba"]
        self.tbl_talaba_qidirish.setColumnCount(len(COLUMNS))
        self.tbl_talaba_qidirish.setHorizontalHeaderLabels(COLUMNS)
        self.tbl_talaba_qidirish.setRowCount(len(rows))
        self.tbl_talaba_qidirish.setColumnWidth(0, 10)
        self.tbl_talaba_qidirish.setColumnWidth(1, 250)
        self.tbl_talaba_qidirish.setColumnHidden(0, True)

        for row, item in enumerate(rows):
            self.tbl_talaba_qidirish.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tbl_talaba_qidirish.setItem(row, 1, QTableWidgetItem(str(item[1])))

    def talabani_tanla(self):
        row = self.tbl_talaba_qidirish.currentRow()
        # talaba_id = self.tbl_talaba_qidirish.item(row, 0).text()
        talaba = self.tbl_talaba_qidirish.item(row, 1).text()
        self.edt_kitob_oluvchi.setText(talaba)

    def kitobni_yuklash(self):
        keyword = self.edt_kitob_qidirish.text()
        self.tbl_kitob_qidirish.clear()
        rows = self.db.kitobni_top(keyword)
        COLUMNS = ["id", "Kitob"]
        self.tbl_kitob_qidirish.setColumnCount(len(COLUMNS))
        self.tbl_kitob_qidirish.setHorizontalHeaderLabels(COLUMNS)
        self.tbl_kitob_qidirish.setRowCount(len(rows))
        self.tbl_kitob_qidirish.setColumnWidth(0, 10)
        self.tbl_kitob_qidirish.setColumnWidth(1, 250)
        self.tbl_kitob_qidirish.setColumnHidden(0, True)

        for row, item in enumerate(rows):
            self.tbl_kitob_qidirish.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tbl_kitob_qidirish.setItem(row, 1, QTableWidgetItem(str(item[1])))

    def kitobni_tanla(self):
        row = self.tbl_kitob_qidirish.currentRow()
        # kitob_id = self.tbl_kitob_qidirish.item(row, 0).text()
        kitob = self.tbl_kitob_qidirish.item(row, 1).text()
        self.edt_olinadigan_kitob.setText(kitob)

    def beriladigan_sanani_ozgartir(self):
        dt = self.dt_olinadigan.date()
        dt = dt.addDays(2)
        self.dt_beriladigan.setDate(dt)

    def kitob_berish(self):
        if self.edt_kitob_oluvchi.text() and self.edt_olinadigan_kitob.text():
            row = self.tbl_kitob_qidirish.currentRow()
            kitob_id = self.tbl_kitob_qidirish.item(row, 0).text()

            row = self.tbl_talaba_qidirish.currentRow()
            talaba_id = self.tbl_talaba_qidirish.item(row, 0).text()

            olingan_sana = self.dt_olinadigan.date()
            berilgan_sana = self.dt_beriladigan.date()
            self.db.olk_kirit(olingan_sana.toPython(), berilgan_sana.toPython(), talaba_id, kitob_id)
