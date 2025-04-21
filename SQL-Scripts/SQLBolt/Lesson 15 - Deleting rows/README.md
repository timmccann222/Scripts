# Lesson 15 - Deleting rows

When you need to delete data from a table in the database, you can use a DELETE statement, which describes the table to act on, and the rows of the table to delete through the **WHERE** clause.

If you decide to leave out the **WHERE** constraint, then **all rows are removed**, which is a quick and easy way to clear out a table completely (if intentional).

```sql
DELETE FROM mytable
WHERE condition;
```

Like the **UPDATE** statement from last lesson, it's recommended that you run the constraint in a **SELECT** query first to ensure that you are removing the right rows. Without a proper backup or test database, it is downright easy to irrevocably remove data, so always read your **DELETE** statements twice and execute once.

## Lesson 15 Exercises

1. This database is getting too big, lets remove all movies that were released before 2005.

```sql
DELETE FROM movies
WHERE year <= 2005;
```

2. Andrew Stanton has also left the studio, so please remove all movies directed by him.

```sql
DELETE FROM movies
WHERE director = "Andrew Stanton";
```
