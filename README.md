# htmlishell

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/PerchunPak/htmlishell/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/htmlishell/actions?query=workflow%3Atest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/htmlishell)](https://www.python.org/downloads/)

A super simple HTML to bash compiler, inspired by [this moment](https://youtu.be/mokGJiXVw_4?t=1384).

```
htmlishell
 |  |^^^^^
 |  \because with sh it didn't sound
 \   what Primagen likes
  I hate JS so much so I won't do react, but rather just html   
```

## Examples

I am too dumb (and lazy too) to do all the bash spec, so I just did a few features.

### Simple `ls`

```html
<ls />
```

Transforms into

```bash
ls
```

### `ls` with arguments

```html
<ls>
  <all />
</ls>
```

Transforms into

```bash
ls --all
```

### `ls` with short arguments

```html
<ls>
  <all />
  <l short=true />
</ls>
```

Transforms into

```bash
ls --all -l
```

## Installing

Do not use `pip` for Python packages (see [this](https://packaging.python.org/en/latest/specifications/externally-managed-environments/#externally-managed-environments)).
TLDR: not venv-wide `pip` installation may break your system, use [`pipx`](https://pipx.pypa.io/stable/installation/) (it will manage venvs for you).

```bash
pipx install htmlishell
```

Then run

```bash
htmlishell ./path/to/your/file.html
```

## Installing for local developing

```bash
git clone https://github.com/PerchunPak/htmlishell.git
cd htmlishell
```

### Installing `poetry`

Next we need install `poetry` with [recommended way](https://python-poetry.org/docs/master/#installation).

If you use Linux, use command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you use Windows, open PowerShell with admin privileges and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installing dependencies

```bash
poetry install
```

### If something is not clear

You can always write to me!

## Thanks

This project was generated with [python-template](https://github.com/PerchunPak/python-template).
