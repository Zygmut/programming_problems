pub fn ways_to_split_array(nums: Vec<i32>) -> i32 {
    let total_sum = nums.iter().fold(0, |acc, &val| acc + (val as i64));
    let mut left_sum : i64 = 0;

    (0..nums.len() - 1).fold(0, |acc, idx| {
        left_sum += nums[idx] as i64;
        let right_sum = total_sum - left_sum;

        acc + (left_sum >= right_sum) as i32
    })
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            (vec![10,4,-8,7], 2),
            (vec![2,3,1,0], 2),
            ((-99999..=0).rev().collect::<Vec<i32>>(), 70710)
        ];

        for (nums, expected) in tests.iter() {
            assert_eq!(
                ways_to_split_array(nums.clone()),
                *expected
            );
        }
    }
}