function function_name(a, b) {
    return a + b;
}
const function_name = function(a, b) {
    return a + b;
}

// arrow
const function_name = (a, b) => {
    return a + b;
}

const function_name = (a, b) => a + b;  // simplification when there is only one statement
const function_name = a => a;  // parantheses are optional whith only one argument

console.log(function_name(2, 3));

// rest parameter
function f(x, ...y) {
    // only one is allowed and it must be at the end 
}

// closure
function outer(x) {
    function inner(y) {
        return x + y;
    }
    return inner
}
const outerReturn = outer(10);
outerReturn(2) // 12

// callback
function foo(bar) {
    bar();
}
foo(function(){  // anonymous function
    console.log('hello');
});

// pure function
// same output from same inputs != impure functions with side effects depend on external parameter

// IIFE - before ES6
(function(){
    console.log();
})()

// recursion
function f(count) {
    if (count === 0) {  // base condition
        return;
    }
    f(count - 1);
}