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
 
 ### Como Testar em Produção

A API está hospedada e operacional no Azure. Você pode testar a consulta de CNPJ utilizando os seguintes métodos:

1. Via Navegador (Método GET)

- Acesse a URL diretamente no seu browser substituindo {cnpj} pelo número desejado (apenas números):

URL Base:
https://consulta-cnpj-lucas-hncmbfadeabrbaay.canadacentral-01.azurewebsites.net/consultar-cnpj?cnpj={cnpj}

Exemplo Real:
Clique aqui para consultar o CNPJ da Google Brasil

2. Via Terminal (cURL)

- Abra o seu terminal (Prompt, PowerShell ou Bash) e execute o comando abaixo:

curl -X GET [https://consulta-cnpj-lucas-hncmbfadeabrbaay.canadacentral-01.azurewebsites.net/consultar-cnp?cnpj=06990590000123](https://consulta-cnpj-lucas-hncmbfadeabrbaay.canadacentral-01.azurewebsites.net/consultar-cnpj?cnpj=06990590000123)

3. Via Postman ou Insomnia

- Crie uma nova requisição do tipo GET.
- Cole a URL: https://consulta-cnpj-lucas-hncmbfadeabrbaay.canadacentral-01.azurewebsites.net/consultar-cnpj?cnpj=06990590000123
- Clique em Send.

O resultado esperado será um JSON contendo a chave razao_social.

Nota: Por estar em uma camada gratuita (F1) do Azure App Service, a aplicação pode entrar em "modo de espera" após períodos de inatividade. Caso a primeira requisição demore alguns segundos, é o processo de cold start (inicialização) do servidor.
