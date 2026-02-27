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
```
---

 ### Deploy em Produção
- A aplicação está publicada na nuvem utilizando o Azure App Service (Linux - F1) e encontra-se acessível publicamente via internet.
- O deploy é realizado de forma automatizada por meio de integração contínua (CI/CD) com GitHub Actions, sendo acionado a cada push na branch principal do repositório.
- Essa configuração simula um fluxo real de desenvolvimento profissional, onde alterações no código são automaticamente publicadas em ambiente de produção.