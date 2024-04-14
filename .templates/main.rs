fn fn_name(n: i32) -> i32 {
    n
}

fn main() {
    let testcases: Vec<(i32, i32)> = vec![(1, 1)];

    for (values, expected) in testcases {
        assert_eq!(fn_name(values), expected);
    }
}
