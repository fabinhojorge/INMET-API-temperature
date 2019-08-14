
_Este projeto esta em fase de refatoração. Será alterado para Python 3 e criado um crawler usando Selenium_


# INMET-API-temperatura
API para extrair os dados __históricos__ de temperatura da Base do INMET

## Descrição
Os dados são da base __BDMEP - Banco de Dados Meteorológicos para Ensino e Pesquisa__. São dados históricos, a partir de 1961 extraidos de estações __convencionais__ ([link](http://www.inmet.gov.br/portal/index.php?r=bdmep/bdmep)).

Os dados do BDMEP são dados históricos e não em tempo real, ou seja, as vezes só estão disponíveis dados anteriores a 1~3 meses.

Um pré requisito para acessar a base é ter cadastro no BDMEP. Veja a sessão de links abaixo.

## Links

* Pagina Inicial do [INMET](http://www.inmet.gov.br/)
* Pagina dos dados [BDMEP](http://www.inmet.gov.br/portal/index.php?r=bdmep/bdmep)
* Caso ainda não possua cadastro para consulta da base BDMEP, acesse [AQUI](http://www.inmet.gov.br/projetos/rede/pesquisa/cad_senha.php)
* Para fazer o login e ver os dados no site acesse [AQUI](http://www.inmet.gov.br/projetos/rede/pesquisa/inicio.php)
* Tabela de código de ventos [AQUI](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_de_codigos.html)
* Lista de estações [AQUI] (http://www.inmet.gov.br/projetos/rede/pesquisa/lista_estacao.php)

## Como executar o projeto?

_--TBD--_

## Sobre o BDMEP

### Detalhes importantes 

Um detalhe importante é que a base do BDMEP são dados de estações __"Convencionais"__. Existem dois tipos de estações:
* __Convêncional__: É composta de vários sensores isolados que registram continuamente os parâmetros meteorológicos (pressão, temperatura, etc..), que são lidos e anotados por um observador (humano ou sistema) a cada intervalo de tempo ([link](http://www.inmet.gov.br/portal/index.php?r=estacoes/estacoesConvencionais)). 
* __Automática__: É composta de uma unidade de memória central ("data logger"), ligada a vários sensores meteorológicos, e que integra os valores observados minuto a minuto e os disponibiliza automaticamente a cada hora ([link](http://www.inmet.gov.br/portal/index.php?r=estacoes/estacoesAutomaticas)).


Então, para neste projeto estamos usando os dados Convêncionais.

As observações ocorrem todos os dias as 0900, 1500 e 2100 (UTC-3).
 
A formula usada para o cálculo da Temperatura média compensada (TC) é:
 
    TC = ( T12 + 2*T0 + T_(min) + T_(max) ) / 5



### Documentos Importantes
* [Esse documento](http://www.inmet.gov.br/webcdp/climatologia/normais/imagens/normais/textos/metodologia.pdf) que explica a metodologia utilizada para construir a base.

* [Essa publicação sobre medias diarias](./documentos/Comparação%20de%20médias%20diarias%20de%20temperatura.pdf) e Temperatura média compensada 



### Parâmetros 

* __Dados Horários__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_horario.php))
    * Dados de 3x ao dia

* __Dados Diários__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_diario.php))
    * Dados de 3x ao dia contendo a media diaria e mais algumas medidas calculadas

* __Dados Mensais__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_mensal.php))
    * Dados de 1x ao mes, com a media mensal

* __Atributos__:
    1. mRelEstacao
    1. btnProcesso
    1. mRelDtInicio
    1. mRelDtFim
    1. mAtributos=,,,,,,,,,,,,,,,, -> Conjunto de atributos separados por virgula. Se tiver o atributo então recebe o valor 1, se não fica vazio (ex: mAtributos=1,1,1,,,,,,,,,,1,1,,,). Lista de atributos:
        2. 1º Direção do Vento Predominante ([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_de_codigos.html))
        2. 2º Velocidade do Vento Média (mps)
        2. 3º Velocidade do Vento Máxima Média (mps)
        2. 4º Evaporação do Piche (mm)
        2. 5º Evapotranspiração Potencial BH (mm)
        2. 6º Evapotranspiração Real BH (mm)
        2. 7º Insolação Total (hs)
        2. 8º Nebulosidade Média (décimos)
        2. 9º Número de Dias com Precipitação (qtd)
        2. 10º Precipitação Total (mm)
        2. 11º Pressão Atm nível Mar Média (mbar)
        2. 12º Pressão Atm Média (mbar)
        2. 13º Temp Máxima Média(ºC)
        2. 14º Temp Compensada Média(ºC)
        2. 15º Temp Mínima Média(ºC)
        2. 16º Umidade Relativa Média (%)
        2. 17º Visibilidade Média (%)([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_visibilidade.html))

* Informações sobre os parametros:
    * [Bulbo Umido](https://pt.wikipedia.org/wiki/Temperatura_de_bulbo_%C3%BAmido)
    * [Bulbo Seco](https://es.wikipedia.org/wiki/Temperatura_de_bulbo_seco)





## TO DO
* [ ] Lista das estações: http://www.inmet.gov.br/projetos/rede/pesquisa/lista_estacao.php -> Pegar o id delas para usar como parametro de consulta -> Tem Estações que não estão nessa lista. Existem estações de aeroportos como a ID 82022. Checar depois em um range de 82000 até 84000. Precisa modificar um pouco para pegar os dados de aeroporto porque tem mais 1 hifen.

* [ ] 


## Saiba mais

* [Organização Metereológica Mundial (OMM)](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_Meteorol%C3%B3gica_Mundial)
* [Institudo Nacional de Metereologia (INMET)](https://pt.wikipedia.org/wiki/Instituto_Nacional_de_Meteorologia)
* [Diferença entre as Estações de Observação](http://www.inmet.gov.br/html/rede_obs/rede_obs.html)
