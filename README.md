![Python](https://img.shields.io/badge/python-3.13-blue)
![Poetry](https://img.shields.io/badge/poetry-managed-blueviolet)

# Obras CPFL

Aplicação Python para consultar **desligamentos programados da CPFL**, montar uma mensagem consolidada com as obras da semana e enviar o resultado via **WhatsApp** utilizando **TextMeBot**.

Quando disponível, o fluxo também tenta localizar o **PDF do documento correspondente** e gerar um **link curto via TinyURL** para facilitar o compartilhamento.

---

## Objetivo

Este projeto foi criado como uma **automação simples** para consultar desligamentos programados da CPFL e enviar um **resumo semanal via WhatsApp** para grupos ou números específicos.

A aplicação não pretende ser um sistema completo, mas sim um **script de automação leve**, focado em simplicidade, execução rápida e uso prático.

---

## Requisitos

- Python **3.13+**
- **Poetry**

---

## Instalação

Execute:

```bash
poetry install
```
---
## Configuração

O projeto lê variáveis de ambiente a partir de um arquivo .env.

Exemplo de `.env`:

```
TEXTMEBOT_TOKEN=seu_token_textmebot
TINY_TOKEN=seu_token_tinyurl
SEND_NUMBERS=5511999999999,5511888888888
LEVEL_LOG=INFO
```
---

## Variáveis utilizadas

| Variável          | Descrição                                                       |
| ----------------- | --------------------------------------------------------------- |
| `TEXTMEBOT_TOKEN` | Token utilizado para envio de mensagens via TextMeBot           |
| `TINY_TOKEN`      | Token da API TinyURL para buscar ou criar links curtos          |
| `SEND_NUMBERS`    | Lista de números separados por vírgula no formato internacional |
| `LEVEL_LOG`       | Nível de log da aplicação (`DEBUG`, `INFO`, etc)                |
---
## Execução
### Executar aplicação (recomendado)
```bash
poetry run python -m obras_cpfl.main
```
### Executar diretamente pelo arquivo
```bash
poetry run python src/obras_cpfl/main.py
```
---

## Fluxo da aplicação

1. Consulta a API de desligamentos programados da CPFL para as cidades configuradas (Cosmopolis e Paulinia)

2. Realiza o parsing da resposta e normaliza campos como data, bairro, rua, status e documento

3. Para cada documento tenta localizar o PDF correspondente

4. Busca ou cria um link curto no TinyURL

5. Monta uma mensagem consolidada com o intervalo semanal

6. Envia a mensagem para todos os números definidos em SEND_NUMBERS

Durante a execução o script utiliza Rich para mostrar spinners e status no terminal, evitando a sensação de travamento enquanto os dados são processados.

---

## Exemplo de execução

### Exemplo de saída real do script no terminal
```
Enviando mensagem no whatsapp...

*OBRAS CPFL 12/03/2026 - 19/03/2026*
------------------------------------------------------------

Cidade: Nome da cidade
Data: 14/03/2026
Documento: TES XXXXX
Status: Aguardando Execução
Horario de início: 11:40:00
Horario do final: 17:40:00
Bairro: XXXXX
Rua: XXXXXX
PDF: https://tinyurl.com/XXXXX

------------------------------------------------------------

Cidade: Nome da cidade
Data: 15/03/2026
Documento: TES XXXXX
Status: Aguardando Execução
Horario de início: 07:00:00
Horario do final: 14:30:00
Bairro: XXXX
Rua: XXXXXX
PDF: Não foi possível gerar o link do pdf

------------------------------------------------------------
```
---

## Estrutura do projeto

```text
src/obras_cpfl/
  main.py                      Ponto de entrada da aplicação
  settings.py                  Configuração de ambiente, logging e console
  services/
    cpfl_client.py             Cliente da API de desligamentos da CPFL
    textmebot_client.py        Cliente responsável pelo envio via WhatsApp
    tinyurl_client.py          Cliente da API TinyURL
  utils/
    parse_works_response.py    Parsing e transformação da resposta da CPFL
    scraper.py                 Busca do link do PDF do documento
tests/

```
---
## Desenvolvimento

### Build do pacote
```bash
poetry build
```
### Verificação simples de sintaxe
```bash
python -m compileall src
```
---

## Observação

A geração de links para os PDFs depende de **scraping em uma página externa.**
Caso a estrutura dessa página seja alterada, essa funcionalidade pode precisar de ajustes.

---

## Licença

Uso livre para fins pessoais ou educacionais.
