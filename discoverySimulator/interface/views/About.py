# discoverySimulator is a Python package allowing to simulate environments in which mobile robots evolve.
# This simulator is accompanied by an interface allowing to visualize and control the simulation.
# This package is ideal for a playful learning of python and a discovery of mobile robotics.
#
# Discovery Simulator - Copyright (C) 2022  Leo Planquette & Eloise Lefebvre
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLayout
from discoverySimulator.config import *

class About(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.setWindowTitle("About")
        self.setWindowIcon(QIcon(os.path.join(config["ressourcesPath"],'toolbar','about.svg')))
        self.setWindowFlags(self.windowFlags() and Qt.WindowCloseButtonHint)

        layout=QVBoxLayout()
        layout.addWidget(self.__createPanelWidget())
        layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(layout)

        self.exec()

    def __createPanelWidget(self) -> QLabel:
        return QSvgWidget(os.path.join(config["ressourcesPath"],'infos','creditPanel.svg'))

