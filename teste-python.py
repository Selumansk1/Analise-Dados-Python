import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

try:
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Portifolio/conta-service.json', scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1THsro0-yuBliIqURdzvr0gZSVfGW9YpKuSf7Nyd768w/edit?usp=sharing')

    worksheet = spreadsheet.get_worksheet(0)
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    df.columns = df.columns.str.strip()
    print("Colunas disponíveis:", df.columns)
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

    valid_data = df.dropna(subset=['Data', 'Modalidade', 'U.O', 'N .TR', 'Veículo'])
    invalid_data = df[df.isnull().any(axis=1)].copy()

    grouped_df = valid_data.groupby(['Data', 'Modalidade', 'U.O', 'Veículo']).size().reset_index(name='Quantidade de Cargas')
    sorted_df = grouped_df.sort_values(by=['Data', 'Modalidade', 'U.O', 'Veículo'])
    print("Quantidade de Cargas Carregadas:")
    print(sorted_df)

    invalid_data['Identificador'] = range(1, len(invalid_data) + 1)
    invalid_count = invalid_data.shape[0]
    print("\nLinhas Não Analisáveis:")
    print(invalid_data[['Identificador']])
    
    profile_aderente_df = valid_data.groupby(['U.O', 'Veículo']).size().reset_index(name='Quantidade')
    profile_aderente_df = profile_aderente_df.sort_values(by=['U.O', 'Quantidade'], ascending=[True, False])
    profile_aderente_df = profile_aderente_df.drop_duplicates(subset=['U.O'])

    print("\nPerfil de Veículo Aderente:")
    print(profile_aderente_df)

except gspread.exceptions.SpreadsheetNotFound as e:
    print("Erro: A planilha não foi encontrada. Verifique a URL e tente novamente.")
    print(e)
except gspread.exceptions.APIError as e:
    print("Erro: Problema ao acessar a API do Google Sheets.")
    print(e)
except FileNotFoundError as e:
    print("Erro: Arquivo de credenciais não encontrado.")
    print(e)
except ValueError as e:
    print("Erro: Problema ao processar os dados.")
    print(e)
except Exception as e:
    print("Erro inesperado:")
    print(e)
