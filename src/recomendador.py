import pandas as pd

def calcular_genero_recente(df_usuario):
    """
    Analisa os últimos 5 filmes assistidos pelo usuário e retorna o gênero mais frequente (moda).
    """
    # Pega os últimos 5 registros do histórico do usuário
    ultimos_filmes = df_usuario.tail(5)
    
    # Calcula a moda do gênero nesse recorte temporal
    genero_favorito = ultimos_filmes['genero'].mode()[0]
    return genero_favorito

def recomendar_filme(df_completo, id_usuario):
    """
    Gera uma recomendação de filme baseada em:
    1. Exclusão de filmes já vistos.
    2. Gênero favorito baseado nos últimos 5 filmes assistidos.
    3. Maior nota média global entre os candidatos.
    """
    # 1. Isolar o histórico do usuário específico
    df_usuario = df_completo[df_completo['id_usuario'] == id_usuario]
    
    if df_usuario.empty:
        return "Usuário não encontrado."
        
    # 2. Descobrir o gênero favorito recente (últimos 5 filmes)
    genero_favorito = calcular_genero_recente(df_usuario)
    
    # 3. Identificar os IDs dos filmes que o usuário já viu
    filmes_vistos = df_usuario['id_filme'].tolist()
    
    # 4. Criar uma base de catálogo única (reovendo duplicatas de filmes)
    catalogo = df_completo.drop_duplicates(subset=['id_filme']).copy()
    
    # 5. Filtrar candidatos: que NÃO foram vistos E pertencem ao gênero favorito recente
    candidatos = catalogo[
        (~catalogo['id_filme'].isin(filmes_vistos)) & 
        (catalogo['genero'] == genero_favorito)
    ]
    
    # Caso de segurança: se não houver filmes do mesmo gênero não vistos, relaxa o filtro de gênero
    if candidatos.empty:
        candidatos = catalogo[~catalogo['id_filme'].isin(filmes_vistos)]
        
    # 6. Calcular a nota média global de cada filme no dataset geral
    media_notas = df_completo.groupby('id_filme')['nota'].mean().reset_index(name='nota_media')
    
    # Fazer o merge da nota média com os filmes candidatos
    candidatos = candidatos.merge(media_notas, on='id_filme', how='left')
    
    # 7. Ordenar os candidatos pela maior nota média (decrescente)
    candidatos = candidatos.sort_values(by='nota_media', ascending=False)
    
    # 8. Retornar o título do melhor filme ranqueado
    if not candidatos.empty:
        melhor_filme = candidatos.iloc[0]['titulo']
        return melhor_filme
    
    return "Nenhum filme disponível para recomendação."