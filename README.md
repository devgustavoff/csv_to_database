# csv_to_database
ETL manual, pega alguns datasets do [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) limpa os arquivos csv tratando valores nulos criticos e tratando tipos de dados.

# Como rodar
### 1. Subir o banco
```bash
docker compose up -d
```
### 2. Criar as tabelas
```bash
docker cp sql/schema.sql olist_postgres:/schema.sql
docker exec -it olist_postgres psql -U postgres -d olist -f /schema.sql
```
### 3. Instalar dependecias Python
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 4. Rodar o pipeline
```bash
python main.py
```
# Queries
## TOP 10 PRODUTOS MAIS VENDIDOS
```sql
SELECT 
    order_items.product_id, 
    SUM(order_items.price) AS total_sales
FROM order_items
GROUP BY order_items.product_id
ORDER BY total_sales DESC
LIMIT 10;
```
            product_id            |    total_sales
----------------------------------+--------------------
 bb50f2e236e5eea0100680137654686c |              63885
 6cdd53843498f92890544667809f1595 | 54730.200000000106
 d6160fb7873f184099d9bc95e30376af |           48899.34
 d1c427060a0f73f6b889a5c7c61f2ac4 |  47214.50999999998
 99a4788cb24856965c36a24e339b6058 |  43025.56000000037
 3dd2a17168ec895c781a9191c1e95ad7 |  41082.60000000021
 25c38557cf793876c5abdd5931f922db |  38907.32000000001
 5f504b3a1c75b73d6151be81eb05bdc9 |  37733.90000000001
 53b36df67ebb7c41585e8d54d6772e08 |  37683.42000000013
 aca2eb7d00ea1a7b8ebd4e68314663af | 37608.900000000314
(10 rows)

## RECEITA POR MÊS
```sql
SELECT
    EXTRACT(YEAR FROM orders.order_purchase_timestamp) AS year,
    EXTRACT(MONTH FROM orders.order_purchase_timestamp) AS month, 
    SUM(order_items.price) AS total_month_revenue
FROM orders
JOIN order_items ON orders.order_id = order_items.order_id
GROUP BY year, month
ORDER BY year, month;
```
year | month | total_month_revenue
------+-------+---------------------
 2016 |     9 |              267.36
 2016 |    10 |  49507.660000000076
 2016 |    12 |                10.9
 2017 |     1 |  120312.87000000034
 2017 |     2 |  247303.01999999903
 2017 |     3 |   374344.2999999949
 2017 |     4 |    359927.229999996
 2017 |     5 |  506071.13999999024
 2017 |     6 |  433038.59999999264
 2017 |     7 |   498031.4799999908
 2017 |     8 |    573971.679999993
 2017 |     9 |   624401.6899999965
 2017 |    10 |   664219.4299999964
 2017 |    11 |  1010271.3700000165
 2017 |    12 |   743914.1700000004
 2018 |     1 |   950030.3600000145
 2018 |     2 |   844178.7100000089
 2018 |     3 |   983213.4400000153
 2018 |     4 |    996647.750000013
 2018 |     5 |   996517.6800000146
 2018 |     6 |   865124.3100000086
 2018 |     7 |   895507.2200000084
 2018 |     8 |   854686.3300000079
 2018 |     9 |                 145

 ## ESTADOS COM MAIS PEDIDOS
 ```sql
SELECT
    customers.customer_state,
    COUNT(orders.order_id) AS orders_total
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_state
ORDER BY orders_total DESC;
```
 customer_state | orders_total
----------------+--------------
 SP             |        41746
 RJ             |        12852
 MG             |        11635
 RS             |         5466
 PR             |         5045
 SC             |         3637
 BA             |         3380
 DF             |         2140
 ES             |         2033
 GO             |         2020
 PE             |         1652
 CE             |         1336
 PA             |          975
 MT             |          907
 MA             |          747
 MS             |          715
 PB             |          536
 PI             |          495
 RN             |          485
 AL             |          413
 SE             |          350
 TO             |          280
 RO             |          253
 AM             |          148
 AC             |           81
 AP             |           68
 RR             |           46
(27 rows)

## TICKET MEDIO POR CATEGORIA
```sql
SELECT
    products.product_category_name,
    AVG(order_items.price) AS avg_ticket
FROM products
JOIN order_items ON products.product_id = order_items.product_id
GROUP BY products.product_category_name
ORDER BY avg_ticket DESC;
```
             product_category_name              |     avg_ticket
------------------------------------------------+--------------------
 pcs                                            | 1098.3405418719212
 portateis_casa_forno_e_cafe                    |  624.2856578947369
 eletrodomesticos_2                             | 476.12495798319344
 agro_industria_e_comercio                      | 342.12485849056617
 instrumentos_musicais                          | 281.61599999999964
 eletroportateis                                |  280.7784683357878
 portateis_cozinha_e_preparadores_de_alimentos  |  264.5686666666667
 telefonia_fixa                                 | 225.69318181818215
 construcao_ferramentas_seguranca               | 208.99237113402057
 relogios_presentes                             | 201.13598397596593
 climatizacao                                   |  185.2692255892258
 moveis_quarto                                  | 183.75027522935773
 pc_gamer                                       | 171.77222222222224
 cool_stuff                                     | 167.35796891464562
 moveis_cozinha_area_de_servico_jantar_e_jardim | 164.86964412811398
 moveis_escritorio                              | 162.01105854524002
 musica                                         |  158.7986842105263
 construcao_ferramentas_construcao              | 155.73475780409044
 construcao_ferramentas_ferramentas             | 154.40728155339806
 industria_comercio_e_negocios                  |   148.020932835821
 la_cuisine                                     |            146.785
 seguros_e_servicos                             | 141.64499999999998
 automotivo                                     | 139.95752302243105
 audio                                          | 139.25412087912105
 consoles_games                                 | 138.49183817062436
 casa_construcao                                | 137.56311258278166
 moveis_sala                                    | 137.01105367793286
 construcao_ferramentas_iluminacao              | 135.13157894736847
 casa_conforto                                  | 134.95861751152106
 bebes                                          |  134.3441729200634
 beleza_saude                                   | 130.16353050672376
 malas_acessorios                               | 128.59888278388308
 brinquedos                                     | 117.54836045664095
 perfumaria                                     | 116.73731207955345
 informatica_acessorios                         | 116.51390315574487
 artes                                          | 115.80210526315783
 moveis_colchao_e_estofado                      | 114.94947368421053
 esporte_lazer                                  | 114.34428538363822
 sem categoria                                  | 111.99955084217106
 ferramentas_jardim                             | 111.63019553714983
 pet_shop                                       | 110.07468412942958
 sinalizacao_e_seguranca                        | 108.08658291457283
 construcao_ferramentas_jardim                  | 108.04995798319324
 artigos_de_festas                              |   104.306511627907
 eletrodomesticos                               | 103.98382619974079
 cine_foto                                      |  96.29805555555556
 dvds_blu_ray                                   |  93.74046875000005
 cama_mesa_banho                                |  93.29632748538377
 papelaria                                      |  91.75336909018614
 market_place                                   |  91.24909967845646
 utilidades_domesticas                          |  90.78814761631182
 tablets_impressao_imagem                       |  90.70373493975904
 fashion_calcados                               |  89.93423664122119
 moveis_decoracao                               |  87.56449364050974
 livros_interesse_geral                         |  84.73215189873434
 fashion_roupa_masculina                        |  81.80166666666663
 livros_importados                              |  77.33083333333335
 artes_e_artesanato                             |           75.58375
 fashion_bolsas_e_acessorios                    |  75.24546528803559
 fashion_underwear_e_moda_praia                 |  72.83625954198472
 livros_tecnicos                                |  71.52082397003741
 fashion_roupa_infanto_juvenil                  |           71.23125
 telefonia                                      |  71.21397799779922
 fashion_esporte                                |  70.65033333333334
 bebidas                                        | 59.178627968337636
 fashion_roupa_feminina                         |  58.40916666666667
 eletronicos                                    |  57.91353089989136
 alimentos                                      | 57.634137254901795
 artigos_de_natal                               |  57.52169934640523
 alimentos_bebidas                              |  54.60244604316543
 cds_dvds_musicais                              | 52.142857142857146
 fraldas_higiene                                |  40.19461538461539
 flores                                         |  33.63757575757575
 casa_conforto_2                                |  25.34233333333333

## TAXA DE PEDIDOS ATRASADOS
```sql
SELECT 
    (COUNT(*) FILTER(WHERE orders.order_delivered_customer_date > orders.order_estimated_delivery_date)::DECIMAL 
    / COUNT(*)) * 100 AS late_order_rate
FROM orders;
```
    late_order_rate
------------------------
 7.87099888376021962800
(1 row)
