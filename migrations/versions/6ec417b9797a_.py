"""empty message

Revision ID: 6ec417b9797a
Revises: 
Create Date: 2023-01-26 08:45:23.224334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ec417b9797a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status',
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('status_name', sa.String(length=50), nullable=False),
    sa.Column('actions', sa.Integer(), nullable=False),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('status_id', name=op.f('pk_status'))
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('registation_date', sa.DateTime(), nullable=True),
    sa.Column('phonenumber', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('user_id', name=op.f('pk_user')),
    sa.UniqueConstraint('phonenumber', name=op.f('uq_user_phonenumber')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('account',
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('balance', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('holder_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['holder_id'], ['user.user_id'], name=op.f('fk_account_holder_id_user')),
    sa.ForeignKeyConstraint(['status_id'], ['status.status_id'], name=op.f('fk_account_status_id_status')),
    sa.PrimaryKeyConstraint('account_id', name=op.f('pk_account'))
    )
    op.create_table('task',
    sa.Column('task_id', sa.String(length=50), nullable=False),
    sa.Column('task_description', sa.String(length=50), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('initiator', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['initiator'], ['user.user_id'], name=op.f('fk_task_initiator_user')),
    sa.PrimaryKeyConstraint('task_id', name=op.f('pk_task'))
    )
    op.create_table('payment',
    sa.Column('payment_id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.String(length=50), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('transaction_date', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.account_id'], name=op.f('fk_payment_account_id_account')),
    sa.PrimaryKeyConstraint('payment_id', name=op.f('pk_payment')),
    sa.UniqueConstraint('transaction_id', name=op.f('uq_payment_transaction_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    op.drop_table('task')
    op.drop_table('account')
    op.drop_table('user')
    op.drop_table('status')
    # ### end Alembic commands ###