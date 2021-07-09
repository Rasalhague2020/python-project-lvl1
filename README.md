# Python course - project #1

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Rasalhague2020/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/Rasalhague2020/python-project-lvl1/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ade59b3a54212ff47124/maintainability)](https://codeclimate.com/github/Rasalhague2020/python-project-lvl1/maintainability)
![example workflow](https://github.com/Rasalhague2020/python-project-lvl1/actions/workflows/main.yml/badge.svg)


This is my first Python project on the Hexlet platform.
See details on [Hexlet site (russian language only)][hex-py1].

The first python project is a set of simple programs united by a common logic of work.
This set contains games such as:

* Even - You need to specify whether the number is even or not three times.
* Calc - You need to specify the correct answer for the simplest arithmetic expression three 
times.
* GCD - You need to specify the greates common divisor ([GCD][gcd]) for two numbers three times.
* Progression - You need to specify the missing number in the arithmetic progression three times.
* Prime - You need to specify whether the number is [prime][prime] or not three times.


### Installation

First of all you should create virtual enviroment via `venv`
```sh
$ python3 -m venv brain_games_env
```
and than activate this enviroment by
```sh
$ source brain_games_env/bin/activate
```
This will allow you to install package in an isolated location and you can easily delete this package in the future. 
To install the full game package, type
```sh
(brain_games_env)$ pip install -i https://test.pypi.org/simple/ Rasalhague2020_brain_games --extra-index-url https://pypi.org/simple/
```
When the package `Rasalhague2020_brain_games` is installed in your virtual enviroment you will be able to run games using the built-in scripts.

### Running games

To start the **Even** game, type
```sh
(brain_games_env)$ brain-even
```

To start the **Calc** game, type
```sh
(brain_games_env)$ brain-calc
```

To start the **GCD** game, type
```sh
(brain_games_env)$ brain-gcd
```

To start the **Progression** game, type
```sh
(brain_games_env)$ brain-progression
```

To start the **Prime** game, type
```sh
(brain_games_env)$ brain-prime
```

### Video tutorial

The process of installation and playing:
[![asciicast](https://asciinema.org/a/Ot0p5LFsPkGfjLkAJM4XNP4GU.svg)](https://asciinema.org/a/Ot0p5LFsPkGfjLkAJM4XNP4GU)

### Delete package

After getting a lot of fun (of course you do!) from the process of playing these little puzzles you could easily delete this package just by deleting your virtual enviroment directory.
For instance in our case just type
```sh
(brain_games_env)$ deactivate
```
and than delete `brain_games_env` directory
```sh
$ rm -r brain_games_env/
```

[hex-py1]:<https://ru.hexlet.io/professions/python/projects/49>
[gcd]:<https://en.wikipedia.org/wiki/Greatest_common_divisor>
[prime]:<https://en.wikipedia.org/wiki/Prime_number>