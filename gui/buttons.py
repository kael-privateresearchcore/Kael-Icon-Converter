from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPushButton


class GlowButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.hue = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_glow)
        self.timer.start(40)
        self.setMinimumHeight(55)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                border-radius: 28px;
                font-size: 15px;
                font-weight: bold;
                color: white;
                background-color: rgba(25, 25, 45, 230);
                border: 2px solid cyan;
                padding: 10px 24px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background-color: rgba(0, 255, 255, 40);
            }
        """)

    def update_glow(self):
        self.hue = (self.hue + 3) % 360
        color = QColor.fromHsv(self.hue, 255, 255)
        self.setStyleSheet(f"""
            QPushButton {{
                border-radius: 28px;
                font-size: 15px;
                font-weight: bold;
                color: white;
                background-color: rgba(25, 25, 45, 230);
                border: 2px solid {color.name()};
                padding: 10px 24px;
                letter-spacing: 1px;
            }}
            QPushButton:hover {{
                background-color: rgba(0, 255, 255, 40);
            }}
        """)