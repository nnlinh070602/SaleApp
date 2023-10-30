def get_categories():
    return [{
        "id": 1,
        "name": "Moblie"
    },{
        "id":2,
        "name": "Table"
    }]

def get_products(kw):
    products = [{
        "id": 1,
        "name": "Iphone 13",
        "price": 200000000,
        "image":"https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQK3RX7pNOblEt4pI1uN4tjJk3IDJsrBnO1jqh5jwCf2CmXhGuSr2PZH7182unrogd7AL--3F5hLQge4oXRRUgHz0wNSMnsHWDN2WClV78e&usqp=CAE"
    },{
        "id": 2,
        "name": "Galaxy 14",
        "price": 200000000,
        "image":"https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQK3RX7pNOblEt4pI1uN4tjJk3IDJsrBnO1jqh5jwCf2CmXhGuSr2PZH7182unrogd7AL--3F5hLQge4oXRRUgHz0wNSMnsHWDN2WClV78e&usqp=CAE"
    },{
        "id": 3,
        "name": "Iphone 13",
        "price": 200000000,
        "image":"https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQK3RX7pNOblEt4pI1uN4tjJk3IDJsrBnO1jqh5jwCf2CmXhGuSr2PZH7182unrogd7AL--3F5hLQge4oXRRUgHz0wNSMnsHWDN2WClV78e&usqp=CAE"
    },{
        "id": 4,
        "name": "Iphone 13",
        "price": 200000000,
        "image":"https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQK3RX7pNOblEt4pI1uN4tjJk3IDJsrBnO1jqh5jwCf2CmXhGuSr2PZH7182unrogd7AL--3F5hLQge4oXRRUgHz0wNSMnsHWDN2WClV78e&usqp=CAE"
    },{
        "id": 5,
        "name": "Iphone 13",
        "price": 200000000,
        "image":"https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQK3RX7pNOblEt4pI1uN4tjJk3IDJsrBnO1jqh5jwCf2CmXhGuSr2PZH7182unrogd7AL--3F5hLQge4oXRRUgHz0wNSMnsHWDN2WClV78e&usqp=CAE"
    },{
        "id": 1,
        "name": "Iphone 13",
        "price": 200000000,
        "image":"https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQK3RX7pNOblEt4pI1uN4tjJk3IDJsrBnO1jqh5jwCf2CmXhGuSr2PZH7182unrogd7AL--3F5hLQge4oXRRUgHz0wNSMnsHWDN2WClV78e&usqp=CAE"
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products