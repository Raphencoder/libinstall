from subprocess import Popen, PIPE
from os import listdir
from os.path import isfile, join, splitext
import click
import random

python_extension = ".py"
mypath = "./"


def install_libraries(lib):
    p = Popen(["pip3", "install", lib], stdout=PIPE, stderr=PIPE)
    while p.poll() is None:
        l = p.stdout.readline()
        click.echo(l.decode("utf-8"))
    click.echo(p.stdout.read().decode("utf-8"))
    output, error = p.communicate()
    if p.returncode != 0:
        click.echo("\n\nERROR occured while installing librairies:")
        return error.decode("utf-8")
    else:
        return False


def get_missing_libraries(traceback):
    tracebacks = traceback.split("\n")
    lib = [elem for elem in tracebacks if "ModuleNotFoundError" in elem]
    if not lib:
        return tracebacks[-5:]
    lib = str(lib)
    lib = lib.split("'")
    click.echo("\n".join(tracebacks[-5:]))
    return lib[-2]


def ispythonfile(pythonfile):
    return isfile(pythonfile) and splitext(pythonfile)[1] == python_extension


def lunch_script(file_name):
    p = Popen(["python3", file_name], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    if p.returncode == 1:
        try:
            if "ModuleNotFoundError" in error:
                pass
        except TypeError:
            error = error.decode("utf-8")
        missing_lib = get_missing_libraries(error)
        if isinstance(missing_lib, list):
            click.echo("\n\nERROR occured while installing librairies:")
            click.echo("\n".join(missing_lib))
            return
        click.echo("Installing " + missing_lib + "")
        error_lib = install_libraries(missing_lib)
        if error_lib:
            click.echo(error_lib)
        else:
            click.echo("Installation of " + missing_lib + " done")
            click.echo("-------------------------------------\n\n")
            lunch_script(file_name)
    return


@click.command()
@click.option("--all", is_flag=True, help="Run all the file in current directory")
@click.argument("file")
def cli(all, file):
    click.echo("Thanks for using lib_install\n\n")
    if all:
        python_files = [f for f in listdir(mypath) if ispythonfile(join(mypath, f))]
        try:
            python_files.remove("setup.py")
        except ValueError:
            pass
        for file_name in python_files:
            click.echo("++++++++++++++++++++++++++++++++")
            click.echo("Starting script for " + file_name + "")
            lunch_script(file_name)
    else:
        lunch_script(file)
