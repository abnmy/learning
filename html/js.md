# Javascript

## The Goals of modularity

* Higher-level abstractions
* Encapsulation
* Reusability
* Simplify dependency management

Popularity leads to bigger apps and bigger apps lead to greater complexity.

Packaging and distribution is hard.

Reducing Global Scope Pollution with **IIFE**, Immediately Invoked Function Expression, an anonymous function invoked when declared

```js
function foo () {
    /* process */
}

(function() {
    /* process */
})();

(function(name) {
    console.log(name);
})('Bob');
```

Revealing Module Pattern, adds one value to global scope per module. It can be implemented as Singleton or as Constructor function.

```js
function foo () {
    /* process */
}
```

## Evolution

from AMD & CommonJS (ES 5) to ES2015 (ES 6)

```js
/* logger.js */
function log(name) {console.log(name);}

exports.log = log;
module.exports.log = log;
module.exports = {log: log};

/* ES6 */
export default function log(name) {console.log(name);}

/* ES6 bis */
export { log };
```

```js
/* CommonJS */
var player = require('./player.js');
player.score;

/* ES6 */
import * as player from './player.js';
player.score;

import logger from './logger.js'; /* it works with export default */

/* ES6 bis */
import { score as player_score } from './player.js';
player_score;
```

## Babel

to transpile ES6 to ES5 to works on old web browsers

## Bundler

to merge multiple file in only one bundle.js

first generation: Browserify

second generation: Webpack