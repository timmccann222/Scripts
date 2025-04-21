# Lesson 16 - Creating tables

When you have new entities and relationships to store in your database, you can create a new database table using the **CREATE TABLE** statement.

The structure of the new table is defined by its table schema, which defines a series of columns. Each column has a name, the type of data allowed in that column, an optional table constraint on values being inserted, and an optional default value.

If there already exists a table with the same name, the SQL implementation will usually throw an error, so to suppress the error and skip creating a table if one exists, you can use the **IF NOT EXISTS** clause.

```sql
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
)
```

## Table data types

| Data Type                            | Description                                                                                                                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INTEGER, BOOLEAN                    | The integer datatypes can store whole integer values like the count of a number or an age. In some implementations, the boolean value is just represented as an integer value of just 0 or 1.              |
| FLOAT, DOUBLE, REAL                 | The floating point datatypes can store more precise numerical data like measurements or fractional values. Different types can be used depending on the floating point precision required for that value.   |
| CHARACTER(num_chars), VARCHAR(num_chars), TEXT | The text based datatypes can store strings and text in all sorts of locales. The distinction between the various types generally amounts to underlying efficiency of the database when working with these columns. |
| DATE, DATETIME                      | SQL can also store date and time stamps to keep track of time series and event data. They can be tricky to work with especially when manipulating data across timezones.                                   |
| BLOB                                | Finally, SQL can store binary data in blobs right in the database. These values are often opaque to the database, so you usually have to store them with the right metadata to requery them.               |

## Table constraints

Each column can have additional table constraints on it which limit what values can be inserted into that column. This is not a comprehensive list, but will show a few common constraints that you might find useful.

| Constraint           | Description                                                                                                                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRIMARY KEY          | This means that the values in this column are unique, and each value can be used to identify a single row in this table.                                                                                                   |
| AUTOINCREMENT        | For integer values, this means that the value is automatically filled in and incremented with each row insertion. Not supported in all databases.                                                                          |
| UNIQUE               | This means that the values in this column have to be unique, so you can't insert another row with the same value in this column as another row in the table. Differs from `PRIMARY KEY` as it doesn’t have to be a key.  |
| NOT NULL             | This means that the inserted value cannot be `NULL`.                                                                                                                                                                        |
| CHECK (expression)   | Allows you to run a more complex expression to test whether inserted values are valid (e.g., values must be positive, exceed a certain size, start with a prefix, etc.).                                                   |
| FOREIGN KEY          | Ensures that each value in this column corresponds to another value in a column of another table, maintaining referential integrity.                                                                                       |
## Example

Here's an example schema for the Movies table that we've been using in the lessons up to now.

Movies table schema
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    director TEXT,
    year INTEGER, 
    length_minutes INTEGER
);

## Lesson 16 Exercise 

1. Create a new table named Database with the following columns:
– Name A string (text) describing the name of the database
– Version A number (floating point) of the latest version of this database
– Download_count An integer count of the number of times this database was downloaded

This table has no constraints.

```sql
CREATE TABLE database (
    name TEXT,
    version FLOAT,
    download_count INTEGER
);
```
