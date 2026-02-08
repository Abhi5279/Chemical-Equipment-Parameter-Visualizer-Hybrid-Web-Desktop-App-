# # import sys
# # import os
# # from PyQt5.QtWidgets import QApplication
# # from PyQt5.QtGui import QFont
# # from app import MainWindow

# # def main():
# #     # 1. Initialize the Application
# #     app = QApplication(sys.argv)
    
# #     # 2. Set a modern system font
# #     # Segoe UI is standard for Windows, San Francisco for Mac
# #     app.setFont(QFont("Segoe UI", 10))
    
# #     # 3. Load Global Stylesheet (QSS)
# #     # We use a context manager (with open) to ensure the file is closed properly
# #     try:
# #         # Get the absolute path to the styles folder to prevent path errors
# #         base_dir = os.path.dirname(os.path.abspath(__file__))
# #         qss_path = os.path.join(base_dir, "styles", "theme.qss")
        
# #         with open(qss_path, "r") as f:
# #             style_data = f.read()
# #             app.setStyleSheet(style_data)
            
# #     except FileNotFoundError:
# #         print("Critical Error: styles/theme.qss not found. Running with default UI.")
# #     except Exception as e:
# #         print(f"Error loading stylesheet: {e}")

# #     # 4. Initialize the Main App Router
# #     # This triggers the construction of your Navbar and QStackedWidget
# #     window = MainWindow()
    
# #     # 5. Show the Window
# #     window.show()
    
# #     # 6. Execute the application loop
# #     sys.exit(app.exec_())

# # if __name__ == "__main__":
# #     main()
# """
# Chemical Equipment Analytics Platform - Desktop Application
# Complete PyQt5 implementation with all web app features
# """

# import sys
# import os
# import json
# import requests
# from datetime import datetime
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
#     QLabel, QPushButton, QLineEdit, QFileDialog, QTableWidget, 
#     QTableWidgetItem, QScrollArea, QFrame, QGridLayout, QStackedWidget,
#     QHeaderView, QMessageBox, QProgressBar, QTabWidget, QSplitter
# )
# from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QSize, QPropertyAnimation, QEasingCurve
# from PyQt5.QtGui import QFont, QColor, QPalette, QIcon, QPainter, QLinearGradient, QBrush
# from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis

# # API Configuration
# API_BASE = "http://127.0.0.1:8000/api"


# class APIClient:
#     """Handles all API interactions"""
    
#     def __init__(self):
#         self.base_url = API_BASE
#         self.token = None
#         self.load_token()
    
#     def load_token(self):
#         """Load token from file"""
#         try:
#             if os.path.exists('token.txt'):
#                 with open('token.txt', 'r') as f:
#                     self.token = f.read().strip()
#         except:
#             pass
    
#     def save_token(self, token):
#         """Save token to file"""
#         self.token = token
#         with open('token.txt', 'w') as f:
#             f.write(token)
    
#     def clear_token(self):
#         """Clear saved token"""
#         self.token = None
#         if os.path.exists('token.txt'):
#             os.remove('token.txt')
    
#     def get_headers(self):
#         """Get request headers with auth token"""
#         headers = {}
#         if self.token:
#             headers['Authorization'] = f'Token {self.token}'
#         return headers
    
#     def register(self, username, password):
#         """Register new user"""
#         try:
#             response = requests.post(
#                 f"{self.base_url}/register/",
#                 json={"username": username, "password": password}
#             )
#             response.raise_for_status()
#             data = response.json()
#             self.save_token(data['token'])
#             return True, "Registration successful"
#         except requests.exceptions.RequestException as e:
#             return False, str(e)
    
#     def login(self, username, password):
#         """Login user"""
#         try:
#             response = requests.post(
#                 f"{self.base_url}/login/",
#                 json={"username": username, "password": password}
#             )
#             response.raise_for_status()
#             data = response.json()
#             self.save_token(data['token'])
#             return True, "Login successful"
#         except requests.exceptions.RequestException as e:
#             return False, "Invalid username or password"
    
#     def upload_csv(self, file_path):
#         """Upload CSV file"""
#         try:
#             with open(file_path, 'rb') as f:
#                 files = {'file': f}
#                 response = requests.post(
#                     f"{self.base_url}/upload/",
#                     files=files,
#                     headers=self.get_headers()
#                 )
#                 response.raise_for_status()
#                 return True, response.json()
#         except requests.exceptions.RequestException as e:
#             return False, str(e)
    
#     def get_latest_summary(self):
#         """Get latest dataset summary"""
#         try:
#             response = requests.get(
#                 f"{self.base_url}/summary/latest/",
#                 headers=self.get_headers()
#             )
#             response.raise_for_status()
#             return True, response.json()
#         except:
#             return False, None
    
#     def get_history(self):
#         """Get upload history"""
#         try:
#             response = requests.get(
#                 f"{self.base_url}/history/",
#                 headers=self.get_headers()
#             )
#             response.raise_for_status()
#             return True, response.json()
#         except:
#             return False, []
    
#     def download_report(self, dataset_id, save_path):
#         """Download PDF report"""
#         try:
#             response = requests.get(
#                 f"{self.base_url}/report/{dataset_id}/",
#                 headers=self.get_headers()
#             )
#             response.raise_for_status()
#             with open(save_path, 'wb') as f:
#                 f.write(response.content)
#             return True, "Report downloaded successfully"
#         except:
#             return False, "Failed to download report"


# class UploadThread(QThread):
#     """Background thread for file upload"""
#     finished = pyqtSignal(bool, object)
    
#     def __init__(self, api_client, file_path):
#         super().__init__()
#         self.api_client = api_client
#         self.file_path = file_path
    
#     def run(self):
#         success, result = self.api_client.upload_csv(self.file_path)
#         self.finished.emit(success, result)


# class GradientWidget(QWidget):
#     """Widget with gradient background"""
    
#     def __init__(self, color1, color2, parent=None):
#         super().__init__(parent)
#         self.color1 = QColor(color1)
#         self.color2 = QColor(color2)
    
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         gradient = QLinearGradient(0, 0, 0, self.height())
#         gradient.setColorAt(0, self.color1)
#         gradient.setColorAt(1, self.color2)
#         painter.fillRect(self.rect(), gradient)


# class StatCard(QFrame):
#     """KPI Stat Card Widget"""
    
#     def __init__(self, label, value, color_start, color_end):
#         super().__init__()
#         self.setObjectName("StatCard")
#         self.setFixedHeight(120)
#         self.setStyleSheet(f"""
#             QFrame#StatCard {{
#                 background-color: white;
#                 border-radius: 16px;
#                 border: 2px solid #e2e8f0;
#             }}
#             QFrame#StatCard:hover {{
#                 border: 2px solid #cbd5e1;
#                 background-color: #fafafa;
#             }}
#         """)
        
#         layout = QVBoxLayout(self)
#         layout.setContentsMargins(20, 15, 20, 15)
#         layout.setSpacing(8)
        
#         # Label
#         lbl = QLabel(label.upper())
#         lbl.setStyleSheet("font-size: 11px; font-weight: bold; color: #64748b;")
        
#         # Value
#         val = QLabel(str(value) if isinstance(value, int) else f"{value:.1f}")
#         val.setStyleSheet(f"""
#             font-size: 32px; 
#             font-weight: 900; 
#             color: {color_start};
#         """)
        
#         layout.addWidget(lbl)
#         layout.addWidget(val)
#         layout.addStretch()


# class FeatureCard(QFrame):
#     """Feature showcase card"""
    
#     def __init__(self, title, description):
#         super().__init__()
#         self.setFixedSize(360, 260)
#         self.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#             QFrame:hover {
#                 border: 2px solid #cbd5e1;
#                 background-color: #f8fafc;
#             }
#         """)
        
#         layout = QVBoxLayout(self)
#         layout.setContentsMargins(25, 25, 25, 25)
#         layout.setSpacing(15)
        
#         # Icon placeholder
#         icon_frame = QFrame()
#         icon_frame.setFixedSize(60, 60)
#         icon_frame.setStyleSheet("""
#             background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
#                 stop:0 #3b82f6, stop:1 #06b6d4);
#             border-radius: 30px;
#         """)
        
#         # Title
#         title_lbl = QLabel(title)
#         title_lbl.setStyleSheet("""
#             font-size: 20px; 
#             font-weight: bold; 
#             color: #0f172a;
#         """)
#         title_lbl.setWordWrap(True)
#         title_lbl.setAlignment(Qt.AlignCenter)
        
#         # Description
#         desc_lbl = QLabel(description)
#         desc_lbl.setStyleSheet("font-size: 14px; color: #64748b;")
#         desc_lbl.setWordWrap(True)
#         desc_lbl.setAlignment(Qt.AlignCenter)
        
#         layout.addWidget(icon_frame, alignment=Qt.AlignCenter)
#         layout.addWidget(title_lbl)
#         layout.addWidget(desc_lbl)
#         layout.addStretch()


# class HomePage(QWidget):
#     """Home page with hero section and features"""
    
#     def __init__(self, main_window):
#         super().__init__()
#         self.main_window = main_window
        
#         # Scroll area
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         scroll.setStyleSheet("QScrollArea { border: none; background-color: #f8fafc; }")
        
#         content = QWidget()
#         main_layout = QVBoxLayout(content)
#         main_layout.setContentsMargins(0, 0, 0, 0)
#         main_layout.setSpacing(0)
        
#         # Hero Section
#         hero = QWidget()
#         hero.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f1f5f9);")
#         hero_layout = QVBoxLayout(hero)
#         hero_layout.setContentsMargins(50, 80, 50, 80)
#         hero_layout.setSpacing(25)
#         hero_layout.setAlignment(Qt.AlignCenter)
        
#         # Badge
#         badge = QLabel("⚡ PRECISION ENGINEERING DASHBOARD")
#         badge.setStyleSheet("""
#             background-color: #eff6ff;
#             color: #1e40af;
#             font-size: 12px;
#             font-weight: bold;
#             padding: 10px 24px;
#             border-radius: 20px;
#             border: 2px solid #bfdbfe;
#         """)
        
#         # Title
#         title = QLabel("Chemical Equipment\nAnalytics Platform")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("""
#             font-size: 56px; 
#             font-weight: 900; 
#             color: #0f172a;
#         """)
        
#         # Subtitle
#         subtitle = QLabel("Transform raw operational data into actionable intelligence.\nAnalyze flowrates and pressures to generate professional reports instantly.")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setWordWrap(True)
#         subtitle.setStyleSheet("font-size: 17px; color: #475569; margin-top: 10px;")
        
#         # Buttons
#         btn_container = QHBoxLayout()
#         btn_container.setSpacing(20)
        
#         btn_start = QPushButton("Start Analysis Engine")
#         btn_start.setFixedSize(260, 55)
#         btn_start.setCursor(Qt.PointingHandCursor)
#         btn_start.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #2563eb);
#                 color: white;
#                 font-size: 16px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #1d4ed8);
#             }
#         """)
#         btn_start.clicked.connect(lambda: self.main_window.navigate("upload"))
        
#         btn_dash = QPushButton("View Dashboard")
#         btn_dash.setFixedSize(260, 55)
#         btn_dash.setCursor(Qt.PointingHandCursor)
#         btn_dash.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 color: #1e293b;
#                 font-size: 16px;
#                 font-weight: bold;
#                 border: 2px solid #e2e8f0;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background-color: #f8fafc;
#                 border-color: #cbd5e1;
#             }
#         """)
#         btn_dash.clicked.connect(lambda: self.main_window.navigate("analytics"))
        
#         btn_container.addWidget(btn_start)
#         btn_container.addWidget(btn_dash)
        
#         hero_layout.addWidget(badge, alignment=Qt.AlignCenter)
#         hero_layout.addWidget(title)
#         hero_layout.addWidget(subtitle)
#         hero_layout.addSpacing(20)
#         hero_layout.addLayout(btn_container)
        
#         # Features Section
#         features = QWidget()
#         features.setStyleSheet("background-color: #f8fafc; border-top: 1px solid #e2e8f0;")
#         features_layout = QVBoxLayout(features)
#         features_layout.setContentsMargins(60, 80, 60, 80)
#         features_layout.setSpacing(50)
        
#         f_title = QLabel("Powerful Analytics Features")
#         f_title.setAlignment(Qt.AlignCenter)
#         f_title.setStyleSheet("font-size: 38px; font-weight: 800; color: #0f172a;")
        
#         f_subtitle = QLabel("Everything you need to monitor and optimize your chemical equipment")
#         f_subtitle.setAlignment(Qt.AlignCenter)
#         f_subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
#         features_layout.addWidget(f_title)
#         features_layout.addWidget(f_subtitle)
        
#         # Grid of features
#         grid = QGridLayout()
#         grid.setSpacing(30)
        
#         features_data = [
#             ("Real-time Metrics", "Track equipment count, average flowrate, and pressure with live updates."),
#             ("Health Scoring", "Automated algorithms analyze parameters to calculate health scores."),
#             ("Risk Assessment", "Advanced systems identify high-risk equipment based on thresholds."),
#             ("CSV Processing", "Upload large-scale logs instantly with intelligent validation."),
#             ("Professional Reports", "Generate executive-ready PDF reports with KPI summaries."),
#             ("Type Distribution", "Visual breakdown of equipment by type with detailed charts.")
#         ]
        
#         for i, (title, desc) in enumerate(features_data):
#             row = i // 3
#             col = i % 3
#             grid.addWidget(FeatureCard(title, desc), row, col, Qt.AlignCenter)
        
#         features_layout.addLayout(grid)
        
#         # Build page
#         main_layout.addWidget(hero)
#         main_layout.addWidget(features)
        
#         scroll.setWidget(content)
        
#         page_layout = QVBoxLayout(self)
#         page_layout.setContentsMargins(0, 0, 0, 0)
#         page_layout.addWidget(scroll)


# class UploadPage(QWidget):
#     """File upload page with drag-drop and analytics preview"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
#         self.selected_file = None
#         self.overview_data = None
        
#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(40, 40, 40, 40)
#         main_layout.setSpacing(30)
        
#         # Title
#         title = QLabel("Chemical Equipment Analysis")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("""
#             font-size: 42px; 
#             font-weight: 900;
#             color: #3b82f6;
#         """)
        
#         subtitle = QLabel("Upload your dataset and unlock powerful insights instantly")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
#         main_layout.addWidget(title)
#         main_layout.addWidget(subtitle)
#         main_layout.addSpacing(20)
        
#         # Content area - split into two columns
#         content_layout = QHBoxLayout()
#         content_layout.setSpacing(30)
        
#         # LEFT: Upload panel
#         upload_panel = self.create_upload_panel()
        
#         # RIGHT: Preview panel
#         self.preview_panel = self.create_preview_panel()
        
#         content_layout.addWidget(upload_panel, 1)
#         content_layout.addWidget(self.preview_panel, 1)
        
#         main_layout.addLayout(content_layout)
    
#     def create_upload_panel(self):
#         """Create upload section"""
#         panel = QFrame()
#         panel.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(panel)
#         layout.setContentsMargins(30, 30, 30, 30)
#         layout.setSpacing(20)
        
#         # Header
#         header_layout = QHBoxLayout()
#         header_icon = QLabel("📁")
#         header_icon.setStyleSheet("font-size: 32px;")
        
#         header_text = QWidget()
#         header_text_layout = QVBoxLayout(header_text)
#         header_text_layout.setContentsMargins(0, 0, 0, 0)
#         header_text_layout.setSpacing(2)
        
#         h_title = QLabel("Upload Dataset")
#         h_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
#         h_subtitle = QLabel("Select or drag & drop CSV file")
#         h_subtitle.setStyleSheet("font-size: 12px; color: #64748b;")
        
#         header_text_layout.addWidget(h_title)
#         header_text_layout.addWidget(h_subtitle)
        
#         header_layout.addWidget(header_icon)
#         header_layout.addWidget(header_text)
#         header_layout.addStretch()
        
#         # File selection area
#         file_area = QFrame()
#         file_area.setMinimumHeight(200)
#         file_area.setStyleSheet("""
#             QFrame {
#                 background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                     stop:0 #f8fafc, stop:1 #eff6ff);
#                 border: 2px dashed #cbd5e1;
#                 border-radius: 16px;
#             }
#         """)
        
#         file_layout = QVBoxLayout(file_area)
#         file_layout.setAlignment(Qt.AlignCenter)
        
#         self.file_label = QLabel("📄\n\nClick to browse or drop CSV file here")
#         self.file_label.setAlignment(Qt.AlignCenter)
#         self.file_label.setStyleSheet("font-size: 14px; color: #64748b;")
        
#         file_layout.addWidget(self.file_label)
        
#         # Browse button
#         browse_btn = QPushButton("Browse Files")
#         browse_btn.setFixedHeight(45)
#         browse_btn.setCursor(Qt.PointingHandCursor)
#         browse_btn.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 color: #3b82f6;
#                 font-size: 14px;
#                 font-weight: bold;
#                 border: 2px solid #3b82f6;
#                 border-radius: 10px;
#                 padding: 0 30px;
#             }
#             QPushButton:hover {
#                 background-color: #eff6ff;
#             }
#         """)
#         browse_btn.clicked.connect(self.browse_file)
        
#         # Upload button
#         self.upload_btn = QPushButton("Upload & Analyze Dataset")
#         self.upload_btn.setFixedHeight(50)
#         self.upload_btn.setCursor(Qt.PointingHandCursor)
#         self.upload_btn.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 15px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#             QPushButton:disabled {
#                 background-color: #cbd5e1;
#             }
#         """)
#         self.upload_btn.clicked.connect(self.upload_file)
#         self.upload_btn.setEnabled(False)
        
#         # Progress bar
#         self.progress_bar = QProgressBar()
#         self.progress_bar.setVisible(False)
#         self.progress_bar.setStyleSheet("""
#             QProgressBar {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 8px;
#                 text-align: center;
#                 background-color: white;
#             }
#             QProgressBar::chunk {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #06b6d4);
#                 border-radius: 6px;
#             }
#         """)
        
#         # Error label
#         self.error_label = QLabel()
#         self.error_label.setVisible(False)
#         self.error_label.setStyleSheet("color: #ef4444; font-size: 12px;")
#         self.error_label.setWordWrap(True)
        
#         layout.addLayout(header_layout)
#         layout.addWidget(file_area)
#         layout.addWidget(browse_btn)
#         layout.addWidget(self.upload_btn)
#         layout.addWidget(self.progress_bar)
#         layout.addWidget(self.error_label)
#         layout.addStretch()
        
#         return panel
    
#     def create_preview_panel(self):
#         """Create data preview panel"""
#         panel = QFrame()
#         panel.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(panel)
#         layout.setContentsMargins(30, 30, 30, 30)
#         layout.setSpacing(20)
        
#         # Header
#         header = QLabel("Dataset Insights")
#         header.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
        
#         # Content area (will be populated after upload)
#         self.preview_content = QWidget()
#         self.preview_layout = QVBoxLayout(self.preview_content)
#         self.preview_layout.setAlignment(Qt.AlignCenter)
        
#         # Default state
#         empty_icon = QLabel("📊")
#         empty_icon.setAlignment(Qt.AlignCenter)
#         empty_icon.setStyleSheet("font-size: 64px;")
        
#         empty_text = QLabel("Upload a dataset to view instant analytics")
#         empty_text.setAlignment(Qt.AlignCenter)
#         empty_text.setStyleSheet("font-size: 14px; color: #94a3b8;")
        
#         self.preview_layout.addWidget(empty_icon)
#         self.preview_layout.addWidget(empty_text)
        
#         layout.addWidget(header)
#         layout.addWidget(self.preview_content)
        
#         return panel
    
#     def browse_file(self):
#         """Open file browser"""
#         file_path, _ = QFileDialog.getOpenFileName(
#             self,
#             "Select CSV File",
#             "",
#             "CSV Files (*.csv)"
#         )
        
#         if file_path:
#             self.selected_file = file_path
#             file_name = os.path.basename(file_path)
#             self.file_label.setText(f"✅ {file_name}")
#             self.upload_btn.setEnabled(True)
#             self.error_label.setVisible(False)
    
#     def upload_file(self):
#         """Upload selected file"""
#         if not self.selected_file:
#             return
        
#         self.upload_btn.setEnabled(False)
#         self.progress_bar.setVisible(True)
#         self.progress_bar.setRange(0, 0)  # Indeterminate
#         self.error_label.setVisible(False)
        
#         # Start upload thread
#         self.upload_thread = UploadThread(self.api_client, self.selected_file)
#         self.upload_thread.finished.connect(self.upload_finished)
#         self.upload_thread.start()
    
#     def upload_finished(self, success, result):
#         """Handle upload completion"""
#         self.progress_bar.setVisible(False)
#         self.upload_btn.setEnabled(True)
        
#         if success:
#             self.overview_data = result
#             self.update_preview(result)
#             QMessageBox.information(self, "Success", "File uploaded successfully!")
#         else:
#             self.error_label.setText(f"Upload failed: {result}")
#             self.error_label.setVisible(True)
    
#     def update_preview(self, data):
#         """Update preview panel with data"""
#         # Clear existing content
#         while self.preview_layout.count():
#             item = self.preview_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # KPI Grid
#         kpi_grid = QGridLayout()
#         kpi_grid.setSpacing(15)
        
#         kpi_grid.addWidget(StatCard("Total Equipment", data.get('total_equipment', 0), "#3b82f6", "#06b6d4"), 0, 0)
#         kpi_grid.addWidget(StatCard("Avg Flowrate", data.get('avg_flowrate', 0), "#8b5cf6", "#d946ef"), 0, 1)
#         kpi_grid.addWidget(StatCard("Avg Pressure", data.get('avg_pressure', 0), "#ef4444", "#f97316"), 1, 0)
#         kpi_grid.addWidget(StatCard("Avg Temperature", data.get('avg_temperature', 0), "#10b981", "#14b8a6"), 1, 1)
        
#         # Health score bar
#         health_widget = QWidget()
#         health_layout = QVBoxLayout(health_widget)
#         health_layout.setContentsMargins(15, 15, 15, 15)
#         health_widget.setStyleSheet("""
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                 stop:0 #f8fafc, stop:1 #eff6ff);
#             border-radius: 12px;
#         """)
        
#         health_header = QHBoxLayout()
#         health_label = QLabel("OVERALL HEALTH SCORE")
#         health_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #64748b;")
#         health_value = QLabel(f"{data.get('health_score', 0)}%")
#         health_value.setStyleSheet("font-size: 28px; font-weight: 900; color: #10b981;")
#         health_header.addWidget(health_label)
#         health_header.addStretch()
#         health_header.addWidget(health_value)
        
#         health_bar = QProgressBar()
#         health_bar.setRange(0, 100)
#         health_bar.setValue(data.get('health_score', 0))
#         health_bar.setTextVisible(False)
#         health_bar.setFixedHeight(24)
        
#         score = data.get('health_score', 0)
#         if score >= 70:
#             color = "#10b981"
#         elif score >= 40:
#             color = "#f59e0b"
#         else:
#             color = "#ef4444"
        
#         health_bar.setStyleSheet(f"""
#             QProgressBar {{
#                 border: none;
#                 border-radius: 12px;
#                 background-color: #e2e8f0;
#             }}
#             QProgressBar::chunk {{
#                 background-color: {color};
#                 border-radius: 12px;
#             }}
#         """)
        
#         health_layout.addLayout(health_header)
#         health_layout.addWidget(health_bar)
        
#         # Action buttons
#         btn_layout = QHBoxLayout()
#         btn_layout.setSpacing(15)
        
#         btn_summary = QPushButton("View Summary")
#         btn_summary.setFixedHeight(45)
#         btn_summary.setCursor(Qt.PointingHandCursor)
#         btn_summary.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 14px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 10px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#         """)
#         btn_summary.clicked.connect(lambda: self.main_window.navigate("summary"))
        
#         btn_analytics = QPushButton("Analytics")
#         btn_analytics.setFixedHeight(45)
#         btn_analytics.setCursor(Qt.PointingHandCursor)
#         btn_analytics.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 color: #3b82f6;
#                 font-size: 14px;
#                 font-weight: bold;
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#             }
#             QPushButton:hover {
#                 background-color: #eff6ff;
#                 border-color: #3b82f6;
#             }
#         """)
#         btn_analytics.clicked.connect(lambda: self.main_window.navigate("analytics"))
        
#         btn_layout.addWidget(btn_summary)
#         btn_layout.addWidget(btn_analytics)
        
#         self.preview_layout.addLayout(kpi_grid)
#         self.preview_layout.addSpacing(20)
#         self.preview_layout.addWidget(health_widget)
#         self.preview_layout.addSpacing(20)
#         self.preview_layout.addLayout(btn_layout)
#         self.preview_layout.addStretch()


# class SummaryPage(QWidget):
#     """Summary page showing latest data and history"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
        
#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(40, 40, 40, 40)
#         main_layout.setSpacing(30)
        
#         # Title
#         title = QLabel("Dataset Summary")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 42px; font-weight: 900; color: #3b82f6;")
        
#         subtitle = QLabel("Comprehensive analytics and historical data overview")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
#         main_layout.addWidget(title)
#         main_layout.addWidget(subtitle)
#         main_layout.addSpacing(20)
        
#         # Content area
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         scroll.setStyleSheet("QScrollArea { border: none; }")
        
#         content = QWidget()
#         self.content_layout = QVBoxLayout(content)
#         self.content_layout.setSpacing(30)
        
#         scroll.setWidget(content)
#         main_layout.addWidget(scroll)
        
#         # Load data
#         self.load_data()
    
#     def load_data(self):
#         """Load summary and history data"""
#         # Clear existing
#         while self.content_layout.count():
#             item = self.content_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # Get latest summary
#         success, latest = self.api_client.get_latest_summary()
#         if success and latest:
#             self.content_layout.addWidget(self.create_latest_card(latest))
        
#         # Get history
#         success, history = self.api_client.get_history()
#         if success and history:
#             self.content_layout.addWidget(self.create_history_table(history))
    
#     def create_latest_card(self, data):
#         """Create latest summary card"""
#         card = QFrame()
#         card.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(card)
#         layout.setContentsMargins(30, 30, 30, 30)
#         layout.setSpacing(25)
        
#         # Header
#         header = QHBoxLayout()
#         h_label = QLabel("Latest Summary")
#         h_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #0f172a;")
        
#         badge = QLabel("LIVE DATA")
#         badge.setStyleSheet("""
#             background-color: #dcfce7;
#             color: #166534;
#             font-size: 10px;
#             font-weight: bold;
#             padding: 6px 12px;
#             border-radius: 8px;
#         """)
        
#         header.addWidget(h_label)
#         header.addStretch()
#         header.addWidget(badge)
        
#         # KPI Grid
#         kpi_grid = QGridLayout()
#         kpi_grid.setSpacing(20)
        
#         kpi_grid.addWidget(StatCard("Total Equipment", data.get('total_equipment', 0), "#3b82f6", "#06b6d4"), 0, 0)
#         kpi_grid.addWidget(StatCard("Avg Flowrate", data.get('avg_flowrate', 0), "#8b5cf6", "#d946ef"), 0, 1)
#         kpi_grid.addWidget(StatCard("Avg Pressure", data.get('avg_pressure', 0), "#ef4444", "#f97316"), 0, 2)
#         kpi_grid.addWidget(StatCard("Avg Temperature", data.get('avg_temperature', 0), "#10b981", "#14b8a6"), 0, 3)
        
#         # Health bar
#         health_widget = QWidget()
#         health_layout = QVBoxLayout(health_widget)
#         health_layout.setContentsMargins(20, 20, 20, 20)
#         health_widget.setStyleSheet("""
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                 stop:0 #f8fafc, stop:1 #eff6ff);
#             border-radius: 12px;
#         """)
        
#         health_header = QHBoxLayout()
#         health_label = QLabel("OVERALL HEALTH SCORE")
#         health_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #64748b;")
#         health_value = QLabel(f"{data.get('health_score', 0)}%")
        
#         score = data.get('health_score', 0)
#         if score >= 70:
#             color = "#10b981"
#         elif score >= 40:
#             color = "#f59e0b"
#         else:
#             color = "#ef4444"
        
#         health_value.setStyleSheet(f"font-size: 32px; font-weight: 900; color: {color};")
#         health_header.addWidget(health_label)
#         health_header.addStretch()
#         health_header.addWidget(health_value)
        
#         health_bar = QProgressBar()
#         health_bar.setRange(0, 100)
#         health_bar.setValue(score)
#         health_bar.setTextVisible(False)
#         health_bar.setFixedHeight(28)
#         health_bar.setStyleSheet(f"""
#             QProgressBar {{
#                 border: none;
#                 border-radius: 14px;
#                 background-color: #e2e8f0;
#             }}
#             QProgressBar::chunk {{
#                 background-color: {color};
#                 border-radius: 14px;
#             }}
#         """)
        
#         health_layout.addLayout(health_header)
#         health_layout.addWidget(health_bar)
        
#         layout.addLayout(header)
#         layout.addLayout(kpi_grid)
#         layout.addWidget(health_widget)
        
#         return card
    
#     def create_history_table(self, history):
#         """Create history table"""
#         card = QFrame()
#         card.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(card)
#         layout.setContentsMargins(0, 0, 0, 0)
        
#         # Header
#         header = QWidget()
#         header.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #eff6ff, stop:1 #e0f2fe); border-radius: 20px 20px 0 0;")
#         header_layout = QHBoxLayout(header)
#         header_layout.setContentsMargins(30, 25, 30, 25)
        
#         h_label = QLabel("Upload History")
#         h_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #0f172a;")
#         header_layout.addWidget(h_label)
        
#         # Table
#         table = QTableWidget()
#         table.setColumnCount(5)
#         table.setHorizontalHeaderLabels(["ID", "File Name", "Health Score", "Upload Date", "Actions"])
#         table.setRowCount(len(history))
#         table.setStyleSheet("""
#             QTableWidget {
#                 border: none;
#                 gridline-color: #f1f5f9;
#                 background-color: white;
#             }
#             QTableWidget::item {
#                 padding: 15px;
#                 border-bottom: 1px solid #f1f5f9;
#             }
#             QTableWidget::item:selected {
#                 background-color: #eff6ff;
#                 color: #0f172a;
#             }
#             QHeaderView::section {
#                 background-color: #f8fafc;
#                 padding: 12px;
#                 border: none;
#                 border-bottom: 2px solid #e2e8f0;
#                 font-weight: bold;
#                 color: #475569;
#                 font-size: 11px;
#             }
#         """)
        
#         table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         table.verticalHeader().setVisible(False)
#         table.setSelectionBehavior(QTableWidget.SelectRows)
#         table.setEditTriggers(QTableWidget.NoEditTriggers)
        
#         for row, item in enumerate(history):
#             # ID
#             table.setItem(row, 0, QTableWidgetItem(str(item.get('id', ''))))
            
#             # File name
#             table.setItem(row, 1, QTableWidgetItem(item.get('file_name', '')))
            
#             # Health score
#             score = item.get('health_score', 0)
#             score_item = QTableWidgetItem(f"{score}%")
#             if score >= 70:
#                 score_item.setForeground(QColor("#10b981"))
#             elif score >= 40:
#                 score_item.setForeground(QColor("#f59e0b"))
#             else:
#                 score_item.setForeground(QColor("#ef4444"))
#             table.setItem(row, 2, score_item)
            
#             # Date
#             date_str = item.get('uploaded_at', '')
#             if date_str:
#                 try:
#                     date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
#                     formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
#                 except:
#                     formatted_date = date_str
#             else:
#                 formatted_date = ""
#             table.setItem(row, 3, QTableWidgetItem(formatted_date))
            
#             # Download button
#             download_btn = QPushButton("📥 Download PDF")
#             download_btn.setCursor(Qt.PointingHandCursor)
#             download_btn.setStyleSheet("""
#                 QPushButton {
#                     background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                         stop:0 #3b82f6, stop:1 #6366f1);
#                     color: white;
#                     font-size: 12px;
#                     font-weight: bold;
#                     border: none;
#                     border-radius: 8px;
#                     padding: 8px 16px;
#                 }
#                 QPushButton:hover {
#                     background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                         stop:0 #2563eb, stop:1 #4f46e5);
#                 }
#             """)
#             download_btn.clicked.connect(lambda checked, id=item.get('id'): self.download_report(id))
#             table.setCellWidget(row, 4, download_btn)
        
#         layout.addWidget(header)
#         layout.addWidget(table)
        
#         return card
    
#     def download_report(self, dataset_id):
#         """Download PDF report"""
#         save_path, _ = QFileDialog.getSaveFileName(
#             self,
#             "Save Report",
#             f"dataset_report_{dataset_id}.pdf",
#             "PDF Files (*.pdf)"
#         )
        
#         if save_path:
#             success, message = self.api_client.download_report(dataset_id, save_path)
#             if success:
#                 QMessageBox.information(self, "Success", message)
#             else:
#                 QMessageBox.warning(self, "Error", message)


# class AnalyticsPage(QWidget):
#     """Analytics dashboard with charts"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
#         self.datasets = []
#         self.selected_data = None
        
#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(40, 40, 40, 40)
#         main_layout.setSpacing(30)
        
#         # Title
#         title = QLabel("Analytics Dashboard")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 42px; font-weight: 900; color: #3b82f6;")
        
#         subtitle = QLabel("Comprehensive visual insights and real-time equipment monitoring")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
#         main_layout.addWidget(title)
#         main_layout.addWidget(subtitle)
#         main_layout.addSpacing(20)
        
#         # Content area
#         content_layout = QHBoxLayout()
#         content_layout.setSpacing(30)
        
#         # LEFT: Dataset selector
#         self.selector_panel = self.create_selector_panel()
        
#         # RIGHT: Analytics view
#         self.analytics_panel = QWidget()
#         self.analytics_layout = QVBoxLayout(self.analytics_panel)
#         self.analytics_layout.setSpacing(20)
        
#         content_layout.addWidget(self.selector_panel, 1)
#         content_layout.addWidget(self.analytics_panel, 3)
        
#         main_layout.addLayout(content_layout)
        
#         # Load data
#         self.load_datasets()
    
#     def create_selector_panel(self):
#         """Create dataset selector"""
#         panel = QFrame()
#         panel.setFixedWidth(300)
#         panel.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(panel)
#         layout.setContentsMargins(20, 20, 20, 20)
#         layout.setSpacing(15)
        
#         # Header
#         header = QLabel("Datasets")
#         header.setStyleSheet("font-size: 18px; font-weight: bold; color: #0f172a;")
        
#         # List area
#         self.dataset_list = QWidget()
#         self.dataset_list_layout = QVBoxLayout(self.dataset_list)
#         self.dataset_list_layout.setSpacing(10)
        
#         scroll = QScrollArea()
#         scroll.setWidget(self.dataset_list)
#         scroll.setWidgetResizable(True)
#         scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         scroll.setStyleSheet("QScrollArea { border: none; }")
        
#         layout.addWidget(header)
#         layout.addWidget(scroll)
        
#         return panel
    
#     def load_datasets(self):
#         """Load datasets from history"""
#         success, history = self.api_client.get_history()
        
#         if not success or not history:
#             # Show empty state
#             empty_label = QLabel("No datasets available.\nUpload a file to get started.")
#             empty_label.setAlignment(Qt.AlignCenter)
#             empty_label.setStyleSheet("color: #94a3b8; font-size: 14px;")
#             self.analytics_layout.addWidget(empty_label)
#             return
        
#         self.datasets = history
        
#         # Clear list
#         while self.dataset_list_layout.count():
#             item = self.dataset_list_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # Add dataset buttons
#         for dataset in self.datasets:
#             btn = self.create_dataset_button(dataset)
#             self.dataset_list_layout.addWidget(btn)
        
#         self.dataset_list_layout.addStretch()
        
#         # Select first dataset
#         if self.datasets:
#             self.select_dataset(self.datasets[0])
    
#     def create_dataset_button(self, dataset):
#         """Create dataset selection button"""
#         btn = QPushButton()
#         btn.setCursor(Qt.PointingHandCursor)
#         btn.setFixedHeight(80)
        
#         layout = QVBoxLayout(btn)
#         layout.setContentsMargins(15, 10, 15, 10)
#         layout.setSpacing(5)
        
#         name_label = QLabel(dataset.get('file_name', 'Unknown'))
#         name_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #0f172a; text-align: left;")
#         name_label.setWordWrap(True)
        
#         health = dataset.get('health_score', 0)
#         health_label = QLabel(f"Health: {health}%")
#         if health >= 70:
#             color = "#10b981"
#         elif health >= 40:
#             color = "#f59e0b"
#         else:
#             color = "#ef4444"
#         health_label.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {color}; text-align: left;")
        
#         layout.addWidget(name_label)
#         layout.addWidget(health_label)
        
#         btn.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 border: 2px solid #e2e8f0;
#                 border-radius: 12px;
#                 text-align: left;
#             }
#             QPushButton:hover {
#                 background-color: #f8fafc;
#                 border-color: #cbd5e1;
#             }
#         """)
        
#         btn.clicked.connect(lambda: self.select_dataset(dataset))
        
#         return btn
    
#     def select_dataset(self, dataset):
#         """Display analytics for selected dataset"""
#         self.selected_data = dataset
        
#         # Clear analytics panel
#         while self.analytics_layout.count():
#             item = self.analytics_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # Dataset info header
#         header = self.create_info_header(dataset)
#         self.analytics_layout.addWidget(header)
        
#         # KPI Cards
#         kpi_grid = QGridLayout()
#         kpi_grid.setSpacing(20)
        
#         kpi_grid.addWidget(StatCard("Total Equipment", dataset.get('total_equipment', 0), "#3b82f6", "#06b6d4"), 0, 0)
#         kpi_grid.addWidget(StatCard("Avg Flowrate", dataset.get('avg_flowrate', 0), "#8b5cf6", "#d946ef"), 0, 1)
#         kpi_grid.addWidget(StatCard("Avg Pressure", dataset.get('avg_pressure', 0), "#ef4444", "#f97316"), 0, 2)
#         kpi_grid.addWidget(StatCard("Avg Temperature", dataset.get('avg_temperature', 0), "#10b981", "#14b8a6"), 0, 3)
        
#         self.analytics_layout.addLayout(kpi_grid)
        
#         # Charts
#         summary = dataset.get('summary', {})
        
#         # Risk analysis
#         risk_widget = self.create_risk_widget(summary.get('risk_analysis', {}))
#         self.analytics_layout.addWidget(risk_widget)
        
#         # Equipment distribution
#         eq_widget = self.create_equipment_distribution(summary.get('equipment_type_distribution', {}))
#         self.analytics_layout.addWidget(eq_widget)
        
#         self.analytics_layout.addStretch()
    
#     def create_info_header(self, dataset):
#         """Create dataset info header"""
#         header = QFrame()
#         header.setStyleSheet("""
#             QFrame {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 border-radius: 16px;
#             }
#         """)
        
#         layout = QHBoxLayout(header)
#         layout.setContentsMargins(30, 25, 30, 25)
        
#         # Left: Name and date
#         left = QWidget()
#         left_layout = QVBoxLayout(left)
#         left_layout.setSpacing(5)
        
#         name = QLabel(dataset.get('file_name', 'Unknown'))
#         name.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        
#         date_str = dataset.get('uploaded_at', '')
#         if date_str:
#             try:
#                 date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
#                 formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
#             except:
#                 formatted_date = date_str
#         else:
#             formatted_date = ""
        
#         date = QLabel(f"Uploaded: {formatted_date}")
#         date.setStyleSheet("font-size: 13px; color: #dbeafe;")
        
#         left_layout.addWidget(name)
#         left_layout.addWidget(date)
        
#         # Right: Health score
#         right = QWidget()
#         right_layout = QVBoxLayout(right)
#         right_layout.setSpacing(2)
#         right_layout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
#         health_label = QLabel("Overall Health")
#         health_label.setStyleSheet("font-size: 12px; color: #dbeafe; text-align: right;")
#         health_label.setAlignment(Qt.AlignRight)
        
#         health_value = QLabel(f"{dataset.get('health_score', 0)}%")
#         health_value.setStyleSheet("font-size: 42px; font-weight: 900; color: white; text-align: right;")
#         health_value.setAlignment(Qt.AlignRight)
        
#         right_layout.addWidget(health_label)
#         right_layout.addWidget(health_value)
        
#         layout.addWidget(left)
#         layout.addStretch()
#         layout.addWidget(right)
        
#         return header
    
#     def create_risk_widget(self, risk_data):
#         """Create risk analysis widget"""
#         widget = QFrame()
#         widget.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 16px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(widget)
#         layout.setContentsMargins(30, 25, 30, 25)
#         layout.setSpacing(20)
        
#         # Header
#         header = QLabel("Risk Analysis")
#         header.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
        
#         # Grid for risk stats
#         grid = QGridLayout()
#         grid.setSpacing(20)
        
#         high_risk = risk_data.get('high_risk', 0)
#         normal = risk_data.get('normal', 0)
#         total = high_risk + normal
        
#         # High risk card
#         high_card = QFrame()
#         high_card.setStyleSheet("""
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                 stop:0 #fef2f2, stop:1 #fee2e2);
#             border: 2px solid #fecaca;
#             border-radius: 12px;
#             padding: 20px;
#         """)
#         high_layout = QVBoxLayout(high_card)
#         high_layout.setSpacing(10)
        
#         high_title = QLabel("High Risk Equipment")
#         high_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #991b1b;")
        
#         high_value = QLabel(str(high_risk))
#         high_value.setStyleSheet("font-size: 36px; font-weight: 900; color: #dc2626;")
        
#         if total > 0:
#             high_pct = QLabel(f"{(high_risk/total*100):.1f}%")
#             high_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #ef4444;")
#         else:
#             high_pct = QLabel("0%")
#             high_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #ef4444;")
        
#         high_layout.addWidget(high_title)
#         high_layout.addWidget(high_value)
#         high_layout.addWidget(high_pct)
        
#         # Normal card
#         normal_card = QFrame()
#         normal_card.setStyleSheet("""
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                 stop:0 #f0fdf4, stop:1 #dcfce7);
#             border: 2px solid #bbf7d0;
#             border-radius: 12px;
#             padding: 20px;
#         """)
#         normal_layout = QVBoxLayout(normal_card)
#         normal_layout.setSpacing(10)
        
#         normal_title = QLabel("Normal Equipment")
#         normal_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #166534;")
        
#         normal_value = QLabel(str(normal))
#         normal_value.setStyleSheet("font-size: 36px; font-weight: 900; color: #16a34a;")
        
#         if total > 0:
#             normal_pct = QLabel(f"{(normal/total*100):.1f}%")
#             normal_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #22c55e;")
#         else:
#             normal_pct = QLabel("0%")
#             normal_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #22c55e;")
        
#         normal_layout.addWidget(normal_title)
#         normal_layout.addWidget(normal_value)
#         normal_layout.addWidget(normal_pct)
        
#         grid.addWidget(high_card, 0, 0)
#         grid.addWidget(normal_card, 0, 1)
        
#         layout.addWidget(header)
#         layout.addLayout(grid)
        
#         return widget
    
#     def create_equipment_distribution(self, distribution):
#         """Create equipment type distribution widget"""
#         widget = QFrame()
#         widget.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 16px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(widget)
#         layout.setContentsMargins(30, 25, 30, 25)
#         layout.setSpacing(20)
        
#         # Header
#         header = QLabel("Equipment Type Distribution")
#         header.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
        
#         # Grid of type cards
#         grid = QGridLayout()
#         grid.setSpacing(15)
        
#         items = list(distribution.items())
#         colors = ["#3b82f6", "#6366f1", "#8b5cf6", "#a855f7", "#ec4899", "#f43f5e"]
        
#         for i, (eq_type, count) in enumerate(items):
#             row = i // 4
#             col = i % 4
            
#             card = QFrame()
#             card.setStyleSheet(f"""
#                 background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                     stop:0 #eff6ff, stop:1 #dbeafe);
#                 border: 2px solid #bfdbfe;
#                 border-radius: 12px;
#                 padding: 15px;
#             """)
            
#             card_layout = QVBoxLayout(card)
#             card_layout.setSpacing(8)
            
#             type_label = QLabel(eq_type.upper())
#             type_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #1e40af;")
            
#             count_label = QLabel(str(count))
#             count_label.setStyleSheet(f"font-size: 28px; font-weight: 900; color: {colors[i % len(colors)]};")
            
#             card_layout.addWidget(type_label)
#             card_layout.addWidget(count_label)
            
#             grid.addWidget(card, row, col)
        
#         layout.addWidget(header)
#         layout.addLayout(grid)
        
#         return widget


# class LoginPage(QWidget):
#     """Login page"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
        
#         main_layout = QHBoxLayout(self)
#         main_layout.setContentsMargins(0, 0, 0, 0)
        
#         # Background gradient
#         main_layout.addWidget(GradientWidget("#f8fafc", "#e0f2fe"))
        
#         # Center content
#         center = QWidget()
#         center.setMaximumWidth(450)
        
#         layout = QVBoxLayout(center)
#         layout.setContentsMargins(40, 60, 40, 60)
#         layout.setSpacing(25)
#         layout.setAlignment(Qt.AlignCenter)
        
#         # Logo/Icon
#         icon_label = QLabel("🔐")
#         icon_label.setAlignment(Qt.AlignCenter)
#         icon_label.setStyleSheet("font-size: 48px;")
        
#         # Title
#         title = QLabel("Welcome Back")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 32px; font-weight: 900; color: #0f172a;")
        
#         subtitle = QLabel("Sign in to access your analytics dashboard")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 14px; color: #64748b;")
        
#         # Form container
#         form_container = QFrame()
#         form_container.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         form_layout = QVBoxLayout(form_container)
#         form_layout.setContentsMargins(30, 30, 30, 30)
#         form_layout.setSpacing(20)
        
#         # Username
#         username_label = QLabel("USERNAME")
#         username_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.username_input = QLineEdit()
#         self.username_input.setPlaceholderText("Enter your username")
#         self.username_input.setFixedHeight(45)
#         self.username_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Password
#         password_label = QLabel("PASSWORD")
#         password_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Enter your password")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         self.password_input.setFixedHeight(45)
#         self.password_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Error label
#         self.error_label = QLabel()
#         self.error_label.setVisible(False)
#         self.error_label.setStyleSheet("color: #ef4444; font-size: 12px;")
#         self.error_label.setWordWrap(True)
        
#         # Login button
#         login_btn = QPushButton("Sign In")
#         login_btn.setFixedHeight(50)
#         login_btn.setCursor(Qt.PointingHandCursor)
#         login_btn.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 16px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#         """)
#         login_btn.clicked.connect(self.handle_login)
        
#         # Register link
#         register_container = QHBoxLayout()
#         register_label = QLabel("Don't have an account?")
#         register_label.setStyleSheet("font-size: 13px; color: #64748b;")
        
#         register_btn = QPushButton("Create one")
#         register_btn.setCursor(Qt.PointingHandCursor)
#         register_btn.setStyleSheet("""
#             QPushButton {
#                 background: none;
#                 border: none;
#                 color: #3b82f6;
#                 font-size: 13px;
#                 font-weight: bold;
#                 text-decoration: underline;
#             }
#             QPushButton:hover {
#                 color: #2563eb;
#             }
#         """)
#         register_btn.clicked.connect(lambda: self.main_window.navigate("register"))
        
#         register_container.addStretch()
#         register_container.addWidget(register_label)
#         register_container.addWidget(register_btn)
#         register_container.addStretch()
        
#         form_layout.addWidget(username_label)
#         form_layout.addWidget(self.username_input)
#         form_layout.addWidget(password_label)
#         form_layout.addWidget(self.password_input)
#         form_layout.addWidget(self.error_label)
#         form_layout.addWidget(login_btn)
        
#         layout.addWidget(icon_label)
#         layout.addWidget(title)
#         layout.addWidget(subtitle)
#         layout.addSpacing(10)
#         layout.addWidget(form_container)
#         layout.addLayout(register_container)
#         layout.addStretch()
        
#         # Position center widget
#         main_layout.takeAt(0)  # Remove gradient temporarily
#         main_layout.addStretch()
#         main_layout.addWidget(center)
#         main_layout.addStretch()
    
#     def handle_login(self):
#         """Handle login"""
#         username = self.username_input.text()
#         password = self.password_input.text()
        
#         if not username or not password:
#             self.error_label.setText("Please enter both username and password")
#             self.error_label.setVisible(True)
#             return
        
#         success, message = self.api_client.login(username, password)
        
#         if success:
#             self.main_window.on_login_success()
#         else:
#             self.error_label.setText(message)
#             self.error_label.setVisible(True)


# class RegisterPage(QWidget):
#     """Registration page"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
        
#         main_layout = QHBoxLayout(self)
#         main_layout.setContentsMargins(0, 0, 0, 0)
        
#         # Background gradient
#         main_layout.addWidget(GradientWidget("#f8fafc", "#e0f2fe"))
        
#         # Center content
#         center = QWidget()
#         center.setMaximumWidth(450)
        
#         layout = QVBoxLayout(center)
#         layout.setContentsMargins(40, 60, 40, 60)
#         layout.setSpacing(25)
#         layout.setAlignment(Qt.AlignCenter)
        
#         # Logo/Icon
#         icon_label = QLabel("✨")
#         icon_label.setAlignment(Qt.AlignCenter)
#         icon_label.setStyleSheet("font-size: 48px;")
        
#         # Title
#         title = QLabel("Create Account")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 32px; font-weight: 900; color: #0f172a;")
        
#         subtitle = QLabel("Get started with your free account today")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 14px; color: #64748b;")
        
#         # Form container
#         form_container = QFrame()
#         form_container.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         form_layout = QVBoxLayout(form_container)
#         form_layout.setContentsMargins(30, 30, 30, 30)
#         form_layout.setSpacing(20)
        
#         # Username
#         username_label = QLabel("USERNAME")
#         username_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.username_input = QLineEdit()
#         self.username_input.setPlaceholderText("Choose a username")
#         self.username_input.setFixedHeight(45)
#         self.username_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Password
#         password_label = QLabel("PASSWORD")
#         password_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Create a strong password")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         self.password_input.setFixedHeight(45)
#         self.password_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Error label
#         self.error_label = QLabel()
#         self.error_label.setVisible(False)
#         self.error_label.setStyleSheet("color: #ef4444; font-size: 12px;")
#         self.error_label.setWordWrap(True)
        
#         # Register button
#         register_btn = QPushButton("Create Account")
#         register_btn.setFixedHeight(50)
#         register_btn.setCursor(Qt.PointingHandCursor)
#         register_btn.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 16px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#         """)
#         register_btn.clicked.connect(self.handle_register)
        
#         # Login link
#         login_container = QHBoxLayout()
#         login_label = QLabel("Already have an account?")
#         login_label.setStyleSheet("font-size: 13px; color: #64748b;")
        
#         login_btn = QPushButton("Sign in")
#         login_btn.setCursor(Qt.PointingHandCursor)
#         login_btn.setStyleSheet("""
#             QPushButton {
#                 background: none;
#                 border: none;
#                 color: #3b82f6;
#                 font-size: 13px;
#                 font-weight: bold;
#                 text-decoration: underline;
#             }
#             QPushButton:hover {
#                 color: #2563eb;
#             }
#         """)
#         login_btn.clicked.connect(lambda: self.main_window.navigate("login"))
        
#         login_container.addStretch()
#         login_container.addWidget(login_label)
#         login_container.addWidget(login_btn)
#         login_container.addStretch()
        
#         form_layout.addWidget(username_label)
#         form_layout.addWidget(self.username_input)
#         form_layout.addWidget(password_label)
#         form_layout.addWidget(self.password_input)
#         form_layout.addWidget(self.error_label)
#         form_layout.addWidget(register_btn)
        
#         layout.addWidget(icon_label)
#         layout.addWidget(title)
#         layout.addWidget(subtitle)
#         layout.addSpacing(10)
#         layout.addWidget(form_container)
#         layout.addLayout(login_container)
#         layout.addStretch()
        
#         # Position center widget
#         main_layout.takeAt(0)
#         main_layout.addStretch()
#         main_layout.addWidget(center)
#         main_layout.addStretch()
    
#     def handle_register(self):
#         """Handle registration"""
#         username = self.username_input.text()
#         password = self.password_input.text()
        
#         if not username or not password:
#             self.error_label.setText("Please enter both username and password")
#             self.error_label.setVisible(True)
#             return
        
#         if len(password) < 8:
#             self.error_label.setText("Password must be at least 8 characters")
#             self.error_label.setVisible(True)
#             return
        
#         success, message = self.api_client.register(username, password)
        
#         if success:
#             self.main_window.on_login_success()
#         else:
#             self.error_label.setText(message)
#             self.error_label.setVisible(True)


# class MainWindow(QMainWindow):
#     """Main application window"""
    
#     def __init__(self):
#         super().__init__()
#         self.api_client = APIClient()
#         self.setup_ui()
        
#         # Check if already logged in
#         if self.api_client.token:
#             self.show_app()
#         else:
#             self.navigate("login")
    
#     def setup_ui(self):
#         """Setup main UI"""
#         self.setWindowTitle("Chemical Equipment Analytics Platform")
#         self.setMinimumSize(1400, 900)
        
#         # Central widget with stacked layout
#         central = QWidget()
#         self.setCentralWidget(central)
        
#         self.main_layout = QVBoxLayout(central)
#         self.main_layout.setContentsMargins(0, 0, 0, 0)
#         self.main_layout.setSpacing(0)
        
#         # Navigation bar (hidden initially)
#         self.navbar = self.create_navbar()
#         self.navbar.setVisible(False)
        
#         # Stacked widget for pages
#         self.pages = QStackedWidget()
        
#         # Create pages
#         self.home_page = HomePage(self)
#         self.upload_page = UploadPage(self, self.api_client)
#         self.summary_page = SummaryPage(self, self.api_client)
#         self.analytics_page = AnalyticsPage(self, self.api_client)
#         self.login_page = LoginPage(self, self.api_client)
#         self.register_page = RegisterPage(self, self.api_client)
        
#         # Add pages to stack
#         self.pages.addWidget(self.home_page)       # 0
#         self.pages.addWidget(self.upload_page)     # 1
#         self.pages.addWidget(self.summary_page)    # 2
#         self.pages.addWidget(self.analytics_page)  # 3
#         self.pages.addWidget(self.login_page)      # 4
#         self.pages.addWidget(self.register_page)   # 5
        
#         self.main_layout.addWidget(self.navbar)
#         self.main_layout.addWidget(self.pages)
        
#         # Apply global stylesheet
#         self.setStyleSheet("""
#             QMainWindow {
#                 background-color: #f8fafc;
#             }
#         """)
    
#     def create_navbar(self):
#         """Create navigation bar"""
#         navbar = QFrame()
#         navbar.setFixedHeight(70)
#         navbar.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-bottom: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QHBoxLayout(navbar)
#         layout.setContentsMargins(30, 0, 30, 0)
#         layout.setSpacing(20)
        
#         # Logo
#         logo = QLabel("⚡ CHEMANALYZE")
#         logo.setStyleSheet("font-size: 20px; font-weight: 900; color: #3b82f6;")
        
#         # Navigation buttons
#         btn_home = self.create_nav_button("Home", "home")
#         btn_upload = self.create_nav_button("Upload", "upload")
#         btn_summary = self.create_nav_button("Summary", "summary")
#         btn_analytics = self.create_nav_button("Analytics", "analytics")
        
#         # Logout button
#         btn_logout = QPushButton("Logout")
#         btn_logout.setCursor(Qt.PointingHandCursor)
#         btn_logout.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 color: #ef4444;
#                 font-size: 13px;
#                 font-weight: bold;
#                 border: 2px solid #fecaca;
#                 border-radius: 10px;
#                 padding: 8px 20px;
#             }
#             QPushButton:hover {
#                 background-color: #fef2f2;
#                 border-color: #ef4444;
#             }
#         """)
#         btn_logout.clicked.connect(self.handle_logout)
        
#         layout.addWidget(logo)
#         layout.addSpacing(30)
#         layout.addWidget(btn_home)
#         layout.addWidget(btn_upload)
#         layout.addWidget(btn_summary)
#         layout.addWidget(btn_analytics)
#         layout.addStretch()
#         layout.addWidget(btn_logout)
        
#         return navbar
    
#     def create_nav_button(self, text, page):
#         """Create navigation button"""
#         btn = QPushButton(text)
#         btn.setCursor(Qt.PointingHandCursor)
#         btn.setStyleSheet("""
#             QPushButton {
#                 background-color: transparent;
#                 color: #64748b;
#                 font-size: 14px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 10px;
#                 padding: 10px 20px;
#             }
#             QPushButton:hover {
#                 background-color: #f1f5f9;
#                 color: #3b82f6;
#             }
#         """)
#         btn.clicked.connect(lambda: self.navigate(page))
#         return btn
    
#     def navigate(self, page_name):
#         """Navigate to page"""
#         page_map = {
#             "home": 0,
#             "upload": 1,
#             "summary": 2,
#             "analytics": 3,
#             "login": 4,
#             "register": 5
#         }
        
#         if page_name in page_map:
#             self.pages.setCurrentIndex(page_map[page_name])
            
#             # Refresh data on certain pages
#             if page_name == "summary":
#                 self.summary_page.load_data()
#             elif page_name == "analytics":
#                 self.analytics_page.load_datasets()
    
#     def on_login_success(self):
#         """Handle successful login"""
#         self.show_app()
    
#     def show_app(self):
#         """Show main app (after login)"""
#         self.navbar.setVisible(True)
#         self.navigate("home")
    
#     def handle_logout(self):
#         """Handle logout"""
#         self.api_client.clear_token()
#         self.navbar.setVisible(False)
#         self.navigate("login")


# def main():
#     app = QApplication(sys.argv)
    
#     # Set application font
#     font = QFont("Segoe UI", 10)
#     app.setFont(font)
    
#     window = MainWindow()
#     window.show()
    
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()


"""
Chemical Equipment Analytics Platform - Desktop Application
Complete PyQt5 implementation with all web app features
"""

import sys
import os
import json
import requests
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QLineEdit, QFileDialog, QTableWidget, 
    QTableWidgetItem, QScrollArea, QFrame, QGridLayout, QStackedWidget,
    QHeaderView, QMessageBox, QProgressBar, QTabWidget, QSplitter
)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QSize, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon, QPainter, QLinearGradient, QBrush
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis

# API Configuration
API_BASE = "http://127.0.0.1:8000/api"


class APIClient:
    """Handles all API interactions"""
    
    def __init__(self):
        self.base_url = API_BASE
        self.token = None
        self.load_token()
    
    def load_token(self):
        """Load token from file"""
        try:
            if os.path.exists('token.txt'):
                with open('token.txt', 'r') as f:
                    self.token = f.read().strip()
        except:
            pass
    
    def save_token(self, token):
        """Save token to file"""
        self.token = token
        with open('token.txt', 'w') as f:
            f.write(token)
    
    def clear_token(self):
        """Clear saved token"""
        self.token = None
        if os.path.exists('token.txt'):
            os.remove('token.txt')
    
    def get_headers(self):
        """Get request headers with auth token"""
        headers = {}
        if self.token:
            headers['Authorization'] = f'Token {self.token}'
        return headers
    
    def register(self, username, password):
        """Register new user"""
        try:
            response = requests.post(
                f"{self.base_url}/register/",
                json={"username": username, "password": password}
            )
            response.raise_for_status()
            data = response.json()
            self.save_token(data['token'])
            return True, "Registration successful"
        except requests.exceptions.RequestException as e:
            return False, str(e)
    
    def login(self, username, password):
        """Login user"""
        try:
            response = requests.post(
                f"{self.base_url}/login/",
                json={"username": username, "password": password}
            )
            response.raise_for_status()
            data = response.json()
            self.save_token(data['token'])
            return True, "Login successful"
        except requests.exceptions.RequestException as e:
            return False, "Invalid username or password"
    
    def upload_csv(self, file_path):
        """Upload CSV file"""
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post(
                    f"{self.base_url}/upload/",
                    files=files,
                    headers=self.get_headers()
                )
                response.raise_for_status()
                return True, response.json()
        except requests.exceptions.RequestException as e:
            return False, str(e)
    
    def get_latest_summary(self):
        """Get latest dataset summary"""
        try:
            response = requests.get(
                f"{self.base_url}/summary/latest/",
                headers=self.get_headers()
            )
            response.raise_for_status()
            return True, response.json()
        except:
            return False, None
    
    def get_history(self):
        """Get upload history"""
        try:
            response = requests.get(
                f"{self.base_url}/history/",
                headers=self.get_headers()
            )
            response.raise_for_status()
            return True, response.json()
        except:
            return False, []
    
    def download_report(self, dataset_id, save_path):
        """Download PDF report"""
        try:
            response = requests.get(
                f"{self.base_url}/report/{dataset_id}/",
                headers=self.get_headers()
            )
            response.raise_for_status()
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True, "Report downloaded successfully"
        except:
            return False, "Failed to download report"


class UploadThread(QThread):
    """Background thread for file upload"""
    finished = pyqtSignal(bool, object)
    
    def __init__(self, api_client, file_path):
        super().__init__()
        self.api_client = api_client
        self.file_path = file_path
    
    def run(self):
        success, result = self.api_client.upload_csv(self.file_path)
        self.finished.emit(success, result)


class GradientWidget(QWidget):
    """Widget with gradient background"""
    
    def __init__(self, color1, color2, parent=None):
        super().__init__(parent)
        self.color1 = QColor(color1)
        self.color2 = QColor(color2)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, self.color1)
        gradient.setColorAt(1, self.color2)
        painter.fillRect(self.rect(), gradient)


class StatCard(QFrame):
    """KPI Stat Card Widget"""
    
    def __init__(self, label, value, color_start, color_end):
        super().__init__()
        self.setObjectName("StatCard")
        self.setFixedHeight(120)
        self.setStyleSheet(f"""
            QFrame#StatCard {{
                background-color: white;
                border-radius: 16px;
                border: 2px solid #e2e8f0;
            }}
            QFrame#StatCard:hover {{
                border: 2px solid #cbd5e1;
                background-color: #fafafa;
            }}
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(8)
        
        # Label
        lbl = QLabel(label.upper())
        lbl.setStyleSheet("font-size: 11px; font-weight: bold; color: #64748b;")
        
        # Value
        val = QLabel(str(value) if isinstance(value, int) else f"{value:.1f}")
        val.setStyleSheet(f"""
            font-size: 32px; 
            font-weight: 900; 
            color: {color_start};
        """)
        
        layout.addWidget(lbl)
        layout.addWidget(val)
        layout.addStretch()


class FeatureCard(QFrame):
    """Feature showcase card"""
    
    def __init__(self, title, description):
        super().__init__()
        self.setFixedSize(360, 260)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                border: 2px solid #e2e8f0;
            }
            QFrame:hover {
                border: 2px solid #cbd5e1;
                background-color: #f8fafc;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)
        
        # Icon placeholder
        icon_frame = QFrame()
        icon_frame.setFixedSize(60, 60)
        icon_frame.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 #3b82f6, stop:1 #06b6d4);
            border-radius: 30px;
        """)
        
        # Title
        title_lbl = QLabel(title)
        title_lbl.setStyleSheet("""
            font-size: 20px; 
            font-weight: bold; 
            color: #0f172a;
        """)
        title_lbl.setWordWrap(True)
        title_lbl.setAlignment(Qt.AlignCenter)
        
        # Description
        desc_lbl = QLabel(description)
        desc_lbl.setStyleSheet("font-size: 14px; color: #64748b;")
        desc_lbl.setWordWrap(True)
        desc_lbl.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(icon_frame, alignment=Qt.AlignCenter)
        layout.addWidget(title_lbl)
        layout.addWidget(desc_lbl)
        layout.addStretch()


class HomePage(QWidget):
    """Home page with hero section and features"""
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: #f8fafc; }")
        
        content = QWidget()
        main_layout = QVBoxLayout(content)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Hero Section
        hero = QWidget()
        hero.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f1f5f9);")
        hero_layout = QVBoxLayout(hero)
        hero_layout.setContentsMargins(50, 80, 50, 80)
        hero_layout.setSpacing(25)
        hero_layout.setAlignment(Qt.AlignCenter)
        
        # Badge
        badge = QLabel("⚡ PRECISION ENGINEERING DASHBOARD")
        badge.setStyleSheet("""
            background-color: #eff6ff;
            color: #1e40af;
            font-size: 12px;
            font-weight: bold;
            padding: 10px 24px;
            border-radius: 20px;
            border: 2px solid #bfdbfe;
        """)
        
        # Title
        title = QLabel("Chemical Equipment\nAnalytics Platform")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 56px; 
            font-weight: 900; 
            color: #0f172a;
        """)
        
        # Subtitle
        subtitle = QLabel("Transform raw operational data into actionable intelligence.\nAnalyze flowrates and pressures to generate professional reports instantly.")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("font-size: 17px; color: #475569; margin-top: 10px;")
        
        # Buttons
        btn_container = QHBoxLayout()
        btn_container.setSpacing(20)
        
        btn_start = QPushButton("Start Analysis Engine")
        btn_start.setFixedSize(260, 55)
        btn_start.setCursor(Qt.PointingHandCursor)
        btn_start.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #3b82f6, stop:1 #2563eb);
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 12px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #2563eb, stop:1 #1d4ed8);
            }
        """)
        btn_start.clicked.connect(lambda: self.main_window.navigate("upload"))
        
        btn_dash = QPushButton("View Dashboard")
        btn_dash.setFixedSize(260, 55)
        btn_dash.setCursor(Qt.PointingHandCursor)
        btn_dash.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #1e293b;
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #e2e8f0;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #f8fafc;
                border-color: #cbd5e1;
            }
        """)
        btn_dash.clicked.connect(lambda: self.main_window.navigate("analytics"))
        
        btn_container.addWidget(btn_start)
        btn_container.addWidget(btn_dash)
        
        hero_layout.addWidget(badge, alignment=Qt.AlignCenter)
        hero_layout.addWidget(title)
        hero_layout.addWidget(subtitle)
        hero_layout.addSpacing(20)
        hero_layout.addLayout(btn_container)
        
        # Features Section
        features = QWidget()
        features.setStyleSheet("background-color: #f8fafc; border-top: 1px solid #e2e8f0;")
        features_layout = QVBoxLayout(features)
        features_layout.setContentsMargins(60, 80, 60, 80)
        features_layout.setSpacing(50)
        
        f_title = QLabel("Powerful Analytics Features")
        f_title.setAlignment(Qt.AlignCenter)
        f_title.setStyleSheet("font-size: 38px; font-weight: 800; color: #0f172a;")
        
        f_subtitle = QLabel("Everything you need to monitor and optimize your chemical equipment")
        f_subtitle.setAlignment(Qt.AlignCenter)
        f_subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
        features_layout.addWidget(f_title)
        features_layout.addWidget(f_subtitle)
        
        # Grid of features
        grid = QGridLayout()
        grid.setSpacing(30)
        
        features_data = [
            ("Real-time Metrics", "Track equipment count, average flowrate, and pressure with live updates."),
            ("Health Scoring", "Automated algorithms analyze parameters to calculate health scores."),
            ("Risk Assessment", "Advanced systems identify high-risk equipment based on thresholds."),
            ("CSV Processing", "Upload large-scale logs instantly with intelligent validation."),
            ("Professional Reports", "Generate executive-ready PDF reports with KPI summaries."),
            ("Type Distribution", "Visual breakdown of equipment by type with detailed charts.")
        ]
        
        for i, (title, desc) in enumerate(features_data):
            row = i // 3
            col = i % 3
            grid.addWidget(FeatureCard(title, desc), row, col, Qt.AlignCenter)
        
        features_layout.addLayout(grid)
        
        # Build page
        main_layout.addWidget(hero)
        # main_layout.addWidget(features)
        
        scroll.setWidget(content)
        
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)


# class UploadPage(QWidget):
#     """File upload page with drag-drop and analytics preview"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
#         self.selected_file = None
#         self.overview_data = None
        
#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(40, 40, 40, 40)
#         main_layout.setSpacing(30)
        
#         # Title
#         title = QLabel("Chemical Equipment Analysis")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("""
#             font-size: 42px; 
#             font-weight: 900;
#             color: #3b82f6;
#         """)
        
#         subtitle = QLabel("Upload your dataset and unlock powerful insights instantly")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
#         main_layout.addWidget(title)
#         main_layout.addWidget(subtitle)
#         main_layout.addSpacing(20)
        
#         # Content area - split into two columns
#         content_layout = QHBoxLayout()
#         content_layout.setSpacing(30)
        
#         # LEFT: Upload panel
#         upload_panel = self.create_upload_panel()
        
#         # RIGHT: Preview panel
#         self.preview_panel = self.create_preview_panel()
        
#         content_layout.addWidget(upload_panel, 1)
#         content_layout.addWidget(self.preview_panel, 1)
        
#         main_layout.addLayout(content_layout)
    
#     def create_upload_panel(self):
#         """Create upload section"""
#         panel = QFrame()
#         panel.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(panel)
#         layout.setContentsMargins(30, 30, 30, 30)
#         layout.setSpacing(20)
        
#         # Header
#         header_layout = QHBoxLayout()
#         header_icon = QLabel("📁")
#         header_icon.setStyleSheet("font-size: 32px;")
        
#         header_text = QWidget()
#         header_text_layout = QVBoxLayout(header_text)
#         header_text_layout.setContentsMargins(0, 0, 0, 0)
#         header_text_layout.setSpacing(2)
        
#         h_title = QLabel("Upload Dataset")
#         h_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
#         h_subtitle = QLabel("Select or drag & drop CSV file")
#         h_subtitle.setStyleSheet("font-size: 12px; color: #64748b;")
        
#         header_text_layout.addWidget(h_title)
#         header_text_layout.addWidget(h_subtitle)
        
#         header_layout.addWidget(header_icon)
#         header_layout.addWidget(header_text)
#         header_layout.addStretch()
        
#         # File selection area
#         file_area = QFrame()
#         file_area.setMinimumHeight(200)
#         file_area.setStyleSheet("""
#             QFrame {
#                 background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                     stop:0 #f8fafc, stop:1 #eff6ff);
#                 border: 2px dashed #cbd5e1;
#                 border-radius: 16px;
#             }
#         """)
        
#         file_layout = QVBoxLayout(file_area)
#         file_layout.setAlignment(Qt.AlignCenter)
        
#         self.file_label = QLabel("📄\n\nClick to browse or drop CSV file here")
#         self.file_label.setAlignment(Qt.AlignCenter)
#         self.file_label.setStyleSheet("font-size: 14px; color: #64748b;")
        
#         file_layout.addWidget(self.file_label)
        
#         # Browse button
#         browse_btn = QPushButton("Browse Files")
#         browse_btn.setFixedHeight(45)
#         browse_btn.setCursor(Qt.PointingHandCursor)
#         browse_btn.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 color: #3b82f6;
#                 font-size: 14px;
#                 font-weight: bold;
#                 border: 2px solid #3b82f6;
#                 border-radius: 10px;
#                 padding: 0 30px;
#             }
#             QPushButton:hover {
#                 background-color: #eff6ff;
#             }
#         """)
#         browse_btn.clicked.connect(self.browse_file)
        
#         # Upload button
#         self.upload_btn = QPushButton("Upload & Analyze Dataset")
#         self.upload_btn.setFixedHeight(50)
#         self.upload_btn.setCursor(Qt.PointingHandCursor)
#         self.upload_btn.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 15px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#             QPushButton:disabled {
#                 background-color: #cbd5e1;
#             }
#         """)
#         self.upload_btn.clicked.connect(self.upload_file)
#         self.upload_btn.setEnabled(False)
        
#         # Progress bar
#         self.progress_bar = QProgressBar()
#         self.progress_bar.setVisible(False)
#         self.progress_bar.setStyleSheet("""
#             QProgressBar {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 8px;
#                 text-align: center;
#                 background-color: white;
#             }
#             QProgressBar::chunk {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #06b6d4);
#                 border-radius: 6px;
#             }
#         """)
        
#         # Error label
#         self.error_label = QLabel()
#         self.error_label.setVisible(False)
#         self.error_label.setStyleSheet("color: #ef4444; font-size: 12px;")
#         self.error_label.setWordWrap(True)
        
#         layout.addLayout(header_layout)
#         layout.addWidget(file_area)
#         layout.addWidget(browse_btn)
#         layout.addWidget(self.upload_btn)
#         layout.addWidget(self.progress_bar)
#         layout.addWidget(self.error_label)
#         layout.addStretch()
        
#         return panel
    
#     def create_preview_panel(self):
#         """Create data preview panel"""
#         panel = QFrame()
#         panel.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(panel)
#         layout.setContentsMargins(30, 30, 30, 30)
#         layout.setSpacing(20)
        
#         # Header
#         header = QLabel("Dataset Insights")
#         header.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
        
#         # Content area (will be populated after upload)
#         self.preview_content = QWidget()
#         self.preview_layout = QVBoxLayout(self.preview_content)
#         self.preview_layout.setAlignment(Qt.AlignCenter)
        
#         # Default state
#         empty_icon = QLabel("📊")
#         empty_icon.setAlignment(Qt.AlignCenter)
#         empty_icon.setStyleSheet("font-size: 64px;")
        
#         empty_text = QLabel("Upload a dataset to view instant analytics")
#         empty_text.setAlignment(Qt.AlignCenter)
#         empty_text.setStyleSheet("font-size: 14px; color: #94a3b8;")
        
#         self.preview_layout.addWidget(empty_icon)
#         self.preview_layout.addWidget(empty_text)
        
#         layout.addWidget(header)
#         layout.addWidget(self.preview_content)
        
#         return panel
    
#     def browse_file(self):
#         """Open file browser"""
#         file_path, _ = QFileDialog.getOpenFileName(
#             self,
#             "Select CSV File",
#             "",
#             "CSV Files (*.csv)"
#         )
        
#         if file_path:
#             self.selected_file = file_path
#             file_name = os.path.basename(file_path)
#             self.file_label.setText(f"✅ {file_name}")
#             self.upload_btn.setEnabled(True)
#             self.error_label.setVisible(False)
    
#     def upload_file(self):
#         """Upload selected file"""
#         if not self.selected_file:
#             return
        
#         self.upload_btn.setEnabled(False)
#         self.progress_bar.setVisible(True)
#         self.progress_bar.setRange(0, 0)  # Indeterminate
#         self.error_label.setVisible(False)
        
#         # Start upload thread
#         self.upload_thread = UploadThread(self.api_client, self.selected_file)
#         self.upload_thread.finished.connect(self.upload_finished)
#         self.upload_thread.start()
    
#     def upload_finished(self, success, result):
#         """Handle upload completion"""
#         self.progress_bar.setVisible(False)
#         self.upload_btn.setEnabled(True)
        
#         if success:
#             self.overview_data = result
#             self.update_preview(result)
#             QMessageBox.information(self, "Success", "File uploaded successfully!")
#         else:
#             self.error_label.setText(f"Upload failed: {result}")
#             self.error_label.setVisible(True)
    
#     def update_preview(self, data):
#         """Update preview panel with data"""
#         # Clear existing content
#         while self.preview_layout.count():
#             item = self.preview_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # KPI Grid
#         kpi_grid = QGridLayout()
#         kpi_grid.setSpacing(15)
        
#         kpi_grid.addWidget(StatCard("Total Equipment", data.get('total_equipment', 0), "#3b82f6", "#06b6d4"), 0, 0)
#         kpi_grid.addWidget(StatCard("Avg Flowrate", data.get('avg_flowrate', 0), "#8b5cf6", "#d946ef"), 0, 1)
#         kpi_grid.addWidget(StatCard("Avg Pressure", data.get('avg_pressure', 0), "#ef4444", "#f97316"), 1, 0)
#         kpi_grid.addWidget(StatCard("Avg Temperature", data.get('avg_temperature', 0), "#10b981", "#14b8a6"), 1, 1)
        
#         # Health score bar
#         health_widget = QWidget()
#         health_layout = QVBoxLayout(health_widget)
#         health_layout.setContentsMargins(15, 15, 15, 15)
#         health_widget.setStyleSheet("""
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                 stop:0 #f8fafc, stop:1 #eff6ff);
#             border-radius: 12px;
#         """)
        
#         health_header = QHBoxLayout()
#         health_label = QLabel("OVERALL HEALTH SCORE")
#         health_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #64748b;")
#         health_value = QLabel(f"{int(data.get('health_score', 0))}%")
#         health_value.setStyleSheet("font-size: 28px; font-weight: 900; color: #10b981;")
#         health_header.addWidget(health_label)
#         health_header.addStretch()
#         health_header.addWidget(health_value)
        
#         health_bar = QProgressBar()
#         health_bar.setRange(0, 100)
#         health_bar.setValue(int(data.get('health_score', 0)))
#         health_bar.setTextVisible(False)
#         health_bar.setFixedHeight(24)
        
#         score = data.get('health_score', 0)
#         if score >= 70:
#             color = "#10b981"
#         elif score >= 40:
#             color = "#f59e0b"
#         else:
#             color = "#ef4444"
        
#         health_bar.setStyleSheet(f"""
#             QProgressBar {{
#                 border: none;
#                 border-radius: 12px;
#                 background-color: #e2e8f0;
#             }}
#             QProgressBar::chunk {{
#                 background-color: {color};
#                 border-radius: 12px;
#             }}
#         """)
        
#         health_layout.addLayout(health_header)
#         health_layout.addWidget(health_bar)
        
#         # Action buttons
#         btn_layout = QHBoxLayout()
#         btn_layout.setSpacing(15)
        
#         btn_summary = QPushButton("View Summary")
#         btn_summary.setFixedHeight(45)
#         btn_summary.setCursor(Qt.PointingHandCursor)
#         btn_summary.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 14px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 10px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#         """)
#         btn_summary.clicked.connect(lambda: self.main_window.navigate("summary"))
        
#         btn_analytics = QPushButton("Analytics")
#         btn_analytics.setFixedHeight(45)
#         btn_analytics.setCursor(Qt.PointingHandCursor)
#         btn_analytics.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 color: #3b82f6;
#                 font-size: 14px;
#                 font-weight: bold;
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#             }
#             QPushButton:hover {
#                 background-color: #eff6ff;
#                 border-color: #3b82f6;
#             }
#         """)
#         btn_analytics.clicked.connect(lambda: self.main_window.navigate("analytics"))
        
#         btn_layout.addWidget(btn_summary)
#         btn_layout.addWidget(btn_analytics)
        
#         self.preview_layout.addLayout(kpi_grid)
#         self.preview_layout.addSpacing(20)
#         self.preview_layout.addWidget(health_widget)
#         self.preview_layout.addSpacing(20)
#         self.preview_layout.addLayout(btn_layout)
#         self.preview_layout.addStretch()


# class UploadPage(QWidget):
#     """File upload page with drag-drop and analytics preview"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
#         self.selected_file = None
#         self.overview_data = None
        
#         # Base background color for the whole page
#         self.setStyleSheet("background-color: #f8fafc;")

#         page_layout = QVBoxLayout(self)
#         page_layout.setContentsMargins(0, 0, 0, 0)

#         # Title Section
#         header_widget = QWidget()
#         header_layout = QVBoxLayout(header_widget)
#         header_layout.setContentsMargins(40, 40, 40, 10)
        
#         title = QLabel("Chemical Equipment Analysis")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 36px; font-weight: 800; color: #1e293b;")
        
#         subtitle = QLabel("Upload your dataset and unlock powerful insights instantly")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 15px; color: #64748b; margin-bottom: 10px;")
        
#         header_layout.addWidget(title)
#         header_layout.addWidget(subtitle)
#         page_layout.addWidget(header_widget)

#         # Main content area (Two Columns)
#         content_container = QWidget()
#         content_layout = QHBoxLayout(content_container)
#         content_layout.setContentsMargins(40, 0, 40, 40)
#         content_layout.setSpacing(30)

#         # LEFT: Upload Panel
#         self.upload_panel = self.create_upload_panel()
        
#         # RIGHT: Preview Panel
#         self.preview_panel = self.create_preview_panel()
        
#         content_layout.addWidget(self.upload_panel, 1)
#         content_layout.addWidget(self.preview_panel, 1)
        
#         page_layout.addWidget(content_container)

#     def create_upload_panel(self):
#         panel = QFrame()
#         panel.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 16px;
#                 border: 1px solid #e2e8f0;
#             }
#         """)
#         layout = QVBoxLayout(panel)
#         layout.setContentsMargins(30, 30, 30, 30)
#         layout.setSpacing(20)

#         # UI Elements
#         h_title = QLabel("📁 Upload Dataset")
#         h_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #0f172a; border: none;")
        
#         self.file_area = QFrame()
#         self.file_area.setMinimumHeight(250)
#         self.file_area.setStyleSheet("""
#             QFrame {
#                 background-color: #f1f5f9;
#                 border: 2px dashed #cbd5e1;
#                 border-radius: 12px;
#             }
#         """)
#         fa_layout = QVBoxLayout(self.file_area)
#         self.file_label = QLabel("Click 'Browse' to select a CSV file")
#         self.file_label.setStyleSheet("color: #64748b; border: none;")
#         fa_layout.addWidget(self.file_label, 0, Qt.AlignCenter)

#         browse_btn = QPushButton("Browse Files")
#         browse_btn.setFixedHeight(45)
#         browse_btn.setCursor(Qt.PointingHandCursor)
#         browse_btn.setStyleSheet("""
#             QPushButton {
#                 background-color: #ffffff;
#                 border: 1px solid #cbd5e1;
#                 border-radius: 8px;
#                 font-weight: 600;
#             }
#             QPushButton:hover { background-color: #f8fafc; border-color: #3b82f6; }
#         """)
#         browse_btn.clicked.connect(self.browse_file)

#         self.upload_btn = QPushButton("Analyze Dataset")
#         self.upload_btn.setFixedHeight(50)
#         self.upload_btn.setEnabled(False)
#         self.upload_btn.setCursor(Qt.PointingHandCursor)
#         self.upload_btn.setStyleSheet("""
#             QPushButton {
#                 background-color: #3b82f6;
#                 color: white;
#                 border-radius: 8px;
#                 font-weight: bold;
#                 font-size: 14px;
#             }
#             QPushButton:hover { background-color: #2563eb; }
#             QPushButton:disabled { background-color: #94a3b8; }
#         """)
#         self.upload_btn.clicked.connect(self.upload_file)

#         self.progress_bar = QProgressBar()
#         self.progress_bar.setVisible(False)
#         self.progress_bar.setFixedHeight(10)
#         self.progress_bar.setTextVisible(False)

#         self.error_label = QLabel()
#         self.error_label.setStyleSheet("color: #ef4444; border: none;")
#         self.error_label.setVisible(False)

#         layout.addWidget(h_title)
#         layout.addWidget(self.file_area)
#         layout.addWidget(browse_btn)
#         layout.addWidget(self.upload_btn)
#         layout.addWidget(self.progress_bar)
#         layout.addWidget(self.error_label)
#         layout.addStretch()
#         return panel

#     def create_preview_panel(self):
#         panel = QFrame()
#         panel.setObjectName("PreviewPanel")
#         panel.setStyleSheet("""
#             QFrame#PreviewPanel {
#                 background-color: white;
#                 border-radius: 16px;
#                 border: 1px solid #e2e8f0;
#             }
#         """)
        
#         self.preview_layout = QVBoxLayout(panel)
#         self.preview_layout.setContentsMargins(30, 30, 30, 30)
#         self.preview_layout.setSpacing(20)
        
#         self.show_empty_state()
#         return panel

#     def show_empty_state(self):
#         # Clear layout
#         self.clear_preview_layout()
        
#         header = QLabel("Dataset Insights")
#         header.setStyleSheet("font-size: 18px; font-weight: bold; color: #0f172a;")
        
#         empty_icon = QLabel("📊")
#         empty_icon.setStyleSheet("font-size: 48px; margin-top: 50px;")
#         empty_text = QLabel("Upload a dataset to view metrics")
#         empty_text.setStyleSheet("color: #94a3b8; font-size: 14px;")
        
#         self.preview_layout.addWidget(header)
#         self.preview_layout.addWidget(empty_icon, 0, Qt.AlignCenter)
#         self.preview_layout.addWidget(empty_text, 0, Qt.AlignCenter)
#         self.preview_layout.addStretch()

#     def clear_preview_layout(self):
#         while self.preview_layout.count():
#             item = self.preview_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()

#     def browse_file(self):
#         file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV", "", "CSV Files (*.csv)")
#         if file_path:
#             self.selected_file = file_path
#             self.file_label.setText(f"Selected: {os.path.basename(file_path)}")
#             self.upload_btn.setEnabled(True)

#     def upload_file(self):
#         self.upload_btn.setEnabled(False)
#         self.progress_bar.setVisible(True)
#         self.progress_bar.setRange(0, 0)
        
#         self.upload_thread = UploadThread(self.api_client, self.selected_file)
#         self.upload_thread.finished.connect(self.upload_finished)
#         self.upload_thread.start()

#     def upload_finished(self, success, result):
#         self.progress_bar.setVisible(False)
#         self.upload_btn.setEnabled(True)
#         if success:
#             self.update_preview(result)
#         else:
#             self.error_label.setText(f"Error: {result}")
#             self.error_label.setVisible(True)

#     def update_preview(self, data):
#         self.clear_preview_layout()
        
#         # Header
#         header = QLabel("Analysis Results")
#         header.setStyleSheet("font-size: 18px; font-weight: bold; color: #0f172a;")
#         self.preview_layout.addWidget(header)

#         # KPI Grid
#         kpi_grid_widget = QWidget()
#         kpi_grid = QGridLayout(kpi_grid_widget)
#         kpi_grid.setContentsMargins(0,0,0,0)
#         kpi_grid.setSpacing(10)

#         # Using the StatCard class provided in your previous code
#         kpi_grid.addWidget(StatCard("Total Items", data.get('total_equipment', 0), "#3b82f6", "#60a5fa"), 0, 0)
#         kpi_grid.addWidget(StatCard("Flowrate", data.get('avg_flowrate', 0), "#8b5cf6", "#a78bfa"), 0, 1)
#         kpi_grid.addWidget(StatCard("Pressure", data.get('avg_pressure', 0), "#ef4444", "#fb7185"), 1, 0)
#         kpi_grid.addWidget(StatCard("Temp", data.get('avg_temperature', 0), "#10b981", "#34d399"), 1, 1)
        
#         self.preview_layout.addWidget(kpi_grid_widget)

#         # Health Section
#         score = int(data.get('health_score', 0))
#         color = "#10b981" if score >= 70 else "#f59e0b" if score >= 40 else "#ef4444"
        
#         health_card = QFrame()
#         health_card.setStyleSheet(f"""
#             QFrame {{
#                 background-color: #f8fafc;
#                 border-radius: 12px;
#                 border: 1px solid #e2e8f0;
#             }}
#         """)
#         hl = QVBoxLayout(health_card)
        
#         ht_layout = QHBoxLayout()
#         ht_title = QLabel("SYSTEM HEALTH")
#         ht_title.setStyleSheet("font-size: 11px; font-weight: bold; color: #64748b; border:none;")
#         ht_val = QLabel(f"{score}%")
#         ht_val.setStyleSheet(f"font-size: 24px; font-weight: 800; color: {color}; border:none;")
#         ht_layout.addWidget(ht_title)
#         ht_layout.addStretch()
#         ht_layout.addWidget(ht_val)
        
#         bar = QProgressBar()
#         bar.setRange(0, 100)
#         bar.setValue(score)
#         bar.setFixedHeight(12)
#         bar.setTextVisible(False)
#         bar.setStyleSheet(f"QProgressBar {{ background: #e2e8f0; border-radius: 6px; border:none; }} "
#                           f"QProgressBar::chunk {{ background: {color}; border-radius: 6px; }}")
        
#         hl.addLayout(ht_layout)
#         hl.addWidget(bar)
#         self.preview_layout.addWidget(health_card)

#         # Actions
#         btn_container = QHBoxLayout()
#         btn_sum = QPushButton("Full Summary")
#         btn_sum.setFixedHeight(40)
#         btn_sum.setCursor(Qt.PointingHandCursor)
#         btn_sum.setStyleSheet("background: #3b82f6; color: white; border-radius: 6px; font-weight: bold;")
#         btn_sum.clicked.connect(lambda: self.main_window.navigate("summary"))
        
#         btn_ana = QPushButton("View Charts")
#         btn_ana.setFixedHeight(40)
#         btn_ana.setCursor(Qt.PointingHandCursor)
#         btn_ana.setStyleSheet("background: white; border: 1px solid #cbd5e1; border-radius: 6px; font-weight: bold;")
#         btn_ana.clicked.connect(lambda: self.main_window.navigate("analytics"))
        
#         btn_container.addWidget(btn_sum)
#         btn_container.addWidget(btn_ana)
#         self.preview_layout.addLayout(btn_container)
        
#         self.preview_layout.addStretch()

class UploadPage(QWidget):
    """File upload page with success redirection"""
    
    def __init__(self, main_window, api_client):
        super().__init__()
        self.main_window = main_window
        self.api_client = api_client
        self.selected_file = None
        
        self.setStyleSheet("background-color: #f8fafc;")
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)

        # Title Section
        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(40, 40, 40, 10)
        
        title = QLabel("Chemical Equipment Analysis")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: 800; color: #1e293b;")
        
        subtitle = QLabel("Upload your dataset and unlock powerful insights instantly")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 15px; color: #64748b; margin-bottom: 10px;")
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        page_layout.addWidget(header_widget)

        # Main content area
        content_container = QWidget()
        content_layout = QHBoxLayout(content_container)
        content_layout.setContentsMargins(40, 0, 40, 40)
        content_layout.setSpacing(30)

        # LEFT: Upload Panel
        self.upload_panel = self.create_upload_panel()
        
        # RIGHT: Preview Panel (Status Panel)
        self.preview_panel = self.create_preview_panel()
        
        content_layout.addWidget(self.upload_panel, 1)
        content_layout.addWidget(self.preview_panel, 1)
        
        page_layout.addWidget(content_container)

    def create_upload_panel(self):
        panel = QFrame()
        panel.setStyleSheet("QFrame { background-color: white; border-radius: 16px; border: 1px solid #e2e8f0; }")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        h_title = QLabel("📁 Upload Dataset")
        h_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #0f172a; border: none;")
        
        self.file_area = QFrame()
        self.file_area.setMinimumHeight(250)
        self.file_area.setStyleSheet("QFrame { background-color: #f1f5f9; border: 2px dashed #cbd5e1; border-radius: 12px; }")
        fa_layout = QVBoxLayout(self.file_area)
        self.file_label = QLabel("Click 'Browse' to select a CSV file")
        self.file_label.setStyleSheet("color: #64748b; border: none;")
        fa_layout.addWidget(self.file_label, 0, Qt.AlignCenter)

        browse_btn = QPushButton("Browse Files")
        browse_btn.setFixedHeight(45)
        browse_btn.setCursor(Qt.PointingHandCursor)
        browse_btn.setStyleSheet("QPushButton { background-color: white; border: 1px solid #cbd5e1; border-radius: 8px; font-weight: 600; } QPushButton:hover { background-color: #f8fafc; border-color: #3b82f6; }")
        browse_btn.clicked.connect(self.browse_file)

        self.upload_btn = QPushButton("Analyze Dataset")
        self.upload_btn.setFixedHeight(50)
        self.upload_btn.setEnabled(False)
        self.upload_btn.setCursor(Qt.PointingHandCursor)
        self.upload_btn.setStyleSheet("QPushButton { background-color: #3b82f6; color: white; border-radius: 8px; font-weight: bold; } QPushButton:hover { background-color: #2563eb; } QPushButton:disabled { background-color: #94a3b8; }")
        self.upload_btn.clicked.connect(self.upload_file)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedHeight(10)
        self.progress_bar.setTextVisible(False)

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: #ef4444; border: none;")
        self.error_label.setVisible(False)

        layout.addWidget(h_title)
        layout.addWidget(self.file_area)
        layout.addWidget(browse_btn)
        layout.addWidget(self.upload_btn)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.error_label)
        layout.addStretch()
        return panel

    def create_preview_panel(self):
        panel = QFrame()
        panel.setStyleSheet("QFrame { background-color: white; border-radius: 16px; border: 1px solid #e2e8f0; }")
        self.preview_layout = QVBoxLayout(panel)
        self.preview_layout.setContentsMargins(30, 30, 30, 30)
        self.preview_layout.setSpacing(20)
        self.show_empty_state()
        return panel

    def show_empty_state(self):
        self.clear_preview_layout()
        icon = QLabel("📊")
        icon.setStyleSheet("font-size: 64px; border: none;")
        text = QLabel("Awaiting Data...\nUpload a file to begin analysis.")
        text.setAlignment(Qt.AlignCenter)
        text.setStyleSheet("color: #94a3b8; font-size: 16px; font-weight: 500; border: none;")
        self.preview_layout.addStretch()
        self.preview_layout.addWidget(icon, 0, Qt.AlignCenter)
        self.preview_layout.addWidget(text, 0, Qt.AlignCenter)
        self.preview_layout.addStretch()

    def clear_preview_layout(self):
        while self.preview_layout.count():
            item = self.preview_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.selected_file = file_path
            self.file_label.setText(f"✅ {os.path.basename(file_path)}")
            self.upload_btn.setEnabled(True)

    def upload_file(self):
        self.upload_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)
        self.error_label.setVisible(False)
        
        self.upload_thread = UploadThread(self.api_client, self.selected_file)
        self.upload_thread.finished.connect(self.upload_finished)
        self.upload_thread.start()

    def upload_finished(self, success, result):
        self.progress_bar.setVisible(False)
        self.upload_btn.setEnabled(True)
        if success:
            self.update_preview(result)
        else:
            self.error_label.setText(f"Error: {result}")
            self.error_label.setVisible(True)

    def update_preview(self, data):
        """Show Success State with Navigation Buttons"""
        self.clear_preview_layout()
        
        success_icon = QLabel("🎉")
        success_icon.setStyleSheet("font-size: 64px; border: none;")
        
        success_msg = QLabel("Analysis Complete!")
        success_msg.setStyleSheet("font-size: 24px; font-weight: 800; color: #10b981; border: none;")
        
        sub_msg = QLabel("Your dataset has been processed successfully.\nYou can now view the full results in the sections below.")
        sub_msg.setAlignment(Qt.AlignCenter)
        sub_msg.setStyleSheet("font-size: 14px; color: #64748b; border: none;")

        # Navigation Buttons
        btn_container = QWidget()
        btn_container.setStyleSheet("border: none;")
        btn_layout = QVBoxLayout(btn_container)
        btn_layout.setSpacing(15)

        btn_summary = QPushButton("Go to Summary Page")
        btn_summary.setFixedHeight(50)
        btn_summary.setCursor(Qt.PointingHandCursor)
        btn_summary.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #2563eb; }
        """)
        btn_summary.clicked.connect(lambda: self.main_window.navigate("summary"))

        btn_analytics = QPushButton("View Visual Dashboard")
        btn_analytics.setFixedHeight(50)
        btn_analytics.setCursor(Qt.PointingHandCursor)
        btn_analytics.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #3b82f6;
                border: 2px solid #3b82f6;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #eff6ff; }
        """)
        btn_analytics.clicked.connect(lambda: self.main_window.navigate("analytics"))

        btn_layout.addWidget(btn_summary)
        btn_layout.addWidget(btn_analytics)

        self.preview_layout.addStretch()
        self.preview_layout.addWidget(success_icon, 0, Qt.AlignCenter)
        self.preview_layout.addWidget(success_msg, 0, Qt.AlignCenter)
        self.preview_layout.addWidget(sub_msg, 0, Qt.AlignCenter)
        self.preview_layout.addSpacing(20)
        self.preview_layout.addWidget(btn_container)
        self.preview_layout.addStretch()

# class SummaryPage(QWidget):
#     """Summary page showing latest data and history"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
        
#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(40, 40, 40, 40)
#         main_layout.setSpacing(30)
        
#         # Title
#         title = QLabel("Dataset Summary")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 42px; font-weight: 900; color: #3b82f6;")
        
#         subtitle = QLabel("Comprehensive analytics and historical data overview")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
#         main_layout.addWidget(title)
#         main_layout.addWidget(subtitle)
#         main_layout.addSpacing(20)
        
#         # Content area
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         scroll.setStyleSheet("QScrollArea { border: none; }")
        
#         content = QWidget()
#         self.content_layout = QVBoxLayout(content)
#         self.content_layout.setSpacing(30)
        
#         scroll.setWidget(content)
#         main_layout.addWidget(scroll)
        
#         # Load data
#         self.load_data()
    
#     def load_data(self):
#         """Load summary and history data"""
#         # Clear existing
#         while self.content_layout.count():
#             item = self.content_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # Get latest summary
#         success, latest = self.api_client.get_latest_summary()
#         if success and latest:
#             self.content_layout.addWidget(self.create_latest_card(latest))
        
#         # Get history
#         success, history = self.api_client.get_history()
#         if success and history:
#             self.content_layout.addWidget(self.create_history_table(history))
    
#     def create_latest_card(self, data):
#         """Create latest summary card"""
#         card = QFrame()
#         card.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(card)
#         layout.setContentsMargins(30, 30, 30, 30)
#         layout.setSpacing(25)
        
#         # Header
#         header = QHBoxLayout()
#         h_label = QLabel("Latest Summary")
#         h_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #0f172a;")
        
#         badge = QLabel("LIVE DATA")
#         badge.setStyleSheet("""
#             background-color: #dcfce7;
#             color: #166534;
#             font-size: 10px;
#             font-weight: bold;
#             padding: 6px 12px;
#             border-radius: 8px;
#         """)
        
#         header.addWidget(h_label)
#         header.addStretch()
#         header.addWidget(badge)
        
#         # KPI Grid
#         kpi_grid = QGridLayout()
#         kpi_grid.setSpacing(20)
        
#         kpi_grid.addWidget(StatCard("Total Equipment", data.get('total_equipment', 0), "#3b82f6", "#06b6d4"), 0, 0)
#         kpi_grid.addWidget(StatCard("Avg Flowrate", data.get('avg_flowrate', 0), "#8b5cf6", "#d946ef"), 0, 1)
#         kpi_grid.addWidget(StatCard("Avg Pressure", data.get('avg_pressure', 0), "#ef4444", "#f97316"), 0, 2)
#         kpi_grid.addWidget(StatCard("Avg Temperature", data.get('avg_temperature', 0), "#10b981", "#14b8a6"), 0, 3)
        
#         # Health bar
#         health_widget = QWidget()
#         health_layout = QVBoxLayout(health_widget)
#         health_layout.setContentsMargins(20, 20, 20, 20)
#         health_widget.setStyleSheet("""
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
#                 stop:0 #f8fafc, stop:1 #eff6ff);
#             border-radius: 12px;
#         """)
        
#         health_header = QHBoxLayout()
#         health_label = QLabel("OVERALL HEALTH SCORE")
#         health_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #64748b;")
#         health_value = QLabel(f"{int(data.get('health_score', 0))}%")
        
#         score = data.get('health_score', 0)
#         if score >= 70:
#             color = "#10b981"
#         elif score >= 40:
#             color = "#f59e0b"
#         else:
#             color = "#ef4444"
        
#         health_value.setStyleSheet(f"font-size: 32px; font-weight: 900; color: {color};")
#         health_header.addWidget(health_label)
#         health_header.addStretch()
#         health_header.addWidget(health_value)
        
#         health_bar = QProgressBar()
#         health_bar.setRange(0, 100)
#         health_bar.setValue(int(score))
#         health_bar.setTextVisible(False)
#         health_bar.setFixedHeight(28)
#         health_bar.setStyleSheet(f"""
#             QProgressBar {{
#                 border: none;
#                 border-radius: 14px;
#                 background-color: #e2e8f0;
#             }}
#             QProgressBar::chunk {{
#                 background-color: {color};
#                 border-radius: 14px;
#             }}
#         """)
        
#         health_layout.addLayout(health_header)
#         health_layout.addWidget(health_bar)
        
#         layout.addLayout(header)
#         layout.addLayout(kpi_grid)
#         layout.addWidget(health_widget)
        
#         return card
    
#     def create_history_table(self, history):
#         """Create history table"""
#         card = QFrame()
#         card.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(card)
#         layout.setContentsMargins(0, 0, 0, 0)
        
#         # Header
#         header = QWidget()
#         header.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #eff6ff, stop:1 #e0f2fe); border-radius: 20px 20px 0 0;")
#         header_layout = QHBoxLayout(header)
#         header_layout.setContentsMargins(30, 25, 30, 25)
        
#         h_label = QLabel("Upload History")
#         h_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #0f172a;")
#         header_layout.addWidget(h_label)
        
#         # Table
#         table = QTableWidget()
#         table.setColumnCount(5)
#         table.setHorizontalHeaderLabels(["ID", "File Name", "Health Score", "Upload Date", "Actions"])
#         table.setRowCount(len(history))
#         table.setStyleSheet("""
#             QTableWidget {
#                 border: none;
#                 gridline-color: #f1f5f9;
#                 background-color: white;
#             }
#             QTableWidget::item {
#                 padding: 15px;
#                 border-bottom: 1px solid #f1f5f9;
#             }
#             QTableWidget::item:selected {
#                 background-color: #eff6ff;
#                 color: #0f172a;
#             }
#             QHeaderView::section {
#                 background-color: #f8fafc;
#                 padding: 12px;
#                 border: none;
#                 border-bottom: 2px solid #e2e8f0;
#                 font-weight: bold;
#                 color: #475569;
#                 font-size: 11px;
#             }
#         """)
        
#         table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         table.verticalHeader().setVisible(False)
#         table.setSelectionBehavior(QTableWidget.SelectRows)
#         table.setEditTriggers(QTableWidget.NoEditTriggers)
        
#         for row, item in enumerate(history):
#             # ID
#             table.setItem(row, 0, QTableWidgetItem(str(item.get('id', ''))))
            
#             # File name
#             table.setItem(row, 1, QTableWidgetItem(item.get('file_name', '')))
            
#             # Health score
#             score = item.get('health_score', 0)
#             score_item = QTableWidgetItem(f"{int(score)}%")
#             if score >= 70:
#                 score_item.setForeground(QColor("#10b981"))
#             elif score >= 40:
#                 score_item.setForeground(QColor("#f59e0b"))
#             else:
#                 score_item.setForeground(QColor("#ef4444"))
#             table.setItem(row, 2, score_item)
            
#             # Date
#             date_str = item.get('uploaded_at', '')
#             if date_str:
#                 try:
#                     date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
#                     formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
#                 except:
#                     formatted_date = date_str
#             else:
#                 formatted_date = ""
#             table.setItem(row, 3, QTableWidgetItem(formatted_date))
            
#             # Download button
#             download_btn = QPushButton("📥 Download PDF")
#             download_btn.setCursor(Qt.PointingHandCursor)
#             download_btn.setStyleSheet("""
#                 QPushButton {
#                     background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                         stop:0 #3b82f6, stop:1 #6366f1);
#                     color: white;
#                     font-size: 12px;
#                     font-weight: bold;
#                     border: none;
#                     border-radius: 8px;
#                     padding: 8px 16px;
#                 }
#                 QPushButton:hover {
#                     background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                         stop:0 #2563eb, stop:1 #4f46e5);
#                 }
#             """)
#             download_btn.clicked.connect(lambda checked, id=item.get('id'): self.download_report(id))
#             table.setCellWidget(row, 4, download_btn)
        
#         layout.addWidget(header)
#         layout.addWidget(table)
        
#         return card
    
#     def download_report(self, dataset_id):
#         """Download PDF report"""
#         save_path, _ = QFileDialog.getSaveFileName(
#             self,
#             "Save Report",
#             f"dataset_report_{dataset_id}.pdf",
#             "PDF Files (*.pdf)"
#         )
        
#         if save_path:
#             success, message = self.api_client.download_report(dataset_id, save_path)
#             if success:
#                 QMessageBox.information(self, "Success", message)
#             else:
#                 QMessageBox.warning(self, "Error", message)


class SummaryPage(QWidget):
    """Summary page showing latest data and history"""
    
    def __init__(self, main_window, api_client):
        super().__init__()
        self.main_window = main_window
        self.api_client = api_client
        
        # Set background for the whole page
        self.setStyleSheet("background-color: #f8fafc;")
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Header Section
        header_widget = QWidget()
        header_widget.setStyleSheet("background-color: white; border-bottom: 1px solid #e2e8f0;")
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(40, 30, 40, 30)
        
        title = QLabel("Dataset Summary")
        title.setStyleSheet("font-size: 32px; font-weight: 800; color: #1e293b;")
        
        subtitle = QLabel("Comprehensive analytics and historical data overview")
        subtitle.setStyleSheet("font-size: 15px; color: #64748b;")
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        main_layout.addWidget(header_widget)
        
        # Scroll area for content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("background-color: transparent;")
        
        content_container = QWidget()
        content_container.setStyleSheet("background-color: transparent;")
        self.content_layout = QVBoxLayout(content_container)
        self.content_layout.setContentsMargins(40, 30, 40, 40)
        self.content_layout.setSpacing(30)
        
        scroll.setWidget(content_container)
        main_layout.addWidget(scroll)
        
        self.load_data()

    def load_data(self):
        """Load summary and history data"""
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Latest Summary Section
        success, latest = self.api_client.get_latest_summary()
        if success and latest:
            self.content_layout.addWidget(self.create_latest_card(latest))
        else:
            # Fallback if no data
            no_data = QLabel("No recent analysis found. Upload a file to see results.")
            no_data.setStyleSheet("color: #94a3b8; font-style: italic; padding: 20px;")
            self.content_layout.addWidget(no_data)
        
        # History Section
        success, history = self.api_client.get_history()
        if success and history:
            self.content_layout.addWidget(self.create_history_table(history))

    def create_latest_card(self, data):
        """Create a polished hero card for the latest data"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e2e8f0;
            }
        """)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(25)
        
        # Title with Badge
        top_row = QHBoxLayout()
        title = QLabel("Latest Analysis Result")
        title.setStyleSheet("font-size: 20px; font-weight: 700; color: #0f172a; border: none;")
        
        badge = QLabel("ACTIVE DATA")
        badge.setStyleSheet("""
            background-color: #dcfce7; color: #166534;
            font-size: 11px; font-weight: 800;
            padding: 5px 12px; border-radius: 6px; border: none;
        """)
        top_row.addWidget(title)
        top_row.addStretch()
        top_row.addWidget(badge)
        layout.addLayout(top_row)

        # KPI Metrics Row (using your existing StatCard)
        kpi_row = QHBoxLayout()
        kpi_row.setSpacing(15)
        kpi_row.addWidget(StatCard("Total Items", data.get('total_equipment', 0), "#3b82f6", "#60a5fa"))
        kpi_row.addWidget(StatCard("Avg Flow", data.get('avg_flowrate', 0), "#8b5cf6", "#a78bfa"))
        kpi_row.addWidget(StatCard("Avg Pressure", data.get('avg_pressure', 0), "#ef4444", "#fb7185"))
        kpi_row.addWidget(StatCard("Avg Temp", data.get('avg_temperature', 0), "#10b981", "#34d399"))
        layout.addLayout(kpi_row)
        
        return card

    # def create_history_table(self, history):
    #     """Create a clean, modern data table"""
    #     container = QFrame()
    #     container.setStyleSheet("background-color: white; border-radius: 16px; border: 1px solid #e2e8f0;")
    #     layout = QVBoxLayout(container)
    #     layout.setContentsMargins(0, 0, 0, 0)
    #     layout.setSpacing(0)
        
    #     # Table Title Header
    #     tbl_header = QLabel("Analysis History")
    #     tbl_header.setStyleSheet("""
    #         font-size: 18px; font-weight: 700; color: #0f172a; 
    #         padding: 25px 30px; border: none; border-bottom: 1px solid #f1f5f9;
    #     """)
    #     layout.addWidget(tbl_header)
        
    #     # Setup Table
    #     table = QTableWidget(len(history), 5)
    #     table.setHorizontalHeaderLabels(["ID", "FILE NAME", "HEALTH STATUS", "UPLOAD DATE", "ACTIONS"])
    #     table.setFrameShape(QFrame.NoFrame)
    #     table.setAlternatingRowColors(True)
    #     table.setShowGrid(False)
    #     table.verticalHeader().setVisible(False)
    #     table.setRowHeight(65) # Professional spacing
        
    #     # Table Styling
    #     table.setStyleSheet("""
    #         QTableWidget {
    #             background-color: white;
    #             alternate-background-color: #fafafa;
    #             selection-background-color: #eff6ff;
    #             border: none;
    #         }
    #         QTableWidget::item {
    #             padding-left: 30px;
    #             color: #475569;
    #             font-size: 13px;
    #         }
    #         QHeaderView::section {
    #             background-color: white;
    #             color: #94a3b8;
    #             padding-left: 30px;
    #             font-size: 11px;
    #             font-weight: 800;
    #             border: none;
    #             border-bottom: 1px solid #f1f5f9;
    #             height: 45px;
    #         }
    #     """)
        
    #     header = table.horizontalHeader()
    #     header.setSectionResizeMode(1, QHeaderView.Stretch) # Stretch filename
    #     header.setSectionResizeMode(4, QHeaderView.Fixed)
    #     table.setColumnWidth(4, 180) # Fixed width for action button
        
    #     for row, item in enumerate(history):
    #         # ID and Name
    #         table.setItem(row, 0, QTableWidgetItem(f"#{item.get('id', '')}"))
    #         table.setItem(row, 1, QTableWidgetItem(item.get('file_name', 'Untitled')))
            
    #         # Health Status (Colored Text)
    #         score = item.get('health_score', 0)
    #         status_item = QTableWidgetItem(f"● {int(score)}%")
    #         if score >= 70: status_item.setForeground(QColor("#059669"))
    #         elif score >= 40: status_item.setForeground(QColor("#d97706"))
    #         else: status_item.setForeground(QColor("#dc2626"))
    #         table.setItem(row, 2, status_item)
            
    #         # Date Formatting
    #         date_str = item.get('uploaded_at', '')
    #         try:
    #             date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    #             formatted_date = date_obj.strftime("%b %d, %Y • %H:%M")
    #         except:
    #             formatted_date = date_str
    #         table.setItem(row, 3, QTableWidgetItem(formatted_date))
            
    #         # Action Button
    #         btn_container = QWidget()
    #         btn_layout = QHBoxLayout(btn_container)
    #         btn_layout.setContentsMargins(10, 10, 30, 10)
            
    #         dl_btn = QPushButton("Download Report")
    #         dl_btn.setCursor(Qt.PointingHandCursor)
    #         dl_btn.setFixedHeight(32)
    #         dl_btn.setStyleSheet("""
    #             QPushButton {
    #                 background-color: #3b82f6; color: white;
    #                 border-radius: 6px; font-size: 11px; font-weight: 700; padding: 0 12px;
    #             }
    #             QPushButton:hover { background-color: #2563eb; }
    #         """)
    #         dl_btn.clicked.connect(lambda checked, i=item.get('id'): self.download_report(i))
    #         btn_layout.addWidget(dl_btn)
    #         table.setCellWidget(row, 4, btn_container)
            
    #     layout.addWidget(table)
        
    #     # Adjust table height based on content to avoid double scrollbars
    #     table.setMinimumHeight(min(len(history) * 65 + 100, 600))
        
    #     return container
    def create_history_table(self, history):
        """Create a clean, modern data table with corrected row height logic"""
        container = QFrame()
        container.setStyleSheet("background-color: white; border-radius: 16px; border: 1px solid #e2e8f0;")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Table Title Header
        tbl_header = QLabel("Analysis History")
        tbl_header.setStyleSheet("""
            font-size: 18px; font-weight: 700; color: #0f172a; 
            padding: 25px 30px; border: none; border-bottom: 1px solid #f1f5f9;
        """)
        layout.addWidget(tbl_header)
        
        # Setup Table
        table = QTableWidget(len(history), 5)
        table.setHorizontalHeaderLabels(["ID", "FILE NAME", "HEALTH STATUS", "UPLOAD DATE", "ACTIONS"])
        table.setFrameShape(QFrame.NoFrame)
        table.setAlternatingRowColors(True)
        table.setShowGrid(False)
        table.verticalHeader().setVisible(False)
        
        # FIX: Correct way to set height for all rows
        table.verticalHeader().setDefaultSectionSize(65) 
        
        # Table Styling
        table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                alternate-background-color: #fafafa;
                selection-background-color: #eff6ff;
                border: none;
            }
            QTableWidget::item {
                padding-left: 30px;
                color: #475569;
                font-size: 13px;
            }
            QHeaderView::section {
                background-color: white;
                color: #94a3b8;
                padding-left: 30px;
                font-size: 11px;
                font-weight: 800;
                border: none;
                border-bottom: 1px solid #f1f5f9;
                height: 45px;
            }
        """)
        
        header = table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch) 
        header.setSectionResizeMode(4, QHeaderView.Fixed)
        table.setColumnWidth(4, 180) 
        
        for row, item in enumerate(history):
            # ID and Name
            table.setItem(row, 0, QTableWidgetItem(f"#{item.get('id', '—')}"))
            table.setItem(row, 1, QTableWidgetItem(item.get('file_name', 'Untitled')))
            
            # Health Status
            score = item.get('health_score', 0)
            status_item = QTableWidgetItem(f"● {int(score)}%")
            if score >= 70: status_item.setForeground(QColor("#059669"))
            elif score >= 40: status_item.setForeground(QColor("#d97706"))
            else: status_item.setForeground(QColor("#dc2626"))
            table.setItem(row, 2, status_item)
            
            # Date Formatting
            date_str = item.get('uploaded_at', '')
            try:
                date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                formatted_date = date_obj.strftime("%b %d, %Y • %H:%M")
            except:
                formatted_date = date_str
            table.setItem(row, 3, QTableWidgetItem(formatted_date))
            
            # Action Button (Download)
            btn_container = QWidget()
            btn_layout = QHBoxLayout(btn_container)
            btn_layout.setContentsMargins(10, 10, 30, 10)
            
            dl_btn = QPushButton("Download PDF")
            dl_btn.setCursor(Qt.PointingHandCursor)
            dl_btn.setFixedHeight(34)
            dl_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3b82f6; 
                    color: white;
                    border-radius: 6px; 
                    font-size: 11px; 
                    font-weight: 700; 
                    padding: 0 15px;
                }
                QPushButton:hover { background-color: #2563eb; }
            """)
            # Connect existing function
            ds_id = item.get('id')
            dl_btn.clicked.connect(lambda checked, i=ds_id: self.download_report(i))
            
            btn_layout.addWidget(dl_btn)
            table.setCellWidget(row, 4, btn_container)
            
        layout.addWidget(table)
        
        # Ensure the table expands to show all rows without internal scrollbars
        table.setMinimumHeight(min(len(history) * 65 + 120, 800))
        
        return container

    def download_report(self, dataset_id):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Report", f"Report_ID_{dataset_id}.pdf", "PDF Files (*.pdf)")
        if save_path:
            success, message = self.api_client.download_report(dataset_id, save_path)
            if success:
                QMessageBox.information(self, "Success", "Report saved successfully.")
            else:
                QMessageBox.warning(self, "Error", message)

# class AnalyticsPage(QWidget):
#     """Analytics dashboard with charts"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
#         self.datasets = []
#         self.selected_data = None
        
#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(40, 40, 40, 40)
#         main_layout.setSpacing(30)
        
#         # Title
#         title = QLabel("Analytics Dashboard")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 42px; font-weight: 900; color: #3b82f6;")
        
#         subtitle = QLabel("Comprehensive visual insights and real-time equipment monitoring")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 16px; color: #64748b;")
        
#         main_layout.addWidget(title)
#         main_layout.addWidget(subtitle)
#         main_layout.addSpacing(20)
        
#         # Content area
#         content_layout = QHBoxLayout()
#         content_layout.setSpacing(30)
        
#         # LEFT: Dataset selector
#         self.selector_panel = self.create_selector_panel()
        
#         # RIGHT: Analytics view
#         self.analytics_panel = QWidget()
#         self.analytics_layout = QVBoxLayout(self.analytics_panel)
#         self.analytics_layout.setSpacing(20)
        
#         content_layout.addWidget(self.selector_panel, 1)
#         content_layout.addWidget(self.analytics_panel, 3)
        
#         main_layout.addLayout(content_layout)
        
#         # Load data
#         self.load_datasets()
    
#     def create_selector_panel(self):
#         """Create dataset selector"""
#         panel = QFrame()
#         panel.setFixedWidth(300)
#         panel.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         layout = QVBoxLayout(panel)
#         layout.setContentsMargins(20, 20, 20, 20)
#         layout.setSpacing(15)
        
#         # Header
#         header = QLabel("Datasets")
#         header.setStyleSheet("font-size: 18px; font-weight: bold; color: #0f172a;")
        
#         # List area
#         self.dataset_list = QWidget()
#         self.dataset_list_layout = QVBoxLayout(self.dataset_list)
#         self.dataset_list_layout.setSpacing(10)
        
#         scroll = QScrollArea()
#         scroll.setWidget(self.dataset_list)
#         scroll.setWidgetResizable(True)
#         scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         scroll.setStyleSheet("QScrollArea { border: none; }")
        
#         layout.addWidget(header)
#         layout.addWidget(scroll)
        
#         return panel
    
#     def load_datasets(self):
#         """Load datasets from history"""
#         success, history = self.api_client.get_history()
        
#         if not success or not history:
#             # Show empty state
#             empty_label = QLabel("No datasets available.\nUpload a file to get started.")
#             empty_label.setAlignment(Qt.AlignCenter)
#             empty_label.setStyleSheet("color: #94a3b8; font-size: 14px;")
#             self.analytics_layout.addWidget(empty_label)
#             return
        
#         self.datasets = history
        
#         # Clear list
#         while self.dataset_list_layout.count():
#             item = self.dataset_list_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # Add dataset buttons
#         for dataset in self.datasets:
#             btn = self.create_dataset_button(dataset)
#             self.dataset_list_layout.addWidget(btn)
        
#         self.dataset_list_layout.addStretch()
        
#         # Select first dataset
#         if self.datasets:
#             self.select_dataset(self.datasets[0])
    
#     def create_dataset_button(self, dataset):
#         """Create dataset selection button"""
#         btn = QPushButton()
#         btn.setCursor(Qt.PointingHandCursor)
#         btn.setFixedHeight(80)
        
#         layout = QVBoxLayout(btn)
#         layout.setContentsMargins(15, 10, 15, 10)
#         layout.setSpacing(5)
        
#         name_label = QLabel(dataset.get('file_name', 'Unknown'))
#         name_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #0f172a; text-align: left;")
#         name_label.setWordWrap(True)
        
#         health = dataset.get('health_score', 0)
#         health_label = QLabel(f"Health: {int(health)}%")
#         if health >= 70:
#             color = "#10b981"
#         elif health >= 40:
#             color = "#f59e0b"
#         else:
#             color = "#ef4444"
#         health_label.setStyleSheet(f"font-size: 12px; font-weight: bold; color: {color}; text-align: left;")
        
#         layout.addWidget(name_label)
#         layout.addWidget(health_label)
        
#         btn.setStyleSheet("""
#             QPushButton {
#                 background-color: white;
#                 border: 2px solid #e2e8f0;
#                 border-radius: 12px;
#                 text-align: left;
#             }
#             QPushButton:hover {
#                 background-color: #f8fafc;
#                 border-color: #cbd5e1;
#             }
#         """)
        
#         btn.clicked.connect(lambda: self.select_dataset(dataset))
        
#         return btn
    
#     def select_dataset(self, dataset):
#         """Display analytics for selected dataset"""
#         self.selected_data = dataset
        
#         # Clear analytics panel
#         while self.analytics_layout.count():
#             item = self.analytics_layout.takeAt(0)
#             if item.widget():
#                 item.widget().deleteLater()
        
#         # Dataset info header
#         header = self.create_info_header(dataset)
#         self.analytics_layout.addWidget(header)
        
#         # KPI Cards
#         kpi_grid = QGridLayout()
#         kpi_grid.setSpacing(20)
        
#         kpi_grid.addWidget(StatCard("Total Equipment", dataset.get('total_equipment', 0), "#3b82f6", "#06b6d4"), 0, 0)
#         kpi_grid.addWidget(StatCard("Avg Flowrate", dataset.get('avg_flowrate', 0), "#8b5cf6", "#d946ef"), 0, 1)
#         kpi_grid.addWidget(StatCard("Avg Pressure", dataset.get('avg_pressure', 0), "#ef4444", "#f97316"), 0, 2)
#         kpi_grid.addWidget(StatCard("Avg Temperature", dataset.get('avg_temperature', 0), "#10b981", "#14b8a6"), 0, 3)
        
#         self.analytics_layout.addLayout(kpi_grid)
        
#         # Charts
#         summary = dataset.get('summary', {})
        
#         # Risk analysis
#         risk_widget = self.create_risk_widget(summary.get('risk_analysis', {}))
#         self.analytics_layout.addWidget(risk_widget)
        
#         # Equipment distribution
#         eq_widget = self.create_equipment_distribution(summary.get('equipment_type_distribution', {}))
#         self.analytics_layout.addWidget(eq_widget)
        
#         self.analytics_layout.addStretch()
    
#     def create_info_header(self, dataset):
#         """Create dataset info header"""
#         header = QFrame()
#         header.setStyleSheet("""
#             QFrame {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 border-radius: 16px;
#             }
#         """)
        
#         layout = QHBoxLayout(header)
#         layout.setContentsMargins(30, 25, 30, 25)
        
#         # Left: Name and date
#         left = QWidget()
#         left_layout = QVBoxLayout(left)
#         left_layout.setSpacing(5)
        
#         name = QLabel(dataset.get('file_name', 'Unknown'))
#         name.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        
#         date_str = dataset.get('uploaded_at', '')
#         if date_str:
#             try:
#                 date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
#                 formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
#             except:
#                 formatted_date = date_str
#         else:
#             formatted_date = ""
        
#         date = QLabel(f"Uploaded: {formatted_date}")
#         date.setStyleSheet("font-size: 13px; color: #dbeafe;")
        
#         left_layout.addWidget(name)
#         left_layout.addWidget(date)
        
#         # Right: Health score
#         right = QWidget()
#         right_layout = QVBoxLayout(right)
#         right_layout.setSpacing(2)
#         right_layout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
#         health_label = QLabel("Overall Health")
#         health_label.setStyleSheet("font-size: 12px; color: #dbeafe; text-align: right;")
#         health_label.setAlignment(Qt.AlignRight)
        
#         health_value = QLabel(f"{int(dataset.get('health_score', 0))}%")
#         health_value.setStyleSheet("font-size: 42px; font-weight: 900; color: white; text-align: right;")
#         health_value.setAlignment(Qt.AlignRight)
        
#         right_layout.addWidget(health_label)
#         right_layout.addWidget(health_value)
        
#         layout.addWidget(left)
#         layout.addStretch()
#         layout.addWidget(right)
        
#         return header

class AnalyticsPage(QWidget):
    """Analytics dashboard with charts - Refined UI"""
    
    def __init__(self, main_window, api_client):
        super().__init__()
        self.main_window = main_window
        self.api_client = api_client
        self.datasets = []
        self.selected_data = None
        
        # Main container setup
        self.setStyleSheet("background-color: #f8fafc;")
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # --- Clean Header ---
        header_area = QWidget()
        header_area.setStyleSheet("background-color: white; border-bottom: 1px solid #e2e8f0;")
        header_layout = QVBoxLayout(header_area)
        header_layout.setContentsMargins(40, 30, 40, 30)
        
        title = QLabel("Analytics Dashboard")
        title.setStyleSheet("font-size: 32px; font-weight: 900; color: #1e293b; border: none;")
        
        subtitle = QLabel("Comprehensive visual insights and real-time equipment monitoring")
        subtitle.setStyleSheet("font-size: 15px; color: #64748b; border: none;")
        
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        main_layout.addWidget(header_area)
        
        # --- Content Area ---
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(30, 30, 30, 30)
        content_layout.setSpacing(30)
        
        # LEFT: Dataset selector
        self.selector_panel = self.create_selector_panel()
        
        # RIGHT: Analytics view (Scrollable to prevent cutoff)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("background: transparent;")
        
        self.analytics_panel = QWidget()
        self.analytics_layout = QVBoxLayout(self.analytics_panel)
        self.analytics_layout.setContentsMargins(0, 0, 10, 0)
        self.analytics_layout.setSpacing(25)
        
        scroll.setWidget(self.analytics_panel)
        
        content_layout.addWidget(self.selector_panel, 1)
        content_layout.addWidget(scroll, 3)
        
        main_layout.addWidget(content_widget)
        
        # Load data
        self.load_datasets()
    
    def create_selector_panel(self):
        """Create dataset selector with polished frame"""
        panel = QFrame()
        panel.setFixedWidth(300)
        panel.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e2e8f0;
            }
        """)
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 25, 20, 25)
        layout.setSpacing(15)
        
        header = QLabel("DATASETS")
        header.setStyleSheet("font-size: 11px; font-weight: 800; color: #94a3b8; letter-spacing: 1px; border: none;")
        
        self.dataset_list = QWidget()
        self.dataset_list.setStyleSheet("border: none;")
        self.dataset_list_layout = QVBoxLayout(self.dataset_list)
        self.dataset_list_layout.setContentsMargins(0, 0, 0, 0)
        self.dataset_list_layout.setSpacing(10)
        
        scroll = QScrollArea()
        scroll.setWidget(self.dataset_list)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("background: transparent; border: none;")
        
        layout.addWidget(header)
        layout.addWidget(scroll)
        
        return panel
    
    def load_datasets(self):
        """Original logic preserved"""
        success, history = self.api_client.get_history()
        
        if not success or not history:
            empty_label = QLabel("No datasets available.\nUpload a file to get started.")
            empty_label.setAlignment(Qt.AlignCenter)
            empty_label.setStyleSheet("color: #94a3b8; font-size: 13px; border: none;")
            self.analytics_layout.addWidget(empty_label)
            return
        
        self.datasets = history
        
        while self.dataset_list_layout.count():
            item = self.dataset_list_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        for dataset in self.datasets:
            btn = self.create_dataset_button(dataset)
            self.dataset_list_layout.addWidget(btn)
        
        self.dataset_list_layout.addStretch()
        
        if self.datasets:
            self.select_dataset(self.datasets[0])
    
    def create_dataset_button(self, dataset):
        """Polished selection button"""
        btn = QPushButton()
        btn.setCursor(Qt.PointingHandCursor)
        btn.setFixedHeight(85)
        
        layout = QVBoxLayout(btn)
        layout.setContentsMargins(15, 12, 15, 12)
        layout.setSpacing(5)
        
        name_label = QLabel(dataset.get('file_name', 'Unknown'))
        name_label.setStyleSheet("font-size: 13px; font-weight: 700; color: #1e293b; border: none; background: transparent;")
        name_label.setWordWrap(True)
        
        health = dataset.get('health_score', 0)
        color = "#10b981" if health >= 70 else "#f59e0b" if health >= 40 else "#ef4444"
        
        health_label = QLabel(f"● Health: {int(health)}%")
        health_label.setStyleSheet(f"font-size: 12px; font-weight: 600; color: {color}; border: none; background: transparent;")
        
        layout.addWidget(name_label)
        layout.addWidget(health_label)
        
        btn.setStyleSheet("""
            QPushButton {
                background-color: #f8fafc;
                border: 1px solid #e2e8f0;
                border-radius: 12px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f1f5f9;
                border-color: #cbd5e1;
            }
        """)
        
        btn.clicked.connect(lambda: self.select_dataset(dataset))
        return btn
    
    def select_dataset(self, dataset):
        """Original logic preserved"""
        self.selected_data = dataset
        
        while self.analytics_layout.count():
            item = self.analytics_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        header = self.create_info_header(dataset)
        self.analytics_layout.addWidget(header)
        
        kpi_grid_container = QWidget()
        kpi_grid = QGridLayout(kpi_grid_container)
        kpi_grid.setContentsMargins(0, 0, 0, 0)
        kpi_grid.setSpacing(15)
        
        kpi_grid.addWidget(StatCard("Total Equipment", dataset.get('total_equipment', 0), "#3b82f6", "#06b6d4"), 0, 0)
        kpi_grid.addWidget(StatCard("Avg Flowrate", dataset.get('avg_flowrate', 0), "#8b5cf6", "#d946ef"), 0, 1)
        kpi_grid.addWidget(StatCard("Avg Pressure", dataset.get('avg_pressure', 0), "#ef4444", "#f97316"), 0, 2)
        kpi_grid.addWidget(StatCard("Avg Temperature", dataset.get('avg_temperature', 0), "#10b981", "#14b8a6"), 0, 3)
        
        self.analytics_layout.addWidget(kpi_grid_container)
        
        summary = dataset.get('summary', {})
        self.analytics_layout.addWidget(self.create_risk_widget(summary.get('risk_analysis', {})))
        self.analytics_layout.addWidget(self.create_equipment_distribution(summary.get('equipment_type_distribution', {})))
        self.analytics_layout.addStretch()
    
    def create_info_header(self, dataset):
        """Original styling updated for alignment"""
        header = QFrame()
        header.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #1e293b, stop:1 #334155);
                border-radius: 16px;
            }
        """)
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(30, 25, 30, 25)
        
        vbox = QVBoxLayout()
        name = QLabel(dataset.get('file_name', 'Unknown'))
        name.setStyleSheet("font-size: 22px; font-weight: 800; color: white; border: none;")
        
        date_str = dataset.get('uploaded_at', '')
        try:
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")
        except:
            formatted_date = date_str
        
        date = QLabel(f"Uploaded: {formatted_date}")
        date.setStyleSheet("font-size: 13px; color: #94a3b8; border: none;")
        vbox.addWidget(name)
        vbox.addWidget(date)
        
        layout.addLayout(vbox)
        layout.addStretch()
        
        health_value = QLabel(f"{int(dataset.get('health_score', 0))}%")
        health_value.setStyleSheet("font-size: 38px; font-weight: 900; color: white; border: none;")
        layout.addWidget(health_value)
        
        return header

    # Original create_risk_widget and create_equipment_distribution 
    # should be used exactly as you had them, as they were functionally correct.
    
    def create_risk_widget(self, risk_data):
        """Create risk analysis widget"""
        widget = QFrame()
        widget.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 16px;
                border: 2px solid #e2e8f0;
            }
        """)
        
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(20)
        
        # Header
        header = QLabel("Risk Analysis")
        header.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
        
        # Grid for risk stats
        grid = QGridLayout()
        grid.setSpacing(20)
        
        high_risk = risk_data.get('high_risk', 0)
        normal = risk_data.get('normal', 0)
        total = high_risk + normal
        
        # High risk card
        high_card = QFrame()
        high_card.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                stop:0 #fef2f2, stop:1 #fee2e2);
            border: 2px solid #fecaca;
            border-radius: 12px;
            padding: 20px;
        """)
        high_layout = QVBoxLayout(high_card)
        high_layout.setSpacing(10)
        
        high_title = QLabel("High Risk Equipment")
        high_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #991b1b;")
        
        high_value = QLabel(str(high_risk))
        high_value.setStyleSheet("font-size: 36px; font-weight: 900; color: #dc2626;")
        
        if total > 0:
            high_pct = QLabel(f"{(high_risk/total*100):.1f}%")
            high_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #ef4444;")
        else:
            high_pct = QLabel("0%")
            high_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #ef4444;")
        
        high_layout.addWidget(high_title)
        high_layout.addWidget(high_value)
        high_layout.addWidget(high_pct)
        
        # Normal card
        normal_card = QFrame()
        normal_card.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                stop:0 #f0fdf4, stop:1 #dcfce7);
            border: 2px solid #bbf7d0;
            border-radius: 12px;
            padding: 20px;
        """)
        normal_layout = QVBoxLayout(normal_card)
        normal_layout.setSpacing(10)
        
        normal_title = QLabel("Normal Equipment")
        normal_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #166534;")
        
        normal_value = QLabel(str(normal))
        normal_value.setStyleSheet("font-size: 36px; font-weight: 900; color: #16a34a;")
        
        if total > 0:
            normal_pct = QLabel(f"{(normal/total*100):.1f}%")
            normal_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #22c55e;")
        else:
            normal_pct = QLabel("0%")
            normal_pct.setStyleSheet("font-size: 16px; font-weight: bold; color: #22c55e;")
        
        normal_layout.addWidget(normal_title)
        normal_layout.addWidget(normal_value)
        normal_layout.addWidget(normal_pct)
        
        grid.addWidget(high_card, 0, 0)
        grid.addWidget(normal_card, 0, 1)
        
        layout.addWidget(header)
        layout.addLayout(grid)
        
        return widget
    
    def create_equipment_distribution(self, distribution):
        """Create equipment type distribution widget"""
        widget = QFrame()
        widget.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 16px;
                border: 2px solid #e2e8f0;
            }
        """)
        
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(20)
        
        # Header
        header = QLabel("Equipment Type Distribution")
        header.setStyleSheet("font-size: 20px; font-weight: bold; color: #0f172a;")
        
        # Grid of type cards
        grid = QGridLayout()
        grid.setSpacing(15)
        
        items = list(distribution.items())
        colors = ["#3b82f6", "#6366f1", "#8b5cf6", "#a855f7", "#ec4899", "#f43f5e"]
        
        for i, (eq_type, count) in enumerate(items):
            row = i // 4
            col = i % 4
            
            card = QFrame()
            card.setStyleSheet(f"""
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #eff6ff, stop:1 #dbeafe);
                border: 2px solid #bfdbfe;
                border-radius: 12px;
                padding: 15px;
            """)
            
            card_layout = QVBoxLayout(card)
            card_layout.setSpacing(8)
            
            type_label = QLabel(eq_type.upper())
            type_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #1e40af;")
            
            count_label = QLabel(str(count))
            count_label.setStyleSheet(f"font-size: 28px; font-weight: 900; color: {colors[i % len(colors)]};")
            
            card_layout.addWidget(type_label)
            card_layout.addWidget(count_label)
            
            grid.addWidget(card, row, col)
        
        layout.addWidget(header)
        layout.addLayout(grid)
        
        return widget


# class LoginPage(QWidget):
#     """Login page"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
        
#         main_layout = QHBoxLayout(self)
#         main_layout.setContentsMargins(0, 0, 0, 0)
        
#         # Background gradient
#         main_layout.addWidget(GradientWidget("#f8fafc", "#e0f2fe"))
        
#         # Center content
#         center = QWidget()
#         center.setMaximumWidth(450)
        
#         layout = QVBoxLayout(center)
#         layout.setContentsMargins(40, 60, 40, 60)
#         layout.setSpacing(25)
#         layout.setAlignment(Qt.AlignCenter)
        
#         # Logo/Icon
#         icon_label = QLabel("🔐")
#         icon_label.setAlignment(Qt.AlignCenter)
#         icon_label.setStyleSheet("font-size: 48px;")
        
#         # Title
#         title = QLabel("Welcome Back")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 32px; font-weight: 900; color: #0f172a;")
        
#         subtitle = QLabel("Sign in to access your analytics dashboard")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 14px; color: #64748b;")
        
#         # Form container
#         form_container = QFrame()
#         form_container.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         form_layout = QVBoxLayout(form_container)
#         form_layout.setContentsMargins(30, 30, 30, 30)
#         form_layout.setSpacing(20)
        
#         # Username
#         username_label = QLabel("USERNAME")
#         username_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.username_input = QLineEdit()
#         self.username_input.setPlaceholderText("Enter your username")
#         self.username_input.setFixedHeight(45)
#         self.username_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Password
#         password_label = QLabel("PASSWORD")
#         password_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Enter your password")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         self.password_input.setFixedHeight(45)
#         self.password_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Error label
#         self.error_label = QLabel()
#         self.error_label.setVisible(False)
#         self.error_label.setStyleSheet("color: #ef4444; font-size: 12px;")
#         self.error_label.setWordWrap(True)
        
#         # Login button
#         login_btn = QPushButton("Sign In")
#         login_btn.setFixedHeight(50)
#         login_btn.setCursor(Qt.PointingHandCursor)
#         login_btn.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 16px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#         """)
#         login_btn.clicked.connect(self.handle_login)
        
#         # Register link
#         register_container = QHBoxLayout()
#         register_label = QLabel("Don't have an account?")
#         register_label.setStyleSheet("font-size: 13px; color: #64748b;")
        
#         register_btn = QPushButton("Create one")
#         register_btn.setCursor(Qt.PointingHandCursor)
#         register_btn.setStyleSheet("""
#             QPushButton {
#                 background: none;
#                 border: none;
#                 color: #3b82f6;
#                 font-size: 13px;
#                 font-weight: bold;
#                 text-decoration: underline;
#             }
#             QPushButton:hover {
#                 color: #2563eb;
#             }
#         """)
#         register_btn.clicked.connect(lambda: self.main_window.navigate("register"))
        
#         register_container.addStretch()
#         register_container.addWidget(register_label)
#         register_container.addWidget(register_btn)
#         register_container.addStretch()
        
#         form_layout.addWidget(username_label)
#         form_layout.addWidget(self.username_input)
#         form_layout.addWidget(password_label)
#         form_layout.addWidget(self.password_input)
#         form_layout.addWidget(self.error_label)
#         form_layout.addWidget(login_btn)
        
#         layout.addWidget(icon_label)
#         layout.addWidget(title)
#         layout.addWidget(subtitle)
#         layout.addSpacing(10)
#         layout.addWidget(form_container)
#         layout.addLayout(register_container)
#         layout.addStretch()
        
#         # Position center widget
#         main_layout.takeAt(0)  # Remove gradient temporarily
#         main_layout.addStretch()
#         main_layout.addWidget(center)
#         main_layout.addStretch()
    
#     def handle_login(self):
#         """Handle login"""
#         username = self.username_input.text()
#         password = self.password_input.text()
        
#         if not username or not password:
#             self.error_label.setText("Please enter both username and password")
#             self.error_label.setVisible(True)
#             return
        
#         success, message = self.api_client.login(username, password)
        
#         if success:
#             self.main_window.on_login_success()
#         else:
#             self.error_label.setText(message)
#             self.error_label.setVisible(True)


# class RegisterPage(QWidget):
#     """Registration page"""
    
#     def __init__(self, main_window, api_client):
#         super().__init__()
#         self.main_window = main_window
#         self.api_client = api_client
        
#         main_layout = QHBoxLayout(self)
#         main_layout.setContentsMargins(0, 0, 0, 0)
        
#         # Background gradient
#         main_layout.addWidget(GradientWidget("#f8fafc", "#e0f2fe"))
        
#         # Center content
#         center = QWidget()
#         center.setMaximumWidth(450)
        
#         layout = QVBoxLayout(center)
#         layout.setContentsMargins(40, 60, 40, 60)
#         layout.setSpacing(25)
#         layout.setAlignment(Qt.AlignCenter)
        
#         # Logo/Icon
#         icon_label = QLabel("✨")
#         icon_label.setAlignment(Qt.AlignCenter)
#         icon_label.setStyleSheet("font-size: 48px;")
        
#         # Title
#         title = QLabel("Create Account")
#         title.setAlignment(Qt.AlignCenter)
#         title.setStyleSheet("font-size: 32px; font-weight: 900; color: #0f172a;")
        
#         subtitle = QLabel("Get started with your free account today")
#         subtitle.setAlignment(Qt.AlignCenter)
#         subtitle.setStyleSheet("font-size: 14px; color: #64748b;")
        
#         # Form container
#         form_container = QFrame()
#         form_container.setStyleSheet("""
#             QFrame {
#                 background-color: white;
#                 border-radius: 20px;
#                 border: 2px solid #e2e8f0;
#             }
#         """)
        
#         form_layout = QVBoxLayout(form_container)
#         form_layout.setContentsMargins(30, 30, 30, 30)
#         form_layout.setSpacing(20)
        
#         # Username
#         username_label = QLabel("USERNAME")
#         username_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.username_input = QLineEdit()
#         self.username_input.setPlaceholderText("Choose a username")
#         self.username_input.setFixedHeight(45)
#         self.username_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Password
#         password_label = QLabel("PASSWORD")
#         password_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #475569;")
        
#         self.password_input = QLineEdit()
#         self.password_input.setPlaceholderText("Create a strong password")
#         self.password_input.setEchoMode(QLineEdit.Password)
#         self.password_input.setFixedHeight(45)
#         self.password_input.setStyleSheet("""
#             QLineEdit {
#                 border: 2px solid #e2e8f0;
#                 border-radius: 10px;
#                 padding: 0 15px;
#                 font-size: 14px;
#                 background-color: #f8fafc;
#             }
#             QLineEdit:focus {
#                 border-color: #3b82f6;
#                 background-color: white;
#             }
#         """)
        
#         # Error label
#         self.error_label = QLabel()
#         self.error_label.setVisible(False)
#         self.error_label.setStyleSheet("color: #ef4444; font-size: 12px;")
#         self.error_label.setWordWrap(True)
        
#         # Register button
#         register_btn = QPushButton("Create Account")
#         register_btn.setFixedHeight(50)
#         register_btn.setCursor(Qt.PointingHandCursor)
#         register_btn.setStyleSheet("""
#             QPushButton {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #3b82f6, stop:1 #6366f1);
#                 color: white;
#                 font-size: 16px;
#                 font-weight: bold;
#                 border: none;
#                 border-radius: 12px;
#             }
#             QPushButton:hover {
#                 background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
#                     stop:0 #2563eb, stop:1 #4f46e5);
#             }
#         """)
#         register_btn.clicked.connect(self.handle_register)
        
#         # Login link
#         login_container = QHBoxLayout()
#         login_label = QLabel("Already have an account?")
#         login_label.setStyleSheet("font-size: 13px; color: #64748b;")
        
#         login_btn = QPushButton("Sign in")
#         login_btn.setCursor(Qt.PointingHandCursor)
#         login_btn.setStyleSheet("""
#             QPushButton {
#                 background: none;
#                 border: none;
#                 color: #3b82f6;
#                 font-size: 13px;
#                 font-weight: bold;
#                 text-decoration: underline;
#             }
#             QPushButton:hover {
#                 color: #2563eb;
#             }
#         """)
#         login_btn.clicked.connect(lambda: self.main_window.navigate("login"))
        
#         login_container.addStretch()
#         login_container.addWidget(login_label)
#         login_container.addWidget(login_btn)
#         login_container.addStretch()
        
#         form_layout.addWidget(username_label)
#         form_layout.addWidget(self.username_input)
#         form_layout.addWidget(password_label)
#         form_layout.addWidget(self.password_input)
#         form_layout.addWidget(self.error_label)
#         form_layout.addWidget(register_btn)
        
#         layout.addWidget(icon_label)
#         layout.addWidget(title)
#         layout.addWidget(subtitle)
#         layout.addSpacing(10)
#         layout.addWidget(form_container)
#         layout.addLayout(login_container)
#         layout.addStretch()
        
#         # Position center widget
#         main_layout.takeAt(0)
#         main_layout.addStretch()
#         main_layout.addWidget(center)
#         main_layout.addStretch()
    
#     def handle_register(self):
#         """Handle registration"""
#         username = self.username_input.text()
#         password = self.password_input.text()
        
#         if not username or not password:
#             self.error_label.setText("Please enter both username and password")
#             self.error_label.setVisible(True)
#             return
        
#         if len(password) < 8:
#             self.error_label.setText("Password must be at least 8 characters")
#             self.error_label.setVisible(True)
#             return
        
#         success, message = self.api_client.register(username, password)
        
#         if success:
#             self.main_window.on_login_success()
#         else:
#             self.error_label.setText(message)
#             self.error_label.setVisible(True)

class LoginPage(QWidget):
    """Refined Login Page with clean alignment"""
    
    def __init__(self, main_window, api_client):
        super().__init__()
        self.main_window = main_window
        self.api_client = api_client
        
        # Base layout
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Background gradient (Stays behind content)
        self.bg = GradientWidget("#f8fafc", "#e0f2fe")
        
        # Container for centering the form
        self.center_container = QWidget()
        self.center_container.setMaximumWidth(450)
        self.center_layout = QVBoxLayout(self.center_container)
        self.center_layout.setContentsMargins(40, 20, 40, 20)
        self.center_layout.setSpacing(20)
        self.center_layout.setAlignment(Qt.AlignCenter)
        
        # Logo/Icon
        icon_label = QLabel("🔐")
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("font-size: 54px; border: none; background: transparent;")
        
        # Title & Subtitle
        title = QLabel("Welcome Back")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 32px; font-weight: 900; color: #0f172a; background: transparent;")
        
        subtitle = QLabel("Sign in to access your analytics dashboard")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 14px; color: #64748b; background: transparent;")
        
        # Form container
        form_container = QFrame()
        form_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                border: 1px solid #e2e8f0;
            }
        """)
        form_layout = QVBoxLayout(form_container)
        form_layout.setContentsMargins(30, 35, 30, 35)
        form_layout.setSpacing(15)
        
        # Inputs
        u_lbl = QLabel("USERNAME")
        u_lbl.setStyleSheet("font-size: 10px; font-weight: 800; color: #94a3b8; border: none;")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setFixedHeight(48)
        self.username_input.setStyleSheet("QLineEdit { border: 2px solid #f1f5f9; border-radius: 10px; padding: 0 15px; background: #f8fafc; } QLineEdit:focus { border-color: #3b82f6; background: white; }")
        
        p_lbl = QLabel("PASSWORD")
        p_lbl.setStyleSheet("font-size: 10px; font-weight: 800; color: #94a3b8; border: none;")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(48)
        self.password_input.setStyleSheet("QLineEdit { border: 2px solid #f1f5f9; border-radius: 10px; padding: 0 15px; background: #f8fafc; } QLineEdit:focus { border-color: #3b82f6; background: white; }")
        
        self.error_label = QLabel()
        self.error_label.setVisible(False)
        self.error_label.setStyleSheet("color: #ef4444; font-size: 12px; border: none;")
        
        login_btn = QPushButton("Sign In")
        login_btn.setFixedHeight(50)
        login_btn.setCursor(Qt.PointingHandCursor)
        login_btn.setStyleSheet("QPushButton { background: #3b82f6; color: white; font-size: 15px; font-weight: bold; border-radius: 12px; } QPushButton:hover { background: #2563eb; }")
        login_btn.clicked.connect(self.handle_login)
        
        form_layout.addWidget(u_lbl)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(p_lbl)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.error_label)
        form_layout.addSpacing(10)
        form_layout.addWidget(login_btn)
        
        # Footer
        reg_btn = QPushButton("Create an account")
        reg_btn.setCursor(Qt.PointingHandCursor)
        reg_btn.setStyleSheet("QPushButton { color: #3b82f6; font-size: 13px; font-weight: bold; border: none; background: transparent; text-decoration: underline; }")
        reg_btn.clicked.connect(lambda: self.main_window.navigate("register"))
        
        # Assembly
        self.center_layout.addWidget(icon_label)
        self.center_layout.addWidget(title)
        self.center_layout.addWidget(subtitle)
        self.center_layout.addWidget(form_container)
        self.center_layout.addWidget(reg_btn)
        
        # Final layout stacking
        self.main_layout.addWidget(self.bg)
        self.bg_layout = QGridLayout(self.bg)
        self.bg_layout.addWidget(self.center_container, 0, 0, Qt.AlignCenter)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            self.error_label.setText("Please enter both credentials")
            self.error_label.setVisible(True)
            return
        success, message = self.api_client.login(username, password)
        if success: self.main_window.on_login_success()
        else:
            self.error_label.setText(message)
            self.error_label.setVisible(True)

class RegisterPage(QWidget):
    """Refined Registration Page with clean alignment"""
    
    def __init__(self, main_window, api_client):
        super().__init__()
        self.main_window = main_window
        self.api_client = api_client
        
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.bg = GradientWidget("#f8fafc", "#e0f2fe")
        
        self.center_container = QWidget()
        self.center_container.setMaximumWidth(450)
        self.center_layout = QVBoxLayout(self.center_container)
        self.center_layout.setContentsMargins(40, 20, 40, 20)
        self.center_layout.setSpacing(15)
        self.center_layout.setAlignment(Qt.AlignCenter)
        
        icon_label = QLabel("✨")
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("font-size: 54px; border: none; background: transparent;")
        
        title = QLabel("Create Account")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 32px; font-weight: 900; color: #0f172a; background: transparent;")
        
        subtitle = QLabel("Get started with your free account today")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 14px; color: #64748b; background: transparent;")
        
        form_container = QFrame()
        form_container.setStyleSheet("QFrame { background-color: white; border-radius: 20px; border: 1px solid #e2e8f0; }")
        form_layout = QVBoxLayout(form_container)
        form_layout.setContentsMargins(30, 35, 30, 35)
        form_layout.setSpacing(15)
        
        u_lbl = QLabel("USERNAME")
        u_lbl.setStyleSheet("font-size: 10px; font-weight: 800; color: #94a3b8; border: none;")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")
        self.username_input.setFixedHeight(48)
        self.username_input.setStyleSheet("QLineEdit { border: 2px solid #f1f5f9; border-radius: 10px; padding: 0 15px; background: #f8fafc; } QLineEdit:focus { border-color: #3b82f6; background: white; }")
        
        p_lbl = QLabel("PASSWORD")
        p_lbl.setStyleSheet("font-size: 10px; font-weight: 800; color: #94a3b8; border: none;")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("At least 8 characters")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(48)
        self.password_input.setStyleSheet("QLineEdit { border: 2px solid #f1f5f9; border-radius: 10px; padding: 0 15px; background: #f8fafc; } QLineEdit:focus { border-color: #3b82f6; background: white; }")
        
        self.error_label = QLabel()
        self.error_label.setVisible(False)
        self.error_label.setStyleSheet("color: #ef4444; font-size: 12px; border: none;")
        
        reg_btn = QPushButton("Create Account")
        reg_btn.setFixedHeight(50)
        reg_btn.setCursor(Qt.PointingHandCursor)
        reg_btn.setStyleSheet("QPushButton { background: #3b82f6; color: white; font-size: 15px; font-weight: bold; border-radius: 12px; } QPushButton:hover { background: #2563eb; }")
        reg_btn.clicked.connect(self.handle_register)
        
        form_layout.addWidget(u_lbl)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(p_lbl)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.error_label)
        form_layout.addSpacing(10)
        form_layout.addWidget(reg_btn)
        
        back_btn = QPushButton("Back to Login")
        back_btn.setCursor(Qt.PointingHandCursor)
        back_btn.setStyleSheet("QPushButton { color: #3b82f6; font-size: 13px; font-weight: bold; border: none; background: transparent; text-decoration: underline; }")
        back_btn.clicked.connect(lambda: self.main_window.navigate("login"))
        
        self.center_layout.addWidget(icon_label)
        self.center_layout.addWidget(title)
        self.center_layout.addWidget(subtitle)
        self.center_layout.addWidget(form_container)
        self.center_layout.addWidget(back_btn)
        
        self.main_layout.addWidget(self.bg)
        self.bg_layout = QGridLayout(self.bg)
        self.bg_layout.addWidget(self.center_container, 0, 0, Qt.AlignCenter)

    def handle_register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            self.error_label.setText("Username and password required")
            self.error_label.setVisible(True)
            return
        if len(password) < 8:
            self.error_label.setText("Password too short")
            self.error_label.setVisible(True)
            return
        success, message = self.api_client.register(username, password)
        if success: self.main_window.on_login_success()
        else:
            self.error_label.setText(message)
            self.error_label.setVisible(True)          

class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.api_client = APIClient()
        self.setup_ui()
        
        # Check if already logged in
        if self.api_client.token:
            self.show_app()
        else:
            self.navigate("login")
    
    def setup_ui(self):
        """Setup main UI"""
        self.setWindowTitle("Chemical Equipment Analytics Platform")
        self.setMinimumSize(1400, 900)
        
        # Central widget with stacked layout
        central = QWidget()
        self.setCentralWidget(central)
        
        self.main_layout = QVBoxLayout(central)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Navigation bar (hidden initially)
        self.navbar = self.create_navbar()
        self.navbar.setVisible(False)
        
        # Stacked widget for pages
        self.pages = QStackedWidget()
        
        # Create pages
        self.home_page = HomePage(self)
        self.upload_page = UploadPage(self, self.api_client)
        self.summary_page = SummaryPage(self, self.api_client)
        self.analytics_page = AnalyticsPage(self, self.api_client)
        self.login_page = LoginPage(self, self.api_client)
        self.register_page = RegisterPage(self, self.api_client)
        
        # Add pages to stack
        self.pages.addWidget(self.home_page)       # 0
        self.pages.addWidget(self.upload_page)     # 1
        self.pages.addWidget(self.summary_page)    # 2
        self.pages.addWidget(self.analytics_page)  # 3
        self.pages.addWidget(self.login_page)      # 4
        self.pages.addWidget(self.register_page)   # 5
        
        self.main_layout.addWidget(self.navbar)
        self.main_layout.addWidget(self.pages)
        
        # Apply global stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8fafc;
            }
        """)
    
    def create_navbar(self):
        """Create navigation bar"""
        navbar = QFrame()
        navbar.setFixedHeight(70)
        navbar.setStyleSheet("""
            QFrame {
                background-color: white;
                border-bottom: 2px solid #e2e8f0;
            }
        """)
        
        layout = QHBoxLayout(navbar)
        layout.setContentsMargins(30, 0, 30, 0)
        layout.setSpacing(20)
        
        # Logo
        logo = QLabel("⚡ CHEMANALYZE")
        logo.setStyleSheet("font-size: 20px; font-weight: 900; color: #3b82f6;")
        
        # Navigation buttons
        btn_home = self.create_nav_button("Home", "home")
        btn_upload = self.create_nav_button("Upload", "upload")
        btn_summary = self.create_nav_button("Summary", "summary")
        btn_analytics = self.create_nav_button("Analytics", "analytics")
        
        # Logout button
        btn_logout = QPushButton("Logout")
        btn_logout.setCursor(Qt.PointingHandCursor)
        btn_logout.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #ef4444;
                font-size: 13px;
                font-weight: bold;
                border: 2px solid #fecaca;
                border-radius: 10px;
                padding: 8px 20px;
            }
            QPushButton:hover {
                background-color: #fef2f2;
                border-color: #ef4444;
            }
        """)
        btn_logout.clicked.connect(self.handle_logout)
        
        layout.addWidget(logo)
        layout.addSpacing(30)
        layout.addWidget(btn_home)
        layout.addWidget(btn_upload)
        layout.addWidget(btn_summary)
        layout.addWidget(btn_analytics)
        layout.addStretch()
        layout.addWidget(btn_logout)
        
        return navbar
    
    def create_nav_button(self, text, page):
        """Create navigation button"""
        btn = QPushButton(text)
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #64748b;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #f1f5f9;
                color: #3b82f6;
            }
        """)
        btn.clicked.connect(lambda: self.navigate(page))
        return btn
    
    def navigate(self, page_name):
        """Navigate to page"""
        page_map = {
            "home": 0,
            "upload": 1,
            "summary": 2,
            "analytics": 3,
            "login": 4,
            "register": 5
        }
        
        if page_name in page_map:
            self.pages.setCurrentIndex(page_map[page_name])
            
            # Refresh data on certain pages
            if page_name == "summary":
                self.summary_page.load_data()
            elif page_name == "analytics":
                self.analytics_page.load_datasets()
    
    def on_login_success(self):
        """Handle successful login"""
        self.show_app()
    
    def show_app(self):
        """Show main app (after login)"""
        self.navbar.setVisible(True)
        self.navigate("home")
    
    def handle_logout(self):
        """Handle logout"""
        self.api_client.clear_token()
        self.navbar.setVisible(False)
        self.navigate("login")


def main():
    app = QApplication(sys.argv)
    
    # Set application font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()