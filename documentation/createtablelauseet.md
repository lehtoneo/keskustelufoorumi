# CREATE TABLE-lauseet


## Thread

```SQL
CREATE TABLE thread (
        id INTEGER NOT NULL,
        posted DATETIME,
        modified DATETIME,
        title VARCHAR NOT NULL,
        description VARCHAR,
        user_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES user (id)
)
```

## Comment 

```SQL
CREATE TABLE comment (
        id INTEGER NOT NULL,
        posted DATETIME,
        modified DATETIME,
        comment_text VARCHAR NOT NULL,
        user_id INTEGER NOT NULL,
        thread_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES user (id),
        FOREIGN KEY(thread_id) REFERENCES thread (id)
)
```

## User

```SQL
CREATE TABLE user (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)
```

## Category

```SQL
CREATE TABLE category (
        id INTEGER NOT NULL,
        name VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
)
```

## Role

```SQL
CREATE TABLE role (
        id INTEGER NOT NULL,
        role VARCHAR NOT NULL,
        PRIMARY KEY (id)
)
```

## Thread_Category

```SQL
CREATE TABLE thread_category (
        id INTEGER NOT NULL,
        thread_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(thread_id) REFERENCES thread (id),
        FOREIGN KEY(category_id) REFERENCES category (id)
)
```

## User_Role

```SQL
CREATE TABLE user_role (
        id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        role_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES user (id),
        FOREIGN KEY(role_id) REFERENCES role (id)
)
```

