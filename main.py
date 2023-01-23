import flet as ft
import json

mapa = {
    0: [0, 1, 2, 3, 4],
    1: [5, 6, 7, 8, 9],
    2: [10, 11, 12, 13, 14],
    3: [15, 16, 17, 18, 19],
    4: [20, 21, 22, 23, 24]
}




def json_read(path):
    with open(path, 'r', encoding='utf-8') as read_info:
        return json.load(read_info)


def json_write(path, var):
    with open(path, 'w', encoding='utf-8') as write_info:
        json.dump(var, write_info, ensure_ascii=False, indent=4)


def create_container(content, margin=10, padding=10, aligment=ft.alignment.center, bgcolor=ft.colors.WHITE, width=150,
                     height=150, border_radius=10, ink=False, data=None, on_click=None):
    return ft.Container(
        content=content,
        margin=margin,
        padding=padding,
        alignment=aligment,
        bgcolor=bgcolor,
        width=width,
        height=height,
        border_radius=border_radius,
        ink=ink,
        data=data,
        on_click=on_click,
    )


def main(page: ft.Page):
    def change_color(e):
        if e.control.bgcolor == ft.colors.BLUE:
            e.control.bgcolor = ft.colors.RED
        elif e.control.bgcolor == ft.colors.RED:
            e.control.bgcolor = ft.colors.WHITE
        else:
            e.control.bgcolor = ft.colors.BLUE
        page.update()

    json_write('map.json', mapa)
    maps = json_read('map.json')  # i - номер строки (str), j - номер элемента (int)
    print(maps)
    for i in range(len(maps.keys())):
        row = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        for j in range(len(maps['0'])):
            zone = str(maps[str(i)][j])
            # row.controls.append(create_container(ft.Text(value=zone, color=ft.colors.BLACK), data=zone, ink=True,
            #                                      on_click=change_color))
            # row.controls.append(create_container(ft.Image(src=ft.colors.WHITE, fit=ft.ImageFit.FILL, border_radius=10),
            #                                      padding=2, border_radius=10), data=zone, ink=True)
        page.add(row)

ft.app(target=main, assets_dir='assets', view=ft.WEB_BROWSER, port=7777)
