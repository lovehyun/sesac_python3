import sqlite3

DATABASE = 'user-sample.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 미션1-1. 여기 DB로부터 가져온 내용을 dict로 하고 싶으면??
    conn.row_factory = sqlite3.Row
    return conn

def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores")
    stores = cursor.fetchall()
    conn.close()
    
    stores = [dict(r) for r in stores]

    # 미션1-2. 미션1-1을 안했다면?? 여기에서 튜플형의 데이터를 dict형으로 변환해서 반납하고 싶으면??
    # stores_dict = []
    # for s in stores:
    #     stores_dict.append({
    #         'id': s[0],
    #         'name': s[1],
    #         'type': s[2],
    #         'address': s[3]
    #     })
    # stores_dict = [{'id':s[0], 'name':s[1], 'type':s[2], 'address':s[3]} for s in stores]    
    
    return stores

def get_stores_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%', ))
    stores = cursor.fetchall()
    conn.close()
    
    stores = [dict(r) for r in stores]
    
    return stores
