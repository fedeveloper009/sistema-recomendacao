from src.processador import carregar_dados, processar_dados, unir_tabelas
from src.recomendador import recomendar_filme

def main():
    print("=== A iniciar o Sistema de Recomendação de Filmes ===")
    
    # 1. Carregar os dados usando a função do módulo
    df_avaliacoes = carregar_dados('data/avaliacoes.csv', sep=',')
    df_usuarios = carregar_dados('data/usuarios.csv', sep=',')
    df_filmes = carregar_dados('data/filmes.csv', sep=',')
    
    # Verificar se a carga ocorreu bem
    if any(df is None for df in [df_avaliacoes, df_usuarios, df_filmes]):
        print("Erro crítico: Falha ao carregar um ou mais ficheiros.")
        return

    # 2. Processar (limpar) cada DataFrame
    df_avaliacoes = processar_dados(df_avaliacoes)
    df_usuarios = processar_dados(df_usuarios)
    df_filmes = processar_dados(df_filmes)

    # 3. Unir as tabelas usando a função do módulo
    # Primeiro junta avaliações com usuarios
    df_temp = unir_tabelas(df_avaliacoes, df_usuarios, 'id_usuario')
    # Depois junta o resultado com os filmes
    df_completo = unir_tabelas(df_temp, df_filmes, 'id_filme')
    
    print("Dados processados e unidos com sucesso!\n")

    # 4. Testar o recomendador
    id_teste = 1
    print(f"A procurar a melhor recomendação para o utilizador ID {id_teste}...")
    
    recomendacao = recomendar_filme(df_completo, id_usuario=id_teste)
    
    print(f"\n> Filme recomendado: {recomendacao}")

if __name__ == "__main__":
    main()