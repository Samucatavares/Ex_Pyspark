# Ex_Pyspark
Para esse teste, foi criada uma aplicação em Python, usando fastApi para inserir os dados em um banco mysql, e com isso fazer o cálculo do valor líquido.Para isso, foram utilizados bibliotecas Python e conexão com um banco mysql Community.A intenção inicial para o mesmo era subir o serviço em um docker na AWS e integrar com alguma solução como o databricks para que fosse siumulado um datalake, porém o tempo não permitiu que fosse feito dessa maneira. Então, para o exercício 1, a aplicação pode inserir todos os dados de contrato e transação e o cálculo feito em um Mysql e retornado no HTML. Os exercícios 2 e 3 foram feitos através de Notebooks no Databricks Community, onde é possível compartilhar os resultados, então a aplicação apenas irá retornar o valor dos mesmos. Já o exercício 4, foi feito através de um draw.io, e a API direcionará para o arquivo hmtl na pasta Static.
Segue imagem da home:
![image](https://raw.githubusercontent.com/Samucatavares/Ex_Pyspark/main/images/Home.png)

# Exercicio 1
Para esse exercício, foi feita uma consulta SQL  simples no banco, e o resultado pode ser visto na figura abaixo.
![image](https://raw.githubusercontent.com/Samucatavares/Ex_Pyspark/main/images/EX_1.png)

# Exercicio 2
Para esse exercício, foi criado um notebook no databricks, onde foram inseridos os dados de transação para criar uma tabela, e com a mesma foi feito o cálculo do Lucro, como pode ser visto no [link](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1423964847060326/2218187778688641/4811315951827152/latest.html).
![image](https://raw.githubusercontent.com/Samucatavares/Ex_Pyspark/main/images/ex_2.png)


# Exercicio 3
Para esse exercício, também foi criado um notebook no databricks,para ler o arquivo json e o separar em duas tabelas diferentes, para isso foram utilizados os conceitos de camdas bronze,silver e gold, e uma modelagem STAR, onde o link seria o Id da nota fiscal. Como melhoria, o ideal seria criar um id para os produtos, e utilizar duas tabelas Dimensão, de Notas e produtos, e uma fato com o total de compras e valores. O resultado está nesse [link](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1423964847060326/2218187778688625/4811315951827152/latest.html).
![image](https://raw.githubusercontent.com/Samucatavares/Ex_Pyspark/main/images/ex_3.png)

# Exercicio 4
Já para o exercício 4, foram consideradas várias arquiteturas, porém pensando pelo preço e facilidade de integração, foram utilizados os componentes AWS. 
DMS: Usado para ler e inserir dados de bancos armazenados na RDS em pastas S3, onde ficará o dado bruto. Pode fazer leituras completas do banco, ou salvar alterações do binlog.
Kinesis; Opção caso a aplicação queira enviar algum evento ou dado que não precisa ser salvo em um banco de dados.
EMR: Solução em nuvem para processar dados, importante para andar entre as camadas fazendo transformações de dados usando Pyspark, utilizando um airflow como orquestrador de jobs.
Redshift: Solução da Amazon que funciona como um Data Warehousel, onde serão armazenados os dados de cada camada (Nesse ponto, é importante se atentar a governança e acesso aos dados)
Apache Superset: Ferramente open-source de vizualização. Poderiam ser utilizadas outras como o Metabase e o Redash, fica a escolha do cliente.
Segue a imagem do HTML
![image](https://raw.githubusercontent.com/Samucatavares/Ex_Pyspark/main/images/ex_4.png)