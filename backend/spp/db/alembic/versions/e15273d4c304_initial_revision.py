"""Initial revision

Revision ID: e15273d4c304
Revises:
Create Date: 2023-02-10 18:51:11.569593

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e15273d4c304"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "example_posts",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("example_posts")
    # ### end Alembic commands ###
