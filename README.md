# Sample BDD Project with Python Behave 
A simple demonstration project using _[behave](https://behave.readthedocs.io/en/latest/)_ in a Python 3 project.
For more information concerning _Behaviour Driven Development_ (BDD) take a read of the excellent summary available at [cucumber.io](https://cucumber.io/docs/bdd/)

## The Initial Requirement
Imagine a simple requirement to look up and check whether a _string_ represents a valid UK postal code and to see what administrative unit in the UK that postcode falls within.
The very simple behaviour of the postcode look-up is described in the [uk-postcode.feature](features/uk-postcode.feature) file written in [Gherkin](https://cucumber.io/docs/gherkin/reference) style natural language.

## Behaviour Driven
Note the atomic commits to this repo.  The initial commit started with describing the initial behaviour, implementing a test for that behaviour in some _step definitions_ and having that call a very simple stub before actually writing any application code.
The order of tasks should be something like:
* define and agree the initial behaviour of an application or function
* add a dummy stub app to see the BDD _scenario_ running and passing
* refine and elaborate the behaviour further if necessary in a [3 amigos session](https://www.velocitypartners.net/blog/2014/02/11/the-3-amigos-in-agile-teams/)
* write an initial app or function with associated unit tests
* replace the stub with actual application code

## Running This Project
Using Python [poetry](https://python-poetry.org/docs/) or pip via your IDE, ensure the dependencies listed in the [pyproject.toml](pyproject.toml) are installed into your _venv_.
Run ```behave```

```
$ behave
...
2 features passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
9 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.007s

```