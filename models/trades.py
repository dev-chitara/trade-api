import uuid
from sqlalchemy import Column, UUID, Integer, String, Date
from db_setup import Base


class Trade(Base):
    __tablename__ = "trades"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    symbol = Column(String(80))
    shares = Column(Integer)
    price = Column(Integer)
    type = Column(String(80))
    timestamp = Column(Date)

    def __str__(self):
        return f"{self.symbol} {self.shares}"