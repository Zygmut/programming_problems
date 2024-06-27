use std::{cmp::Ordering, collections::HashSet};

fn main() {
    assert_eq!(intersection(vec![1, 2, 2, 1], vec![2, 2]), vec![2]);
    assert_eq!(intersection(vec![4, 9, 5], vec![9, 4, 9, 8, 4]), vec![4, 9]);
}

pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
    let left = nums1.into_iter().collect::<HashSet<_>>();
    nums2
        .into_iter()
        .filter(|num| left.contains(num))
        .collect::<HashSet<_>>()
        .into_iter()
        .collect::<Vec<_>>()
}

// Using two pointers
pub fn intersection2p(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
    let mut left_set: Vec<i32> = nums1
        .into_iter()
        .collect::<HashSet<_>>()
        .into_iter()
        .collect();
    left_set.sort();

    let mut right_set: Vec<i32> = nums2
        .into_iter()
        .collect::<HashSet<_>>()
        .into_iter()
        .collect();
    right_set.sort();

    let mut left_idx = 0;
    let mut right_idx = 0;

    let mut intersection: Vec<i32> = vec![];

    while left_idx < left_set.len() && right_idx < right_set.len() {
        match left_set[left_idx].cmp(&right_set[right_idx]) {
            Ordering::Greater => right_idx += 1,
            Ordering::Less => left_idx += 1,
            Ordering::Equal => {
                intersection.push(left_set[left_idx]);
                left_idx += 1;
                right_idx += 1;
            }
        }
    }

    intersection
}
