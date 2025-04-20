# Lesson 10 - Queries with aggregates (Pt. 1)

SQL also supports the use of aggregate expressions (or functions) that allow you to summarize information about a group of rows of data. With the Pixar database that you've been using, aggregate functions can be used to answer questions like, "How many movies has Pixar produced?", or "What is the highest grossing Pixar film each year?".

Without a specified grouping, each aggregate function is going to run on the whole set of result rows and return a single value. And like normal expressions, giving your aggregate functions an alias ensures that the results will be easier to read and process.

```sql
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression;
```

## Common Aggregate Functions

| Function                  | Description                                                                                                                                       |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| COUNT(*), COUNT(column)   | A common function used to count the number of rows in the group if no column name is specified. Otherwise, counts the number of rows with non-NULL values in the specified column. |
| MIN(column)               | Finds the smallest numerical value in the specified column for all rows in the group.                                                             |
| MAX(column)               | Finds the largest numerical value in the specified column for all rows in the group.                                                              |
| AVG(column)               | Finds the average numerical value in the specified column for all rows in the group.                                                              |
| SUM(column)               | Finds the sum of all numerical values in the specified column for the rows in the group.                                                          |

## Grouped Aggregate Functions

In addition to aggregating across all the rows, you can instead apply the aggregate functions to individual groups of data within that group (ie. box office sales for Comedies vs Action movies).

This would then create as many results as there are unique groups defined as by the **GROUP BY** clause. The **GROUP BY** clause works by grouping rows that have the same value in the column specified.

```sql
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression
GROUP BY column;
```

## Lesson 10 Exercise

For this exercise, we are going to work with our Employees table. Notice how the rows in this table have shared data, which will give us an opportunity to use aggregate functions to summarize some high-level metrics about the teams. Go ahead and give it a shot.

| Role    | Name       | Building | Years Employed |
|---------|------------|----------|----------------|
| Engineer| Becky A.   | 1e       | 4              |
| Engineer| Dan B.     | 1e       | 2              |
| Engineer| Sharon F.  | 1e       | 6              |
| Engineer| Dan M.     | 1e       | 4              |
| Engineer| Malcom S.  | 1e       | 1              |
| Artist  | Tylar S.   | 2w       | 2              |
| Artist  | Sherman D. | 2w       | 8              |
| Artist  | Jakob J.   | 2w       | 6              |
| Artist  | Lillia A.  | 2w       | 7              |
| Artist  | Brandon J. | 2w       | 7              |
| Manager | Scott K.   | 1e       | 9              |
| Manager | Shirlee M. | 1e       | 3              |
| Manager | Daria O.   | 2w       | 6              |

1. Find the longest time that an employee has been at the studio?

```sql
SELECT MAX(years_employed) AS longest_time FROM employees;
```

2. For each role, find the average number of years employed by employees in that role?

```sql
SELECT role, AVG(years_employed) as Average_years_employed
FROM employees
GROUP BY role;
```

3. Find the total number of employee years worked in each building?

```sql
SELECT role, building, SUM(years_employed) as total_years_employed
FROM employees
GROUP BY building;
```


