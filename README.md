# Esquina da TI - repositório do backend

## Como usar

### Registro e Login de Usuários

Acesse o endpoint `https://esquinati.herokuapp.com/auth/login/` utilizando o metodo http `POST` para realizar a authenticação no backend. Somente um usuário authenticado poderá realizar determinadas tarefas.

Para registrar um novo usuário, acesse o endpoint `https://esquinati.herokuapp.com/auth/register/` utilizando o metodo http `POST`.

Caso as tarefas acima sejão executadas com sucesso, você receberá um tocken, é importante armazenar esse tocken na sua aplicação frontend, pois é com ele que você conseguirá acessar alguns endpoints.

### Artigos

Acesse o endpoint `https://esquinati.herokuapp.com/article/` ou `https://esquinati.herokuapp.com/article/all/` utilizando o metodo http `GET` para receber todos os artigos cadastrados.
Com esse mesmo endpoint utilize o metodo `POST` para submeter um novo artigo em formato `json`.
> veja a estrutura do corpo do arquivo `json` para inserir um novo artigo.
```json
{
  "title": "Titulo do seu artigo",
  "category_id": 1,
  "abstract": "Um breve resumo sobre o conteudo",
  "content": "O conteudo principal do seu artigo",
  "user_id": 12
}
```
> `category_id` se trata do id da categoria do artigo e `user_id` do id do autor do artigo.

Acesse o endpoint `https://esquinati.herokuapp.com/article/<id>` ou `https://esquinati.herokuapp.com/article/<id>/` utilizando o metodo http `GET` para receber um artigo especifico.
Com esse mesmo endpoint utilize o metodo `PUT` e `DELETE` para atualizar ou deletar um artigo.

> Utilize a seguinte estrutura de arquivo em `json` para atualizar um Artigo. (O unico campo obrigatório é o `ID`)
```json
{
  "id": 1
  "title": "Titulo do seu artigo atualizado",
  "category_id": 1,
  "content": "O conteudo principal do seu artigo",
}
```

### Obtendo Usuários
Acesse o endpoint `https://esquinati.herokuapp.com/author/` utilizando o metodo http `GET` para uma lista de todos os usuários registrados.
Ou acesse `https://esquinati.herokuapp.com/author/<id>` para obter um usuário especifico.

