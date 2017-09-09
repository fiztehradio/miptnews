import time
from sqlalchemy import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from objs.news import News


class Database(object):
    """
    Класс для обработки сессии SQLAlchemy.
    Так же включает в себя минимальный набор методов, вызываемых в управляющем классе.
    """

    def __init__(self, obj):
        engine = create_engine(obj, echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_news(self, news):
        self.session.add(news)
        self.session.commit()

    def get_post_without_message_id(self):
        return self.session.query(News).filter(and_(News.message_id == 0,
                                                    News.publish <= int(time.mktime(time.localtime())))).all()

    def update(self, link, chat, msg_id):
        self.session.query(News).filter_by(link=link).update(
            {"chat_id": chat, "message_id": msg_id})
        self.session.commit()

    def find_link(self, link):
        if self.session.query(News).filter_by(link=link).first():
            return True
        else:
            return False
