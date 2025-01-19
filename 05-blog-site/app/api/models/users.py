from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Text, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(254), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(1024))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    # Relationships
    posts: Mapped[List["Post"]] = relationship("Post", back_populates="author")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="author")

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    published: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                               onupdate=text("TIMEZONE('utc', now())"))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Relationships
    author: Mapped["User"] = relationship("User", back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="post")
    categories: Mapped[List["Category"]] = relationship("Category",
                                                      secondary="post_categories",
                                                      back_populates="posts")
    tags: Mapped[List["Tag"]] = relationship("Tag",
                                           secondary="post_tags",
                                           back_populates="posts")

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("comments.id"), nullable=True)

    # Relationships
    post: Mapped["Post"] = relationship("Post", back_populates="comments")
    author: Mapped["User"] = relationship("User", back_populates="comments")
    replies: Mapped[List["Comment"]] = relationship("Comment",
                                                  backref=relationship("parent", remote_side=[id]),
                                                  cascade="all, delete-orphan")

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relationships
    posts: Mapped[List["Post"]] = relationship("Post",
                                             secondary="post_categories",
                                             back_populates="categories")

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    slug: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    # Relationships
    posts: Mapped[List["Post"]] = relationship("Post",
                                             secondary="post_tags",
                                             back_populates="tags")

# Association tables
class PostCategory(Base):
    __tablename__ = "post_categories"

    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)

class PostTag(Base):
    __tablename__ = "post_tags"

    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)