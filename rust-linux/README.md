- [1. introduction of rust](#1-introduction-of-rust)
  - [1.1. check something in container](#11-check-something-in-container)
  - [1.2. convenience to compile in docker](#12-convenience-to-compile-in-docker)
  - [1.3. simple rust test](#13-simple-rust-test)
  - [1.4. compile and run](#14-compile-and-run)
- [2. Tutorial : Gessing Game](#2-tutorial--gessing-game)
- [3. ownership](#3-ownership)
- [4. struct / impl / derived](#4-struct--impl--derived)
- [5. enum == union in C](#5-enum--union-in-c)
- [6. Option<T>](#6-optiont)
- [7. match](#7-match)
- [8. module](#8-module)
- [9. collection](#9-collection)
  - [9.1. vector](#91-vector)
  - [9.2. string](#92-string)
  - [9.3. Hash Map](#93-hash-map)
- [10. error handling](#10-error-handling)
- [Generic Types, Traits, and Lifetimes](#generic-types-traits-and-lifetimes)
  - [Generic](#generic)

--------

# 1. introduction of rust
- documents of rust
  - brief explanation (korean): https://parksb.github.io/article/35.html
    - english nanaul : https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html
    - korean manual : https://rinthel.github.io/rust-lang-book-ko/ch02-00-guessing-game-tutorial.html
  - documents
    - https://doc.rust-lang.org/rust-by-example/std/hash.html
    - https://doc.rust-lang.org/std/collections/struct.HashMap.html
    - https://doc.rust-lang.org/rust-by-example/flow_control/for.html
    - https://doc.rust-lang.org/rust-by-example/flow_control/while.html
- leetcode supports rust.
- learn rust using docker
- docker hub container name is rust:latest


## 1.1. check something in container
- files
    - hello-rust-cargo/src/main.rs
    - hello-rust-cargo/Makefile
    - hello-rust-cargo/Cargo.toml
- ```docker run -it --rm -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust /bin/sh```

## 1.2. convenience to compile in docker
- i use 2 kinds of alias
    - ```alias cargo='docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust cargo'```
        - host$ cargo run    -> it will compile then remove container. so it download everytime.
    - ```alias rustit='docker run -it --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust'```
        - docker$ cargo run   -> it is in container.   so it is slow at the first time
        - when i need keyboard input as input , this interactive mode is more proper.

## 1.3. simple rust test
- cd test
- ```docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust rustc main.rs```
- main

## 1.4. compile and run
- method 1
    - ```docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust cargo build --release```
    - ./target/debug/hello-rust
- method 2
    - ```docker run --rm --user `id -u`:`id -g` -v `pwd`:/usr/src/myapp -w /usr/src/myapp rust cargo run```

# 2. Tutorial : Gessing Game
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

# 3. ownership
- [Rust- 러스트의 꽃, Ownership 파헤치기](https://medium.com/@kwoncharles/rust-%EB%9F%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%BD%83-ownership-%ED%8C%8C%ED%97%A4%EC%B9%98%EA%B8%B0-2f9c6b744c38#:~:text=Rust%EB%8A%94%20%EC%98%A4%EB%84%88%EC%8B%AD%EC%9D%84%20%EA%B8%B0%EB%B0%98,%ED%95%B4%EC%A0%9C%20%EC%97%90%EB%9F%AC%EA%B0%80%20%EC%9D%BC%EC%96%B4%EB%82%98%EC%A7%80%20%EC%95%8A%EB%8A%94%EB%8B%A4.)
- korean : https://rinthel.github.io/rust-lang-book-ko/ch04-01-what-is-ownership.html
- english : https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/ownership.html
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
# 4. struct / impl / derived

# 5. enum == union in C
- 서로 다른 type들을 enum안에 넣을수 있음. 

# 6. Option<T>
- T type의 값이 들어가거나 , NULL 값을 가질수 있음.   요즘 types에서 이 부분이 hit
- null 을 고안한 Tony Hoare 의 "Null 참조 : 10 억 달러의 실수"에서 다음과 같이 말합니다:
  - 나는 그것을 나의 10억 달러의 실수라고 생각한다. 그 당시 객체지향 언어에서 처음 참조를 위한 포괄적인 타입 시스템을 디자인하고 있었다. 내 목표는 컴파일러에 의해 자동으로 수행되는 체크를 통해 모든 참조의 사용은 절대적으로 안전하다는 것을 확인하는 것이었다. 그러나 null 참조를 넣고 싶은 유혹을 참을 수 없었다. 간단한 이유는 구현이 쉽다는 것이었다. 이것은 수없이 많은 오류와 취약점들, 시스템 종료를 유발했고, 지난 40년간 10억 달러의 고통과 손실을 초래했을 수도 있다.
- T 에 대한 연산을 수행하기 전에 Option<T> 를 T 로 변환해야 합니다. 일반적으로, 이런 방식은 null 과 관련된 가장 흔한 이슈 중 하나를 발견하는데 도움을 줍니다: 실제로 null 일 때, null 이 아니라고 가정하는 경우입니다.
- null 이 아닌 값을 갖는다는 가정을 놓치는 경우에 대해 걱정할 필요가 없게 되면, 코드에 더 확신을 갖게 됩니다. null 일 수 있는 값을 사용하기 위해서, 명시적으로 값의 타입을 Option<T> 로 만들어 줘야 합니다. 그다음엔 값을 사용할 때 명시적으로 null 인 경우를 처리해야 합니다. 값의 타입이 Option<T> 가 아닌 모든 곳은 값이 null 아 아니라고 안전하게 가정할 수 있습니다. 이것은 null을 너무 많이 사용하는 문제를 제한하고 러스트 코드의 안정성을 높이기 위한 러스트의 의도된 디자인 결정사항입니다.

# 7. match
- 모든 case를 만족하지 않으면 compile error
- _ 은 default: 와 같은 의미

# 8. module
- ```cargo new communicator --lib```  : src/lib.rs를 볼수 있다.
- 파일에 관한 모듈의 규칙을 정리해봅시다:
  - 만일 foo라는 이름의 모듈이 서브모듈을 가지고 있지 않다면, foo.rs라는 이름의 파일 내에 foo에 대한 선언을 집어넣어야 합니다.
  - 만일 foo가 서브모듈을 가지고 있다면, foo/mod.rs라는 이름의 파일에 foo에 대한 선언을 집어넣어야 합니다.
```
├── foo
│   ├── bar.rs (contains the declarations in `foo::bar`)
│   └── mod.rs (contains the declarations in `foo`, including `mod bar`)
```
- use를 사용하여 c++ namespace와 같은 기능 지원
  - ```use TrafficLight::*```

# 9. collection
## 9.1. vector
- Vec<T> 
- 러스트는 편의를 위해 vec! 매크로를 제공합니다. 이 매크로는 우리가 준 값들을 저장하고 있는 새로운 Vec을 생성합니다.
  - !이 있는 것은 Macro인 것을 의미한다. Macro는 함수가 아니기에 ownership이 넘어가는게 아니다.
  - ```let v = vec![1, 2, 3];```
- vector update
```rust
    let mut v = Vec::new();

    v.push(5);
    v.push(6);
    v.push(7);
    v.push(8);
```
- 벡터의 요소들 읽기
```rust
    let v = vec![1, 2, 3, 4, 5];

    let third: &i32 = &v[2];
    let third: Option<&i32> = v.get(2);
```
- 유효하지 않은 참조자 : 같은 스코프 내에서 가변 참조자와 불변 참조자를 가질 수 없다는 규칙을 상기하세요.
  - 새로운 요소를 벡터의 끝에 추가하는 것은 새로 메모리를 할당하여 예전 요소를 새 공간에 복사하는 일을 필요로 할 수 있는데, 이는 벡터가 모든 요소들을 붙여서 저장할 공간이 충분치 않는 환경에서 일어날 수 있습니다. 
```rust
    let mut v = vec![1, 2, 3, 4, 5];

    let first = &v[0];

    v.push(6);

    error[E0502]: cannot borrow `v` as mutable because it is also borrowed as
    immutable
    |
    4 | let first = &v[0];
    |              - immutable borrow occurs here
    5 |
    6 | v.push(6);
    | ^ mutable borrow occurs here
    7 | }
    | - immutable borrow ends here
```
- 벡터 내의 값들에 대한 반복처리
```rust
    let v = vec![100, 32, 57];
    for i in &v {
        println!("{}", i);
    }

    // 가변 참조자가 참고하고 있는 값을 바꾸기 위해서, i에 += 연산자를 이용하기 전에 역참조 연산자 (*)를 사용하여 값을 얻어야 합니다.
    let mut v = vec![100, 32, 57];
    for i in &mut v {
        *i += 50;
    }
```
- 열거형을 사용하여 여러 타입을 저장하기
```rust
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];
```

## 9.2. string
- 생성하기
```rust
    let mut s = String::new();
    let s = "initial contents".to_string();
    let s = String::from("initial contents");
```
- 추가하기
```rust
    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(&s2);
    println!("s2 is {}", s2);
```
- + 연산자나 format! 매크로를 이용한 접합
```rust
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2; // s1은 여기서 이동되어 더이상 쓸 수 없음을 유의하세요
    // s1.+(&s2) 이므로 s1은 없어짐.
```
- 더 복잡한 스트링 조합을 위해서는 format! 매크로를 사용할 수 있습니다: **어떠한 파라미터들의 소유권도 가져가지 않습니다.**
```rust
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = format!("{}-{}-{}", s1, s2, s3);
```
- 스트링 내에서 반복적으로 실행되는 메소드
```rust
    for c in "नमस्ते".chars() {
        println!("{}", c);
    }
    for b in "नमस्ते".bytes() {
        println!("{}", b);
    }
```

## 9.3. Hash Map
- HashMap<K, V>
  - 벡터와 마찬가지로, 해쉬맵도 데이터를 힙에 저장합니다. 
- 생성하기
```rust
    use std::collections::HashMap;

    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
```
- 팀의 리스트와 점수의 리스트로부터 해쉬맵 생성하기
  - zip 메소드를 이용하여 “Blue”와 10이 한 쌍이 되는 식으로 튜플의 벡터를 생성할 수 있습니다.  https://www.educba.com/rust-zip/
```rust
    use std::collections::HashMap;

    let teams  = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 50];

    let scores: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();
```
- 해쉬맵과 소유권
```rust
    use std::collections::HashMap;

    let field_name = String::from("Favorite color");
    let field_value = String::from("Blue");

    let mut map = HashMap::new();
    map.insert(field_name, field_value);
    // field_name과 field_value은 이 지점부터 유효하지 않습니다.
    // 이들을 이용하는 시도를 해보고 어떤 컴파일러 에러가 나오는지 보세요!
```
  - 만일 우리가 해쉬맵에 값들의 참조자들을 삽입한다면, 이 값들은 해쉬맵으로 이동되지 않을 것입니다. 하지만 참조자가 가리키고 있는 값은 해쉬맵이 유효할 때까지 계속 유효해야합니다. 이것과 관련하여 10장의 “라이프타임을 이용한 참조자 유효화”절에서 더 자세히 이야기할 것입니다.
- 해쉬맵 내의 값 접근하기
  - 결과값은 Some(&10)일 것입니다. 결과값은 Some으로 감싸져 있는데 왜냐하면 get이 Option<&V>를 반환하기 때문입니다. 프로그램은 우리가 6장에서 다루었던 방법 중 하나로 Option을 처리해야 할 것입니다.
  - 
```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name);

for (key, value) in &scores {
    println!("{}: {}", key, value);
}
```
- 해쉬맵 갱신하기
  - 값을 덮어쓰기
    ```rust
        let mut scores = HashMap::new();
        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Blue"), 25);
    ```
  - 키에 할당된 값이 없을 경우에만 삽입하기
    ```rust
        let mut scores = HashMap::new();
        scores.insert(String::from("Blue"), 10);
        scores.entry(String::from("Yellow")).or_insert(50);
        scores.entry(String::from("Blue")).or_insert(50);
    ```
  - 예전 값을 기초로 값을 갱신하기
    - 가변 참조자는 for 루프의 끝에서 스코프 밖으로 벗어나고, 따라서 모든 값들의 변경은 안전하며 빌림 규칙에 위배되지 않습니다.
    ```rust
        use std::collections::HashMap;

        let text = "hello world wonderful world";

        let mut map = HashMap::new();

        for word in text.split_whitespace() {
            let count = map.entry(word).or_insert(0);  // or_insert 메소드는 실제로는 해당 키에 대한 값의 가변 참조자 (&mut V)를 반환합니다.
            *count += 1;   // 여기에 값을 할당하기 위해 먼저 애스터리스크 (*)를 사용
        }

        println!("{:?}", map);
        // {"world": 2, "hello": 1, "wonderful": 1}를 출력
    ```

# 10. error handling
- 러스트는 에러를 두 가지 범주로 묶습니다: 복구 가능한(recoverable) 에러와 복구 불가능한(unrecoverable) 에러입니다. 복구 가능한 에러는 사용자에게 문제를 보고하고 연산을 재시도하는 것이 보통 합리적인 경우인데, 이를테면 파일을 찾지 못하는 에러가 그렇습니다. 복구 불가능한 에러는 언제나 버그의 증상이 나타나는데, 예를 들면 배열의 끝을 넘어선 위치의 값에 접근하려고 시도하는 경우가 그렇습니다.
- 복구 가능한 에러를 위한 Result<T, E> 값과 복구 불가능한 에러가 발생했을 때 실행을 멈추는 panic! 매크로를 가지고 있습니다. 이번 장에서는 panic!을 호출하는 것을 먼저 다룬 뒤, Result<T, E> 값을 반환하는 것에 대해 이야기 하겠습니다.
- backtrace on : ```$ RUST_BACKTRACE=1 cargo run```
  - 에러가 났을 때 패닉을 위한 숏컷: unwrap과 expect
- 에러 전파하기 : Err(e) => return Err(e)
  - 러스트에서 에러를 전파하는 패턴은 너무 흔하여 러스트에서는 이를 더 쉽게 해주는 물음표 연산자 ?를 제공합니다.
  - ```let mut f = File::open("hello.txt")?;```
- File::open 호출 부분의 끝에 있는 ?는 Ok내의 값을 변수 f에게 반환해줄 것입니다. 만일 에러가 발생하면 ?는 전체 함수로부터 일찍 빠져나와 호출하는 코드에게 어떤 Err 값을 줄 것입니다. read_to_string 호출의 끝부분에 있는 ?도 같은 것이 적용되어 있습니다.
  - ?는 많은 수의 보일러플레이트(boilerplate)를 제거해주고 이 함수의 구현을 더 단순하게 만들어 줍니다. 심지어는 Listing 9-8과 같이 ? 뒤에 바로 메소드 호출을 연결하는 식으로 (chaining) 이 코드를 더 줄일 수도 있습니다:
  - ```File::open("hello.txt")?.read_to_string(&mut s)?;```
- ?는 Result를 반환하는 함수에서만 사용될 수 있습니다.
```rust
pub struct Guess {
    value: u32,
}

impl Guess {
    pub fn new(value: u32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Guess value must be between 1 and 100, got {}.", value);
        }

        Guess {
            value
        }
    }

    pub fn value(&self) -> u32 {
        self.value
    }
}
```

# Generic Types, Traits, and Lifetimes
- Every programming language has tools for effectively handling the duplication of concepts. In Rust, one such tool is generics.  모든 프로그래밍 언어는 컨셉의 복제를 효율적으로 다루기 위한 도구를 가지고 있습니다; 러스트에서, 그러한 도구 중 하나가 바로 제네릭(generic) 입니다.  ex. Option<T>
- Traits (속성) : traits to define behavior in a generic way.  트레잇(trait) 에 대하여 논의할 것인데, 이는 동작을 제네릭 한 방식으로 정의하는
방법을 말합니다. 트레잇은 제네릭 타입과 결합되어 제네릭 타입에 대해 아무 타입이나 허용하지 않고,
특정 동작을 하는 타입으로 제한할 수 있습니다.
- lifetimes, a variety of generics that give the compiler information about how references relate to each other. Lifetimes allow
us to borrow values in many situations while still enabling the compiler to
check that the references are valid. 라이프타임은 수많은 상황에서 값을 빌릴 수 있도록 허용해 주고도 여전히 참조자들이 유효할지를 컴파일러가 검증하도록 해주는 러스트의 지능입니다.

## Generic
- C++ template
- 





