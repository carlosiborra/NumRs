/// main.rs is the entry point of the program in Rust


#[no_mangle]  // Not to mangle the name of the function, not interfere with the name of the function in the Python code
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    a + b
}