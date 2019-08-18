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
* Lista de estações [AQUI](http://www.inmet.gov.br/projetos/rede/pesquisa/lista_estacao.php)

## Como executar o projeto?

### Requerimentos
* Python 3
* Selenium
* Selenium web driver (chromedriver.exe ou outro se [sua escolha](https://www.seleniumhq.org/download/#thirdPartyDrivers))
* Beautiful Soup4

### Instalação
* Instale Git e faça o download deste projeto ([para Windows](https://gitforwindows.org/))
* Instale Python 3
* Na linha de comando, crie um VirtualEnv para seu codigo python: ```> python -m venv venv```
* Inicie seu virtualEnv com: ```> venv\Scripts\activate```
    * Se precisar desativar é só ```> venv\Scripts\deactivate```
* Após criar o VirtualEnv e inicia-lo, vamos agora instalar as dependencias deste projeto. Para isso use:
    
    ```> pip install -r requirements.txt```
* Pronto, tudo certinho para executar o projeto :)

### Executando o projeto
* A base do BDMEP possui varios tipo de consultas. Para facilitar o uso, foram criados alguns Templates:
    * __HOUR__ | Consulta de apenas alguns parametros e 3x ao dia
    * __DAY__ | Consulta de apenas alguns parametros e 2x ao dia
    * __DAYFULL__ | Consulta de todos os parametros e 3x ao dia
    * __MONTH__ | Consulta de todos os parametros e 1x ao mes

_*Recomendo utilizar ou o Template __DAYFULL__, pois é o que aparenta estar mais completo._

* Para executar use o comando abaixo:

```> python extract_data.py DAYFULL```

* O arquivo será gerado em ``` data/output_data.csv ```

_*Por enquanto não foi adicionado nem a opção de data nem a opção de nome do arquivo. Para alterar a data de extraão edite a linha 94 do extract_data.py_

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

* [Essa publicação sobre medias diarias](./documents/Comparação%20de%20médias%20diarias%20de%20temperatura.pdf) e Temperatura média compensada 



### Parâmetros 

* __Dados Horários__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_horario.php))
    * Dados de 3x ao dia

* __Dados Diários__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_diario.php))
    * Dados de 3x ao dia contendo a media diaria e mais algumas medidas calculadas

* __Dados Mensais__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_mensal.php))
    * Dados de 1x ao mes, com a media mensal

* __Atributos__:
    * mRelEstacao
    * btnProcesso
    * mRelDtInicio
    * mRelDtFim
    * mAtributos=,,,,,,,,,,,,,,,, -> Conjunto de atributos separados por virgula. Se tiver o atributo então recebe o valor 1, se não fica vazio (ex: mAtributos=1,1,1,,,,,,,,,,1,1,,,). Lista de atributos:
        * 1º Direção do Vento Predominante ([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_de_codigos.html))
        * 2º Velocidade do Vento Média (mps)
        * 3º Velocidade do Vento Máxima Média (mps)
        * 4º Evaporação do Piche (mm)
        * 5º Evapotranspiração Potencial BH (mm)
        * 6º Evapotranspiração Real BH (mm)
        * 7º Insolação Total (hs)
        * 8º Nebulosidade Média (décimos)
        * 9º Número de Dias com Precipitação (qtd)
        * 10º Precipitação Total (mm)
        * 11º Pressão Atm nível Mar Média (mbar)
        * 12º Pressão Atm Média (mbar)
        * 13º Temp Máxima Média(ºC)
        * 14º Temp Compensada Média(ºC)
        * 15º Temp Mínima Média(ºC)
        * 16º Umidade Relativa Média (%)
        * 17º Visibilidade Média (%)([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_visibilidade.html))

* Informações sobre os parametros:
    * [Bulbo Umido](https://pt.wikipedia.org/wiki/Temperatura_de_bulbo_%C3%BAmido)
    * [Bulbo Seco](https://es.wikipedia.org/wiki/Temperatura_de_bulbo_seco)





## TO DO
* [ ] Tratamento para login com usuario errado.
* [X] Exportar para arquivo
* [ ] Adicionar input para data
 


## Saiba mais

* [Organização Metereológica Mundial (OMM)](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_Meteorol%C3%B3gica_Mundial)
* [Institudo Nacional de Metereologia (INMET)](https://pt.wikipedia.org/wiki/Instituto_Nacional_de_Meteorologia)
* [Diferença entre as Estações de Observação](http://www.inmet.gov.br/html/rede_obs/rede_obs.html)
