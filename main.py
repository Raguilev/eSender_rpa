import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import RPAConfigUI

def main():
    app = QApplication(sys.argv)
    ventana = RPAConfigUI()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()