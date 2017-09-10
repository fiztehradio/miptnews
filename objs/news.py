import base64
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class News(Base):
    """
    Класс, описывающий объект новости. Так же, осуществляется взаимодействие с БД.
    Описание полей таблицы ниже.
    """
    __tablename__ = 'miptnews'
    id = Column(Integer, primary_key=True)  # Порядковый номер новости
    # Текст (Заголовок), который будет отправлен в сообщении
    text = Column(String)
    # Ссылка на статью на сайте. Так же отправляется в сообщении
    link = Column(String)
    date = Column(Integer)
    # Дата появления новости на сайте. Носит Чисто информационный характер. UNIX_TIME.
    publish = Column(Integer)
    # Планируемая дата публикации. Сообщение будет отправлено НЕ РАНЬШЕ этой даты. UNIX_TIME.
    chat_id = Column(Integer)
    # Информационный столбец. В данной версии функциональной нагрузки не несет.
    message_id = Column(Integer)
    # Информационный столбец. В данной версии функциональной нагрузки не несет.

    def __init__(self, text, link, date, publish=0, chat_id=0, message_id=0):
        self.link = link
        self.text = text
        self.date = date
        self.publish = publish
        self.chat_id = chat_id
        self.message_id = message_id

    def _keys(self):
        return self.text, self.link

    def __eq__(self, other):
        return self._keys() == other._keys()

    def __hash__(self):
        return hash(self._keys())

    def __repr__(self):
        return "<News ('%s','%s', %s)>" % (base64.b64decode(self.text).decode(),
                                           base64.b64decode(
                                               self.link).decode(),
                                           datetime.fromtimestamp(self.publish))
        # Для зрительного восприятия данные декодируется
