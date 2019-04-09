from appJar import gui


class GUI:
    def __init__(self):
        self.app = gui('Simulador de Trânsito', '800x400')
        self.app.setGuiPadding(40, 40)
        self.app.setLocation('CENTER')
        self.app.setFont(16, family='Verdana')

    def main_page(self):
        self.app.startFrameStack("Pages")

        self.app.startFrame('LogIn')
        self.login_page()
        self.app.stopFrame()

        self.app.startFrame('MainMenu')
        self.main_menu()
        self.app.stopFrame()

        self.app.startFrame('Progress')
        self.app.addLabel('l10', '')
        self.app.stopFrame()

        self.app.startFrame('Saving Options')
        self.app.addLabel('l11', '')
        self.app.stopFrame()

        self.app.startFrame('Merge Searches')
        self.app.addLabel('l12', '')
        self.app.stopFrame()

        self.app.stopFrameStack()

        self.app.firstFrame('Pages')
        self.app.go()

    def login_page(self):
        self.app.setStretch('column')
        self.app.setSticky('n')
        self.app.addLabel('label_login1', 'Bem Vindo ao Simulador de Trânsito!', row=0, colspan=2)
        self.app.getLabelWidget('label_login1').config(font="Verdana 20 overstrike")
        self.app.addLabel('empty1', '', row=1)
        self.app.addLabel('label_login2', 'Entre com sua conta:', row=2, colspan=2)
        self.app.setSticky('e')
        self.app.addLabel('label_user', 'Usuário:', row=3, column=0)
        self.app.setSticky('w')
        self.app.addEntry('Entry_user', row=3, column=1)
        self.app.setSticky('e')
        self.app.addLabel('label_password', 'Senha:', row=4, column=0)
        self.app.setSticky('w')
        self.app.addSecretEntry('Entry_password', row=4, column=1)
        self.app.addLabel('empty2', '')
        self.app.setSticky('')
        self.app.addButtons(['Log In', 'Sign In'], self.press, colspan=2)

    def main_menu(self):
        self.app.setStretch('column')
        self.app.setSticky('n')
        self.app.addLabel('Label_main1', 'Configure sua Simulação:')
        self.app.addLabel('empty3', '')
        self.app.setSticky('ew')
        self.app.addButton('Configurar Motorista', self.press)
        self.app.addButton('Configurar Carros', self.press)
        self.app.addButton('Configurar Rotas', self.press)
        self.app.addButton('Configurar Semaforos', self.press)
        self.app.addButton('Configurar Ambiente', self.press)
        self.app.addLabel('empty4', '')
        self.app.setStretch('both')
        self.app.setSticky('s')
        self.app.addButton('Iniciar Simulação', self.press)

    def config_motorista(self):
        self.app.setStretch('both')
        self.app.setSticky('n')
        self.app.startSubWindow("Configurar Motorista", modal=True)
        self.app.addLabel("l1", "Tempo de Resposta (s)")
        self.app.setSticky('new')
        self.app.addScale('Quantity_scale1')
        self.app.setScaleRange('Quantity_scale1', 0, 10, 1)
        self.app.showScaleIntervals('Quantity_scale1', 2)
        self.app.showScaleValue('Quantity_scale1', True)
        self.app.setScaleRelief('Quantity_scale1', 'groove')
        self.app.setSticky('n')
        self.app.addLabel('empty5', '')
        self.app.addLabel("l2", "Distancia do Proximo Veiculo (m)")
        self.app.setSticky('new')
        self.app.addScale('Quantity_scale2')
        self.app.setScaleRange('Quantity_scale2', 1, 5, 1)
        self.app.showScaleIntervals('Quantity_scale2', 1)
        self.app.showScaleValue('Quantity_scale2', True)
        self.app.setScaleRelief('Quantity_scale2', 'groove')
        self.app.setSticky('s')
        self.app.addNamedButton('Ok', 'OK1', self.press)
        self.app.addLabel('empty6', '')
        self.app.setSize(400, 400)
        self.app.stopSubWindow()
        self.app.showSubWindow("Configurar Motorista")

    def config_carros(self):
        self.app.setStretch('column')
        self.app.setSticky('n')
        self.app.startSubWindow("Configurar Carros", modal=True)
        self.app.addLabel("l2", "SubWindow One")
        self.app.addNamedButton('Ok', 'OK2', self.press)
        self.app.setSize(400, 400)
        self.app.stopSubWindow()
        self.app.showSubWindow("Configurar Carros")

    def config_rotas(self):
        self.app.setStretch('column')
        self.app.setSticky('n')
        self.app.startSubWindow("Configurar Rotas", modal=True)
        self.app.addLabel("l3", "Configurar Rotas")
        self.app.addNamedButton('Ok', 'OK3', self.press)
        self.app.setSize(400, 400)
        self.app.stopSubWindow()
        self.app.showSubWindow("Configurar Rotas")

    def config_semaforos(self):
        self.app.setStretch('column')
        self.app.setSticky('n')
        self.app.startSubWindow("Configurar Semaforos", modal=True)
        self.app.addLabel("l4", "Configurar Semaforos")
        self.app.addNamedButton('Ok', 'OK4', self.press)
        self.app.setSize(400, 400)
        self.app.stopSubWindow()
        self.app.showSubWindow("Configurar Semaforos")

    def config_ambiente(self):
        self.app.setStretch('column')
        self.app.setSticky('n')
        self.app.startSubWindow("Configurar Ambiente", modal=True)
        self.app.addLabel("l5", "Configurar Ambiente")
        self.app.addNamedButton('Ok', 'OK5', self.press)
        self.app.setSize(400, 400)
        self.app.stopSubWindow()
        self.app.showSubWindow("Configurar Ambiente")

    def iniciar_simulacao(self):
        self.app.setStretch('column')
        self.app.setSticky('nsew')
        self.app.startSubWindow("Simulação", modal=True)
        self.app.addLabel("l6", "Simulação Rodando.")
        self.app.setSize(800, 800)
        self.app.stopSubWindow()
        self.app.showSubWindow("Simulação")

    def press(self, btn):
        if btn == 'Log In':
            if self.app.getEntry('Entry_user') == 'admin' and self.app.getEntry('Entry_password') == 'admin':
                self.app.selectFrame('Pages', num=1)
            else:
                self.app.infoBox('ERRO!', 'Senha ou Usuário Incorreto(s)!')
        elif btn == 'Configurar Motorista':
            self.config_motorista()
        elif btn == 'Configurar Carros':
            self.config_carros()
        elif btn == 'Configurar Rotas':
            self.config_rotas()
        elif btn == 'Configurar Semaforos':
            self.config_semaforos()
        elif btn == 'Configurar Ambiente':
            self.config_ambiente()
        elif btn == 'Iniciar Simulação':
            self.iniciar_simulacao()
        elif btn == 'Sign In':
            pass
        elif btn == 'OK1':
            self.app.destroySubWindow('Configurar Motorista')
        elif btn == 'OK2':
            self.app.destroySubWindow('Configurar Carros')
        elif btn == 'OK3':
            self.app.destroySubWindow('Configurar Rotas')
        elif btn == 'OK4':
            self.app.destroySubWindow('Configurar Semaforos')
        elif btn == 'OK5':
            self.app.destroySubWindow('Configurar Ambiente')
        elif btn == 'OK6':
            self.app.destroySubWindow('Simulação')
