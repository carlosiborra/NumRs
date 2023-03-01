use libloading::{Library, Symbol}; // Used to load the library at runtime and get the function pointer to the function

fn main() {
    // Load the library at runtime
    let lib = unsafe { Library::new("libNumRS.dll").unwrap() };
    // Get the function pointer to the function (reference)
    let hello_world: Symbol<unsafe extern "C" fn() -> &'static str> = unsafe { lib.get(b"hello_world").unwrap() };
    // Call the function
    let result = unsafe { hello_world() };
    println!("Result: {}", result);
}


