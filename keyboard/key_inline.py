from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline1():
    keyboard_inline = InlineKeyboardMarkup(row_width=3)
    but_inline = InlineKeyboardButton('Роберт Левандовски', url='https://www.sportsgamblingpodcast.com/wp-content/uploads/2022/10/450d159220907018_plzen_v_barca.jpg')
    but_inline2 = InlineKeyboardButton('Тер Штеген', url='https://www.fussballeuropa.com/images/xtra/marc-andre-ter-stegen-2020-200.jpg')
    but_inline3 = InlineKeyboardButton('Араухо', url='https://cdn1.thechelseachronicle.com/uploads/17/2022/02/GettyImages-1368974517-scaled.jpg')
    keyboard_inline.add(but_inline, but_inline2, but_inline3)
    return keyboard_inline
def get_keyboard_inline_2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=2)
    but_inline3 = InlineKeyboardButton('Винисиус', url='https://sun9-29.userapi.com/impg/Vc_SX8983a2ugt8xLy6cTEVWmM1CV5Gib0NfyQ/kwUS6wCwqS4.jpg?size=1280x853&quality=95&sign=0bcba37833379e9a5c959d0513849ae0&c_uniq_tag=kzgfdKZUhzqz9z1WF2aUdJW8Mz5n1YRndk6TrUK82RA&type=album')
    but_inline4 = InlineKeyboardButton('Родриго', url='https://f.i.uol.com.br/fotografia/2022/05/06/165180936862749c58977f4_1651809368_3x2_rt.jpg')
    but_inline5 = InlineKeyboardButton('Белигем', url='https://sun9-29.userapi.com/impg/Vc_SX8983a2ugt8xLy6cTEVWmM1CV5Gib0NfyQ/kwUS6wCwqS4.jpg?size=1280x853&quality=95&sign=0bcba37833379e9a5c959d0513849ae0&c_uniq_tag=kzgfdKZUhzqz9z1WF2aUdJW8Mz5n1YRndk6TrUK82RA&type=album')
    keyboard_inline2.add(but_inline3, but_inline4, but_inline5)
    return keyboard_inline2