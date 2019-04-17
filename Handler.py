from Configurations import Configurations


class Handler:
    def __init__(self):
        self.configurations = Configurations()

    def configura_motorista(self, tempo_resposta, distancia):
        self.configurations.motorista_tempo_resposta = tempo_resposta
        self.configurations.motorista_distancia = distancia

    def configura_carros(self, combustivel, quantidade):
        self.configurations.carros_combustivel = combustivel
        self.configurations.carros_quantidade = quantidade

    def configura_rotas(self, pista, quantidade):
        self.configurations.rotas_pistas = pista
        self.configurations.rotas_quantidade = quantidade

    def configura_semaforos(self, tempo):
        self.configurations.semaforos_tempo = tempo

    def configura_ambiente(self, clima):
        self.configurations.ambientes_clima = clima

    def print_configs(self):
        print("Tempo de resposta dos motoristas: " + str(self.configurations.motorista_tempo_resposta))
        print("Distancia dos motoristas: " + str(self.configurations.motorista_distancia))
        print("Combustivel dos veiculos: " + str(self.configurations.carros_combustivel))
        print("Quantidade de veiculos na simulação: " + str(self.configurations.carros_quantidade))
        print("Tipo de pista: " + str(self.configurations.rotas_pistas))
        print("Quantidade de pistas na simulação: " + str(self.configurations.rotas_quantidade))
        print("Tempo de espera dos semaforos: " + str(self.configurations.semaforos_tempo))
        print("Clima do ambiente: " + str(self.configurations.ambientes_clima))

    def calcula_impacto(self, variacao):
        # 16kg de CO2 por hora gasolina, 8kg de CO2 por hora diesel, 12kg de CO2 por hora Alcool e 10kg para GNV
        if self.configurations.carros_combustivel == 'Alcool':
            impact = variacao * self.configurations.carros_quantidade * (12/1000)
        elif self.configurations.carros_combustivel == 'Gasolina':
            impact = variacao * self.configurations.carros_quantidade * (16/1000)
        elif self.configurations.carros_combustivel == 'Diesel':
            impact = variacao * self.configurations.carros_quantidade * (8/1000)
        else:
            impact = variacao * self.configurations.carros_quantidade * (10/1000)
        return impact


