import requests

class Extract:
    def __init__(self):
        pass

    def pix(self):
        url = "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='202011'&$top=100&$format=json&$select=AnoMes,Municipio_Ibge,Municipio,Estado_Ibge,Estado,VL_PagadorPF,QT_PagadorPF,VL_RecebedorPF"
        r = requests.get(url)
        data = r.json()
        return data
