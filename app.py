import happybase
import os
from flask import Flask, jsonify, request


app = Flask(__name__)

#Connect to the HBase database
def connect_to_hbase():
    connection = happybase.Connection(os.environ["HBASE_IP"], os.environ["HBASE_PORT"], autoconnect=False)
    connection.open()
    return connection

def bytes_to_json(byte_array):
    result = []
    for val, data in byte_array:
        item = {k.decode('utf8'): v.decode('utf8') for k, v in data.items()}
        if ('info:o_id' in item.keys()):
            result.append(item)
    return result

def items_in_order(o_id):
    connection = connect_to_hbase() 
    table = connection.table('orders')
    result = table.scan(filter="SingleColumnValueFilter ('info','o_id',=,'regexstring:" + str(o_id) + "')") 
    return bytes_to_json(list(result))

def orders_in_restaurant(rest_id):
    connection = connect_to_hbase() 
    table = connection.table('orders')
    result = table.scan(filter="SingleColumnValueFilter ('ids','r_id',=,'regexstring:" + str(rest_id) + "')") 
    return bytes_to_json(list(result)) 

statuses = ["Processing", "Pending", "Rejected", "Accepted", "ReadyForPickup", "OutForDelivery", "Delivered"]

def mark_status_on_order(row_key, status):
    if (status in statuses):
        connection = connect_to_hbase() 
        table = connection.table('orders')
        table.put(str(row_key), {b'info:state': str(status)})
    else:
        raise Exception("Wrong status type")


@app.route('/items/<o_id>', methods=['GET'])
def items_in_order_endpoint(o_id):
    return jsonify(items_in_order(o_id))

@app.route('/orders/<rest_id>', methods=['GET'])
def orders_in_restaurant_endpoint(rest_id):
    return jsonify(orders_in_restaurant(rest_id))
    
@app.route('/status', methods=['PUT'])
def mark_status_on_order_endpoint():
    data = request.get_json()
    mark_status_on_order(data.get('row_key'), data.get('status'))
    return jsonify("Status changed")


if __name__ == '__main__':
    app.run(debug=False)