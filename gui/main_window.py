import os
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame, QScrollArea, QFileDialog, QMessageBox
)

from gui.title_bar import TitleBar
from gui.drop_area import DropArea
from gui.buttons import GlowButton
from gui.dialogs import SizeSelectionDialog
from gui.footer import AnimatedFooter
from gui.particles import ParticleWidget
from core.converter import convert_to_ico


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kael-Icon Converter")
        self.setMinimumSize(900, 650)
        self.resize(1000, 720)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.drag_pos = None

        # Central widget container (rounded frame)
        self.central = QWidget()
        self.central.setObjectName("CentralWidget")
        self.central.setStyleSheet("""
            #CentralWidget {
                background-color: rgba(15, 15, 25, 220);
                border-radius: 28px;
                border: 1px solid rgba(0, 255, 255, 80);
            }
        """)
        self.setCentralWidget(self.central)

        central_layout = QVBoxLayout(self.central)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(0)

        # Title bar
        self.title_bar = TitleBar(self)
        central_layout.addWidget(self.title_bar)

        # Scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: rgba(20,20,40,180);
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: cyan;
                min-height: 30px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgb(0,255,180);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        # Content widget
        content = QWidget()
        content.setStyleSheet("background: transparent;")
        content_layout = QVBoxLayout(content)
        content_layout.setSpacing(24)
        content_layout.setContentsMargins(32, 24, 32, 32)

        self.title = QLabel("🛡️ Kael-Icon Converter")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 34px;
                font-weight: bold;
                letter-spacing: 2px;
                background: transparent;
            }
        """)

        self.subtitle = QLabel("⚡ Professional Smart Icon Generator")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setStyleSheet("""
            QLabel {
                color: #AAAAAA;
                font-size: 14px;
                letter-spacing: 1px;
                padding-bottom: 8px;
                background: transparent;
            }
        """)

        self.drop_area = DropArea()

        self.preview_container = QFrame()
        self.preview_container.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 100);
                border-radius: 20px;
                border: 1px solid rgba(0, 255, 255, 60);
            }
        """)
        preview_layout = QVBoxLayout(self.preview_container)
        self.preview = QLabel("🖼️ Preview")
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview.setMinimumHeight(200)
        self.preview.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 16px;
                font-weight: normal;
                background: transparent;
            }
        """)
        preview_layout.addWidget(self.preview)

        self.select_button = GlowButton("📂 Select Image")
        self.convert_button = GlowButton("⚡ Convert To ICO")

        self.select_button.clicked.connect(self.select_image)
        self.convert_button.clicked.connect(self.convert_image)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.select_button)
        button_layout.addWidget(self.convert_button)
        button_layout.setSpacing(24)

        self.footer = AnimatedFooter(
            "💫 Developed By : Kaelion (Kyaw Wai Yan Naing)    "
            "⚡ Powered By : Kael-Private Research Core (Myanmar)"
        )

        content_layout.addWidget(self.title)
        content_layout.addWidget(self.subtitle)
        content_layout.addWidget(self.drop_area)
        content_layout.addWidget(self.preview_container)
        content_layout.addLayout(button_layout)
        content_layout.addWidget(self.footer)

        self.scroll_area.setWidget(content)
        central_layout.addWidget(self.scroll_area)

        # Background particle
        self.background = ParticleWidget(self.central)
        self.background.lower()
        self.background.setGeometry(0, 0, self.central.width(), self.central.height())
        self.background.show()

        # Animate title color
        self.hue = 0
        self.title_timer = QTimer()
        self.title_timer.timeout.connect(self.animate_title)
        self.title_timer.start(50)

    def resizeEvent(self, event):
        self.background.setGeometry(0, 0, self.central.width(), self.central.height())
        super().resizeEvent(event)

    def animate_title(self):
        self.hue = (self.hue + 2) % 360
        color = QColor.fromHsv(self.hue, 255, 255)
        self.title.setStyleSheet(f"""
            QLabel {{
                font-size: 34px;
                font-weight: bold;
                letter-spacing: 2px;
                color: {color.name()};
                background: transparent;
            }}
        """)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "",
            "Images (*.png *.jpg *.jpeg *.bmp *.webp)"
        )
        if file_path:
            self.drop_area.file_path = file_path
            self.drop_area.label.setText(f"✅ {os.path.basename(file_path)}")
            self.drop_area.sub_label.setText("Ready for conversion")
            self.drop_area.icon_label.setText("🖼️")
            self.show_preview(file_path)

    def show_preview(self, path):
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            scaled = pixmap.scaled(
                200, 200,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.preview.setPixmap(scaled)
            self.preview.setStyleSheet("background: transparent;")

    def convert_image(self):
        path = self.drop_area.file_path
        if not path:
            QMessageBox.warning(self, "Error", "Please select or drop an image first.")
            return

        dialog = SizeSelectionDialog(self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        sizes = dialog.get_selected_sizes()
        if not sizes:
            QMessageBox.warning(self, "Error", "No sizes selected. Please choose at least one size.")
            return

        save_path, _ = QFileDialog.getSaveFileName(
            self, "Save ICO", "icon.ico", "ICO Files (*.ico)"
        )
        if not save_path:
            return

        if convert_to_ico(path, save_path, sizes):
            QMessageBox.information(
                self, "Success",
                f"ICO Successfully Created!\n\n{save_path}\n\n"
                f"Included sizes: {', '.join(f'{w}x{h}' for w,h in sizes)}"
            )