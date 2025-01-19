use std::{fs::File, io::Read};

// First version 0.034 s

pub fn main() {
    // Read contents of the file
    let mut file = File::open("../input.txt").expect("Unable to open the file");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("Unable to read the contents of the file");

    // Parse contents
    let lines = contents.split("\r\n").collect::<Vec<_>>();

    // Populate Vectors
    let (mut first, mut second) = (Vec::<i32>::with_capacity(lines.len()), Vec::<i32>::with_capacity(lines.len()));

    for line in lines{
        let numbers = line.split_whitespace().collect::<Vec<&str>>();

        first.push(numbers[0].parse::<i32>().expect("Unable to parse first number"));
        second.push(numbers[1].parse::<i32>().expect("Unable to parse first number"));
    }

    // Sort
    first.sort();
    second.sort();

    // Calculate
    let result: i32 = first.iter().zip(second.iter()).map(|(a, b)| {
        (a-b).abs()
    }).sum();

    println!("{}", result)
}