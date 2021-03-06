from multiprocessing import freeze_support
import sys
from PyQt5 import QtGui

from mbci_lab.common.architecture import Architecture
from mbci_lab.common.arguments import *
from mbci_lab.common.logger import Logger as Log
from mbci_lab.core.constants import MinimalPython
from mbci_lab.ui import mainWindow


TAG = "mbci_lab"


class mbci_lab:
    def __init__(self, argv=sys.argv):
        freeze_support()
        self._args = self._init_logger()
        self._app = QtGui.QApplication(argv)

    def run(self):
        if Architecture.is_python_version(MinimalPython.major, minor=MinimalPython.minor):
            Log.i(TAG, "Starting mbci_lab")
            win = mainWindow.MainWindow(samples=self._args.get_user_samples())
            win.setWindowTitle("{} - {}".format(Constants.app_title, Constants.app_version))
            win.show()
            self._app.exec()
            Log.i(TAG, "Finishing mbci_lab\n")
            win.close()
        else:
            self._fail()
        self.close()

    def close(self):
        self._app.exit()
        Log.close()
        sys.exit()

    @staticmethod
    def _init_logger():
        args = Arguments()
        args.create()
        args.set_user_log_level()
        return args

    @staticmethod
    def _fail():
        txt = str("mbci_lab requires Python {}.{} to run"
                  .format(MinimalPython.major, MinimalPython.minor))
        Log.e(TAG, txt)


if __name__ == '__main__':
    mbci_lab().run()
