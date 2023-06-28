from aiogram.types import BotCommand

# Создаем список с командами и их описанием для кнопки menu
main_menu_commands = [
    BotCommand(command='/help',
               description='Справка по работе бота'),
    BotCommand(command='/support',
               description='Поддержка'),
    BotCommand(command='/contacts',
               description='Другие способы связи'),
    BotCommand(command='/payments',
               description='Платежи')]
