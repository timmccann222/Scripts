# Lesson 10 - Queries with aggregates (Pt. 1)

SQL also supports the use of aggregate expressions (or functions) that allow you to summarize information about a group of rows of data. With the Pixar database that you've been using, aggregate functions can be used to answer questions like, "How many movies has Pixar produced?", or "What is the highest grossing Pixar film each year?".

Without a specified grouping, each aggregate function is going to run on the whole set of result rows and return a single value. And like normal expressions, giving your aggregate functions an alias ensures that the results will be easier to read and process.

```sql
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression;
```

## Common aggregate functions

| Function                  | Description                                                                                                                                       |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| COUNT(*), COUNT(column)   | A common function used to count the number of rows in the group if no column name is specified. Otherwise, counts the number of rows with non-NULL values in the specified column. |
| MIN(column)               | Finds the smallest numerical value in the specified column for all rows in the group.                                                             |
| MAX(column)               | Finds the largest numerical value in the specified column for all rows in the group.                                                              |
| AVG(column)               | Finds the average numerical value in the specified column for all rows in the group.                                                              |
| SUM(column)               | Finds the sum of all numerical values in the specified column for the rows in the group.                                                          |
