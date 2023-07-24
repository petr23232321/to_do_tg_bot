from aiogram import types

mainMenu = types.InlineKeyboardMarkup(row_width=2)

btn_add = types.InlineKeyboardButton(text='/add', callback_data='add')
btn_done = types.InlineKeyboardButton(text='/done', callback_data='done')
btn_list = types.InlineKeyboardButton(text='/list', callback_data='list')
btn_delete = types.InlineKeyboardButton(text='/delete', callback_data='delete')

mainMenu.insert(btn_add)
mainMenu.insert(btn_done)
mainMenu.insert(btn_list)
mainMenu.insert(btn_delete)