# Sistema de Votação Desenvolvido em Python

Aplicação simples de votação executada no terminal. Permite cadastrar vários
candidatos, registrar votos e consultar os resultados atualizados após cada
voto ou sempre que o usuário solicitar.

## Requisitos

- Python 3.9 ou superior
- Nenhuma biblioteca externa (usa apenas a biblioteca padrão do Python)

## Estrutura do projeto

'''text
sistema_votacao/
├── main.py                 # Interface de terminal
├── votacao.py              # Classes Candidato e SistemaDeVotacao
├── README.md               # Documentação
└── tests/
    └── test_votacao.py     # Testes automatizados
'''

## Como executar

2. Abra o terminal na pasta 'sistema_votacao'.
3. Execute:

   '''bash
   python main.py
   '''

   No Windows, se o comando 'python' não funcionar, tente 'py main.py'.

4. Use o menu para cadastrar candidatos, votar e consultar os resultados.
   Após cada voto, o programa apresenta automaticamente o placar atualizado.

## Como executar os testes

Na pasta raiz do projeto, execute:

'''bash
python -m unittest discover -s tests -v
'''

No Windows, também pode ser necessário usar 'py' no lugar de 'python'.

## Regras e tratamento de erros

- Não permite cadastrar nomes vazios.
- Não permite cadastrar duas vezes o mesmo nome (a comparação ignora
  maiúsculas/minúsculas e espaços excedentes).
- Não permite votar em candidato não cadastrado.
- Não permite registrar votos antes de cadastrar pelo menos um candidato.
- Erros de entrada esperados são informados ao usuário sem encerrar o programa.
- Os resultados são ordenados do maior para o menor número de votos; empates
  são ordenados alfabeticamente.

## Organização e orientação a objetos

- 'Candidato': representa um candidato e controla a própria contagem de votos.
- 'SistemaDeVotacao': centraliza o cadastro, validação, registro e consulta.
- 'main.py': cuida apenas da interação com o usuário, mantendo a lógica de
  votação separada da interface.

Essa separação facilita a manutenção e permite testar as regras sem simular
entradas pelo terminal.
