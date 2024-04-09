# My first Python App

Simple Python scripts, first look at ETL and use of Venv

## Scripts folder

Some Python scripts to lear how this language works:

- [How to print something on the terminal](./scripts/hello.py)
- [How to create variables](./scripts/variables.py)
- [How to create and use functions](./scripts/functions.py)
- [How to perform flow control](./scripts/flow-control.py)
- [How to create list, iterate it and add new
  values](./scripts/loops-and-lists.py)
- [How to install, import and use Pandas library](./scripts/basic-pandas.py)

## Star Wars Extract, Transform and Load (ETL)

An example opf how works ETL. In this exercise I extract data about some
characters of Star Wars. Then, I create a new column and a new table with the
data filtered. At the end, I load each table in a file to save the changes.

Take a look at the [statement](./star-wars-character-etl/statement.md) and the
[source code](./star-wars-character-etl/etl_star_wars.py).

## Virtual Environment

As a `Python beginner` I miss some kind of `package.json` or `node_modules` like
in any `JS` project with tooling. When I told that to a experienced programmer
he suggested me to take a look to `venv`. So I going to use this section as a
PKB of this topic for future me and anyone who reads this.

The steps are similar in Linux and Windows. However, when it differs I will
specify it.

### Installation

- Linux

  In order to use `venv` you might install it. The specific version of this
  library depends on your current `Python` version. In my case, it was 3.11.2:

  ```bash
  sudo apt install python3.11-venv
  ```

- Windows

  You don't need to install anything because it is installed when you install
  Python.

### Creation

Then, creating a `Virtual Environment` is made with the following command:

- Linux

  ```bash
  python3 -m venv .venv
  ```

- Windows

  ```bash
  python -m venv .venv
  ```

Let's take a look to this command:

- `-m`: flag for `modules`.
- `.venv`: the name of the virtual environment. This could be whatever you want.

### Activation

To use this virtual environment you need to activate it. The steps differ
between Linux and Windows:

- Linux

  ```bash
  source .venv/bin/activate
  ```

- Windows

  ```cmd
  .venv/Scripts/activate
  ```

In your terminal you should see the name of the virtual environment that is
activated between parenthesis:

```txt
(.venv) username@hostname:~/my-first-python-app$
```

### Installing dependencies

Then, you can install any library, for example `pandas` and it will remain
isolated inside this virtual environment:

```bash
pip install pandas
```

### Deactivation

If you want to stop the virtual environment, it's as simple as `deactivate` it:

```bash
deactivate
```

So your terminal will no longer display the venv name:

```txt
username@hostname:~/my-first-python-app$
```

### Recreating Virtual Environments

In JS projects, when you install any library, it's name and version is
automatically store inside `package.json`. So if you clone a repository, you can
clone the environment too. If you want to do so with Python, you must do it
manually `with the virtual environment activated`.

1. List packages:

    ```bash
    pip freeze
    ```

    ```txt
    (.venv) username@hostname:~/my-first-python-app$ pip freeze
    numpy==1.26.3
    pandas==2.1.4
    python-dateutil==2.8.2
    pytz==2023.3.post1
    six==1.16.0
    tzdata==2023.4
    ```

1. Save this list inside `requirements.txt` using the greater than (>) operator:

    ```bash
    pip freeze > requirements.txt
    ```

    ```txt
    (.venv) username@hostname:~/my-first-python-app$ cat requirements.txt
    numpy==1.26.3
    pandas==2.1.4
    python-dateutil==2.8.2
    pytz==2023.3.post1
    six==1.16.0
    tzdata==2023.4
    ```

    Don't forget to add `requirements.txt` to `Version Control` or you won´t be able
    to recreate your environment.

Once `requirements.txt` has been created, you can recreate the environment
whatever you want with `pip` command:

```bash
pip install -r requirements.txt
```

## Bugs or suggestions

If you found a bug or have a suggestion please don't hesitate to contact me or
open an
[issue on GitHub](https://github.com/pablocru/hello-python/issues).
