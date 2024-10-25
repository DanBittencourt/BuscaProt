# BuscaProtocolos.py

## Descrição
O **BuscaProtocolos.py** é um script em Python desenvolvido para automatizar a verificação de informações contidas em arquivos CSV. Ele busca por CNPJs alvo, identifica protocolos repetidos e verifica se os registros de protocolo estão associados a cidades diferentes da especificada no script. Ao final, gera um arquivo de texto listando os protocolos que foram identificados em cada verificação.

Este projeto foi desenvolvido para otimizar e automatizar tarefas repetitivas no trabalho, facilitando a análise de grandes volumes de dados.

## Funcionalidades
- Verifica se algum CNPJ alvo está presente no arquivo CSV e guarda o protocolo correspondente.
- Identifica protocolos repetidos, independentemente do CNPJ.
- Verifica se a cidade associada ao protocolo é diferente da especificada no script.
- Gera um arquivo de saída em formato `.txt` com os protocolos classificados por tipo de verificação (CNPJ alvo, protocolos repetidos, e cidades diferentes).

## Tecnologias Utilizadas
O script utiliza as seguintes bibliotecas padrão do Python:
- `csv`: Para manipulação e leitura do arquivo CSV.
- `re`: Para trabalhar com expressões regulares na manipulação de strings.
- `time`: Para gerenciamento de pausas e intervalos durante a execução do script.

## Pré-requisitos
- Python 3.x instalado.
- Arquivo CSV contendo as colunas: CNPJ, Tipo, Cidade e Número de Protocolo.

## Instalação
1. Clone este repositório ou faça o download dos arquivos.
    ```bash
    git clone https://github.com/seu-usuario/buscaprotocolos.git
    ```

2. Certifique-se de que o Python 3.x está instalado em seu sistema.

3. Garanta que o arquivo CSV esteja corretamente formatado e nomeado conforme os requisitos do script.

## Como Executar
1. Abra o prompt de comando no diretório onde o script está localizado.

2. Execute o script com o Python:
    ```bash
    python BuscaProtocolos.py
    ```

3. Insira os CNPJs alvo diretamente no script antes da execução. O script irá processar o arquivo CSV, identificar os protocolos correspondentes, e gerar um arquivo de saída `.txt` contendo os resultados das verificações.

## Saída do Script
Ao final da execução, o script gera um arquivo `resultado_protocolos.txt` contendo:

- Protocolos associados aos CNPJs alvo.
- Protocolos que se repetem.
- Protocolos associados a cidades diferentes da especificada no script.

## Contribuições
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades! Você pode abrir uma issue ou fazer um pull request.

## Licença
Este projeto não possui uma licença específica.

---

**Autor:** Daniel Bittencourt  
- [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/danielbittenc)
- [![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/danibittenc/)
- [![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/smashpump)
