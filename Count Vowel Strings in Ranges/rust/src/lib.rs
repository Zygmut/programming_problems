use std::collections::HashSet;

fn is_valid(word: &str, vowels: &HashSet<char>) -> bool {
    vowels.contains(&word.chars().next().unwrap())
        && vowels.contains(&word.chars().last().unwrap())
}

pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
    let vowels: HashSet<char> = HashSet::from(['a', 'e', 'i', 'o', 'u']);

    let prefix: Vec<i32> = vec![0].into_iter().chain(words.iter()
    .scan(0, |state, word| {
        *state += is_valid(word, &vowels) as i32;
        Some(*state)
    })).collect();

    queries
        .iter()
        .map(|elem| {
            let left = elem[0] as usize;
            let right = (elem[1] + 1) as usize;

            prefix[right] - prefix[left]
        })
        .collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            (
                vec![
                    String::from("aba"),
                    String::from("bcb"),
                    String::from("ece"),
                    String::from("aa"),
                    String::from("e"),
                ],
                vec![vec![0, 2], vec![1, 4], vec![1, 1]],
                vec![2, 3, 0],
            ),
            (
                vec![String::from("a"), String::from("e"), String::from("i")],
                vec![vec![0, 2], vec![0, 1], vec![2, 2]],
                vec![3, 2, 1],
            ),
        ];

        for (words, queries, expected) in tests.iter() {
            assert_eq!(vowel_strings(words.clone(), queries.clone()), *expected);
        }
    }
}
