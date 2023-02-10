from uuid import UUID, uuid4

from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ExamplePost(Base):
    __tablename__ = "example_posts"

    id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True), primary_key=True, default=uuid4
    )
    content: Mapped[str] = mapped_column(Text())
