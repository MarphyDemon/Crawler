# 插入数据，插入之前先查询是否存在，如果存在就不再插入
    def insertData(self, my_dict):
        table = "home_list"  # 要操作的表格
        # 注意，这里查询的sql语句url=' %s '中%s的前后要有空格
        sqlExit = "SELECT url FROM home_list  WHERE url = ' %s '" % (my_dict['url'])
        res = self.cursor.execute(sqlExit)
        if res:  # res为查询到的数据条数如果大于0就代表数据已经存在
            print("数据已存在", res)
            return 0
        # 数据不存在才执行下面的插入操作
        try:
            cols = ', '.join(my_dict.keys())#用，分割
            values = '"," '.join(my_dict.values())
            sql = "INSERT INTO home_list (%s) VALUES (%s)" % (cols, '"' + values + '"')
            #拼装后的sql如下
            # INSERT INTO home_list (img_path, url, id, title) VALUES ("https://img.huxiucdn.com.jpg"," https://www.huxiu.com90.html"," 12"," ")
            try:
                result = self.cursor.execute(sql)
                insert_id = self.conn.insert_id()  # 插入成功后返回的id
                self.conn.commit()
                # 判断是否执行成功
                if result:
                    print("插入成功", insert_id)
                    return insert_id + 1
            except pymysql.Error as e:
                # 发生错误时回滚
                self.conn.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print("数据已存在，未插入数据")
                else:
                    print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))