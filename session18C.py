from session18A import Customer
from session18B import MongoDBHelper
from bson.objectid import ObjectId
def main():
    db = MongoDBHelper()
    customer = Customer()
    #customer.read_customer_data()

    #document = vars(customer)
    #db.insert(document)

    #query = {'phone': '+91 6677543210'}
    query = {'email': 'John@example.com'}
    #query = {'_id': ObjectId('64c35f992f3049018b374c05')}

    #db.delete(query)
    #db.fetch()
    db.fetch(query=query)
    document_data_to_update = {'name':'John Watson','age': 33}
    db.update(document_data_to_update, query)

if __name__ == "__main__":
    main()
