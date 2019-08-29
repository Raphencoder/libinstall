## Description

### This project is under construction.

  Libinstall allows you to install all requirements python libraries of a repo that don't contain 'requirements.txt.'

  It's using the return of the shell to know which libraries is missing and installed it.

  Many errors still occured thought.

## How to use:

  First you need to install the library:

````
pip install libinstall
````

Then go to the folder you want to install the libraries to, and simply run the main file of the project.

For example if the main file is a file named 'main.py' then simply run

````
libinstall main.py
````

There also is a "--all" option that allows you to run all file in the directory. But you still have to put a file after -all options.

````
libinstall --all main.py
````

## Suggestion

If you have some errors or suggestion or you want to improve this project, feel free to create a pull request or open an issue.
