from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QColor, QPainter, QLinearGradient, QBrush
from PyQt6.QtWidgets import QWidget


class ParticleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.particles = []
        for i in range(50):
            self.particles.append({
                "x": (i * 41) % 1200,
                "y": (i * 29) % 800,
                "size": (i % 3) + 1,
                "speed": (i % 2) + 1,
                "alpha": (i % 80) + 40,
            })
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_particles)
        self.timer.start(50)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def animate_particles(self):
        for p in self.particles:
            p["y"] += p["speed"]
            if p["y"] > self.height():
                p["y"] = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(18, 18, 30))
        gradient.setColorAt(0.5, QColor(12, 12, 22))
        gradient.setColorAt(1, QColor(8, 8, 18))
        painter.fillRect(self.rect(), gradient)

        for p in self.particles:
            color = QColor(0, 200, 255, p["alpha"])
            painter.setBrush(QBrush(color))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPoint(int(p["x"]), int(p["y"])), p["size"], p["size"])