# Lesson 6 - Multi-table queries with JOINs

Up to now, we've been working with a single table, but entity data in the real world is often broken down into pieces and stored across multiple orthogonal tables using a process known as **normalization**

## Database Normalization

Database normalization is useful because it minimizes duplicate data in any single table, and allows for data in the database to grow independently of each other (ie. Types of car engines can grow independent of each type of car). As a trade-off, queries get slightly more complex since they have to be able to find data from different parts of the database, and performance issues can arise when working with many large tables.

## Multi-table queries with JOINs

Tables that share information about a single entity need to have a **primary key** that identifies that entity **uniquely** across the database. One common primary key type is an auto-incrementing integer (because they are space efficient), but it can also be a string, hashed value, so long as it is unique.

Using the **JOIN** clause in a query, we can combine row data across two separate tables using this unique key. 

The **INNER JOIN** is a process that matches rows from the first table and the second table which have the same key (as defined by the ON constraint) to create a result row with the combined columns from both tables. 

```sql
SELECT column, another_table_column, …
FROM mytable
INNER JOIN another_table 
    ON mytable.id = another_table.id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

## Exercise 6

We've added a new table to the Pixar database so that you can try practicing some joins. The **BoxOffice** table stores information about the ratings and sales of each particular Pixar movie, and the **Movie_id** column in that table corresponds with the **Id** column in the **Movies** table 1-to-1. Try and solve the tasks below using the **INNER JOIN** introduced above.

| id  | title               | director         | year | length_minutes |
|-----|---------------------|------------------|------|----------------|
| 1   | Toy Story           | John Lasseter    | 1995 | 81             |
| 2   | A Bug's Life        | John Lasseter    | 1998 | 95             |
| 3   | Toy Story 2         | John Lasseter    | 1999 | 93             |
| 4   | Monsters, Inc.      | Pete Docter      | 2001 | 92             |
| 5   | Finding Nemo        | Andrew Stanton   | 2003 | 107            |
| 6   | The Incredibles     | Brad Bird        | 2004 | 116            |
| 7   | Cars                | John Lasseter    | 2006 | 117            |
| 8   | Ratatouille         | Brad Bird        | 2007 | 115            |
| 9   | WALL-E              | Andrew Stanton   | 2008 | 104            |
| 10  | Up                  | Pete Docter      | 2009 | 101            |
| 11  | Toy Story 3         | Lee Unkrich      | 2010 | 103            |
| 12  | Cars 2              | John Lasseter    | 2011 | 120            |
| 13  | Brave               | Brenda Chapman   | 2012 | 102            |
| 14  | Monsters University | Dan Scanlon      | 2013 | 110            |

| movie_id | rating | domestic_sales | international_sales |
|----------|--------|----------------|----------------------|
| 5        | 8.2    | 380,843,261    | 555,900,000          |
| 14       | 7.4    | 268,492,764    | 475,066,843          |
| 8        | 8.0    | 206,445,654    | 417,277,164          |
| 12       | 6.4    | 191,452,396    | 368,400,000          |
| 3        | 7.9    | 245,852,179    | 239,163,000          |
| 6        | 8.0    | 261,441,092    | 370,001,000          |
| 9        | 8.5    | 223,808,164    | 297,503,696          |
| 11       | 8.4    | 415,004,880    | 648,167,031          |
| 1        | 8.3    | 191,796,233    | 170,162,503          |
| 7        | 7.2    | 244,082,982    | 217,900,167          |
| 10       | 8.3    | 293,004,164    | 438,338,580          |
| 4        | 8.1    | 289,916,256    | 272,900,000          |
| 2        | 7.2    | 162,798,565    | 200,600,000          |
| 13       | 7.2    | 237,283,207    | 301,700,000          |

1. Find the domestic and international sales for each movie?

```sql
SELECT title, domestic_sales, international_sales 
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```

2. Show the sales numbers for each movie that did better internationally rather than domestically?

```sql
SELECT title, domestic_sales, international_sales 
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;
```

3. List all the movies by their ratings in descending order?

```sql
SELECT title, rating
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;
```
