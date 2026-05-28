import flet as ft


GRADIENT = ft.RadialGradient(
    center=ft.Alignment.BOTTOM_CENTER,
    radius=1.5,

    colors=[
        "#FACC15",  # жовтий центр
        "#FEF3C7",  # світло-жовтий
        "#FFF8DB",  # майже білий
        "#FFFFFF",  # білий край
    ],

    stops=[0.0, 0.35, 0.7, 1.0])