#[allow(dead_code)]
pub fn one_liner(words: Vec<String>, pref: String) -> i32 {
    words.iter().fold(0, |acc, item| {
        acc + (item.len() >= pref.len() && item[..pref.len()] == pref) as i32
    })
}

#[allow(dead_code)]
pub fn naive(words: Vec<String>, pref: String) -> i32 {
    let mut sol = 0;
    for word in words {
        if word.len() < pref.len() {
            continue;
        }

        if word[..pref.len()] == pref {
            sol += 1;
        }
    }
    sol
}

pub fn f(words: Vec<String>, pref: String) -> i32 {
    words
        .iter()
        .filter(|word| word.len() >= pref.len() && word[..pref.len()] == pref)
        .count() as i32
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
                (vec![String::from("pay"),String::from("attention"),String::from("practice"),String::from("attend")], String::from("at"), 2),
                (vec![String::from("leetcode"),String::from("win"),String::from("loops"),String::from("success")], String::from("code"), 0),
                (vec![String::from("jqclbnvrbpdivpsrnlziatmqxxezmcalpnzuczafqpdpdcyuckdddylevyemabynhxrvnjakjlsglcfnylldll"),String::from("wzpsyqbydaaqyhjmbwfdvkgeyu"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmurkreyfyvraojedbdoxec"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmutmjfwmcammqvodenwxatsouojdgdpkxsabgve"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmuzsndtnkhdzrcgtkzeafa"),String::from("cciaewsuyzccnzziczcmuaohsnudsuptlgrdzzryajluaxghxbwf"),String::from("amtodzsovkmgdlw"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmuiqvnsluuynyblohrhhlqhakkcdabwklwsk"),String::from("cqgytlphkffnmmmahesxelsicqyjyfullvymoqceemtnpyfgejcnabjeinljtfespnwvftldcholuujys"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmunyockixnilatozvfkyqpbzcfnkpexbghjsklu"),String::from("wqhngwactepbsbmqahnjannhssnyazgbnrfygfqdpddqpotffkcgvepfmfmjvinpayfgkeimywrdfiisndvavkuuzdydvd"),String::from("gtahklmdpknhtzdxfxherktwctnwvrjudmmtyqtqxohzeziimvbus"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmunbzcuaekqqhwozxdnldfb"),String::from("egfkuytqptzqewpweeokurqmnqiyqdyeihucxzmgdu"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmutcgvtqoxgmwjmqdckyksnpgqbncsljzbpkpdy"),String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmuhzxpkltm"),String::from("kbvytpxvmuojitddvttknckrtbxhkobijobcv")], String::from("kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmu"), 8)
        ];

        for (words, prefix, expected) in tests.iter() {
            assert_eq!(f(words.clone(), prefix.clone()), *expected);
        }
    }
}
