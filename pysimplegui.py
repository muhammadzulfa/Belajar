import PySimpleGUI as sg

window = sg.Window(title="Latihan Pertama", layout=[
    [sg.Text("Nama      : Muhammad Zulfa")],
    [sg.Text("NIM       : 2210010080")],
    [sg.Text("Kelas     : 5A Non Reguler Banjarmasin")],
    [sg.Text("Matkul    : Pemrograman Visual 3")],
], size=(400,200))
window()
window.close()