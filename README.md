# INMET-API-temperatura
API para dados de temperatura da Base do INMET


## Descrição
Os dados são captados do projeto **BDMEP - Banco de Dados Meteorológicos para Ensino e Pesquisa**. 
Esse projeto tem o objetivo de criar uma interface para capturar os dados da base de dados e exporta-los para arquivos _.csv_


## Links

* Pagina Inicial do [INMET](http://www.inmet.gov.br/)
* Pagina dos dados [BDMEP](http://www.inmet.gov.br/portal/index.php?r=bdmep/bdmep)
* Caso ainda não possua cadastro para consulta da base BDMEP, acesse [AQUI](http://www.inmet.gov.br/projetos/rede/pesquisa/cad_senha.php)
* Para fazer o login e ver os dados no site acesse [AQUI](http://www.inmet.gov.br/projetos/rede/pesquisa/inicio.php)


## BDMEP Parametros

### Importante observar [esse documento](http://www.inmet.gov.br/webcdp/climatologia/normais/imagens/normais/textos/metodologia.pdf)

### Importante observar [Essa publicação sobre medias diarias](http://www.cbmet.com/cbm-files/13-9060ba328e42e419c5472c95d37020ec.pdf)
* A formula usada para o calcul é: TC = ( T12 + 2*T0 + T_(min) + T_(max) ) / 5

As observações ocorrem todos os dias as 0900, 1500 e 2100 (UTC-3)


* **Dados Diarios** ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/mapas_c_horario.php))
    * Dados de 3x ao dia
* **Dados Mensais** ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_mensal.php))
    * Dados de 3x ao dia contendo a media diaria e mais algumas medidas [USAR]
* **Dados Diarios** ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_diario.php))
    * Dados de 1x ao mes, com a media mensal
* Atributos:
    1. mRelEstacao
    1. btnProcesso
    1. mRelDtInicio
    1. mRelDtFim
    1. mAtributos=,,,,,,,,,,,,,,,, -> Conjunto de atributos separados por virgula. Se tiver o atributo então recebe o valor 1, se não fica vazio. Lista de atributos:
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

** Precisa terminar essa documentação


## Afazer
* Lista das estações: http://www.inmet.gov.br/projetos/rede/pesquisa/lista_estacao.php -> Pegar o id delas para usar como parametro de consulta -> Tem Estações que não estão nessa lista. Existem estações de aeroportos como a ID 82022. Checar depois em um range de 82000 até 84000. Precisa modificar um pouco para pegar os dados de aeroporto porque tem mais 1 hifen.
* Futuramente verificar se digitou a senha certa analisando, e voltar para pedir novamente
* Separar as classes em outros arquivos posteriormente
* Criar consulta a URL diaria de todas as bases. Armazenar esses dados. Analizar a possibilidade de banco MongoDB.


## Saiba mais

* [Organização Metereológica Mundial (OMM)](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_Meteorol%C3%B3gica_Mundial)
* [Institudo Nacional de Metereologia (INMET)](https://pt.wikipedia.org/wiki/Instituto_Nacional_de_Meteorologia)
* [Diferença entre as Estações de Observação](http://www.inmet.gov.br/html/rede_obs/rede_obs.html)