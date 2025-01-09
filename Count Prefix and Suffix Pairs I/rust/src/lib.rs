pub fn f(words: Vec<String>) -> i32 {
    let mut sol = 0;

    for idx1 in 0..words.len() {
        for idx2 in (idx1 + 1)..words.len() {
            let prefix = words[idx2].starts_with(&words[idx1]);
            let sufix = words[idx2].ends_with(&words[idx1]);

            sol += (prefix && sufix) as i32
        }
    }

    sol
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            (
                vec![
                    String::from("a"),
                    String::from("aba"),
                    String::from("ababa"),
                    String::from("aa"),
                ],
                4,
            ),
            (
                vec![
                    String::from("pa"),
                    String::from("papa"),
                    String::from("ma"),
                    String::from("mama"),
                ],
                2,
            ),
        ];

        for (words, expected) in tests.iter() {
            assert_eq!(f(words.clone()), *expected);
        }
    }
}
