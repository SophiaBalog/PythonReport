import flet as ft
from .colors import TEXT_PRIMARY, TEXT_SECONDARY, TEXT_LIGHT, PRIMARY_YELLOW_DARK, TEXT_WHITE,DARK,PRIMARY_YELLOW

# Заголовки (Headings)
HEADER_DISPLAY = ft.TextStyle(
    size=48,
    weight=ft.FontWeight.BOLD,
    color=TEXT_PRIMARY,
    letter_spacing=1,
)

HEADER_H1 = ft.TextStyle(
    size=32,
    weight=ft.FontWeight.W_800,
    color=TEXT_PRIMARY,
)

HEADER_H2 = ft.TextStyle(
    size=24,
    weight=ft.FontWeight.W_700,
    color=TEXT_PRIMARY,
)

# Текстові стилі для контенту
BODY_LARGE = ft.TextStyle(
    size=18,
    weight=ft.FontWeight.NORMAL,
    color=TEXT_PRIMARY,
)

BODY_MEDIUM = ft.TextStyle(
    size=16,
    weight=ft.FontWeight.NORMAL,
    color=TEXT_SECONDARY,
)

BODY_SMALL = ft.TextStyle(
    size=14,
    weight=ft.FontWeight.NORMAL,
    color=TEXT_LIGHT,
)

# Акцентні та функціональні стилі
LABEL_BOLD = ft.TextStyle(
    size=14,
    weight=ft.FontWeight.BOLD,
    color=TEXT_PRIMARY,
)

# Для посилань або кнопок усередині тексту
LINK_STYLE = ft.TextStyle(
    size=16,
    weight=ft.FontWeight.W_500,
    color=PRIMARY_YELLOW_DARK,
    decoration=ft.TextDecoration.UNDERLINE,
)

# Спеціально для карток (білий текст на темному або контрастному фоні)
CARD_TITLE_WHITE = ft.TextStyle(
    size=20,
    weight=ft.FontWeight.W_600,
    color=TEXT_WHITE,
)

HEADER_TITLE_STYLE = ft.TextStyle(
    size=24,
    weight=ft.FontWeight.W_900,
    color=DARK,                   # Темний колір для контрасту
    letter_spacing=1,
)


STAT_NUMBER_STYLE = ft.TextStyle(
    size=36,
    weight=ft.FontWeight.W_900,
    color=PRIMARY_YELLOW,
)


# Стиль для тексту копірайту
FOOTER_TEXT_STYLE = ft.TextStyle(
    size=12,
    color="#9CA3AF",
    weight=ft.FontWeight.NORMAL,
)

# Стиль для посилань (Курси, Тести...)
FOOTER_LINK_STYLE = ft.TextStyle(
    size=14,
    color=TEXT_WHITE,
    weight=ft.FontWeight.W_500,
)

ERROR_TEXT_STYLE = ft.TextStyle(
    size=12,
    color=ft.Colors.RED_400,
    weight=ft.FontWeight.W_500,
)

# Стиль тексту заголовка курсу
COURSE_TITLE_STYLE = ft.TextStyle(
    size=20,
    weight=ft.FontWeight.BOLD,
    color=DARK,
)

# Колір іконок та тексту для відео-картки
VIDEO_TEXT_STYLE = ft.TextStyle(color=ft.Colors.WHITE,)
VIDEO_SUBTITLE_STYLE = ft.TextStyle(color="#9CA3AF", size=12)