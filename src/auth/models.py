"""Модели для модуля аутентификации"""

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    """Модель пользователя (User)"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True, default="")
    image: Mapped[str | None] = mapped_column(String(255), nullable=True, default="")
