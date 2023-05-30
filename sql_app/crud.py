import datetime

from sqlalchemy.orm import Session, joinedload

from sql_app.schemas import CategoryCreate, ProductCreate
from sql_app.models import DBCategory, DBProduct


def get_all_categories(db: Session) -> list[DBCategory]:
    return db.query(DBCategory).all()


def create_category(db: Session, category: CategoryCreate) -> DBCategory:
    db_category = DBCategory(
        name=category.name,
        description=category.description
    )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def get_all_products(db: Session) -> list[DBProduct]:
    return db.query(DBProduct).options(joinedload(DBProduct.category)).all()


def create_product(db: Session, product: ProductCreate) -> DBProduct:
    db_product = DBProduct(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
        created_at=product.created_at or datetime.datetime.utcnow(),
        category_id=product.category_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
