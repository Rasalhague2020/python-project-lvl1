# Python course - project #1

[![Maintainability](https://api.codeclimate.com/v1/badges/c1894ba5ed3bfd905f78/maintainability)](https://codeclimate.com/github/Rasalhague2020/python-project-lvl1/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/c1894ba5ed3bfd905f78/test_coverage)](https://codeclimate.com/github/Rasalhague2020/python-project-lvl1/test_coverage) [![Build Status](https://travis-ci.org/Rasalhague2020/python-project-lvl1.svg?branch=master)](https://travis-ci.org/Rasalhague2020/python-project-lvl1)


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
$ make install
```

To start the **Even** game, type
```sh
$ poetry run brain-even
```

To start the **Calc** game, type
```sh
$ poetry run brain-calc
```

To start the **GCD** game, type
```sh
$ poetry run brain-gcd
```

To start the **Progression** game, type
```sh
$ poetry run brain-progression
```

To start the **Prime** game, type
```sh
$ poetry run brain-prime
```

Installation guide and showing the games progress:
[![asciicast](https://asciinema.org/a/Ot0p5LFsPkGfjLkAJM4XNP4GU.svg)](https://asciinema.org/a/Ot0p5LFsPkGfjLkAJM4XNP4GU)


[hex-py1]:<https://ru.hexlet.io/professions/python/projects/49>
[gcd]:<https://en.wikipedia.org/wiki/Greatest_common_divisor>
[prime]:<https://en.wikipedia.org/wiki/Prime_number>