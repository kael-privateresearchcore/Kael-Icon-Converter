import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel


class DropArea(QFrame):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.file_path = None
        self.setMinimumHeight(220)

        self.icon_label = QLabel("📂")
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_label.setStyleSheet("font-size: 52px; background: transparent;")

        self.label = QLabel("Drag & Drop Image Here")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: #E0E0E0;
                font-size: 18px;
                font-weight: bold;
                background: transparent;
                letter-spacing: 0.5px;
            }
        """)

        self.sub_label = QLabel("PNG, JPG, JPEG, BMP, WEBP")
        self.sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sub_label.setStyleSheet("""
            QLabel {
                color: #AAAAAA;
                font-size: 12px;
                background: transparent;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.addStretch()
        layout.addWidget(self.icon_label)
        layout.addWidget(self.label)
        layout.addWidget(self.sub_label)
        layout.addStretch()
        self.setLayout(layout)

        self.setStyleSheet("""
            QFrame {
                border: 2px dashed rgba(0, 255, 255, 120);
                border-radius: 24px;
                background-color: rgba(0, 0, 0, 80);
            }
            QFrame:hover {
                border: 2px dashed cyan;
                background-color: rgba(0, 255, 255, 20);
            }
        """)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setStyleSheet("""
                QFrame {
                    border: 2px solid cyan;
                    border-radius: 24px;
                    background-color: rgba(0, 255, 255, 40);
                }
            """)

    def dragLeaveEvent(self, event):
        self.setStyleSheet("""
            QFrame {
                border: 2px dashed rgba(0, 255, 255, 120);
                border-radius: 24px;
                background-color: rgba(0, 0, 0, 80);
            }
            QFrame:hover {
                border: 2px dashed cyan;
                background-color: rgba(0, 255, 255, 20);
            }
        """)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.file_path = urls[0].toLocalFile()
            filename = os.path.basename(self.file_path)
            self.label.setText(f"✅ {filename}")
            self.sub_label.setText("Ready for conversion")
            self.icon_label.setText("🖼️")
            main_window = self.window()
            if hasattr(main_window, 'show_preview'):
                main_window.show_preview(self.file_path)
            event.acceptProposedAction()
        self.dragLeaveEvent(event)