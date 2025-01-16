pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
    const MOD: i32 = 1000000007;

    let low = low as usize;
    let high = high as usize;
    let zero = zero as usize;
    let one = one as usize;

    let mut memo = vec![0; high + 1];
    memo[0] = 1;

    (1..=high).fold(0, |mut acc, idx| {
        if idx >= zero {
            memo[idx] += memo[idx - zero]
        }

        if idx >= one {
            memo[idx] += memo[idx - one]
        }

        memo[idx] %= MOD;

        if idx >= low {
            acc = (acc + memo[idx]) % MOD;
        }

        acc
    })
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![(3, 3, 1, 1, 8), (2, 3, 1, 2, 5)];

        for (low, high, zero, one, expected) in tests.iter() {
            assert_eq!(count_good_strings(*low, *high, *zero, *one), *expected);
        }
    }
}
