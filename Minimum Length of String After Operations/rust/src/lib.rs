use std::collections::HashMap;

pub fn f(s: String) -> i32 {
    let mut is_even: HashMap<char, bool> = HashMap::new();

    for ch in s.chars() {
        let even = is_even.entry(ch).or_insert(true);
        *even = !*even;
    }

    is_even.len() as i32 + is_even.values().map(|&b| b as i32).sum::<i32>()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![(String::from("abaacbcbb"), 5), (String::from("aa"), 2)];

        for (words, expected) in tests.iter() {
            assert_eq!(f(words.clone()), *expected);
        }
    }
}
