from playsound import playsound
import winsound
import shutil
import keyboard
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from PyQt5.QtCore import Qt
import os


BALATRO_DIR = 'C:\\Users\\jzy\\AppData\\Roaming\\Balatro\\1\\save.jkr'
SAVE_DIR = '.\\all_data\\'


def play_sound():
    playsound('.\\sound\\f1_radio_team.mp3')


def get_file_names_in_folder(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names


def save():
    try:
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowFlags(Qt.WindowStaysOnTopHint)
        layout = QVBoxLayout()

        # 创建输入框
        input_box = QLineEdit()
        layout.addWidget(input_box)

        # 创建按钮
        button = QPushButton("确定")
        button.clicked.connect(lambda: save_file(input_box))
        layout.addWidget(button)

        window.setLayout(layout)
        window.show()
        app.exec_()
    except Exception as e:
        print(f"创建保存窗口时出现错误: {e}")


def save_file(input_box):
    try:
        # 获取输入框中的内容
        input_text = input_box.text()
        if input_text:
            # 生成新的文件名，包括时间戳
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            new_file_name = f"{input_text}_{timestamp}.jkr"
            target_file = os.path.join(SAVE_DIR, new_file_name)
            # 使用 shutil.copy 函数将源文件复制到目标文件
            shutil.copy(BALATRO_DIR, target_file)
            print(f"已存档到 {target_file}")
            play_sound()
        else:
            print("输入框不能为空")
    except Exception as e:
        print(f"复制文件时出现错误: {e}")


def load():
    try:
        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowFlags(Qt.WindowStaysOnTopHint)
        layout = QVBoxLayout()

        # 创建选择框
        combo_box = QComboBox()
        combo_box.addItems(get_file_names_in_folder(SAVE_DIR))
        layout.addWidget(combo_box)

        # 创建按钮
        button = QPushButton("确定")
        button.clicked.connect(lambda: load_file(combo_box))
        layout.addWidget(button)

        window.setLayout(layout)
        window.show()
        app.exec_()
    except Exception as e:
        print(f"创建读档窗口时出现错误: {e}")


def load_file(combo_box):
    try:
        # 获取选择框中选中的文件
        selected_file = combo_box.currentText()
        if selected_file:
            source_file = os.path.join(SAVE_DIR, selected_file)
            # 使用 shutil.copy 函数将选中文件复制到目标文件夹
            shutil.copy(source_file, BALATRO_DIR)
            print(f"已读档 {selected_file}")
            play_sound()
        else:
            print("未选择文件")
    except Exception as e:
        print(f"复制文件时出现错误: {e}")


def main():
    while True:
        if keyboard.is_pressed('alt+s'):
            save()
        if keyboard.is_pressed('alt+l'):
            load()
        if keyboard.is_pressed('alt+p'):
            play_sound()
        # 保持程序运行
        time.sleep(0.01)

main()

