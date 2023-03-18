import calendar
from datetime import datetime, timedelta
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

calendar_callback = CallbackData('simple_calendar', 'action', 'year', 'month', 'day')


class SimpleCalendar:
    MONTHS = [
        'Январь', 'Февраль',
        'Март', 'Апрель',
        'Май', 'Июнь',
        'Июль', 'Август',
        'Cентябрь', 'Октябрь',
        'Ноябрь', 'Декабрь'
    ]
    WEEK_DAYS = ['Пн',
                 'Вт',
                 'Ср',
                 'Чт',
                 'Пт',
                 'Сб',
                 'Вс']
    async def start_calendar(self,
                             year: int = datetime.now().year,
                             month: int = datetime.now().month
                             ) -> InlineKeyboardMarkup:
        """
            Создает клавиатуру с указанным годом и месяцем
        :param year: Год,для календаря.Если None,то равен текущему году
        :param month: Месяц,для календаря.Если None,то равен текущему месяцему
        :return: InlineKeyboardMarkup обьект с календарем
        """
        inline_kb = InlineKeyboardMarkup(row_width=7)
        ignore_callback = calendar_callback.new('IGNORE',year,month)

        """Первая строка - Месяц и Год"""
        inline_kb.row()

        inline_kb.insert(InlineKeyboardMarkup(
            '<<',
            callback_data = calendar_callback.new('PREV-YEAR',year,month,1)
            )
        )

        str_date = str(self.MONTHS[month - 1])
        inline_kb.insert(InlineKeyboardButton(
            f'{str_date} {str(year)}',
            callback_data=ignore_callback
        ))

        inline_kb.insert(InlineKeyboardMarkup(
            '>>',
            callback_data = calendar_callback.new('NEXT-YEAR',year,month,1)
            )
        )
        """Вторая строка - дни недели"""
        inline_kb.row()

        for day in self.WEEK_DAYS:
            inline_kb.insert(
                InlineKeyboardButton(day,callback_data=ignore_callback
            ))
        """Основные строки - дни месяца"""
        month_calendar = calendar.monthcalendar(year,month)
        for week in month_calendar:
            inline_kb.row()
            for day in week:
                if day == 0:
                    inline_kb.insert(InlineKeyboardButton(
                        ' ',
                        callback_data=ignore_callback
                    ))
                    continue
                inline_kb.insert(InlineKeyboardButton(
                    str(day),
                    callback_data=calendar_callback.new('DAY',year,month,day)
                ))



