# Projeto de Análise de Dados de Planilha do Google Sheets

Este projeto realiza a análise de dados a partir de uma planilha do Google Sheets. 

## Requisitos

Antes de executar o projeto, você precisa garantir que os seguintes requisitos estejam atendidos:

- Python 3.12.5
- Bibliotecas Python: gspread, pandas, oauth2client

## Configuração do Ambiente

### Passo 1: Instalar Dependências

Instale as bibliotecas necessárias usando pip. Execute o seguinte comando no terminal:

pip install gspread pandas oauth2client

Config na Google Cloud Console

Criar um novo projeto para atender a esse sistema.
  - Ativar as APIs necessárias.
      - Goolge Sheets API
      - Google Driver API
  - Criar credencias do tipo conta de servico
     - O json gerado será baixado automaticamente
  - Config código PYTHON
      - pege o caminho aonde esta o arquivo json e cloque no codigo "creds = ServiceAccountCredentials.from_json_keyfile_name('C:/diretorio-do-arquivo/arquivo-conta.json', scope)"
  - Execute o código "python nome-arquivo-codigo.py.

Funcionamento do codigo 
  - Primeiramente faz a autenticacao usando as credenciais da conta de servico na api do google sheets e google drive
  - Acessa a planilha e faz a leitura dos dados somente da primeira aba da planilha
  - Processa os dados
      - Calcula e faz uma filtragem de cargas carregadas atraves dos filtros mes, modalidade, veiculo e u.o
      - Valida e identifica as linhas que nao foram analisdas
      - Valida qual perfil de veiculo e mais frequentemente usado em determinada unidade
  OBS: Toda a tratativa e feita dentro de um try para realizar a tratativa de possiveis erros.
