from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QLabel


class AnimatedFooter(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.hue = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_color)
        self.timer.start(50)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                font-size: 12px;
                font-weight: normal;
                padding: 8px;
                background: transparent;
                letter-spacing: 0.5px;
            }
        """)

    def animate_color(self):
        self.hue = (self.hue + 2) % 360
        color = QColor.fromHsv(self.hue, 255, 255)
        self.setStyleSheet(f"""
            QLabel {{
                font-size: 12px;
                font-weight: normal;
                padding: 8px;
                color: {color.name()};
                background: transparent;
                letter-spacing: 0.5px;
            }}
        """)