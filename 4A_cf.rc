use std::io::{self, Write};

fn main() {
    let mut input = String::new();

    // Read a line of input from the standard input (stdin)
    io::stdin().read_line(&mut input).expect("Failed to read line");

    // Trim any trailing newline characters and parse the input as an integer
    let input: i32 = input.trim().parse().expect("Failed to parse input as an integer");

    if input%2==0 && input!=2{
        print!("YES")
    }
    else{
        print!("NO")
    }
}
