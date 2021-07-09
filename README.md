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

To install the full game package, type
```sh
$ python3 -m pip install --user git+https://github.com/Rasalhague2020/python-project-lvl1.git
```
When the package `hexlet-code` is installed will be able to run games using the built-in scripts.

### Running games

To start the **Even** game, type
```sh
$ brain-even
```

To start the **Calc** game, type
```sh
$ brain-calc
```

To start the **GCD** game, type
```sh
$ brain-gcd
```

To start the **Progression** game, type
```sh
$ brain-progression
```

To start the **Prime** game, type
```sh
$ brain-prime
```

### Video tutorial

The process of installation and playing:
[![asciicast](https://asciinema.org/a/v7J4p7nv8PjFKQPL22asg5j7e.svg)](https://asciinema.org/a/v7J4p7nv8PjFKQPL22asg5j7e)

### Delete package

After getting a lot of fun (of course you do!) from the process of playing these little puzzles you could easily delete this package.

Just type
```sh
$ python3 -m pip uninstall hexlet-code
```


[hex-py1]:<https://ru.hexlet.io/professions/python/projects/49>
[gcd]:<https://en.wikipedia.org/wiki/Greatest_common_divisor>
[prime]:<https://en.wikipedia.org/wiki/Prime_number>