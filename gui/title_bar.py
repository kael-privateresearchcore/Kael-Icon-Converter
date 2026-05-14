from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFixedHeight(48)
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(15, 15, 25, 240);
                border-top-left-radius: 24px;
                border-top-right-radius: 24px;
            }
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding-left: 16px;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                color: #CCCCCC;
                font-size: 16px;
                font-weight: bold;
                width: 46px;
                height: 46px;
                border-radius: 0px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 30);
                color: white;
            }
            #closeBtn:hover {
                background-color: #E81123;
                color: white;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.title_label = QLabel("Kael-Icon Converter")

        self.min_btn = QPushButton("─")
        self.min_btn.clicked.connect(parent.showMinimized)

        self.max_btn = QPushButton("□")
        self.max_btn.clicked.connect(self.toggle_maximize)

        self.close_btn = QPushButton("✕")
        self.close_btn.setObjectName("closeBtn")
        self.close_btn.clicked.connect(parent.close)

        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(self.min_btn)
        layout.addWidget(self.max_btn)
        layout.addWidget(self.close_btn)

    def toggle_maximize(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
            self.max_btn.setText("□")
        else:
            self.parent.showMaximized()
            self.max_btn.setText("❐")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.parent.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if hasattr(self.parent, 'drag_pos') and not self.parent.isMaximized():
            delta = event.globalPosition().toPoint() - self.parent.drag_pos
            self.parent.move(self.parent.pos() + delta)
            self.parent.drag_pos = event.globalPosition().toPoint()

    def mouseDoubleClickEvent(self, event):
        self.toggle_maximize()