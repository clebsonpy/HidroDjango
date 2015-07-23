
import Site.Ana.ListaDadosDB as DadosArq
import Site.Ana.Datas as Data
from Site.models import Serie_Temporal


'''
import InserirDados as inserir
import AtualizarDados as atualizar
'''
c = (2,3,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
x = DadosArq.LerArquivo(c, 'F:\\Clebson\\HidroDjango\\SiteHidro\\Site\\Ana\\Vazoes')
x.DadosAna()
lista = x.dados
Datas = Data.Datas(x.anoInicio,x.anoFim)
Datas.Rdata()
listadado = []

for i in Datas.ListaDatas:
    dataehora = Serie_Temporal(Data_e_Hora=i[1])
    dado = Serie_Temporal(Dado=i[0])
    id = Serie_Temporal(Serie_Temporal_ID=1)
    listadado.append([id, dataehora, dado])
print(listadado[1])
Serie_Temporal.objects.bulk_create(listadado)
'''
class run():
    def __init__(self, NomeBD):
        self.NomeBD = NomeBD
        self.Fonte = None
        self.dados = None
        self.CodigoANA = None
        self.DatasSerie = None
        self.Tipo_Posto = None

    def getDados(self, NomeArquivo, Fonte, Tipo_Posto):
        c = (2,3,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
         31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47)
        LerANA = DadosArq.LerArquivo(c,NomeArquivo)
        if Fonte == 'ONS':
            LerANA.DadosOns()
        elif Fonte == 'ANA':
            LerANA.DadosAna()

        anoInicio = LerANA.anoInicio
        anoFim = LerANA.anoFim
        Datas = Data.Datas(anoInicio,anoFim)
        Datas.Rdata()
        self.Tipo_Posto = Tipo_Posto
        self.dados = LerANA.dados
        self.Fonte = Fonte
        self.CodigoANA = LerANA.codigo
        self.DatasSerie = Datas.ListaDatas

listaReducao = ['Mínima', 'Máxima', 'Falha', 'Média']
listaTipoDePosto = ['Fluviométrico', 'Pluviométrico']
listaVariavel = ['Precipitação', 'Intercepção', 'Evapotranspiração', 'Infiltração', 'Escoamento']
listaUnidade = ['m³/s', 'mm', 'l/s']
listaNivelConstencia = ['Consistido', 'Bruto', 'Bruto e Consistido']
listaDiscretizacao = ['Dia', 'Mês', 'Ano']

get = run('BancoHidro')

inserir.inserirDados(listaReducao, get.NomeBD).Reducao()
inserir.inserirDados(listaVariavel, get.NomeBD).Variavel()
inserir.inserirDados(listaTipoDePosto, get.NomeBD).Tipo_Posto()
inserir.inserirDados(listaUnidade, get.NomeBD).Unidade()
inserir.inserirDados(listaNivelConstencia, get.NomeBD).Nivel_Consistencia()
inserir.inserirDados(listaDiscretizacao, get.NomeBD).Discretizacao()

for i in [['vazoes', 'ANA'],['vazoesp', 'ANA'],['xingo', 'ONS']]:
    get.getDados(i[0], i[1], 'Fluviométrico')

    inserir.inserirDados(get.Fonte, get.NomeBD).Fonte(get.Fonte)
    inserir.inserirDados(get.CodigoANA, get.NomeBD).Posto(get.Tipo_Posto, get.Fonte)
    inserir.inserirDados(get.DatasSerie, get.NomeBD).Serie_Temporal()
    atualizar.atualizaDados(get.dados, get.NomeBD).atualizarDadosSerieTemporal()


listadados = ListaDadosDB.LerArquivo(c, "vazoesp")
listadados.DadosAna()
GravaBanco.GravaBanco(listadados.dados, 'BancoHidro', 'Serie_Temporal').atualizarDados()

ListaDados = []
Posto_ID = s.Selecao('BancoHidro').lerPosto(s.Selecao('BancoHidro').lerTipoPosto('Fluviométrico'),
                                            s.Selecao('BancoHidro').lerFonte('ANA'))
Arquivo_Fonte_Data = 'ANA ' + str(datetime.datetime.now().year)
Variavel_ID = s.Selecao('BancoHidro').lerVariavel('Escoamento')
Tipo_Dado_ID = s.Selecao('BancoHidro').lerNivelConsistencia('Bruto e Consistido')
Discretizacao_ID = s.Selecao('BancoHidro').lerDiscretizacao('Dia')
Unidade_ID = s.Selecao('BancoHidro').lerUnidade('m³/s')
Serie_Temporal_ID = s.Selecao('BancoHidro').lerSerieTemporal()
ListaDados = [[Posto_ID, Arquivo_Fonte_Data, Variavel_ID, Tipo_Dado_ID, Discretizacao_ID,
              Unidade_ID,Serie_Temporal_ID]]
print(ListaDados)
GravaBanco.GravaBanco(ListaDados, 'BancoHidro', 'Serie_Original').inserirDados()


ano = anoI_e_anoF.anoI_e_anoF('vazoes.txt')
ano.anos_I_F()
listadados = Datas.Datas(ano.anoInicio, ano.anoFim)
listadados.Rdata()
GravaBanco.GravaBanco(listadados.ListaDatas,'BancoHidro','Serie_Temporal').inserirDados()
listadados = DadosArq.LerArquivo(nome_arq="xingo")
listadados.DadosOns()
GravaBanco.GravaBanco(listadados.dados, 'BancoHidro', 'Serie_Temporal').atualizarDados()

ListaDados = []
Posto_ID = selecao.Selecao('BancoHidro').lerPosto(selecao.Selecao('BancoHidro').lerTipoPosto('Fluviométrico'),
                                            selecao.Selecao('BancoHidro').lerFonte('ONS'))
Arquivo_Fonte_Data = 'ONS ' + str(datetime.datetime.now().year)
Variavel_ID = selecao.Selecao('BancoHidro').lerVariavel('Escoamento')
Tipo_Dado_ID = selecao.Selecao('BancoHidro').lerNivelConsistencia('Bruto')
Discretizacao_ID = selecao.Selecao('BancoHidro').lerDiscretizacao('Dia')
Unidade_ID = selecao.Selecao('BancoHidro').lerUnidade('m³/s')
Serie_Temporal_ID = selecao.Selecao('BancoHidro').lerSerieTemporal()
ListaDados = [[Posto_ID, Arquivo_Fonte_Data, Variavel_ID, Tipo_Dado_ID, Discretizacao_ID,
              Unidade_ID,Serie_Temporal_ID]]
print(ListaDados)

GravaBanco.GravaBanco(ListaDados, 'BancoHidro', 'Serie_Original').inserirDados()
'''