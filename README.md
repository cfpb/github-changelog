# github-changelog

This is a small utility that generates a changelog between two git tags based on GitHub pull request titles as either plaintext or markdown.

An example might look like:

- Improve test coverage for mygreatpackage.subpackage [#1234]()
- Add support for Python 3 [#1233]()

## Installing

```
pip install git+https://github.com/cfpb/github-changelog
```

## Using

```
changelog [-h] [-m] OWNER REPO PREVIOUS [CURRENT]
```

The `changelog` command that takes a GitHub repository owner (user or organization), repository name, and at least one tag as arguments. With those arguments it will list all GitHub pull requests that have been merged between the given tags or between the tag and `HEAD` if only one tag is given. If `-m` is specified the output will be formatted in markdown and include links to the pull requests.

### Examples

```
changelog cfpb github-changelog 1.0.0
```

Will generate a text changelog between `1.0.0` and `HEAD`.

```
changelog -m cfpb github-changelog 1.0.0 1.0.1
```

Will generate a markdown changelog between `1.0.0` and `1.0.1`.

## Getting help

Please add issues to the [issue tracker](https://github.com/cfpb/wagtail-flags/issues).

## Getting involved

General instructions on _how_ to contribute can be found in [CONTRIBUTING](CONTRIBUTING.md).

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)
