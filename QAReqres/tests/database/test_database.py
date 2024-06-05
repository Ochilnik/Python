import pytest
from modules.common.database import Database

@pytest.mark.dbquery
def test_database_query():
    db = Database()
    print(db.test_query())

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_customers():
    db = Database()
    customers = db.get_all_customers()
#    print(customers)
#    print(customers[51][4])
    assert customers[51][4] == '202 Hoxton Street'

@pytest.mark.database
def test_check_customer():
    name = 'Martha'
    db = Database()
    customer = db.get_customer_address(name)
#    print(customer[0][1])
    assert customer[0][1] == name
    assert customer[0][3] == '194A Chain Lake Drive'
    assert customer[0][4] == 'Halifax'
    assert customer[0][6] == 'Canada'

@pytest.mark.database
def test_all_invoice_items():
    db = Database()
    items = db.get_invoice_items()
    print(items[2238])
#    print(customers[51][4])
#    assert customers[51][4] == '202 Hoxton Street'

@pytest.mark.database
def test_invoice_qnt_update():
    itemid = 22
#    qnt = 25
    db = Database()
    print(db.select_invoice_quantity(itemid))
#    db.update_invoice_quantity(itemid, qnt)
#    print(db.select_invoice_quantity(itemid))
#    water_qnt = db.select_product_qnt_by_id(2238)
#    assert water_qnt[0][0] == 25

'''
@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
'''