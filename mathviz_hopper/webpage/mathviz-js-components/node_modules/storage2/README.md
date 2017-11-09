# storage2
[![Build Status](https://travis-ci.org/pqx/storage2.svg)](https://travis-ci.org/pqx/storage2) [![codecov.io](http://codecov.io/github/pqx/storage2/coverage.svg?branch=master)](http://codecov.io/github/pqx/storage2?branch=master)

One single html5 storage interface for node and browser (`browserify`)

1. `node`: simple memory storage
2. `browser with storage api available`: return storage object directly (`window.localStorage` and `window.sessionStorage`)
3. `browser without storage api`: cookie fallback

### Installation
``` sh
npm install storage2 --save
```
### Usage
``` javascript
var ls = require('storage2').localStorage;
var ss = require('storage2').sessionStorage;
```

For safari private mode, `localStorage` and `sessionStorage` will still be available but storage usage will cause an exception. `localStorage = require('storage2').localStorage` is not recommended and a different variable name like `ls` should always be used.

### API
[Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Storage)
### License
ISC
