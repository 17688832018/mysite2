import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","dbtest")
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
# cursor.execute("select version()")
# 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()
# print("数据库版本为：%s"%data)

# 使用 execute() 方法执行 SQL，如果"同事"表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE2")
# 使用预处理语句创建表 可行
# sql_create = """CREATE TABLE EMPLOYEE2 (
#          FIRST_NAME2  CHAR(20) NOT NULL,
#          LAST_NAME2  CHAR(20),
#          AGE2 INT,
#          SEX2 CHAR(1),
#          INCOME2 FLOAT )"""
# 执行sql
# cursor.execute(sql_create)
# 插入
# sql_insert = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     cursor.execute(sql_insert)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 若发生错误则回滚 回滚游标的所有操作
#     db.rollback()

# 查询  fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
# sql_select="SELECT * FROM EMPLOYEE \
#             WHERE INCOME > '%d'" % (1000)
# try:
#     # 执行SQL语句
#     cursor.execute(sql_select)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#               (fname, lname, age, sex, income))
# except:
#     print("Error: unable to fetch data")

# 修改
# sql_update = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql_update)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# 删除
# sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (99)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
# # 关闭数据库连接
# db.close()




# 另外插入写法：
# user_id = "test123"
# password = "password"
#
# cursor.execute('insert into 表名 values("%s", "%s")' % \
#              (user_id, password))
