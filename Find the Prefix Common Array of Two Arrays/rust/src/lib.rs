pub fn f(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    let mut freq = vec![0; a.len() + 1];
    let mut sol = vec![0; a.len()];

    for idx in 0..a.len() {
        let a_idx = a[idx] as usize;
        freq[a_idx] += 1;

        if freq[a_idx] == 2 {
            sol[idx] += 1;
        }

        let b_idx = b[idx] as usize;
        freq[b_idx] += 1;

        if freq[b_idx] == 2 {
            sol[idx] += 1;
        }

        sol[idx] += if idx > 0 { sol[idx - 1] } else { 0 }
    }

    sol
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            (vec![1, 3, 2, 4], vec![3, 1, 2, 4], vec![0, 2, 3, 4]),
            (vec![2, 3, 1], vec![3, 1, 2], vec![0, 1, 3]),
        ];

        for (a, b, expected) in tests.iter() {
            assert_eq!(f(a.clone(), b.clone()), *expected);
        }
    }
}
