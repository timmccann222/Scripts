# Lesson 8 - A short note on NULLs

It's always good to reduce the possibility of **NULL** values in databases because they require special attention when constructing queries, constraints (certain functions behave differently with null values) and when processing the results.

An alternative to **NULL** values in your database is to have **data-type appropriate default values**, like 0 for numerical data, empty strings for text data, etc. But if your database needs to store incomplete data, then **NULL** values can be appropriate if the default values will skew later analysis (for example, when taking averages of numerical data).

Sometimes, it's also not possible to avoid **NULL** values, as we saw in the last lesson when outer-joining two tables with asymmetric data. In these cases, you can test a column for NULL values in a **WHERE** clause by using either the **IS NULL** or **IS NOT NULL** constraint.

```sql
SELECT column, another_column, …
FROM mytable
WHERE column IS/IS NOT NULL
AND/OR another_condition
AND/OR …;
```

## Lesson 8 Exercises

We're using the same Employees and Buildings table from the last lesson, but we've hired a few more people, who haven't yet been assigned a building.

| building_name | capacity |
|---------------|----------|
| 1e            | 24       |
| 1w            | 32       |
| 2e            | 16       |
| 2w            | 20       |

| role    | name        | building | years_employed |
|---------|-------------|----------|----------------|
| Engineer| Becky A.    | 1e       | 4              |
| Engineer| Dan B.      | 1e       | 2              |
| Engineer| Sharon F.   | 1e       | 6              |
| Engineer| Dan M.      | 1e       | 4              |
| Engineer| Malcom S.   | 1e       | 1              |
| Artist  | Tylar S.    | 2w       | 2              |
| Artist  | Sherman D.  | 2w       | 8              |
| Artist  | Jakob J.    | 2w       | 6              |
| Artist  | Lillia A.   | 2w       | 7              |
| Artist  | Brandon J.  | 2w       | 7              |
| Manager | Scott K.    | 1e       | 9              |
| Manager | Shirlee M.  | 1e       | 3              |
| Manager | Daria O.    | 2w       | 6              |
| Engineer| Yancy I.    |          | 0              |
| Artist  | Oliver P.   |          | 0              |

1. Find the name and role of all employees who have not been assigned to a building?

```sql
SELECT * 
FROM employees
WHERE building IS NULL;
```

2. Find the names of the buildings that hold no employees?

```sql
SELECT DISTINCT building_name
FROM buildings 
  LEFT JOIN employees
    ON building_name = building
WHERE role IS NULL;
```






