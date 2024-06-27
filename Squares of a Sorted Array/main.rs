pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
    let mut res: Vec<i32> = nums.iter().map(|n| n * n).collect();
    res.sort();
    res
}

fn main() {
    let testcases = vec![
        (vec![-4, -1, 0, 3, 10], vec![0, 1, 9, 16, 100]),
        (vec![-7, -3, 2, 3, 11], vec![4, 9, 9, 49, 121]),
    ];

    for (input, expected) in testcases {
        assert_eq!(sorted_squares(input), expected)
    }
}
