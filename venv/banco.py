import pymysql

class Banco():

    def __init__(self, host, user, senha, bd):
        self.con = pymysql.connect(""+host, ""+user, ""+senha, ""+bd)
        self.cursor = self.con.cursor()

    def insere(self, dia, disciplina, horario):
        sql = "INSERT INTO "+dia+" (disciplina, horario) VALUES ('"+disciplina+"', '"+horario+"')"
        self.executa(sql)

    def exclui(self, dia, disciplina):
        sql = "DELETE * from "+dia+" WHERE disciplina = '"+disciplina+"'"
        self.executa(sql)

    def atualiza(self, dia, disciplina, horario):
        sql = "UPDATE from "+dia+" set disciplina='"+disciplina+"', horario='"+horario+"'"
        self.executa(sql)

    def executa(self, sql):
        try:
            self.cursor.execute(sql)
            print("Deu")
            self.con.commit()

        except:
            print("Não deu")
            self.con.rollback()

        self.con.close()