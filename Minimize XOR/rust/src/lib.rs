use std::cmp::Ordering::{Equal, Greater, Less};

pub fn f(num1: i32, num2: i32) -> i32 {
    let nb1 = num1.count_ones();
    let nb2 = num2.count_ones();

    match nb1.cmp(&nb2) {
        Less => (nb1..nb2).fold(num1, |acc, _| acc | acc + 1),
        Equal => num1,
        Greater => (nb2..nb1).fold(num1, |acc, _| acc & acc - 1),
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![(3, 5, 3), (1, 12, 3), (12, 1, 8), (25, 72, 24)];

        for (a, b, expected) in tests.iter() {
            assert_eq!(f(a.clone(), b.clone()), *expected);
        }
    }
}
