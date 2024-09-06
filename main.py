from youtubesearchpython import VideosSearch, Transcript
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QUrl, Qt, QThread, Signal
from PySide6.QtGui import QPalette, QColor, QDesktopServices
from ui_mainwindow import Ui_MainWindow


class SearchWorker(QThread):
    progress = Signal(int)
    status = Signal(str)
    result = Signal(list)
    finished = Signal()

    def __init__(self, ytsearchterm, searchterm, maxresults):
        super().__init__()
        self.ytsearchterm = ytsearchterm
        self.searchterm = searchterm
        self.maxresults = maxresults

    def run(self):
        results = []
        self.status.emit("Searching...")
        s = VideosSearch(query=self.ytsearchterm, limit=self.maxresults, language="en")
        results = s.result()["result"]

        pages = self.maxresults / len(results)
        if not pages.is_integer():
            pages = int(pages + 1)

        for i in range(int(pages)):
            self.progress.emit(int(((i + 1) / pages) * 100))
            s.next()
            results += s.result()["result"]

        if len(results) > self.maxresults:
            results = results[: self.maxresults]

        self.status.emit("Downloading and parsing subtitles...")
        filtered_results = []
        for i, video in enumerate(results):
            self.progress.emit(int(((i + 1) / len(results)) * 100))
            subtitles = self.download_subtitles(video["id"])
            if subtitles:
                timestamps = self.parse_subtitles(video["id"], subtitles)
                if timestamps:
                    filtered_results.extend(timestamps)

        self.result.emit(filtered_results)
        self.finished.emit()

    def download_subtitles(self, video_id):
        url = f"https://www.youtube.com/watch?v={video_id}"
        try:
            return Transcript.get(url)["segments"]
        except:
            return None

    def parse_subtitles(self, video_id, subtitles):
        timestamps = []
        for segment in subtitles:
            if self.searchterm.lower() in segment["text"].lower():
                timestamp = f"https://youtu.be/{video_id}?t={segment['startMs'][:-3]}"
                timestamps.append(timestamp)
        return timestamps


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.searchButton.clicked.connect(self.start_search)
        self.ui.listWidget.itemDoubleClicked.connect(self.open_listbox_link)
        self.setFixedSize(639, 336)
        self.search_worker = None

    def start_search(self):
        self.ui.listWidget.clear()
        self.ui.searchButton.setEnabled(False)

        ytsearchterm = self.ui.ytSearchInput.text()
        searchterm = self.ui.searchTermInput.text()
        maxresults = self.ui.maxSearchSpinBox.value()

        self.search_worker = SearchWorker(ytsearchterm, searchterm, maxresults)
        self.search_worker.progress.connect(self.ui.progressBar.setValue)
        self.search_worker.status.connect(self.ui.statusLabel.setText)
        self.search_worker.result.connect(self.update_list_widget)
        self.search_worker.finished.connect(self.search_finished)
        self.search_worker.start()

    def update_list_widget(self, results):
        self.ui.listWidget.addItems(results)

    def search_finished(self):
        self.ui.searchButton.setEnabled(True)
        self.ui.statusLabel.setText("Search completed")

    def open_listbox_link(self):
        link = self.ui.listWidget.currentItem().text()
        url = QUrl(link)
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    palette = QPalette()

    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)

    # New lighter colors for disabled widgets
    palette.setColor(QPalette.Disabled, QPalette.Window, QColor(80, 80, 80))
    palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.gray)
    palette.setColor(QPalette.Disabled, QPalette.Base, QColor(40, 40, 40))
    palette.setColor(QPalette.Disabled, QPalette.Text, Qt.gray)
    palette.setColor(QPalette.Disabled, QPalette.Button, QColor(80, 80, 80))
    palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.gray)

    app = QApplication(sys.argv + ["-platform", "windows:darkmode=1"])
    app.setStyle("Fusion")
    app.setPalette(palette)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
