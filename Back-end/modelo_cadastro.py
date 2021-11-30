from config import * 
# modelos

class Medico(db.Model):

    #Atributos do médico
    id_medico = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(55))
    sobrenome = db.Column(db.String(55))
    crm = db.Column(db.String(24))
    

    

    #Expressão da classe em forma de texto
    def __str__(self):
        return f"{self.id_medico}, {self.nome}, {self.sobrenome}, {self.crm}"

    #Expressao da classe no formato json
    def json(self):
        return{
            "id_medico": self.id_medico,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "crm": self.crm
        }


class Paciente(db.Model):
    #Atributos do paciente
    id_paciente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    sobrenome = db.Column(db.String(255))
    
    #Essa parte está em comentário para dar uma agilizada na hora de testar, e não ter que botar muitas informações por agora
    cpf = db.Column(db.String(11))
    data_nasc = db.Column(db.String(255))
    sexo =  db.Column(db.String(10))
    e_civil = db.Column(db.String(50))
    cns = db.Column(db.String(255))
    
    #Endereço 
    cep =  db.Column(db.String(50))
    logradouro =  db.Column(db.String(255))
    numero = db.Column(db.String(5))
    bairro = db.Column(db.String(55))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(30))

    #contato
    telefone1 = db.Column(db.String(255))
    telefone2 = db.Column(db.String(255))
    email = db.Column(db.String(255))
    

    #login
    usuario = db.Column(db.String(255))
    senha = db.Column(db.String(255))



    

    #Método para expressar o paciente em forma de texto
    def __str__(self):
        return f"{self.id_paciente}, {self.nome}, {self.sobrenome} ,  {self.email} "

    #Expressao da classe no formato json
    def json(self):
        return{
            "id_paciente": self.id_paciente,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "senha": self.senha
        }
        
class Consulta(db.Model):
    id_consulta = db.Column(db.Integer, primary_key=True)
    dataConsulta = db.Column(db.String(255)) # dataConsulta da consulta
    motivo = db.Column(db.String(255)) # motivo: consulta por dor de cabeça, de barriga(sitomas)

    # atributo de chave estrangeira
    paciente_id_consulta = db.Column(db.Integer, db.ForeignKey(Paciente.id_paciente), nullable=False)
    medico_id_consulta = db.Column(db.Integer, db.ForeignKey(Medico.id_medico), nullable=False)

    # atributo de relacionamento, para acesso aos dados via objeto
    paciente = db.relationship("Paciente", foreign_keys=paciente_id_consulta)    
    medico = db.relationship("Medico", foreign_keys=medico_id_consulta)    

    
    def __str__(self): 
        # expressão da classe em forma de texto
        return f"{self.id_consulta}, {self.dataConsulta}, {self.motivo}, {self.paciente}, {self.medico} " 

    def strestiloso(self):
        # estiloso
        return f"O paciente {self.paciente.nome} tem uma consulta marcado para o dia \
            {self.dataConsulta} com o médico {self.medico.nome} devido à {self.motivo}."


    def json(self):
        # expressao da classe no formato json
        return {
            "id_consulta": self.id_consulta,
            "dataConsulta": self.dataConsulta,
            "motivo": self.motivo,
            "paciente_id_consulta": self.paciente_id_consulta,
            "paciente": self.paciente.json(),
            "medico_id_consulta": self.medico_id_consulta,
            "medico": self.medico.json()
        }

"""
*Data da realização do exame	
*Médico solicitante	
*TipoExame do exame	
*Resultado do exame	
*Data da consulta em que foi solicitado
"""
class Exame(db.Model):
    id_exame = db.Column(db.Integer, primary_key=True)
    dataExame = db.Column(db.String(254))
    tipoExame = db.Column(db.String(254))
    
    
    
    paciente_id_exame = db.Column(db.Integer, db.ForeignKey(Paciente.id_paciente), nullable=False)
    medico_id_exame = db.Column(db.Integer, db.ForeignKey(Medico.id_medico), nullable=False)
    consulta_id_exame = db.Column(db.Integer, db.ForeignKey(Consulta.id_consulta), nullable=False)
    
    paciente = db.relationship("Paciente", foreign_keys=paciente_id_exame)    
    medico = db.relationship("Medico", foreign_keys=medico_id_exame)    
    consulta = db.relationship("Consulta", foreign_keys=consulta_id_exame)    
    
    resultadoExame = db.Column(db.String(254))

    
    def __str__(self): 
        # expressão da classe em forma de texto
        return f"{self.id_exame}, {self.dataExame}, {self.paciente.nome} {self.paciente.sobrenome},\
        {self.consulta.dataConsulta}, {self.consulta.medico},{self.tipoExame}, {self.resultadoExame}" 




    def json(self):
        # expressao da classe no formato json
        return {
            "id_exame": self.id_exame,
            "dataExame": self.dataExame,
            "tipoExame": self.tipoExame,
            "paciente": self.paciente.json(),
            "medico": self.medico.json(),
            "consulta": self.consulta.json(),
            "resultadoExame": self.resultadoExame
        }
        """return {
            "id_exame": self.id_exame,
            "dataExame": self.dataExame,
            "paciente_id_exame": self.paciente_id_exame,
            "paciente": self.paciente.json(),
            "medico_id_exame": self.medico_id_exame,
            "medico": self.medico.json(),
            "consulta_id_exame": self.consulta_id_exame,
            #"consulta": self.consulta.json(),
            "resultadoExame": self.resultadoExame
        }"""

"""
class Exame(db.Model):
    id_exame = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254)) # nome do exame
    unidade = db.Column(db.String(254)) # unidade de medida
    vr = db.Column(db.String(254)) # valores de referência
    paciente_id_exame = db.Column(db.Integer, db.ForeignKey(Paciente.id), nullable=False)
    paciente = db.relationship("Paciente")
    def __str__(self):
        return f"{self.nome} [{self.id_exame}], unidade={self.unidade} ({self.vr})"  

    def json(self):
        return {
            "id_exame":self.id_exame,
            "nome":self.nome,
            "unidade":self.unidade,
            "vr":self.vr,
            "paciente_id_exame":self.paciente_id_exame,
            "paciente":self.paciente.json()
            
        }
    

class ExameRealizado(db.Model):
    id_exame = db.Column(db.Integer, primary_key=True)
    #dataExame = db.Column(db.String(254)) # data do exame - relacao
    data = db.Column(db.Integer, db.ForeignKey(Paciente.id), nullable=False)
    resultado = db.Column(db.String(254)) # apenas o valor
    exame_id =  db.Column(db.Integer, db.ForeignKey(Exame.id), nullable=False)
    exame = db.relationship("Exame")

    def __str__(self): # expressão da classe em forma de texto
        return f"{self.data}, {self.resultado}, {self.exame}""
             

    def json(self):
        return {
            "id":self.id,
            "data":self.data,
            "resultado":self.resultado,
            "exame_id":self.exame_id,
            "exame":self.exame.json()
        }
"""


#Testes das classes
if __name__ == "__main__":
    #Apaga o arquivo .bd, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    #Cria as tabelas
    db.create_all()

    #Teste da classe Pacienteca
    paciente3 = Paciente(nome = "Benlove", sobrenome = "Anelus", email="johnnydinheiro@gmail.com", senha = "8956")
    paciente2 = Paciente(nome = "Gabriel", sobrenome = "Speckart", email="espiga@gmail.com", senha = "5421")
    paciente1 = Paciente(nome = "Carlos", sobrenome = "Landeira", email="ferrarigol123@gmail.com", senha = "1234")
    
    #Persistir
    db.session.add(paciente1)
    db.session.add(paciente2)
    db.session.add(paciente3)
    db.session.commit()


    #Teste da classe Medico

    medico1 = Medico(nome = "Paulo Cesar", sobrenome = "McCartney", crm = "123456-78/SC")
    medico2 = Medico(nome = "João Barra", sobrenome = "Lennon", crm = "123456-78/SC")
    medico3 = Medico(nome = "Jorge Santos", sobrenome = "Harrison", crm = "123456-78/SC")
    
    #Persistir
    db.session.add(medico1)
    db.session.add(medico2)
    db.session.add(medico3)
    db.session.commit()



    # teste da classe Consulta

    consulta1 = Consulta(dataConsulta="04/08/2021", motivo= "dor no ouvido esquerdo", paciente=paciente1, medico=medico1)
    consulta2 = Consulta(dataConsulta="06/09/2021", motivo="dor no joelho", paciente=paciente2, medico=medico2)
    consulta3 = Consulta(dataConsulta="07/10/2021", motivo="dor nas costas", paciente=paciente3, medico=medico3)

    #Persistir
    db.session.add(consulta1)
    db.session.add(consulta2)
    db.session.add(consulta3)
    db.session.commit()
    print(f"\nDetalhado: {consulta1.strestiloso()}")
    

    

    #teste marcar exame 
    exame1 = Exame(dataExame="04/08/2021", paciente= paciente1, consulta=consulta1, medico=medico1, tipoExame="Sangue", resultadoExame = "1ML 300Kwh")
    exame2 = Exame(dataExame="04/08/2021", paciente= paciente1, consulta=consulta2, medico=medico2, tipoExame="Sangue",resultadoExame = "1ML 300Kwh")
    db.session.add(exame1)
    db.session.add(exame2)
    
    db.session.commit()
    print(exame1)
    print(exame2)
    

    """
    print all in a class
    pacientes = db.session.query(Paciente).all()
    for paciente in pacientes:
        print(paciente.nome)
    """

