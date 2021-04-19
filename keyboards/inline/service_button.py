from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(row_width=2)

choose_apple_music = InlineKeyboardButton(text="Apple Music", url="https://www.apple.com/by/apple-music/" )
choice.insert(choose_apple_music)

choose_spotify = InlineKeyboardButton(text="Spotify", url="https://open.spotify.com/?_gl=1*139ah7w*_gcl_aw*R0NMLjE2MTg4MzE5MDMuQ2owS0NRancxUFNEQmhEYkFSSXNBUGVUcXJmV2NmR1oyOHlJRXFGY3lZSS1STVR4blRKZVJEWE9OUklDWkxhUlNObGFMOVoySTBxa2dMb2FBakdlRUFMd193Y0I.*_gcl_dc*R0NMLjE2MTg4MzE5MDMuQ2owS0NRancxUFNEQmhEYkFSSXNBUGVUcXJmV2NmR1oyOHlJRXFGY3lZSS1STVR4blRKZVJEWE9OUklDWkxhUlNObGFMOVoySTBxa2dMb2FBakdlRUFMd193Y0I.&_ga=2.92953053.1737066752.1618831905-524338588.1618399927&_gac=1.247266934.1618831905.Cj0KCQjw1PSDBhDbARIsAPeTqrfWcfGZ28yIEqFcyYI-RMTxnTJeRDXONRICZLaRSNlaL9Z2I0qkgLoaAjGeEALw_wcB")
choice.insert(choose_spotify)

choose_yandex_music = InlineKeyboardButton(text="Yandex Музыка", url="https://music.yandex.by/")
choice.insert(choose_yandex_music)

choose_mixcloud = InlineKeyboardButton(text="Mixcloud", url="https://www.mixcloud.com/Kontrapunktura/")
choice.insert(choose_mixcloud)


cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

