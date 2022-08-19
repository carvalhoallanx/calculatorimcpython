from PyQt5 import uic, QtWidgets

def limpfundverde():
    imc.LblMenorque18.setStyleSheet("background-color:rgba(255, 255, 255, 0);");
    imc.LblEntre18e24.setStyleSheet("background-color:rgba(255, 255, 255, 0);");
    imc.LblEntre25e29.setStyleSheet("background-color:rgba(255, 255, 255, 0);");
    imc.LblEntre30e39.setStyleSheet("background-color:rgba(255, 255, 255, 0);");
    imc.LblMaiorque40.setStyleSheet("background-color:rgba(255, 255, 255, 0);");

def calimc():
    Altura = float(imc.LeAltura.text())
    Peso = float(imc.LePeso.text())
    RespostaIMC = (Peso/(Altura*Altura))
    RespostaIMC2 = round(RespostaIMC,2)
    StringRespostaIMC = str(RespostaIMC2)

    if RespostaIMC <= 18.5:
        imc.LblResposta.setText(StringRespostaIMC)
        limpfundverde();
        imc.LblMenorque18.setStyleSheet("background-color:#ebfdea");

    elif RespostaIMC > 18.5 and RespostaIMC <= 24.9:
        imc.LblResposta.setText(StringRespostaIMC)
        limpfundverde();
        imc.LblEntre18e24.setStyleSheet("background-color:#ebfdea");

    elif RespostaIMC >= 25.0 and RespostaIMC <= 29.9:
        imc.LblResposta.setText(StringRespostaIMC)
        limpfundverde();
        imc.LblEntre25e29.setStyleSheet("background-color:#ebfdea");

    elif RespostaIMC >= 30.0 and RespostaIMC <= 39.9:
        imc.LblResposta.setText(StringRespostaIMC)
        limpfundverde();
        imc.LblEntre30e39.setStyleSheet("background-color:#ebfdea");

    elif RespostaIMC >= 40:
        imc.LblResposta.setText(StringRespostaIMC)
        limpfundverde();
        imc.LblMaiorque40.setStyleSheet("background-color:#ebfdea");


def limpa():
    #limpar os campos a baixo
    imc.LeAltura.clear();
    imc.LePeso.clear();
    imc.LblResposta.clear();
    limpfundverde();

app=QtWidgets.QApplication([])
imc=uic.loadUi("imc.ui")
imc.BtnCalcular.clicked.connect(calimc)
imc.BtnLimpar.clicked.connect(limpa)
imc.show()
app.exec()