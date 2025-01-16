use std::cmp::max;

#[allow(dead_code)]
fn max_score_sightseeing_pair(values: &[i32]) -> i32 {
    let mut max_score: i32 = 0;
    let mut candidate: i32 = values[0];

    for idx in 1..values.len() {
        max_score = max(max_score, candidate + values[idx] - idx as i32);
        candidate = max(candidate, values[idx] + idx as i32)
    }

    max_score
}

#[derive(Debug)]
#[allow(dead_code)]
struct TestCase {
    input: Vec<i32>,
    expected: i32,
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let test_cases = vec![
            TestCase {
                input: vec![8, 1, 5, 2, 6],
                expected: 11,
            },
            TestCase {
                input: vec![1, 2],
                expected: 2,
            },
            TestCase {
                input: vec![1, 3, 5],
                expected: 7,
            },
        ];

        for case in &test_cases {
            assert_eq!(
                max_score_sightseeing_pair(&case.input),
                case.expected,
                "{:?}",
                case
            )
        }
    }
}
