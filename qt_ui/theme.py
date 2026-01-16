"""Theme management for dark and light modes"""
from PySide6.QtWidgets import QApplication, QGraphicsView
from PySide6.QtGui import QColor
from qt_ui import settings


DARK_STYLESHEET = """
/* Main Window and Widgets */
QMainWindow, QWidget {
    background-color: #3d3d3d;
    color: #e0e0e0;
}

QFrame {
    background-color: #3d3d3d;
    color: #e0e0e0;
}

/* Menu Bar */
QMenuBar {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border-bottom: 1px solid #5d5d5d;
}

QMenuBar::item:selected {
    background-color: #5d5d5d;
}

/* Menus */
QMenu {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
}

QMenu::item:selected {
    background-color: #0d47a1;
    color: #ffffff;
}

/* Buttons */
QPushButton {
    background-color: #0d47a1;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 5px 15px;
}

QPushButton:hover {
    background-color: #1565c0;
}

QPushButton:pressed {
    background-color: #0c3f8f;
}

QPushButton:disabled {
    background-color: #424242;
    color: #757575;
}

/* Labels */
QLabel {
    color: #e0e0e0;
}

/* Line Edit */
QLineEdit {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    border-radius: 4px;
    padding: 5px;
}

QLineEdit:focus {
    border: 1px solid #0d47a1;
}

/* Spin Box */
QSpinBox, QDoubleSpinBox {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    border-radius: 4px;
    padding: 5px;
}

QSpinBox:focus, QDoubleSpinBox:focus {
    border: 1px solid #0d47a1;
}

/* Sliders */
QSlider::groove:horizontal {
    background-color: #5d5d5d;
    height: 8px;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background-color: #0d47a1;
    width: 18px;
    margin: -5px 0;
    border-radius: 9px;
}

QSlider::handle:horizontal:hover {
    background-color: #1565c0;
}

/* ComboBox */
QComboBox {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    border-radius: 4px;
    padding: 5px;
}

QComboBox:focus {
    border: 1px solid #0d47a1;
}

QComboBox::drop-down {
    border: none;
}

QComboBox::down-arrow {
    image: none;
    background-color: #0d47a1;
    width: 12px;
    height: 12px;
}

/* CheckBox and RadioButton */
QCheckBox, QRadioButton {
    color: #e0e0e0;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 18px;
    height: 18px;
    border-radius: 3px;
    border: 1px solid #5d5d5d;
}

QCheckBox::indicator:unchecked, QRadioButton::indicator:unchecked {
    background-color: #4d4d4d;
}

QCheckBox::indicator:checked, QRadioButton::indicator:checked {
    background-color: #0d47a1;
    border: 1px solid #0d47a1;
}

/* GroupBox */
QGroupBox {
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    border-radius: 4px;
    margin-top: 10px;
    padding-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px 0 3px;
}

/* Tabs */
QTabBar::tab {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    padding: 8px 20px;
}

QTabBar::tab:selected {
    background-color: #0d47a1;
    color: #ffffff;
}

QTabWidget::pane {
    border: 1px solid #5d5d5d;
}

/* ScrollBar */
QScrollBar:vertical {
    background-color: #3d3d3d;
    width: 12px;
    border: none;
}

QScrollBar::handle:vertical {
    background-color: #626262;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #727272;
}

QScrollBar:horizontal {
    background-color: #3d3d3d;
    height: 12px;
    border: none;
}

QScrollBar::handle:horizontal {
    background-color: #626262;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #727272;
}

/* ProgressBar */
QProgressBar {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    border-radius: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #0d47a1;
    border-radius: 3px;
}

/* Text Edit */
QTextEdit, QPlainTextEdit {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    border-radius: 4px;
}

/* List View and Table View */
QListView, QTableView, QTreeView {
    background-color: #4d4d4d;
    color: #e0e0e0;
    border: 1px solid #5d5d5d;
    gridline-color: #5d5d5d;
}

QListView::item:selected, QTableView::item:selected, QTreeView::item:selected {
    background-color: #0d47a1;
}

QHeaderView::section {
    background-color: #4d4d4d;
    color: #e0e0e0;
    padding: 5px;
    border: 1px solid #5d5d5d;
}

/* Dialogs */
QDialog {
    background-color: #3d3d3d;
    color: #e0e0e0;
}

QFileDialog, QColorDialog {
    background-color: #1e1e1e;
}
"""

LIGHT_STYLESHEET = ""


def apply_theme(app: QApplication, dark_mode: bool = None):
    """Apply theme to the application - dark mode is always enabled
    
    Args:
        app: QApplication instance
        dark_mode: Ignored, dark mode is always enabled
    """
    # Dark mode is always enabled
    app.setStyle('Fusion')
    app.setStyleSheet(DARK_STYLESHEET)
    settings.dark_mode_enabled.set(True)
    
    # Update graphics views
    update_graphics_views(app, True)


def toggle_dark_mode(app: QApplication):
    """Toggle dark mode on/off"""
    current = settings.dark_mode_enabled.get()
    apply_theme(app, not current)
    update_graphics_views(app, not current)


def update_graphics_views(app: QApplication, dark_mode: bool = None):
    """Update all graphics views in the application to match theme"""
    from qt_ui import resources
    
    if dark_mode is None:
        dark_mode = settings.dark_mode_enabled.get()
    
    # Get all graphics views
    for widget in app.allWidgets():
        if isinstance(widget, QGraphicsView):
            if dark_mode:
                widget.setBackgroundBrush(QColor("#2d2d2d"))
            else:
                widget.setBackgroundBrush(QColor("#ffffff"))
            widget.update()  # Force repaint
    
    # Update phase diagram SVG based on theme
    # This will reload graphics items that use the SVG
    for widget in app.allWidgets():
        if hasattr(widget, 'svg') and hasattr(widget, 'scene'):
            # Remove old SVG
            if widget.svg:
                widget.scene.removeItem(widget.svg)
            
            # Add new SVG with correct theme
            from PySide6 import QtSvgWidgets
            from PySide6.QtCore import QPointF
            
            svg_path = resources.phase_diagram_bg if dark_mode else resources.phase_diagram_bg_light
            svg = QtSvgWidgets.QGraphicsSvgItem(svg_path)
            widget.scene.addItem(svg)
            svg.setPos(-svg.boundingRect().width()/2.0, -svg.boundingRect().height()/2.0)
            widget.svg = svg
            widget.update()  # Force repaint


