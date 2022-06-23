import mysql.connector
con = mysql.connector.connect(host='us-cdbr-east-05.cleardb.net',database='heroku_5f43538c673bfde',user='b2c05faf4c2dfd',password='f3f5d418')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")
