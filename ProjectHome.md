## Overview ##

Python library for querying/updating Saleforce.com data via SOAP API

A distutils packaged version of the beatbox module by Simon Fell http://www.pocketsoap.com/beatbox/

This module contains 2 versions of the Salesforce client. XMLClient which is the original beatbox version of the client which returns xmltramp objects and PythonClient which returns dicts with proper python data types. ie integer fields return integers.

### History ###

This code was previously hosted at https://svn.plone.org/svn/collective/beatbox for use in various Plone-related Salesforce projects. Since beatbox can be used by other Python projects (and is not exclusive to Plone) we've moved the project here.

## Setup Instructions ##

Just install this for Python 2.4 via EasyInstall from the CheeseShop:

```
easy_install-2.4 beatbox
```

## Checkout Instructions ##

1. The source code is available here:

```
svn co http://salesforce-beatbox.googlecode.com/svn/trunk/ beatbox
```

2. See README.txt