import flet as ft
from .colors import BACKGROUND, PRIMARY_YELLOW, DARK


INFO_CARD_CONFIG = {
    "padding": ft.Padding(25, 25, 25, 25),
    "bgcolor": "#F3F4F6",  # Можна замінити на BORDER_LIGHT з твоєї палітри
    "border_radius": 15,
    "width": 360,
}

LOGIN_CARD_CONFIG = {
    "width": 400,
    "padding": ft.Padding(40, 40, 40, 40),
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 20,
    "shadow": ft.BoxShadow(
        blur_radius=20,
        color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
        offset=ft.Offset(0, 10),
    ),
}

# Налаштування сітки
COURSE_GRID_CONFIG = {
    "expand": True,
    "runs_count": 3,
    "max_extent": 400,
    "spacing": 30,
    "run_spacing": 30,
}

# Стиль контейнера картки курсу
COURSE_CARD_STYLE = {
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 15,
    "padding": 0,
    "shadow": ft.BoxShadow(
        blur_radius=15,
        color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK),
        offset=ft.Offset(0, 5),
    ),
}

# Налаштування сітки тем
THEME_GRID_CONFIG = {
    "expand": True,
    "runs_count": 2,
    "max_extent": 600,
    "child_aspect_ratio": 1.2,
    "spacing": 30,
    "run_spacing": 30,
}

# Стиль карти тем
THEME_CARD_STYLE = {
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 20,
    "padding": 25,
    "shadow": ft.BoxShadow(
        blur_radius=15,
        color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK),
        offset=ft.Offset(0, 5),
    ),
}

# Стиль прогрес-бару
PROGRESS_BAR_COLOR = PRIMARY_YELLOW
PROGRESS_BG_COLOR = "#F3F4F6"

# Стиль елемента списку (ListTile)
LESSON_TILE_STYLE = {
    "bgcolor": BACKGROUND,
    "border_radius": 10,
}

# Стиль для іконок
CARD_ICON_COLOR = DARK
CARD_ICON_SIZE = 22


# Контейнер для текстового контенту (лекції/матеріалів)
LESSON_CONTENT_STYLE = {
    "padding": ft.Padding(30, 30, 30, 30),
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 15,
    "border": ft.border.all(1, "#E5E7EB"),
}

# Стиль картки відео
VIDEO_CARD_STYLE = {
    "bgcolor": DARK,
    "border_radius": 15,
    "padding": 10,
    "shadow": ft.BoxShadow(
        blur_radius=20,
        color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK),
        offset=ft.Offset(0, 10),
    ),
}

