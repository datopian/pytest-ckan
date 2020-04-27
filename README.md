CKAN 2.8 Pytest Plugin and Fixtures
===================================
This project backports the `pytest` environment for CKAN from CKAN 2.9 to CKAN
2.8. This allows CKAN extension developers to test CKAN plugins built to 
work with CKAN 2.8 as well as CKAN 2.9 or newer using a single unified test
suite. 

This work is entirely based on 
[@wardi's work for ckanext-scheming](https://github.com/ckan/ckanext-scheming/pull/242). 
It has been extracted so it can be re-used by other CKAN extensions.


Installation & Usage
--------------------
To use this in your project:

 * Add this library to your CKAN plugin project
 * Write your tests with pytest (you can use CKAN fixtures as described below)
 * Run `pytest`
 * When tested with CKAN 2.9 or newer, CKAN's built-in pytest plugin and fixtures 
   will be used
 * When tested with older versions of CKAN, the code in `pytest_ckan` will
   be used instead

### Adding to CKAN project

To use this plugin to test your CKAN extension, simply install this library to
your development / testing environment; If you maintain a 
`dev-requirements.txt` or `test-requirements.txt` file you can add this 
library to it. 

### Running Pytest
To enable CKAN testing, simply add `--ckan-ini=<path/to/test.ini>` to your 
`pytest` command, for example:

```bash
pytest --ckan-ini=test.ini ckanext/yourextension/tests
```

### Using CKAN Fixtures in Tests
 
TBD
