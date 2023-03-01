/// main.rs is the entry point of the program in Rust

// ! rustc --crate-type=dylib lib.rs -o libNumRS.dll // Compile the library to a dynamic library
// ! Py03

// #[no_mangle]  // Not to mangle the name of the function, not interfere with the name of the function in the Python code
// /// Sum of numbers in an array
// pub extern "C" fn sum(arr: *const i32) -> i32 {
//     let sum = arr.iter().fold(0, |acc, x| acc + x);
//     sum // return the sum
// }

#[no_mangle]
/// Basic function to print "Hello World"
pub extern "C" fn hello_world() -> &'static str {
    return "Hello World";
}

// rustc --crate-type=dylib lib.rs -o libNumRs.dll // Compile the library to a dynamic library