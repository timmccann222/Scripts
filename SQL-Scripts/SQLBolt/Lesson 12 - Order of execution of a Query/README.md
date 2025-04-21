# Lesson 12 - Order of execution of a Query

Now that we have an idea of all the parts of a query, we can now talk about how they all fit together in the context of a complete query. Each query begins with finding the data that we need in a database, and then filtering that data down into something that can be processed and understood as quickly as possible. Because each part of the query is executed sequentially, it's important to understand the order of execution so that you know what results are accessible where.

```sql
SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
FROM mytable
    JOIN another_table
      ON mytable.column = another_table.column
    WHERE constraint_expression
    GROUP BY column
    HAVING constraint_expression
    ORDER BY column ASC/DESC
    LIMIT count OFFSET COUNT;
```

## Query order of execution

### 1. FROM and JOINs

The **FROM** clause, and subsequent **JOINs** are first executed to determine the total working set of data that is being queried. This includes subqueries in this clause, and can cause temporary tables to be created under the hood containing all the columns and rows of the tables being joined.

### 2. WHERE

Once we have the total working set of data, the first-pass **WHERE** constraints are applied to the individual rows, and rows that do not satisfy the constraint are discarded. Each of the constraints can only access columns directly from the tables requested in the **FROM** clause. Aliases in the **SELECT** part of the query are **not accessible** in most databases since they may include expressions dependent on parts of the query that have not yet executed.

### 3. GROUP BY

The remaining rows after the **WHERE** constraints are applied are then grouped based on common values in the column specified in the **GROUP BY** clause. As a result of the grouping, there will only be as many rows as there are unique values in that column. Implicitly, this means that you should only need to use this when you have aggregate functions in your query.

### 4. HAVING

If the query has a **GROUP BY** clause, then the constraints in the **HAVING** clause are then applied to the grouped rows, discard the grouped rows that don't satisfy the constraint. Like the **WHERE** clause, **aliases are also not accessible** from this step in most databases.

### 5. SELECT

Any expressions in the **SELECT** part of the query are finally computed.

### 6. DISTINCT

Of the remaining rows, rows with duplicate values in the column marked as **DISTINCT** will be discarded.

### 7. ORDER BY

If an order is specified by the **ORDER BY** clause, the rows are then sorted by the specified data in either ascending or descending order. Since all the expressions in the **SELECT** part of the query have been computed, **you can reference aliases** in this clause.

### 8. LIMIT / OFFSET

Finally, the rows that fall outside the range specified by the **LIMIT** and **OFFSET** are discarded, leaving the final set of rows to be returned from the query.

## Lesson 12 Exercises

Here ends our lessons on SELECT queries, congrats of making it this far! This exercise will try and test your understanding of queries, so don't be discouraged if you find them challenging. Just try your best.

| ID | Title               | Director         | Year | Length (minutes) |
|----|---------------------|------------------|------|------------------|
| 1  | Toy Story           | John Lasseter    | 1995 | 81               |
| 2  | A Bug's Life        | John Lasseter    | 1998 | 95               |
| 3  | Toy Story 2         | John Lasseter    | 1999 | 93               |
| 4  | Monsters, Inc.      | Pete Docter      | 2001 | 92               |
| 5  | Finding Nemo        | Andrew Stanton   | 2003 | 107              |
| 6  | The Incredibles     | Brad Bird        | 2004 | 116              |
| 7  | Cars                | John Lasseter    | 2006 | 117              |
| 8  | Ratatouille         | Brad Bird        | 2007 | 115              |
| 9  | WALL-E              | Andrew Stanton   | 2008 | 104              |
| 10 | Up                  | Pete Docter      | 2009 | 101              |
| 11 | Toy Story 3         | Lee Unkrich      | 2010 | 103              |
| 12 | Cars 2              | John Lasseter    | 2011 | 120              |
| 13 | Brave               | Brenda Chapman   | 2012 | 102              |
| 14 | Monsters University | Dan Scanlon      | 2013 | 110              |

| Movie ID | Rating | Domestic Sales | International Sales |
|----------|--------|----------------|---------------------|
| 5        | 8.2    | 380,843,261    | 555,900,000         |
| 14       | 7.4    | 268,492,764    | 475,066,843         |
| 8        | 8.0    | 206,445,654    | 417,277,164         |
| 12       | 6.4    | 191,452,396    | 368,400,000         |
| 3        | 7.9    | 245,852,179    | 239,163,000         |
| 6        | 8.0    | 261,441,092    | 370,001,000         |
| 9        | 8.5    | 223,808,164    | 297,503,696         |
| 11       | 8.4    | 415,004,880    | 648,167,031         |
| 1        | 8.3    | 191,796,233    | 170,162,503         |
| 7        | 7.2    | 244,082,982    | 217,900,167         |
| 10       | 8.3    | 293,004,164    | 438,338,580         |
| 4        | 8.1    | 289,916,256    | 272,900,000         |
| 2        | 7.2    | 162,798,565    | 200,600,000         |
| 13       | 7.2    | 237,283,207    | 301,700,000         |

1. Find the number of movies each director has directed?

```sql
SELECT director, COUNT(title) AS num_movies 
FROM movies
GROUP BY director;
```

2. Find the total domestic and international sales that can be attributed to each director?

```sql
SELECT director, SUM(domestic_sales + international_sales) AS total_sales
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
GROUP BY director;
```


