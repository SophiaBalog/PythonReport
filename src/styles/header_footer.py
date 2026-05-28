import flet as ft
from .colors import BACKGROUND, DARK


# Основні параметри AppBar
HEADER_CONFIG = {
    "bgcolor": BACKGROUND,        # Світлий фон з вашої палітри
    "elevation": 0,               # Робимо плоским (сучасний стиль)
    "center_title": False,        # Заголовок зліва
    "toolbar_height": 70,         # Трохи збільшена висота для простору
}

# Контейнер для відступів кнопок (actions)
HEADER_ACTIONS_PADDING = ft.padding.only(right=20)


# Налаштування самого контейнера футера
FOOTER_CONFIG = {
    "bgcolor": DARK,                # Темний фон для контрасту з білим сайтом
    "padding": ft.Padding(40, 20, 40, 20),
    "height": 100,
}

