use std::collections::{HashMap, HashSet};

pub fn word_pattern(pattern: String, s: String) -> bool {
    if pattern.len() != s.matches(" ").count() + 1 {
        return false;
    }

    let mut map = HashMap::<char, &str>::new();
    let mut word_set = HashSet::<&str>::new();

    for (glyph, word) in pattern.chars().zip(s.split_ascii_whitespace()) {
        match map.insert(glyph, word) {
            None => {
                if !word_set.insert(word) {
                    return false;
                }
            }
            Some(value) => {
                if value != word {
                    return false;
                }
            }
        }
    }

    true
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            ("abba", "dog cat cat dog", true),
            ("abba", "dog cat cat rat", false),
            ("aaaa", "dog cat cat dog", false),
            ("abba", "dog dog dog dog", false),
            ("aaa", "dog dog dog dog", false),
        ];

        for (pattern, words, expected) in tests.iter() {
            assert_eq!(
                word_pattern(String::from(*pattern), String::from(*words)),
                *expected
            );
        }
    }
}
