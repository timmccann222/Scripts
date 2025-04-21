# Lesson 18 - Dropping tables

In some rare cases, you may want to remove an entire table including all of its data and metadata, and to do so, you can use the **DROP TABLE** statement, which differs from the **DELETE** statement in that it also removes the table schema from the database entirely.

```sql
DROP TABLE IF EXISTS mytable;
```

Like the **CREATE TABLE** statement, the database may throw an error if the specified table does not exist, and to suppress that error, you can use the **IF EXISTS** clause.

In addition, if you have another table that is dependent on columns in table you are removing (for example, with a **FOREIGN KEY** dependency) then you will have to either update all dependent tables first to remove the dependent rows or to remove those tables entirely.


## Lesson 18 Exercises

1. We've sadly reached the end of our lessons, lets clean up by removing the Movies table.

```sql
DROP TABLE IF EXISTS movies;
```

2. And drop the BoxOffice table as well.

```sql
DROP TABLE IF EXISTS movies;
```
