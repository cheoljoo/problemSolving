# introduction of rust
- documents of rust
    - english : https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/syntax-and-semantics.html
    - korean : https://rinthel.github.io/rust-lang-book-ko/ch02-00-guessing-game-tutorial.html
- leetcode supports rust.
- learn rust using docker
- docker hub container name is rust:latest


## check something in container
- files
    - hello-rust-cargo/src/main.rs
    - hello-rust-cargo/Makefile
    - hello-rust-cargo/Cargo.toml
- docker run -it --rm -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust /bin/sh

## convenience to compile in docker
- i use 2 kinds of alias
    - alias cargo='docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust cargo'
        - host$ cargo run    -> it will compile then remove container. so it download everytime.
    - alias rustit='docker run -it --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust'
        - docker$ cargo run   -> it is in container.   so it is slow at the first time
        - when i need keyboard input as input , this interactive mode is more proper.

## simple rust test
- cd test
- docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust rustc main.rs
- main

## compile and run
- method 1
    - docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust cargo build --release
    - ./target/debug/hello-rust
- method 2
    - docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust cargo run

# Tutorial : Gessing Game
- cd gessing_game
```
$ cargo new guessing_game --bin
     Created binary (application) `guessing_game` project
$ cd guessing_game
$ cargo build
$ cargo run
```
- it takes a &mut String. Rust has a feature called ‘references’, which allows you to have multiple references to one piece of data, which can reduce copying. 
    - ```
        io::stdin().read_line(&mut guess)
            .expect("Failed to read line");
      ```
- [rand crate](https://crates.io/crates/rand) : crate == box : crates.io (package)
    -  It now says extern crate rand. Because we declared rand in our [dependencies], we can use extern crate to let Rust know we’ll be making use of it. This also does the equivalent of a use rand; as well, so we can make use of anything in the rand crate by prefixing it with rand::.
- rust compiler : it gives good explanation when i have the compile error.
    - &secret_number -> &secret_number.to_string()
```
$ cargo run
   Compiling guessing_game v0.1.0 (/usr/src/myapp)
error[E0308]: mismatched types
  --> src/main.rs:24:21
   |
24 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ expected struct `String`, found integer
   |
   = note: expected reference `&String`
              found reference `&{integer}`

error[E0283]: type annotations needed for `{integer}`
```
- guess is string. so guess.cmp want to string as argument variable.  parse() this string slice into another type.  parse can parse into any type that implements the FromStr trait.

# ownership
- [Rust- 러스트의 꽃, Ownership 파헤치기](https://medium.com/@kwoncharles/rust-%EB%9F%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%BD%83-ownership-%ED%8C%8C%ED%97%A4%EC%B9%98%EA%B8%B0-2f9c6b744c38#:~:text=Rust%EB%8A%94%20%EC%98%A4%EB%84%88%EC%8B%AD%EC%9D%84%20%EA%B8%B0%EB%B0%98,%ED%95%B4%EC%A0%9C%20%EC%97%90%EB%9F%AC%EA%B0%80%20%EC%9D%BC%EC%96%B4%EB%82%98%EC%A7%80%20%EC%95%8A%EB%8A%94%EB%8B%A4.)
```rust
fn main() {
    let s1 = String::from("hello");
    let _s2 = s1;
    println!("{}, world!", s1);
}
```
    - error msg : move the ownership of s1 to _s2
    ```
        $ rustc test.rs
        error[E0382]: borrow of moved value: `s1`
         --> test.rs:4:28
          |
        2 |     let s1 = String::from("hello");
          |         -- move occurs because `s1` has type `String`, which does not implement the `Copy` trait
        3 |     let _s2 = s1;
          |               -- value moved here
        4 |     println!("{}, world!", s1);
          |                            ^^ value borrowed here after move
          |
          = note: this error originates in the macro `$crate::format_args_nl` (in Nightly builds, run with -Z macro-backtrace for more info)

        error: aborting due to previous error

        For more information about this error, try `rustc --explain E0382`.
    ```

