from sqlalchemy import Column, Integer, String
from database import Base


class StudentDB(Base):

    __tablename__ = "students"


    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    department = Column(String)

    contact_number = Column(String, unique=True)

    fathers_name = Column(String)

    mothers_name = Column(String)
