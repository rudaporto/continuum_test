import sqlalchemy as sa
from sqlalchemy_continuum import make_versioned
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

SQLALCHEMY_URL = "postgresql+psycopg2://postgres:postgres@localhost:8432/postgres"

Base = declarative_base()

make_versioned(user_cls=None)

engine = sa.create_engine(SQLALCHEMY_URL)
Session = sessionmaker(bind=engine)


class Trip(Base):

    __versioned__ = {}
    __tablename__ = 'trips'

    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    payload = sa.Column(JSONB)


# after you have defined all your models, call configure_mappers:
sa.orm.configure_mappers()


def db_init():
    Base.metadata.create_all(engine)

