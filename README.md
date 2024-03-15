# Endpoints

1. Create user 
    ``http://127.0.0.1:5000/usuarios``
    <br><br>
    a. Input ``{"nome_completo" : "souzaaa", "email" : "lucasfjoaquim12@gmail.com", "senha" : "Teste123"}``
    <br><br><br>
    b. Output ``{
    "data_registro": "Fri, 15 Mar 2024 17:07:20 GMT",
    "email": "lucasfjoaquim12@gmail.com",
    "nome": "souzaaa",
    "user_id": 3 }``
    <br><br>
    c. Verbo HTML : POST
    <br><br>
    d. ![img.png](img.png)

2. Login 
    ``http://127.0.0.1:5000/login``
    <br><br>
    a. Input ``{
    "email" : "lucasfjoaquim@gmail.com",
    "senha" : "Teste123"}``
    <br><br>
    b. Output ``{
    "data_registro": "Fri, 15 Mar 2024 17:06:59 GMT",
    "email": "lucasfjoaquim@gmail.com",
    "jwt_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDUzMzI0NSwianRpIjoiMWUyMWJmYjktYTRjNi00YmU5LWFkMjMtMWMwNTVkNGZkNzhhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imx1Y2FzZmpvYXF1aW1AZ21haWwuY29tIiwibmJmIjoxNzEwNTMzMjQ1LCJjc3JmIjoiYTBkMTc3NzAtYmJlNy00ZWFiLWEwZGQtZDA1ZDBmMTkwZmRmIiwiZXhwIjoxNzEwNTM2ODQ1fQ.qjc_ViU46ALYuodc0AZaaevoa3WEIEXJWI-22jS6fPI",
    "nome": "souza",
    "user_id": 0 }``
    <br><br>
    c.Verbo HTML : Post
    <br><br>
    d. ![img_1.png](img_1.png)

3. Lista de usuarios
    ``http://127.0.0.1:5000/usuarios``
    <br><br>
    a. Input N/A
    <br><br>
    b. Output ``
    "user_list": [
        {
            "data de cadastro": "Fri, 15 Mar 2024 17:06:59 GMT",
            "email": "lucasfjoaquim@gmail.com",
            "id": 0,
            "nome": "souza"
        },
        {
            "data de cadastro": "Fri, 15 Mar 2024 17:07:15 GMT",
            "email": "lucasfjoaquim1@gmail.com",
            "id": 2,
            "nome": "souzaa"
        },
        {
            "data de cadastro": "Fri, 15 Mar 2024 17:07:20 GMT",
            "email": "lucasfjoaquim12@gmail.com",
            "id": 3,
            "nome": "souzaaa"
        }
    ]
}``
    <br><br>
    c. Verbo HTML : GET
    <br><br>
    d. ![img_2.png](img_2.png)
    <br><br>
    f. Esta rota necessita do Bearer Token