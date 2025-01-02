from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QPushButton, QLabel
)

from instr import *
from second_win import *

class MainWin(QWidget):
    def _init_(self):
        # Konstruktor untuk kelas MainWin.
        # Fungsi ini mempersiapkan jendela utama dengan elemen antarmuka pengguna,
        # mengatur tampilan jendela, dan memulai aplikasi.
        super()._init_()
        # Mengatur tampilan jendela
        self.set_appear()
        # Membuat elemen-elemen antarmuka pengguna
        self.initUI()
        # Menyambungkan elemen-elemen antarmuka dengan fungsinya
        self.connects()
        # Menampilkan jendela
        self.show()

    def initUI(self):
        # Membuat elemen-elemen antarmuka pengguna, seperti tombol dan label,
        # serta mengatur tata letak elemen-elemen tersebut di dalam jendela.
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        # Mengatur tata letak elemen
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        # Menyambungkan tombol dengan fungsi yang akan dipanggil saat tombol diklik.
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        # Mengatur tampilan awal jendela, seperti judul, ukuran, dan posisi jendela.
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


def main():
    #Fungsi utama untuk menjalankan aplikasi.
    #Membuat instance QApplication dan MainWin, lalu memulai event loop aplikasi.
    app = QApplication([])
    mw = MainWin()
    app.exec_()


if __name__ == "_main_":
    #Blok ini memastikan bahwa fungsi main hanya akan dijalankan
    #jika file ini dijalankan sebagai skrip utama, bukan diimpor sebagai modul.
    main()