# Lesson 13 - Inserting rows

## What is a Schema?

We previously described a table in a database as a two-dimensional set of rows and columns, with the columns being the properties and the rows being instances of the entity in the table. In SQL, the database schema is what **describes the structure of each table**, and the datatypes that each column of the table can contain.

For example, in our Movies table, the values in the Year column must be an **Integer**, and the values in the Title column must be a **String**.

## Inserting new data

When inserting data into a database, we need to use an **INSERT** statement, which declares which table to write into, the columns of data that we are filling, and one or more rows of data to insert. In general, each row of data you insert should contain values for every corresponding column in the table. You can insert multiple rows at a time by just listing them sequentially.

```sql
INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;
```

In some cases, if you have incomplete data and the table contains columns that support default values, you can insert rows with only the columns of data you have by specifying them explicitly.

```sql
INSERT INTO mytable
(column, another_column, …)
VALUES (value_or_expr, another_value_or_expr, …),
      (value_or_expr_2, another_value_or_expr_2, …),
      …;
```

In these cases, the number of values need to match the number of columns specified. Despite this being a more verbose statement to write, inserting values this way has the benefit of being forward compatible. For example, if you add a new column to the table with a default value, no hardcoded **INSERT** statements will have to change as a result to accommodate that change.

In addition, you can use mathematical and string expressions with the values that you are inserting. This can be useful to ensure that all data inserted is formatted a certain way.

```sql
INSERT INTO boxoffice
(movie_id, rating, sales_in_millions)
VALUES (1, 9.9, 283742034 / 1000000);
```

## Lesson 13 Exercise

In this exercise, we are going to play studio executive and add a few movies to the Movies to our portfolio. In this table, the Id is an auto-incrementing integer, so you can try inserting a row with only the other columns defined.

Since the following lessons will modify the database, you'll have to manually run each query once they are ready to go.

| ID | Title         | Director      | Year | Length (minutes) |
|----|---------------|---------------|------|------------------|
| 1  | Toy Story     | John Lasseter | 1995 | 81               |
| 2  | A Bug's Life  | John Lasseter | 1998 | 95               |
| 3  | Toy Story 2   | John Lasseter | 1999 | 93               |

| Movie ID | Rating | Domestic Sales | International Sales |
|----------|--------|----------------|---------------------|
| 3        | 7.9    | 245,852,179    | 239,163,000         |
| 1        | 8.3    | 191,796,233    | 170,162,503         |
| 2        | 7.2    | 162,798,565    | 200,600,000         |


1. Add the studio's new production, Toy Story 4 to the list of movies (you can use any director).

```sql
INSERT INTO movies
(title, director,year,length_minutes)
VALUES ("Toy Story 4", "John Lasseter", 2015, 100);
```

2. Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.

```sql
INSERT INTO boxoffice
(movie_id,rating, domestic_sales,international_sales)
VALUES (15,8.7, 340000000, 270000000);
```
