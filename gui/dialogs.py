from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QGroupBox, QCheckBox, QDialogButtonBox
)


class SizeSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Icon Sizes")
        self.setModal(True)
        self.setFixedSize(400, 480)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(20, 20, 35);
                border-radius: 20px;
            }
            QGroupBox {
                font-weight: bold;
                color: cyan;
                border: 1px solid rgba(0, 255, 255, 100);
                border-radius: 16px;
                margin-top: 16px;
                padding-top: 12px;
                font-size: 14px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 20px;
                padding: 0 10px;
            }
            QCheckBox {
                color: white;
                spacing: 12px;
                font-size: 14px;
                padding: 6px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border-radius: 6px;
                border: 2px solid cyan;
                background-color: rgba(0,0,0,100);
            }
            QCheckBox::indicator:checked {
                background-color: cyan;
            }
            QPushButton {
                background-color: rgba(0, 255, 255, 30);
                border: 1px solid cyan;
                border-radius: 12px;
                padding: 10px 20px;
                color: cyan;
                font-weight: bold;
                font-size: 14px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: rgba(0, 255, 255, 80);
                color: white;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(24, 24, 24, 24)

        self.std_group = QGroupBox("Standard Sizes (max 256x256)")
        std_layout = QVBoxLayout()
        std_layout.setSpacing(8)
        self.sizes = {
            16: QCheckBox("16 x 16"),
            24: QCheckBox("24 x 24"),
            32: QCheckBox("32 x 32"),
            48: QCheckBox("48 x 48"),
            64: QCheckBox("64 x 64"),
            128: QCheckBox("128 x 128"),
            256: QCheckBox("256 x 256"),
        }
        for cb in self.sizes.values():
            cb.setChecked(False)
            std_layout.addWidget(cb)
        self.std_group.setLayout(std_layout)
        layout.addWidget(self.std_group)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.setStyleSheet("QDialogButtonBox { background: transparent; }")
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_selected_sizes(self):
        return [(w, w) for w, cb in self.sizes.items() if cb.isChecked()]