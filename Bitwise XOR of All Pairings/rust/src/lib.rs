pub fn f(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
    let a = if nums2.len() % 2 == 1 {
        nums1.iter().fold(0, |acc, val| acc ^ val)
    } else {
        0
    };

    let b = if nums1.len() % 2 == 1 {
        nums2.iter().fold(0, |acc, val| acc ^ val)
    } else {
        0
    };

    a ^ b
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            (vec![2, 1, 3], vec![10, 2, 5, 0], 13),
            (vec![1, 2], vec![3, 4], 0),
        ];

        for (a, b, expected) in tests.iter() {
            assert_eq!(f(a.clone(), b.clone()), *expected);
        }
    }
}
