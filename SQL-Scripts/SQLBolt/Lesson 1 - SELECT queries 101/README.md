# Lession 1 - SELECT queries 101

To retrieve data from a SQL database, we need to write **SELECT** statements, which are often colloquially refered to as _queries_.

Think of a table in SQL as a type of an **entity** (ie. Dogs), and each row in that table as a specific **instance** of that type (ie. A pug, a beagle, a different colored pug, etc). This means that the columns would then represent the **common properties** shared by all instances of that entity (ie. Color of fur, length of tail, etc).

## SELECT Statements

SELECT Statement Syntax:

```sql
SELECT column, another_column, …
FROM mytable;
```

SELECT Statement to retrieve all Columns:

```sql
SELECT * 
FROM mytable;
```

## Lession 1 Exercises

We will be using a database with data about some of Pixar's classic movies for most of our exercises. This first exercise will only involve the **Movies** table.

```
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
```

1. Find the **title** of each film?

```sql
SELECT Title FROM movies;
```

2. Find the **director** of each film?

```sql
SELECT Director FROM movies;
```

3. Find the **title** and **director** of each film?

```sql
SELECT Title, Director FROM movies;
```

4. Find the **title** and **year** of each film?

```sql
SELECT Title, Year FROM movies;
```

5. Find **all** the information about each film?

```sql
SELECT * FROM movies;
```




















