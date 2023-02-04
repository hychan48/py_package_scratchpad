import os.path
import unittest

# https://pypi.org/project/SQLAlchemy/

# Quick start
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html


from sqlalchemy.orm import Session
from sqlalchemy import select
# 1. Declare class / model
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# Unit Test Here
class AlchemyClientOnly(unittest.TestCase):
    def setUp(self):
        from sqlalchemy import create_engine
        print('setUp engine')
        from pathlib import Path
        # sqlite_path = "sqlite://"+str(Path(__file__).parent.joinpath("sqlite3.db").as_posix())
        # sqlite_path = "sqlite:////" + os.getcwd() + '\\dev\\demo1.db' # it's relative path i think
        # 3 slashes relative to getcwd
        sqlite_path = "sqlite:///sqlite\\demo.db"  # it's relative path i think
        # sqlite_path = "sqlite:////" + os.getcwd() + '\\dev\\cards.cdb'
        print(sqlite_path)
        # with open(sqlite_path) as my_file:
        #     print(my_file.read())
        # todo google how to do window path on python
        # self.engine = create_engine(sqlite_path, echo=True)
        self.engine = create_engine(sqlite_path, echo=False)
        # self.engine = create_engine("sqlite://", echo=False)

        # Base.metadata.create_all(self.engine)

        self.assertEqual(True, True)  # add assertion here

    def test_run_raw_query(self):
        from sqlalchemy.sql import text

        with self.engine.connect() as con:
            str_query = "select sqlite_version();"
            str_query = "select * from sqlite_master;"

            cursorResult = con.execute(text(str_query))
            i = 0
            for row in cursorResult:
                print(row)
                i += 1
            print(i) # Count

    def test_simple_query(self):
        engine = self.engine
        session = Session(engine)
        stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
        i = 0
        for user in session.scalars(stmt):
            print(user)
            i += 1
        print(i)


if __name__ == '__main__':
    unittest.main()
