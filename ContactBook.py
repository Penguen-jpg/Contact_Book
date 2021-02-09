import sqlite3 as sql

# 建立連線
connection = sql.connect('C:/Users/Administrator/Desktop/Python_projects/Contact_Book/contact.db')

# 建立游標(指向連線)
cursor = connection.cursor()

# 新增聯絡人
def add(name, number, c_type):
    if c_type == "手機" and len(number) != 10:
        print("無效的手機號碼，請重新輸入")
        return False
    elif c_type == "電話" and len(number) != 9:
        print("無效的電話號碼，請重新輸入")
        return False
    else:
        sql = 'INSERT INTO CONTACT (name, number, c_type) values(?, ?, ?)'
        data = (name, number, c_type)
        cursor.execute(sql, data)
        connection.commit()
        return True

# 刪除聯絡人
def delete(number):
    cursor.execute('DELETE FROM CONTACT WHERE number=?', (number,))
    connection.commit()

# 查詢聯絡人
def query(number):
    cursor.execute('SELECT * FROM CONTACT WHERE number=?', (number, ))
    row = cursor.fetchone()
    if row == None:
        print('查不到此聯絡人')
    else:
        print(row)

# 列出所有聯絡人
def traverse():
    cursor.execute('SELECT * FROM CONTACT')
    rows = cursor.fetchall()
    # 檢查是否為空
    if not rows:
        print('目前沒有聯絡人')
    else:
        for row in rows:
            print(row)

while True:
    print('1. 新增聯絡人')
    print('2. 刪除聯絡人')
    print('3. 查詢聯絡人')
    print('4. 列出所有聯絡人')
    print('5. 退出程式')
    option = input('請輸入選項:')
    if option == '1':
        name = input('請輸入聯絡人名稱(不可空白):')
        number = input('請輸入聯絡人號碼:')
        c_type = input('請輸入聯絡人使用的裝置(電話/手機):')
        while True:
            if not add(name, number, c_type):
                number = input('請輸入聯絡人號碼:')
                c_type = input('請輸入聯絡人使用的裝置(電話/手機):')
            else:
                print('新增完成!!')
                break
    elif option == '2':
        number = input('請輸入聯絡人號碼:')
        delete(number)
        print('刪除完成!!')
    elif option == '3':
        number = input('請輸入要查詢的聯絡人號碼:')
        query(number)
    elif option == '4':
        traverse()
    elif option == '5':
        # 關閉連線
        connection.close()
        break
    print()
        
