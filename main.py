from youtubesearchpython import VideosSearch, Transcript
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QPalette, QColor, QDesktopServices
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.results = None

        self.ui.searchButton.clicked.connect(self.main)
        self.ui.listWidget.itemDoubleClicked.connect(self.open_listbox_link)

    def main(self):

        self.ytsearchterm: str = self.ui.ytSearchInput.text()
        self.searchterm: str = self.ui.searchTermInput.text()
        self.maxresults: int = self.ui.maxSearchSpinBox.value()

        self.ui.listWidget.clear()

        self.search()
        print("Videos: " + str(len(self.results)))

        for i, video in enumerate(self.results):
            self.ui.statusLabel.setText("Downloading and parsing subtitles...")
            self.ui.progressBar.setValue(((i + 1) / len(self.results)) * 100)
            self.download_subtitles(video["id"])
            self.parse_subtitles(video["id"])

    def search(self):
        self.ui.statusLabel.setText("Searching...")
        # Search for the video
        s = VideosSearch(
            query=self.ytsearchterm,
            limit=self.maxresults,
            language="en",
        )
        self.results = s.result()["result"]

        pages = self.maxresults / len(self.results)
        if pages.is_integer() == False:
            pages = int(pages + 1)
        for i in range(int(pages)):
            print(i + 1)
            print(pages)
            print(((i + 1) / pages) * 100)

            self.ui.progressBar.setValue(((i + 1) / pages) * 100)
            s.next()
            self.results += s.result()["result"]
        n = len(self.results)
        if n > self.maxresults:
            for i in range(0, n - self.maxresults):
                self.results.pop()

    def download_subtitles(self, id):
        url = "https://www.youtube.com/watch?v=" + id

        try:
            self.subtitles = Transcript.get(url)

            self.subtitles = self.subtitles["segments"]
        except:
            pass

    def parse_subtitles(self, id):
        for segment in self.subtitles:

            try:
                if self.searchterm.lower() in segment["text"].lower():
                    print(
                        self.searchterm
                        + " found in: "
                        + "https://youtu.be/"
                        + id
                        + "?t="
                        + segment["startMs"][:-3]
                    )
                    print(
                        "start: "
                        + str(segment["startMs"])
                        + "\nend: "
                        + str(segment["endMs"])
                    )
                    self.ui.listWidget.addItem(
                        "https://youtu.be/" + id + "?t=" + segment["startMs"][:-3]
                    )
            except AttributeError:
                pass

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
