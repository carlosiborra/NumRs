/// main.rs is the entry point of the program in Rust


#[no_mangle]  // Not to mangle the name of the function, not interfere with the name of the function in the Python code
pub extern "C" fn sum(arr: *const i32) -> i32 {
    /// Sum of numbers in an array
    /// :param a: pointer to the array
    /// :param n: length of the array
    /// :return: sum of the array
    let sum = arr.iter().fold(0, |acc, x| acc + x);
    sum // return the sum
}