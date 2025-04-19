# Lesson 4 - Filtering and sorting Query results

Even though the data in a database may be unique, the results of any particular query may not be – take our Movies table for example, many different movies can be released the same year. In such cases, SQL provides a convenient way to discard rows that have a duplicate column value by using the **DISTINCT** keyword.

```sql
SELECT DISTINCT column, another_column, …
FROM mytable
WHERE condition(s);
```

Unlike our neatly ordered table in the last few lessons, most data in real databases are added in no particular column order. As a result, it can be difficult to read through and understand the results of a query as the size of a table increases to thousands or even millions rows. To help with this, SQL provides a way to sort your results by a given column in ascending or descending order using the **ORDER BY** clause.

```sql
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC;
```

Another clause which is commonly used with the **ORDER BY** clause are the **LIMIT** and **OFFSET** clauses, which are a useful optimization to indicate to the database the subset of the results you care about. The **LIMIT** will reduce the number of rows to return, and the optional **OFFSET** will specify where to begin counting the number rows from.

```sql
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

## Lesson 4 Exercises

There are a few concepts in this lesson, but all are pretty straight-forward to apply. To spice things up, we've gone and scrambled the Movies table for you in the exercise to better mimic what kind of data you might see in real life. Try and use the necessary keywords and clauses introduced above in your queries.

| id  | title               | director         | year | length_minutes |
|-----|---------------------|------------------|------|----------------|
| 1   | Toy Story 2         | John Lasseter    | 1999 | 93             |
| 2   | Cars 2              | John Lasseter    | 2011 | 120            |
| 3   | Finding Nemo        | Andrew Stanton   | 2003 | 107            |
| 4   | Up                  | Pete Docter      | 2009 | 101            |
| 5   | WALL-E              | Andrew Stanton   | 2008 | 104            |
| 6   | Toy Story 3         | Lee Unkrich      | 2010 | 103            |
| 7   | Cars                | John Lasseter    | 2006 | 117            |
| 8   | Ratatouille         | Brad Bird        | 2007 | 115            |
| 9   | The Incredibles     | Brad Bird        | 2004 | 116            |
| 10  | Monsters, Inc.      | Pete Docter      | 2001 | 92             |
| 11  | Brave               | Brenda Chapman   | 2012 | 102            |
| 12  | A Bug's Life        | John Lasseter    | 1998 | 95             |
| 13  | Monsters University | Dan Scanlon      | 2013 | 110            |
| 14  | Toy Story           | John Lasseter    | 1995 | 81             |

1. List all directors of Pixar movies (alphabetically), without duplicates?

```sql
SELECT DISTINCT director FROM movies ORDER BY director;
```

2. List the last four Pixar movies released (ordered from most recent to least)?

```sql
SELECT * FROM movies ORDER BY year DESC LIMIT 4;
```

3. List the first five Pixar movies sorted alphabetically?

```sql
SELECT * FROM movies ORDER BY title LIMIT 5;
```

5. List the **next** five Pixar movies sorted alphabetically?

```sql
SELECT * FROM movies ORDER BY title LIMIT 5 OFFSET 5;
```
