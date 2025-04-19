# Lesson 3 - Queries with constraints (Pt. 2)

When writing **WHERE** clauses with columns containing text data, SQL supports a number of useful operators to do things like case-insensitive string comparison and wildcard pattern matching. We show a few common text-data specific operators below:

| Operator     | Condition                                                                 | Example                                |
|--------------|---------------------------------------------------------------------------|----------------------------------------|
| =            | Case sensitive exact string comparison (notice the single equals)         | col_name = "abc"                       |
| != or <>     | Case sensitive exact string inequality comparison                         | col_name != "abcd"                     |
| LIKE         | Case insensitive exact string comparison                                  | col_name LIKE "ABC"                    |
| NOT LIKE     | Case insensitive exact string inequality comparison                       | col_name NOT LIKE "ABCD"               |
| %            | Matches a sequence of zero or more characters (use with LIKE/NOT LIKE)    | col_name LIKE "%AT%" <br>(matches "AT", "ATTIC", "CAT", "BATS") |
| _            | Matches a single character (use with LIKE/NOT LIKE)                       | col_name LIKE "AN_" <br>(matches "AND", but not "AN") |
| IN (…)       | String exists in a list                                                    | col_name IN ("A", "B", "C")            |
| NOT IN (…)   | String does not exist in a list                                            | col_name NOT IN ("D", "E", "F")        |

All strings **must be quoted** so that the query parser can distinguish words in the string from SQL keywords.

## Lesson 3 Exercises

Complete the exercises below using the **Movies** table.

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
| 87  | WALL-G              | Brenda Chapman   | 2042 | 97             |


1. Find all the Toy Story movies?

```sql
SELECT * FROM movies WHERE title LIKE "Toy Story%";
```

2. Find all the movies directed by John Lasseter?

```sql
SELECT * FROM movies WHERE director = "John Lasseter";
```

3. Find all the movies (and director) not directed by John Lasseter?

```sql
SELECT * FROM movies WHERE director != "John Lasseter";
```

4. Find all the `WALL-*` movies?

```sql
SELECT * FROM movies WHERE title LIKE "WALL-_";
```





