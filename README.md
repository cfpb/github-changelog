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
changelog [-h] [-m] OWNER REPO [PREVIOUS] [CURRENT]
```

The `changelog` command takes a GitHub repository owner (user or organization), repository name and zero, one, or two tags to limit the set of changes to consider. If no tags are provided, the changelog will be computed between the latest tag and `HEAD`. One tag may be provided to set the base tag to compare against `HEAD`. Two tags may be provided to specify both base tag and ending tag. The generated changelog will list all GitHub pull requests that have been merged between the specified or inferred tags. If `-m` is specified the output will be formatted in markdown and include links to the pull requests.

Pull request merges are identified by their commit message, usually taking the form of `Merge pull request #123…`. Pull requests merged with "Squash and merge" are not currently supported.

### Examples

```
changelog cfpb github-changelog
```

Will generate a text changelog between the latest tag and `HEAD`.

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
