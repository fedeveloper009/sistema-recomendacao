# 🎬 Sistema de Recomendação de Filmes

> Um sistema de recomendação de filmes robusto, desenvolvido em Python utilizando **Pandas**, com uma arquitetura modular orientada a boas práticas de engenharia de dados e lógica baseada em regras (*Rule-based*).

---

## 🛠️ Arquitetura do Projeto

O projeto foi construído de forma modular para garantir a separação de responsabilidades, facilitando a manutenção, testes e escalabilidade:

```text
projeto-recomendacao/
│
├── data/
│   ├── avaliacoes.csv
│   ├── filmes.csv
│   └── utilizadores.csv
│
├── src/
│   ├── __init__.py
│   ├── processamento.py
│   └── recomendador.py
│
├── main.py
└── README.md
```

* **`src/processamento.py`**: Módulo responsável por carregar os arquivos CSV, padronizar nomes de colunas, tratar valores ausentes ou duplicados e realizar a união relacional (*merge*) das tabelas.
* **`src/recomendador.py`**: Módulo contendo a inteligência de recomendação baseada no histórico e comportamento do usuário.
* **`main.py`**: Script orquestrador que executa a pipeline de dados e exibe a recomendação final.

---

## 🧠 Lógica de Recomendação

O algoritmo de recomendação simula abordagens reais de filtragem baseada em conteúdo, seguindo três pilares principais:

1. **Janela Temporal (Visto Recentemente):** O sistema analisa os **últimos 5 filmes** assistidos pelo usuário para capturar seu interesse recente, filtrando ruídos ou anomalias de longo prazo.
2. **Filtro por Categoria:** Identifica o gênero dominante (moda estatística) dentro dessa janela temporal recente.
3. **Exclusão de Histórico & Qualidade (Nota Média):** Remove todos os filmes que o usuário já assistiu e ranqueia os candidatos restantes no mesmo gênero com base na **nota média global** dada por toda a comunidade de usuários.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3 instalado, além da biblioteca **Pandas**:

```bash
pip install pandas
```

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Acessar a pasta do projeto:**
   ```bash
   cd seu-repositorio
   ```

3. **Verificar os dados:**
   Garanta que os arquivos CSV (`avaliacoes.csv`, `filmes.csv`, `utilizadores.csv`) estejam localizados dentro do diretório `data/`.

4. **Executar a aplicação:**
   ```bash
   python main.py
   ```

---

## 💡 Tecnologias Utilizadas

* **Python 3**
* **Pandas** (manipulação, limpeza, tratamento de inconsistências, união relacional e agregações de dados)