import flet as ft
from .colors import *
from .text import LABEL_BOLD, BODY_LARGE, BODY_MEDIUM

# Кнопка "Заклик до дії" (найбільша та найяскравіша)
EASY_START_BUTTON = ft.ButtonStyle(
    bgcolor=ACCENT_GOLD,
    color=TEXT_WHITE,
    elevation=6,
    padding=24,
    shape=ft.RoundedRectangleBorder(radius=18),
    text_style=ft.TextStyle(
        size=20,
        weight=ft.FontWeight.BOLD,
        letter_spacing=0.5
    ),
)

# Кнопка входу (акцентна жовта)
LOGIN_BUTTON = ft.ButtonStyle(
    bgcolor=PRIMARY_YELLOW,
    color=DARK,
    elevation=3,
    padding=18,
    shape=ft.RoundedRectangleBorder(radius=12),
    text_style=LABEL_BOLD, # Використовуємо ваш стиль: 14px, Bold
)

# Кнопка реєстрації (контрастна темна)
REGISTER_BUTTON = ft.ButtonStyle(
    bgcolor=DARK,
    color=PRIMARY_YELLOW,
    elevation=3,
    padding=18,
    shape=ft.RoundedRectangleBorder(radius=12),
    text_style=LABEL_BOLD,
)

BASE_BUTTON = ft.ButtonStyle(
    bgcolor=CARD_BG,
    color=TEXT_PRIMARY,
    padding=16,
    side=ft.BorderSide(1, BORDER),
    shape=ft.RoundedRectangleBorder(radius=10),
    text_style=BODY_MEDIUM, # 16px, Normal
)

NAV_BUTTON = ft.ButtonStyle(
    bgcolor="transparent",
    color=TEXT_PRIMARY,
    padding=12,
    shape=ft.RoundedRectangleBorder(radius=8),
    text_style=ft.TextStyle(
        size=16,
        weight=ft.FontWeight.W_500,
    ),
)

COURSE_BUTTON_STYLE = ft.ButtonStyle(
    color=DARK,
    bgcolor=PRIMARY_YELLOW,
    shape=ft.RoundedRectangleBorder(radius=10),
    padding=ft.Padding(20, 15, 20, 15),
)

TESTING_BUTTON = ft.ButtonStyle(
    bgcolor=PRIMARY_YELLOW,
    color=DARK,
    padding=25,
    shape=ft.RoundedRectangleBorder(radius=10),
)