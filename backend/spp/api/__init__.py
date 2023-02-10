from sqlalchemy import select

from spp.db import session
from spp.db.models import ExamplePost


def get():
    stmt = select(ExamplePost)
    posts = [post.content for post in session.scalars(stmt)]
    return posts
