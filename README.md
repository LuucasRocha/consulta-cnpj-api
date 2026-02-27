# Consulta de Razão Social por CNPJ — API Flask

## Descrição do Projeto
Este projeto consiste em uma **API desenvolvida em Python com Flask**, cujo objetivo é consultar a **razão social de uma empresa a partir do CNPJ**, utilizando a **API gratuita do [CNPJJá](https://cnpja.com/api/open)**.

O sistema foi desenvolvido com o objetivo de demonstrar conhecimentos em:
- Desenvolvimento de APIs RESTful com Flask;
- Integração com APIs externas;
- Publicação de aplicações Python no **Azure App Service**.

---

## Funcionalidades
- Receber um número de **CNPJ** via requisição HTTP (`GET` ou `POST`);
- Realizar uma requisição à API pública do **CNPJJá**;
- Processar a resposta e retornar **apenas a razão social** da empresa em formato JSON.

### Exemplo de resposta:
```json
{
  "razao_social": "Empresa Exemplo LTDA"
}

Este projeto simula um cenário real de backend onde um sistema atua como intermediário entre o cliente e uma API externa, aplicando regras de negócio, controle e abstração de dados.

A aplicação está publicada em ambiente de produção na Azure com deploy automatizado.

# Objetivo do Projeto

Demonstrar na prática:
Construção de API REST
Consumo de API externa
Estruturação de backend
Deploy em nuvem
Integração contínua com GitHub Actions

O projeto representa um microserviço responsável por intermediar requisições externas e retornar dados tratados ao cliente.