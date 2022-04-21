import xlwt


def export_to_excel(match_, data):
    style_bold = xlwt.XFStyle()
    style_border = xlwt.XFStyle()

    font = xlwt.Font()
    font.bold = True
    style_bold.font = font

    borders = xlwt.Borders()
    borders.bottom = xlwt.Borders.THICK
    style_bold.borders = borders
    style_border.borders = borders

    work_book = xlwt.Workbook()
    for item in data:
        work_sheet = work_book.add_sheet(item['map'])
        work_sheet.write(0, 0, 'Nickname', style=style_bold)
        work_sheet.write(0, 1, 'Basic', style=style_bold)
        work_sheet.write(0, 2, 'Extra', style=style_bold)
        work_sheet.write(0, 3, 'Total', style=style_bold)

        work_sheet.col(1).width = len('Basic') * 512 + 20
        work_sheet.col(2).width = len('Extra') * 512 + 20
        work_sheet.col(3).width = len('Total') * 512 + 20
        max_width = 6
        for index, member in enumerate(match_['members']):
            score = item['scores'][member['user_id']]
            if len(member['nickname']) > max_width:
                max_width = len(member['nickname'])
            work_sheet.write(index + 1, 0, member['nickname'], style=style_border)
            work_sheet.write(index + 1, 1, round(score['basic'], 3), style=style_border)
            work_sheet.write(index + 1, 2, round(score['extra'], 3), style=style_border)
            work_sheet.write(index + 1, 3, round(score['total'], 3), style=style_border)
        work_sheet.col(0).width = max_width * 512
        work_book.save(f"match_{match_['id']}_{match_['started_at']}.xls")
