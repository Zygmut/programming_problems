pub fn maximum_odd_binary_number(s: String) -> String {
    let ones = s.chars().filter(|&c| c == '1').count();
    let zeroes = s.chars().filter(|&c| c == '0').count();
    "1".repeat(ones - 1) + &"0".repeat(zeroes) + "1"
}

fn main() {
    let testcases = vec![("010", "001"), ("0101", "1001")];

    for (input, expected) in testcases {
        assert_eq!(maximum_odd_binary_number(input.to_string()), expected)
    }
}
