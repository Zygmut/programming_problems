pub fn f(derived: Vec<i32>) -> bool {
    derived.iter().fold(0, |acc, val| acc ^ val) == 0
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            (vec![1, 1, 0], true),
            (vec![1, 1], true),
            (vec![1, 0], false),
        ];

        for (derived, expected) in tests.iter() {
            assert_eq!(f(derived.clone()), *expected);
        }
    }
}
