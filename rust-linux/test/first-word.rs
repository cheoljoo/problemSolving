fn main() {
    let s = String::from("hello world");

    let word = first_word(&s);

    //s.clear(); // Error!

    println!("the first word is: {}", word);            // ok
    println!("the string is: {}", s);           // ok
}

fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
