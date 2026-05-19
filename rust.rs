const PI: f32 = 3.14159;

fn add(x: i32, y: i32) -> i32 {
    // x and y are parameters of the function
    // arguments are data used when calling the function
    return x + y;
}

fn subtract(x: i32, y: i32) -> i32 {
    x - y
}

fn swap(x: i32, y: i32) -> (i32, i32) {
    return (y, x);
}
fn make_nothing() -> () {
    return ();
}

fn make_nothing2() {}  // the return type is implied as ()

fn example() -> i32 {
    let x = 42;
    // Rust's ternary expression
    let v = if x < 42 { -1 } else { 1 };

    let food = "hamburger";
    let result = match food {
        // notice the braces {} are optional when its just a single return expression
        "hotdog" => "is hotdog",
        _ => "is not hotdog",
    };

    let v = {
        // This scope block lets us get a result without polluting function scope
        let a = 1;
        let b = 2;
        a + b
    };

    // The idiomatic way to return a value in rust from a function at the end
    v + 4
}

fn main() {
    // I. variables (always in snake_case)
    let x;
    x = 0;  // Rust can also declare and initialize later, but this is rarely done
    
    let mut x = 42;  // Mutable values are denoted with a mut keyword
    x = 13;

    let x = 13;  // Rust infers the type of x, by default this is i32
    let x: f64 = 3.14159; // Rust can also be explicit about the type, by default this is f64
    let x = 3.14159f32; // explicitly specified by appending the type to the end
    let t = (13, false);  // tuples are fixed size, t.0, t.1
    let nums: [i32; 3] = [1, 2, 3];  // arrays are fixed size of similar elements
    println!("{:?} {}", nums, nums[1]);
    let ferris = '🦀'; // a unicode character
    let sentence = "hello world!";

    let a = 13u8;
    let b = 7u32;
    let c = a as u32 + b;
    println!("{}", c as u8);

    let result = swap(123, 321);  // return a tuple of return values
    println!("{} {}", result.0, result.1);
    
    let (a, b) = swap(result.0, result.1);  // destructure the tuple into two variables names
    println!("{} {}", a, b);

    // II. basic control flow
    if x < 42 {  // ==, !=, <, >, <=, >=, !, ||, &&
        println!("less than 42");
    } else if x == 42 {
        println!("is 42");
    } else {
        println!("greater than 42");
    }

    loop {
        x += 1;
        if x == 42 {
            break;
        }
    }

    let v = loop {
        x += 1;
        if x == 13 {
            break "found the 13";  // return
        }
    };

    while x != 42 {
        x += 1;
    }

    // from any expression that evaluates into an iterator
    for x in 0..5 {  // excluding 5
        println!("{}", x);
    }

    for x in 0..=5 {  // including 5
        println!("{}", x);
    }

    match x {
        0 => {
            println!("found zero");
        }
        1 | 2 => {  // we can match against multiple values
            println!("found 1 or 2!");
        }
        3..=9 => {  // we can match against ranges
            println!("found a number 3 to 9 inclusively");
        }
        matched_num @ 10..=100 => {  // we can bind the matched number to a variable
            println!("found {} number between 10 to 100!", matched_num);
        }
        _ => {  // this is the default match that must exist if not all cases are handled
            println!("found something else!");
        }
    }
}