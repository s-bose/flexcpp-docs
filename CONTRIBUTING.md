# Contributing

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

Contributions are welcome, and they are greatly appreciated! Every bit helps, and credit always be given. You can contribute in many ways.

## Types of Contributions

### Report Errors / deprecated info in the docs

Report bugs at https://github.com/s-bose/flexcpp-docs/issues

If you are reporting a error in the documentation, please include:
+ Which page you noticed the mistake
+ The location of the error
+ What you suggest is the right thing.

### Write Documentation

This is a documentation project itself, so we could always use more documentation and examples in this repo.

#### Get Started!

Ready to contribute? Here's how to set up `flexcpp-docs` for local development

1. Fork the `flexcpp-docs` repo on [GitHub](https://github.com/s-bose/flexcpp-docs).
2. Clone your fork locally:
```bash
$ git clone git@github.com:your_username_here/flexcpp-docs.git
```
3. Installing the dependency
```bash
$ pip install mkdocs
```
3. Serve the documentations locally,
```bash
$ mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 1.28 seconds
INFO     -  [00:00:00] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [00:00:10] Serving on http://127.0.0.1:8000/
INFO     -  [00:00:15] Browser connected: http://localhost:8000/
```

Now if you make some changes to the existing markdown files the server will reload and you would be able to see the changes taking place live at [localhost:8000](http://localhost:8000/)

#### Adding new page to the documentation

If you want to add any new page to the project, do the following

1. Create a new `*.md` file inside the `docs` directory.
2. Obviously write stuff in appropriate format.
3. Add the file inside the `nav` list in the `mkdocs.yml` file at the root of the project.

**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://kcd.im/pull-request)