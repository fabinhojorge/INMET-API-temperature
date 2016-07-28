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



## Afazer
* Lista das estações: http://www.inmet.gov.br/projetos/rede/pesquisa/lista_estacao.php -> Pegar o id delas para sar como parametro de consulta
* Fazer logica do session cookie: Salvar a cookie em um arquivo. Ao executar o script, usar a cookie do arquivo. Se a cookie nao for mais valida, ai sim pede o usuario e a senha
* Separar as classes em outros arquivos posteriormente 