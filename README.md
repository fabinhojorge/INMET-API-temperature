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


## Virtual Enviroment Python

A pasta **venv** é o Virtual Eviroment(_venv_) do python.
O venv é um ambiente virtual que guarda todos os pacotes e requisitos do projeto. Abaixo segue as instruções de uso para iniciar o ambiente:
* Abra o terminal do Sistema operacional (Linux):
* Entre na pasta do projeto
* Digite no terminal
```shell
source venv/bin/activate
```
* Agora use tranquilamente. Todas as chamadas de scripts usadas já estarão configuradas para usar as dependencias


Os pacotes e dependências são para análise de dados, o chamado [SciPy](https://www.scipy.org/install.html):
* sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

## BDMEP Parametros


* **Dados Mensais** ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_mensal.php))
* **Dados Diarios** ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_diario.php))
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

* 

** Precisa terminar essa documentação


## Afazer
* Lista das estações: http://www.inmet.gov.br/projetos/rede/pesquisa/lista_estacao.php -> Pegar o id delas para usar como parametro de consulta
* Futuramente verificar se digitou a senha certa analisando, e voltar para pedir novamente
* Separar as classes em outros arquivos posteriormente 