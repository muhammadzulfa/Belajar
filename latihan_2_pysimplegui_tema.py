import PySimpleGUI as sg

sg.theme('Dark Green 1')

window = sg.Window(
    title="Latihan Pertama",
    layout=[
        [sg.Text("Perkenalkan Nama Saya: ", font=("Algerian", 30, "italic", "bold"))],
        [sg.Text("Nama      : Muhammad Zulfa")],
        [sg.Text("NIM       : 2210010080")],
        [sg.Text("Kelas     : 5A Non Reguler Banjarmasin")],
        [sg.Text("Matkul    : Pemrograman Visual 3")],
    ], 
    size=(600, 300),
    font=("Arial", 18)
)

window()
window.close()