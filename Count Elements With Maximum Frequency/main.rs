use std::collections::HashMap;

fn main() {
    assert_eq!(max_frequency_elements(vec![1, 2, 2, 3, 1, 4]), 4);
    assert_eq!(max_frequency_elements(vec![1, 2, 3, 4, 5]), 5);
}

pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
    let frequencies = nums.iter().copied().fold(HashMap::new(), |mut acc, val| {
        acc.entry(val).and_modify(|freq| *freq += 1).or_insert(1);
        acc
    });

    let values: Vec<i32> = frequencies.values().copied().collect();

    let max_value = values.iter().max().expect("max value wasn't found");

    let max_value_freq = frequencies.iter().fold(0, |acc, val|{
        if val.1 == max_value {
            return acc + 1
        }

        acc
    });

    max_value * max_value_freq
}
