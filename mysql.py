import pymysql
class Connection:
    
    def __init__(self, password, host='localhost', user='zezeon', database='csv', charset='utf8'):
        conn = pymysql.connect(host, user, password, database, charset)
        self.cur = conn.cursor()

    def set_table(self, table):
        self.table = table

    def st(self,query):
        self.cur.execute(query)
        results = self.cur.fetchall()
        widths = []
        columns = []
        tavnit = '|'
        separator = '+' 

        for cd in self.cur.description:
            widths.append(max(cd[2], len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-"+"%ss |" % (w,)
            separator += '-'*w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
        print(separator)

    def select(self, columns):
        query = 'select ' + columns + ' from ' + self.table
        self.st(query)
        
