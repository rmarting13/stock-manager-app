from log.logger_base import log
from db_context.pool_cursor import Cursor
from models.product import Product


class ProductDao:
    """
    DAO: Database access object for a Product instance entity that provides
    useful methods to perform a basic CRUD.
    """
    _SELECT = 'SELECT * FROM products ORDER BY id_product'
    _INSERT = 'INSERT INTO products (description, price, brand) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE products SET description=%s, price=%s, brand=%s WHERE id_product=%s'
    _DELETE = 'DELETE FROM products WHERE id_product=%s'

    @classmethod
    def select(cls):
        with Cursor() as cursor:
            log.debug('Selecting products')
            cursor.execute(cls._SELECT)
            rows = cursor.fetchall()
            products = []
            for reg in rows:
                products.append(Product(reg[0], reg[1], reg[2], reg[3]))
            return products

    @classmethod
    def insert(cls, product:Product):
        with Cursor() as cursor:
            log.debug(f'Inserting product: {product}')
            values = (product.description, product.price, product.brand)
            cursor.execute(cls._INSERT, values)
            return cursor.rowcount

    @classmethod
    def update(cls, product:Product):
        with Cursor() as cursor:
            log.debug(f'Updating product: {product}')
            values = (product.description, product.price, product.brand, product.code)
            cursor.execute(cls._UPDATE, values)
            return cursor.rowcount

    @classmethod
    def delete(cls, product:Product):
        with Cursor() as cursor:
            log.debug(f'Deleting product: {product}')
            values = (product.code,)
            cursor.execute(cls._DELETE, values)
            return cursor.rowcount

if __name__ == '__main__':
    # INSERT
    # p1 = Product(description ='Coca 3lt',
    #              price=1300,
    #              brand='Coca-Cola')
    # p2 = Product(description='CERVEZA RUBIA 1200ml',
    #              price=950,
    #              brand='QUILMES')
    # inserted = ProductDao.insert(p2)
    # log.debug(f'Inserted products: {inserted}')

    # UPDATE
    p1 = Product(code=1,
                 description ='Coca 2500ml',
                 price=850,
                 brand='Coca-Cola')
    updated = ProductDao.update(p1)
    log.debug(f'Updated products: {updated}')
    # DELETE
