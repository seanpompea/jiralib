# jiralib

Python functions for working with the Jira Server REST API.

## functions

- `create_issue`
- `do_transition`
- `set_assignee`
- `add_watcher`

## jira_spec data structure

All functions in the library take an argument called `jira_spec`. This should be a map like so:

~~~~
{"user": "myusername"
,"pass": "mypassword"
,"issue-url": "https://z.edu/rest/api/2/issue/"}
~~~~

## running example.py from scratch

`example.py` will create a test ticket; pass the assignee (which should be a username your Jira system recognizes) as an argument. 

    python example.py user1234

## requirements

Compatible with:

* Python 2.7
* Jira Project Management Software 6.4.1

