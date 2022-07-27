- [1. introduction of rust](#1-introduction-of-rust)
  - [1.1. check something in container](#11-check-something-in-container)
  - [1.2. convenience to compile in docker](#12-convenience-to-compile-in-docker)
  - [1.3. simple rust test](#13-simple-rust-test)
  - [1.4. compile and run](#14-compile-and-run)
- [2. Tutorial : Gessing Game](#2-tutorial--gessing-game)
- [3. ownership](#3-ownership)
- [4. struct / impl / derived  & enum == union in C](#4-struct--impl--derived---enum--union-in-c)
- [5. Option<T>](#5-optiont)
- [6. match](#6-match)
- [7. module](#7-module)
- [8. collection](#8-collection)
  - [8.1. vector](#81-vector)
  - [8.2. string](#82-string)
  - [8.3. Hash Map](#83-hash-map)
- [9. error handling](#9-error-handling)
- [10. Generic Types, Traits, and Lifetimes](#10-generic-types-traits-and-lifetimes)
  - [10.1. Generic](#101-generic)
  - [10.2. trait](#102-trait)
  - [10.3. lifetime](#103-lifetime)
- [11. 자동화된 테스트 작성하기](#11-자동화된-테스트-작성하기)
  - [11.1. 테스트의 실행 방식 제어하기](#111-테스트의-실행-방식-제어하기)
  - [11.2. 테스트 조직화](#112-테스트-조직화)
- [12. I/O 프로젝트: 커맨드 라인 프로그램 만들기 (예제)](#12-io-프로젝트-커맨드-라인-프로그램-만들기-예제)
  - [12.1. 커맨드라인 인자 허용하기](#121-커맨드라인-인자-허용하기)
  - [12.2. 파일 읽기](#122-파일-읽기)
  - [12.3. 모듈성과 에러처리의 향상을 위한 **리팩토링**](#123-모듈성과-에러처리의-향상을-위한-리팩토링)
  - [12.4. 테스트 주도 개발로 라이브러리의 기능 개발하기](#124-테스트-주도-개발로-라이브러리의-기능-개발하기)
- [13. 함수형 언어의 특성들: 반복자들과 클로저들](#13-함수형-언어의-특성들-반복자들과-클로저들)
  - [13.1. closure : 익명 함수](#131-closure--익명-함수)
  - [13.2. 반복자로 일련의 항목들 처리하기](#132-반복자로-일련의-항목들-처리하기)
  - [13.3. 성능 비교하기: 루프 vs. 반복자](#133-성능-비교하기-루프-vs-반복자)
- [14. Cargo 와 Crates.io 더 알아보기](#14-cargo-와-cratesio-더-알아보기)
  - [14.1. Crates.io에 크레이트 배포하기](#141-cratesio에-크레이트-배포하기)
    - [14.1.1. 유용한 문서화 주석 만들기](#1411-유용한-문서화-주석-만들기)
    - [14.1.2. pub use 를 이용해 공개 API 를 편리한 형태로 export 하기](#1412-pub-use-를-이용해-공개-api-를-편리한-형태로-export-하기)
    - [14.1.3. 다시 읽어보세요.. 실제로 배포 할거면....](#1413-다시-읽어보세요-실제로-배포-할거면)
  - [14.2. Cargo 작업공간](#142-cargo-작업공간)
- [15. 스마트 포인터](#15-스마트-포인터)
- [16. 겁 없는 동시성](#16-겁-없는-동시성)
  - [16.1. thread](#161-thread)
- [17. (Appendix) miscellaneous](#17-appendix-miscellaneous)
  - [17.1. code coverage](#171-code-coverage)

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
# 4. struct / impl / derived  & enum == union in C
- 서로 다른 type들을 enum안에 넣을수 있음. 

# 5. Option<T>
- T type의 값이 들어가거나 , NULL 값을 가질수 있음.   요즘 types에서 이 부분이 hit
- null 을 고안한 Tony Hoare 의 "Null 참조 : 10 억 달러의 실수"에서 다음과 같이 말합니다:
  - 나는 그것을 나의 10억 달러의 실수라고 생각한다. 그 당시 객체지향 언어에서 처음 참조를 위한 포괄적인 타입 시스템을 디자인하고 있었다. 내 목표는 컴파일러에 의해 자동으로 수행되는 체크를 통해 모든 참조의 사용은 절대적으로 안전하다는 것을 확인하는 것이었다. 그러나 null 참조를 넣고 싶은 유혹을 참을 수 없었다. 간단한 이유는 구현이 쉽다는 것이었다. 이것은 수없이 많은 오류와 취약점들, 시스템 종료를 유발했고, 지난 40년간 10억 달러의 고통과 손실을 초래했을 수도 있다.
- T 에 대한 연산을 수행하기 전에 Option<T> 를 T 로 변환해야 합니다. 일반적으로, 이런 방식은 null 과 관련된 가장 흔한 이슈 중 하나를 발견하는데 도움을 줍니다: 실제로 null 일 때, null 이 아니라고 가정하는 경우입니다.
- null 이 아닌 값을 갖는다는 가정을 놓치는 경우에 대해 걱정할 필요가 없게 되면, 코드에 더 확신을 갖게 됩니다. null 일 수 있는 값을 사용하기 위해서, 명시적으로 값의 타입을 Option<T> 로 만들어 줘야 합니다. 그다음엔 값을 사용할 때 명시적으로 null 인 경우를 처리해야 합니다. 값의 타입이 Option<T> 가 아닌 모든 곳은 값이 null 아 아니라고 안전하게 가정할 수 있습니다. 이것은 null을 너무 많이 사용하는 문제를 제한하고 러스트 코드의 안정성을 높이기 위한 러스트의 의도된 디자인 결정사항입니다.

# 6. match
- 모든 case를 만족하지 않으면 compile error
- _ 은 default: 와 같은 의미

# 7. module
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

# 8. collection
## 8.1. vector
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

## 8.2. string
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

## 8.3. Hash Map
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

# 9. error handling
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

# 10. Generic Types, Traits, and Lifetimes
- Every programming language has tools for effectively handling the duplication of concepts. In Rust, one such tool is generics.  모든 프로그래밍 언어는 컨셉의 복제를 효율적으로 다루기 위한 도구를 가지고 있습니다; 러스트에서, 그러한 도구 중 하나가 바로 제네릭(generic) 입니다.  ex. Option<T>
- Traits (속성) : traits to define behavior in a generic way.  트레잇(trait) 에 대하여 논의할 것인데, 이는 동작을 제네릭 한 방식으로 정의하는
방법을 말합니다. 트레잇은 제네릭 타입과 결합되어 제네릭 타입에 대해 아무 타입이나 허용하지 않고,
특정 동작을 하는 타입으로 제한할 수 있습니다.
- lifetimes, a variety of generics that give the compiler information about how references relate to each other. Lifetimes allow
us to borrow values in many situations while still enabling the compiler to
check that the references are valid. 라이프타임은 수많은 상황에서 값을 빌릴 수 있도록 허용해 주고도 여전히 참조자들이 유효할지를 컴파일러가 검증하도록 해주는 러스트의 지능입니다.

## 10.1. Generic
- C++ template
- generic2.rs
```rust
struct Point<T,U> {
    x: T,
    y: U,
}

impl<T,U> Point<T,U> {
    fn x(&self) -> &T {
        &self.x
    }
    fn y(&self) -> &U {
        &self.y
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());

    let p = Point { x: 5, y: 10.3 };
    println!("p.y = {}", p.y());
}

```
- example
```rust
enum Option<T> {
    Some(T),
    None,
}
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```
- 제네릭을 이용한 코드의 성능 : 구체적인 타입을 명시했을 때와 비교해 전혀 느려지지 않을 것이란 점입니다!  어떠한 런타임 비용도 없음을 의미합니다

## 10.2. trait
- 정의 : 어떤 타입의 동작은 우리가 해당 타입 상에서 호출할 수 있는 메소드들로 구성되어 있습니다. 만일 우리가 서로 다른 타입에 대해 모두 동일한j 메소드를 호출할 수 있다면 이 타입들은 동일한 동작을 공유하는 것입니다. 트레잇의 정의는 어떠한 목적을 달성하기 위해 필요한 동작의 집합을 정의하기 위해 메소드 시그니처들을 함께 묶는 방법입니다.
- 트레잇은 한 줄 당 하나의 메소드 시그니처와 각 줄의 끝에 세미콜론을 갖도록 함으로써, 본체 내에 여러 개의 메소드를 가질 수 있습니다.
- 트레잇 구현과 함께 기억할 한 가지 제한사항이 있습니다: 트레잇 혹은 타입이 우리의 크레이트 내의 것일 경우에만 해당 타입에서의 트레잇을 정의할 수 있습니다. 바꿔 말하면, 외부의 타입에 대한 외부 트레잇을 구현하는 것은 허용되지 않습니다. 예를 들어, Vec에 대한 Display 트레잇은 구현이 불가능한데, Display와 Vec 모두 표준 라이브러리 내에 정의되어 있기 때문입니다. 우리의 aggregator 크레이트 기능의 일부로서 Tweet과 같은 커스텀 타입에 대한 Display와 같은 표준 라이브러리 트레잇을 구현하는 것은 허용됩니다. 또한 우리의 aggregator 크레이트 내에서 Vec에 대한 Summarizable을 구현하는 것도 가능한데, 이는 우리 크레이트 내에 Summarizable이 정의되어 있기 때문입니다. 이러한 제한은 고아 규칙(orphan rule) 이라고 불리는 것의 일부인데, 이는 타입 이론에 흥미가 있다면 찾아볼 수 있습니다. 간단하게 말하면, 부모 타입이 존재하지 않기 때문에 고아 규칙이라고 부릅니다. 이 규칙이 없다면, 두 크레이트는 동일한 타입에 대해 동일한 트레잇을 구현할 수 있게 되고, 이 두 구현체가 충돌을 일으킬 것입니다: 러스트는 어떤 구현을 이용할 것인지 알지 못할 것입니다. 러스트가 고아 규칙을 강제하기 때문에, 다른 사람의 코드는 여러분의 코드를 망가뜨리지 못하고 반대의 경우도 마찬가지입니다.

## 10.3. lifetime
- 라이프타임은 댕글링 참조자를 방지합니다
  - 스코프 밖으로 벗어난 값에 대한 참조자를 사용하는 시도

    ```rust
    {
        let r;         // -------+-- 'a
                      //        |
        {              //        |
            let x = 5; // -+-----+-- 'b
            r = &x;    //  |     |
        }              // -+     |
                      //        |
        println!("r: {}", r); // |
                      //        |
                      // -------+
    }
    ```
  - 데이터가 참조자에 비해 더 긴 라이프타임을 갖고 있기 때문에 유효한 참조자
- 라이프타임 명시 문법
- 러스트는 우리가 댕글링 참조자를 만들게끔 놔두지 않습니다. : 해제된 메모리를 가리키는 참조자
- 라이프타임 생략 규칙(lifetime elision rules) 
  1. 참조자인 각각의 파라미터는 고유한 라이프타임 파라미터를 갖습니다. 바꿔 말하면, 하나의 파라미터를 갖는 함수는 하나의 라이프타임 파라미터를 갖고: fn foo<'a>(x: &'a i32), 두 개의 파라미터를갖는 함수는 두 개의 라이프타임 파라미터를 따로 갖고: fn foo<'a, 'b>(x: &'a i32, y: &'b i32),이와 같은 식입니다.
  2. 만일 정확히 딱 하나의 라이프타임 파라미터만 있다면, 그 라이프타임이 모든 출력 라이프타임 파라미터들에 대입됩니다: fn foo<'a>(x: &'a i32) -> &'a i32.
  3. 만일 여러 개의 입력 라이프타임 파라미터가 있는데, 메소드라서 그중 하나가 &self 혹은 &mut self라고 한다면, self의 라이프타임이 모든 출력 라이프타임 파라미터에 대입됩니다. 이는 메소드의 작성을 더욱 멋지게 만들어줍니다.


# 11. 자동화된 테스트 작성하기
- 러스트 내의 테스트란 test 속성(attribute)이 주석으로 달려진 (annotated) 함수입니다. 속성은 러스트 코드 조각에 대한 메타데이터입니다: 한 가지 예로 5장에서 우리가 구조체와 함께 사용했던 derive 속성이 있습니다. 함수를 테스트 함수로 변경하기 위해서는, fn 전 라인에 #[test]를 추가합니다. cargo test 커맨드를 사용하여 테스트를 실행시키면, 러스트는 test 속성이 달려있는 함수들을 실행하고 각 테스트 함수가 성공 혹은 실패했는지를 보고하는 테스트 실행용 바이너리를 빌드할 것입니다.
- cd rust-linux/adder
  - cargo test

## 11.1. 테스트의 실행 방식 제어하기
- cargo test -- --help를 실행하는 것은 구분자 -- 이후에 나올 수 있는
옵션을 표시합니다.
- 기본적으로 스레드를 이용하여 병렬적으로 수행됩니다. 
- ```$ cargo test -- --test-threads=1``` 병렬처리 안함
- 기본적으로 어떤 테스트가 통과하면, 러스트의 테스트 라이브러리는 표준 출력(standard output)으로 출력되는 어떤 것이든 캡처합니다. 예를 들면, 우리가 테스트 내에서 println!을 호출하고 이 테스트가 통과하면, println! 출력을 터미널에서 볼 수 없습니다: 우리는 오직 그 테스트가 통과되었다고 표시된 라인만 볼 뿐입니다. 만일 테스트가 실패하면, 실패 메세지 아래에 표준 출력으로 출력되었던 어떤 것이든 보게 될 것입니다.
- ```$ cargo test -- --nocapture``` 만일 성공하는 테스트에 대한 출력 값 또한 볼 수 있기를 원한다면, --nocapture 플래그를 이용하여 출력 캡처 동작을 비활성화시킬 수 있습니다.
- ```$ cargo test another``` : 1개만 test
- ```$ cargo test test```  : test로 시작하는 것은 모두 test
- ```$ cargo test -- --ignored``` : ignored 들만 test
- 비공개 함수 테스트하기 : 기본이 비공개 함수도 test됨 (internal_adder)
  
## 11.2. 테스트 조직화
- 통합 test
  - rust-linux/adder/tests/integration_test.rs
  - tests directory는 integration test를 말하며,  이것은 unit test가 모두 성공했을때만 수행된다. 
  - ```cargo test``` : 출력에 세 개의 섹션이 생겼습니다: 단위 테스트, 통합 테스트, 그리고 문서 테스트입니다.
  - tests (integration test)만을 수행 하고 싶을때 
    - ```cargo test --test integration_test``` -> ```cargo test --test integration_test```
- 우리의 프로젝트가 src/lib.rs 파일이 없고 src/main.rs 파일만 갖고 있는 바이너리 프로젝트라면, tests 디렉토리 내에 통합 테스트를 만들어서 src/main.rs에 정의된 함수를 가져오기 위하여 extern crate를 이용할 수 없습니다. 오직 라이브러리 크레이트만 다른 크레이트에서 호출하고 사용할 수 있는 함수들을 노출시킵니다; 바이너리 크레이트는 그 스스로 실행될 것으로 여겨집니다.
- 이는 바이너리를 제공하는 러스트 프로젝트들이 src/lib.rs에 위치한 로직을 호출하는 간단한 형태의 src/main.rs를 가지고 있는 이유 중 하나입니다. 이러한 구조와 함께라면, extern crate를 이용하여 중요한 기능들을 커버하도록 하기 위해 통합 테스트가 라이브러리 크레이트를 테스트할 수 있습니다. 만일 중요 기능이 작동한다면, src/main.rs 내의 소량의 코드 또한 동작할 것이고, 이 소량의 코드는 테스트할 필요가 없습니다.

# 12. I/O 프로젝트: 커맨드 라인 프로그램 만들기 (예제)
- [greprs](https://github.com/cheoljoo/problemSolving/tree/master/rust-linux/greprs)
## 12.1. 커맨드라인 인자 허용하기
- crates.io 참조
- std::env::args. 이 함수는 반복자(iterator) 형식으로 커맨드라인 인자들을 우리 프로그램에 전달해줍니다. 
  - 반복자는 하나의 연속된 값을 생성합니다.
  - 반복자에 collect 함수 호출을 통해 반복자가 생성하는 일련의 값을 벡터로 변환할 수 있습니다.
## 12.2. 파일 읽기
- main에 에러 처리 없이 구현 해봄.
## 12.3. 모듈성과 에러처리의 향상을 위한 **리팩토링**
- lib.rs 로 떼어내고 , Result<(),Box<dyn Error>> 로 error나 Ok(())를 return하게 하는 것도 만들었다.
## 12.4. 테스트 주도 개발로 라이브러리의 기능 개발하기
- cargo test
- contains 메소드에 인자로 query를 전달할 때 contains의 선언이 문자열 slice를 인자로 받게 정의되어 있으니 앰퍼샌드(&)를 추가해야합니다.
- CASE_SENSITIVE=1 cargo run to poem.txt  <- in my case it is not working

# 13. 함수형 언어의 특성들: 반복자들과 클로저들

## 13.1. closure : 익명 함수
- https://github.com/cheoljoo/problemSolving/tree/master/rust-linux/closure
- 실제로 결과가 필요한 곳에서만 그 코드를 실행하고 싶습니다. 이것이 클로저의 유스 케이스 입니다.
- 코드를 저장하기 위해 클로저를 사용해서 리팩토링 하기 : if 블럭 전에 항상 simulated_expensive_calculation 함수를 호출하는 대신, 리스트 13-5에 보이는 것 처럼, 클로저를 정의하고 변수에 결과를 저장하기 보단 클로저를 변수에 저장 할 수 있습니다.
  - 클로저 정의는 변수 expensive_closure 에 그것을 할당하기 위해 = 다음에
옵니다. 클로저를 정의하기 위해, 수직의 파이프 (|) 한쌍으로 시작하며, 그 사이에
클로저에 대한 파라미터를 기술합니다; 이 문법은 스몰토크와 루비에서 클로저
정의와의 유사성 때문에 선택 되었습니다. 이 클로저는 num 이라는 하나의
파라미터를 갖습니다: 하나 이상의 파라미터를 갖는다면, |param1, param2| 와 같이
콤마로 구분합니다.
```rust
let expensive_closure = |num| {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```
- 클로저 타입 추론과 어노테이션
  - 클로저는 fn 함수처럼 파라미터나 반환값의 타입을 명시할 것을 요구하지 않습니다. 타입 어노테이션은 사용자에게 노출되는 명시적인 인터페이스의 일부이기 때문에 함수에 필요 합니다. 
  - 클로저는 이와 같이 노출된 인터페이스에 사용되지 않습니다: 변수에 저장되고 이름없이 우리의 라이브러리 사용자들에게 노출되지 않고 사용 됩니다.
  - type 명시해도 됨.
  - ```rust
      let expensive_closure = |num: u32| -> u32 {
          println!("calculating slowly...");
          thread::sleep(Duration::from_secs(2));
          num
      };
    ```
  - 모두 동일
    - ```rust
      fn  add_one_v1   (x: u32) -> u32 { x + 1 }
      let add_one_v2 = |x: u32| -> u32 { x + 1 };
      let add_one_v3 = |x|             { x + 1 };
      let add_one_v4 = |x|               x + 1  ;
      ```
  - 정의에 타입 어노테이션을 추가하지 않았을때 ,  클로저를 두번 호출하는데, 첫번째는 String 을 인자로 사용하고 두번째는 u32 을 사용한다면 에러가 발생합니다
- 제너릭 파라미터와 Fn 트레잇을 사용하여 클로저 저장하기
  - 운 좋게도, 다른 해결책이 있습니다. 우리는 클로저와 클로저를 호출한 결과값을 갖고 있는 구조체를 만들 수 있습니다. 그 구조체는 결과값을 필요로 할 때만 클로저를 호출 할 것이며, 결과값을 캐시에 저장해 두어 우리의 나머지 코드에서 결과를 저장하고 재사용 하지 않아도 되도록 할 것입니다. 이 패턴을 메모이제이션(memoization) 혹은 *지연 평가(lazy evaluation)*로 알고 있을 것 입니다.
  - closure 를 담는 것으로 Fn Trait 사용 : Fn 트레잇은 표준 라이브러리에서 제공 합니다. 모든 클로저들은 다음 트레잇 중 하나를 구현 합니다: Fn, FnMut, 혹은 FnOnce. 환경을 캡처하는 것에 대한 다음 절에서 이 트레잇들의 차이점들에 대해 설명할 것입니다
  - generric struct와 impl을 이용하여 구현 : value 값이 None이면 함수 수행 , 이미 수행했으면 value 반환
- 클로저로 환경 캡처 하기
  - 비록 x 가 equal_to_x 의 파라미터 중에 하나가 아니더라도, equal_to_x 는 equal_to_x 가 정의된 동일한 스코프에 정의된 x 변수를 사용하는 것이 허용 됩니다.
  - ```rust
      fn main() {
          let x = 4;
          let equal_to_x = |z| z == x;
          let y = 4;
          assert!(equal_to_x(y));
      }
    ```
- 클로저는 세가지 방식으로 그들의 환경에서 값을 캡처 할 수 있는데, 함수가 파라미터 를 받는 세가지 방식과 직접 연결 됩니다: 소유권 받기, 불변으로 빌려오기, 가변으로 빌려오기. 이것들은 다음과 같이 세개의 Fn 트레잇으로 표현 합니다:
  - FnOnce 는 클로저의 환경으로 알고 있는, 그것을 둘러싼 환경에서 캡처한 변수 들을 소비합니다. 캡처한 변수를 소비하기 위해, 클로저는 이 변수의 소유권을 가져야 하고 그것이 정의될 때 클로저 안으로 그것들을 옮겨와야 합니다. 이름의 일부인 Once 는 그 클로저가 동일한 변수들에 대해 한번이상 소유권을 얻을수 없다는 사실을 의미하며, 그래서 한 번만 호출 될 수 있습니다.
    - move 이용 : ```let equal_to_x = move |z| z == x;```
  - Fn 은 그 환경으로 부터 값들을 불변으로 빌려 옵니다.
  - FnMut 값들을 가변으로 빌려오기 때문에 그 환경을 변경할 수 있습니다.

## 13.2. 반복자로 일련의 항목들 처리하기
- iterator
  ```rust
  let v1 = vec![1, 2, 3];
  let v1_iter = v1.iter();
  for val in v1_iter {
      println!("Got: {}", val);
  }
  ```
- Iterator trait and next method
  ```rust
  trait Iterator {
      type Item;
      fn next(&mut self) -> Option<Self::Item>;
      // methods with default implementations elided
  } 
  ```
- next 호출로 얻어온 값들은 벡터 안에 있는 값들에 대한 불변 참조라는 점 역시
유의 하세요. iter 메서드는 불변 참조에 대한 반복자를 만듭니다. 만약 v1 의
소유권을 갖고 소유된 값들을 반환하도록 하고 싶다면, iter 대신 into_iter 를
호출해야 합니다. 비슷하게, 가변 참조에 대한 반복자를 원한다면, iter 대신
iter_mut 을 호출할 수 있습니다.
  - [iter.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/iter.rs)
  - ```v1_iter.sum();``` 반복자의 모든 항목에 대한 합계를 얻기 위해 sum 메서드 호출 하기. sum 은 호출한 반복자의 소유권을 갖기 때문에, sum 을 호출한 후 v1_iter 은 사용할 수 없습니다.
- 다른 반복자를 생성하는 메서드들 (ex. map)
  - iterator가 lazy이므로 그냥 선언만 하면 안되고 , collect() 같은 것을 직접 호출해주는게 있어야 한다.
  - map 은 클로저를 인자로 받기 때문에, 각 항목에 대해 수행하기를 원하는 어떤 연산도 기술할 수 있습니다. 이것은 Iterator 트레잇이 제공하는 반복자 행위를 재사용 하면서 클로저가 어떻게 일부 행위를 맞춤 조작할 수 있는지를 보여주는 굉장한 예제 입니다.
  ```rust
  let v1: Vec<i32> = vec![1, 2, 3];
  let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();
  assert_eq!(v2, vec![2, 3, 4]);
  ```
- 환경을 캡쳐하는 클로저 사용하기 (ex. filter)
  - 반복자의 filter 메서드는 반복자로 부터 각 항목을 받아 Boolean 을 반환하는 클로저를 인자로 받습니다.
- Iterator trait으로 자신만의 반복자 만들기
  - [counterIter.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/counterIter.rs)

## 13.3. 성능 비교하기: 루프 vs. 반복자
- 클로저와 반복자는 함수형 프로그래밍 아이디어에서 영감을 받은 러스트의 특징들 입니다. 이것들은 고수준의 개념을 저수준의 성능으로 명확하게 표현할 수 있는 러스트의 능력에 기여하고 있습니다. 클로저와 반복자의 구현들은 런타임 성능에 영향을 미치지 않습니다. 이것은 제로-비용 추상을 제공하기 위해 노력하는 러스트의 목표 중의 일부 입니다.

# 14. Cargo 와 Crates.io 더 알아보기
- [Cargo 공식 문서](https://doc.rust-lang.org/cargo/)

- opt-level 설정은 러스트가 여러분의 코드에 적용할 최적화 수치이며, 0 ~ 3 사이의 값을 가집니다. 여러분이 개발을 할 때와 같이 코드를 자주 컴파일 하는 상황에서는 코드의 실행 속도가 조금 느려지는 한이 있더라도 컴파일이 빨리 되길 원합니다. 하지만 높은 최적화 수치를 적용 할 수록 컴파일에 걸리는 시간은 증가합니다. 따라서 dev 의 기본 opt-level 값은 0 으로 되어 있습니다. 만약 여러분이 코드를 릴리즈 하려 한다면, 컴파일에 걸리는 시간이 늘어나도 상관이 없을 겁니다. 릴리즈 할 경우 컴파일은 한 번이지만, 실행 횟수는 여러번 이니까요. 따라서 릴리즈 모드에서는 컴파일 시간을 희생하는 대신 빠른 코드 실행 속도를 얻기 위해 release 프로필의 기본 opt-level 값이 3 으로 되어 있습니다.
  - ```txt
      [profile.dev]
      opt-level = 0
      [profile.release]
      opt-level = 3
    ```

## 14.1. Crates.io에 크레이트 배포하기
### 14.1.1. 유용한 문서화 주석 만들기
- 문서화 주석은 슬래시 두 개가 아니라 세 개(///) 를 이용하며 텍스트 서식을 위한 **마크다운** 표기법을 지원합니다. 문서화 주석은 문서화할 대상 바로 이전에 배치하면 됩니다.
- cd cargo
  - https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/cargo
  - ```cargo doc```
    - 결과 : target/doc
    - http://lotto645.lge.com:8088/cheoljoo.lee/code/problemSolving/rust-linux/cargo/target/doc/cargo/fn.add_one.html
- HTML 에 "Examples." 제목을 가진 구절을 만들기 위해 # Examples 마크다운 헤더를 사용했습니다. 이외에 크레이트의 제작자가 일반적으로 문서에 사용하는 구절은 다음과 같습니다.
  - Panics: 문서화된 기능이 패닉을 일으킬 수 있는 시나리오입니다. 함수를 호출하는 사람들에게 "프로그램이 패닉을 일으키지 않게 하려면 이러한 상황에서는 이 함수를 호출하지 않아야 합니다" 라는 내용을 알려줍니다.
  - Errors: 해당 함수가 Result 를 반환할 경우에는 발생할 수 있는 에러의 종류와 해당 에러들이 발생하는 조건을 설명해 주어서 호출하는 사람이 여러 에러를 여러 방법으로 처리할 수 있도록 해야합니다.
  - Safety: 함수가 안전하지 않을(unsafe) 경우에 (19장에서 다루는 내용입니다) 왜 이 함수가 안전하지 않은지와 이 함수가 호출하는 사람에게 지키길 기대하는 불변성에 대해 알려주는 구절이 있어야 합니다.
- **문서화 주석에 예시 코드를 추가하는 건 여러분의 라이브러리를 어떻게 사용하는지 알려줄 수 있을뿐더러 또 다른 효과도 있습니다: 무려 cargo test 를 실행하면 여러분의 문서에 들어있던 예시 코드들이 테스트로서 실행**됩니다! 백문이 불여일견이라는 말이 있듯이, 예시를 포함한 문서보다 좋은 문서는 없습니다. 
- 문서화 주석의 또 다른 스타일로 //! 가 있습니다. 이는 주석 뒤에 오는 항목을 문서화 하는게 아닌 주석을 포함하는 항목을 문서화 합니다. 일반적으로 크레이트의 루트 파일 (관례적으로 src/lib.rs 입니다) 이나 크레이트 혹은 모듈 전체를 문서화하는 모듈 내부에 이 문서화 주석을 작성합니다.
  - //! 로 시작하는 줄 중 마지막 줄에 코드가 뒤따르지 않는다는 점을 주목하세요. 
  - ```cargo doc --open```

### 14.1.2. pub use 를 이용해 공개 API 를 편리한 형태로 export 하기
- 특정 부분에서 중첩된 모듈이 많을 경우, 모듈의 상위 계층에서 pub use 를 이용해 타입을 다시 export 함으로써 크레이트의 사용자들에게 더 뛰어난 경험을 제공할 수 있습니다.

###  14.1.3. 다시 읽어보세요.. 실제로 배포 할거면....

## 14.2. Cargo 작업공간

# 15. 스마트 포인터
- 러스트에서는, 표준 라이브러리에 정의된 다양한 종류의 스마트 포인터들이 참조자들에 의해 제공되는 것을 넘어서는 추가 기능을 제공합니다. 우리가 이번 장에서 탐구할 한 가지 예로는 참조 카운팅 (reference counting) 스마트 포인터 타입이 있습니다. 이 포인터는 소유자의 수를 계속 추적하고, 더 이상 소유자가 없으면 데이터를 정리하는 방식으로, 여러분들이 어떤 데이터에 대한 여러 소유자들을 만들 수 있게 해 줍니다.
- 스마트 포인터가 일반적인 구조체와 구분되는 특성은 바로 스마트 포인터가 Deref와 Drop 트레잇을 구현한다는 것입니다. Deref 트레잇은 스마트 포인터 구조체의 인스턴스가 참조자처럼 동작하도록 하여 참조자나 스마트 포인터 둘 중 하나와 함께 작동하는 코드를 작성하게 해 줍니다. Drop 트레잇은 스마트 포인터의 인스턴스가 스코프 밖으로 벗어났을 때 실행되는 코드를 커스터마이징 가능하도록 해 줍니다.
- [cons.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/cons.rs)
  - 에러는 이 타입이 “무한한 크기를 갖는다”라고 말해줍니다. 그 원인은 우리가 재귀적인 variant를 이용하여 List를 정의했기 때문입니다: 즉 이것은 또 다른 자신을 직접 값으로 갖습니다. 결과적으로, 러스트는 List 값을 저장하는데 필요한 크기가 얼마나 되는지 알아낼 수 없습니다.
  - Box<T>는 Cons variant 안에 있기보다는 힙에 있을 다음의 List 값을 가리킬 것입니다.
  - Box<T> 타입은 스마트 포인터인데 그 이유는 이것이 Deref 트레잇을 구현하고 있기 때문이며, 이는 Box<T> 값이 참조자와 같이 취급되도록 허용해줍니다. Box<T> 값이 스코프 밖으로 벗어날 때, 박스가 가리키고 있는 힙 데이터도 마찬가지로 정리되는데 이는 Drop 트레잇의 구현 때문에 그렇습니다. 
- [deref.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/deref.rs)
  - type Target = T; 문법은 Deref 트레잇이 사용할 연관 타입 (associated type) 을 정의합니다.  우리는 deref 메소드의 본체를 &self.0로 채웠으므로 deref는 우리가 * 연산자를 이용해 접근하고자 하는 값의 참조자를 반환합니다.
  - Deref 트레잇 없이, 컴파일러는 오직 & 참조자들만 역참조 할 수 있습니다. 
- 함수와 메소드를 이용한 암묵적 역참조 강제
  - 역참조 강제(deref coercion) 는 러스트가 함수 및 메소드의 인자에 수행하는 편의성 기능입니다.
  - 역참조 강제가 러스트에 도입되어서 함수와 메소드 호출을 작성하는 프로그래머들은 &와 *를 이용한 많은 수의 명시적 참조 및 역참조를 추가하지 않아도 됩니다. 역참조 강제 기능은 또한 우리가 참조자나 스마트 포인터 둘 중 어느 경우라도 작동할 수 있는 코드를 더 많이 작성할 수 있도록 해 줍니다.
- 역참조 강제가 가변성과 상호작용 하는 법
  - T: Deref<Target=U>일때 &T에서 &U로
  - T: DerefMut<Target=U>일때 &mut T에서 &mut U로
  - T: Deref<Target=U>일때 &mut T에서 &U로
- Rc<T>, 참조 카운팅 스마트 포인터
  - 러스트는 Rc<T>라 불리우는 타입을 가지고 있습니다. 이 이름은 참조 카운팅 (reference counting) 의 약자
  - 우리 프로그램의 여러 부분에서 읽을 데이터를 힙에 할당하고 싶고, 어떤 부분이 그 데이터를 마지막에 이용하게 될지 컴파일 타임에는 알 수 없는 경우 Rc<T> 타입을 사용합니다. 만일 어떤 부분이 마지막으로 사용하는지 알 수 있다면, 우리는 그냥 그 해당 부분을 데이터의 소유자로 만들면 되고, 컴파일 타임에 집행되는 보통의 소유권 규칙이 효과를 발생시킬 것입니다.
  - Rc<T>가 오직 단일 스레드 시나리오 상에서만 사용 가능하다는 점을 주의하세요. 
- Rc<T>를 사용하여 데이터 공유하기
  - ![](https://rinthel.github.io/rust-lang-book-ko/img/trpl15-03.svg)
  - ```rust
        enum List {
            Cons(i32, Box<List>),
            Nil,
        }

        use List::{Cons, Nil};

        fn main() {
            let a = Cons(5,
                Box::new(Cons(10,
                    Box::new(Nil))));
            let b = Cons(3, Box::new(a));
            let c = Cons(4, Box::new(a));
        }
    ```
    - error : 소유권 문제로 허용되지 않음.
  - ```rust
        enum List {
            Cons(i32, Rc<List>),
            Nil,
        }

        use List::{Cons, Nil};
        use std::rc::Rc;

        fn main() {
            let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
            let b = Cons(3, Rc::clone(&a));
            let c = Cons(4, Rc::clone(&a));
        }
    ```
      - Rc::clone의 호출은 오직 참조 카운트만 증가 시키는데, 이는 큰 시간이 들지 않습니다. 데이터의 깊은 복사는 많은 시간이 걸릴 수 있습니다. 
      - Rc<T>의 클론 생성은 참조 카운트를 증가시킵니다.
- RefCell<T>을 가지고 런타임에 빌림 규칙을 집행하기
  - 참조자와 Box<T>를 이용할 때, 빌림 규칙의 불변성은 컴파일 타임에 집행됩니다. RefCell<T>를 이용할 때, 이 불변성은 런타임에 집행됩니다. 참조자를 가지고서 여러분이 이 규칙을 어기면 컴파일러 에러를 얻게 될 것입니다. RefCell<T>를 가지고서 여러분이 이 규칙을 어기면, 여러분의 프로그램은 panic!을 일으키고 종료될 것입니다.  
  - RefCell<T> 타입은 여러분의 코드가 빌림 규칙을 따르는 것을 여러분이 확신하지만, 컴파일러는 이를 이해하고 보장할 수 없을 경우 유용합니다.
  - Rc<T>와 유사하게, RefCell<T>은 단일 스레드 시나리오 내에서만 사용 가능
- Box<T>, Rc<T>, 혹은 RefCell<T>을 선택하는 이유의 요점은 다음과 같습니다:
  - Rc<T>는 동일한 데이터에 대해 복수개의 소유자를 가능하게 합니다; Box<T>와 RefCell<T>은 단일 소유자만 갖습니다.
  - Box<T>는 컴파일 타임에 검사된 불변 혹은 가변 빌림을 허용합니다; Rc<T>는 오직 컴파일 타임에 검사된 불변 빌림만 허용합니다; RefCell<T>는 런타임에 검사된 불변 혹은 가변 빌림을 허용합니다.
  - RefCell<T>이 런타임에 검사된 가변 빌림을 허용하기 때문에, RefCell<T>이 불변일 때라도 RefCell<T> 내부의 값을 변경할 수 있습니다.
- RefCell<T>를 이용하는 것은 우리가 오직 불변 값만 허용하는 콘텍스트 내에서 그것이 본 메세지를 추적하기 위해서 스스로를 변경할 수 있는 목 객체를 작성하도록 해줍니다. 우리는 일반적인 참조자가 우리에게 제공하는 것보다 더 많은 기능을 얻기 위해서 트레이드 오프에도 불구하고 RefCell<T>를 이용할 수 있습니다.
- Rc<T>와 RefCell<T>를 조합하여 가변 데이터의 복수 소유자 만들기
  - Rc<T>이 어떤 데이터에 대해 복수의 소유자를 허용하지만, 그 데이터에 대한 불변 접근만 제공하는 것을 상기하세요. 만일 우리가 RefCell<T>을 들고 있는 Rc<T>를 갖는다면, 우리가 변경 가능하면서 복수의 소유자를 갖는 값을 가질 수 있습니다!
- 표준 라이브러리는 내부 가변성을 제공하는 다른 타입을 가지고 있는데, 이를 테면 Cell<T>는 내부 값의 참조자를 주는 대신 값이 복사되어 Cell<T> 밖으로 나오는 점만 제외하면 비슷합니다. 또한 Mutex<T>가 있는데, 이는 스레드들을 건너가며 사용해도 안전한 내부 가변성을 제공합니다.
- 순환 참조는 메모리 릭을 발생시킬 수 있습니다 : List 열거형과 tail 메소드 정의를 가지고서 어떻게 순환 참조가 생길 수 있고, 이를 어떻게 방지
  - [memory_leak.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/memory_leak.rs)
  - 순환 참조를 피하는 또다른 해결책은 여러분의 데이터 구조를 재구성하여 어떤 참조자는 소유권을 갖고 어떤 참조자는 그렇지 않도록 하는 것입니다. 결과적으로 여러분은 몇 개의 소유권 관계와 몇 개의 소유권 없는 관계로 이루어진 순환을 가질 수 있으며, 소유권 관계들만이 값을 버릴지 말지에 관해 영향을 주게 됩니다. 
  - Weak<T> 참조

# 16. 겁 없는 동시성
## 16.1. thread
- 그린 스레드 M:N 구조는 스레드들을 관리하기 위해 더 큰 언어 런타임이 필요합니다. 그런 이유로 러스트 표준 라이브러리는 오직 1:1 스레드 구현만 제공합니다. 러스트가 이러한 저수준 언어이기 때문에, 여러분이 예를 들어 어떤 스레드를 언제 실행시킬지에 대한 더 많은 제어권과 콘텍스트 교환(context switching)의 더 저렴한 비용 같은 관점을 위해 오버헤드와 맞바꾸겠다면 M:N 스레드를 구현한 크레이트도 있습니다.
- [thread.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/thread.rs)
- 스레드에 move 클로저 사용하기
  - move 클로저는 thread::spawn와 함께 자주 사용되는데 그 이유는 이것이 여러분으로 하여금 어떤 스레드의 데이터를 다른 스레드 내에서 사용하도록 해주기 때문입니다.
  - [thread-move.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/thread-move.rs)
- message passing
  - Go 언어 문서 의 슬로건에 있는 아이디어는 다음과 같습니다: "메모리를 공유하는 것으로 통신하지 마세요; 대신, 통신해서 메모리를 공유하세요"
  - 러스트가 메세지 보내기 방식의 동시성을 달성하기 위해 갖춘 한가지 주요 도구는 **채널 (channel)** 인데, 이는 러스트의 표준 라이브러리가 구현체를 제공하는 프로그래밍 개념입니다. 프로그래밍에서의 채널은 개울이나 강 같은 물의 통로와 비슷하다고 상상할 수 있습니다.
  - mpsc::channel
    - [channel.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/channel.rs)
    - mpsc는 복수 생성자, 단수 소비자 (multiple producer, single consumer) 를 나타냅니다. 
    - recv -> try_recv
  - 여러 메시지 보내고 받기
    - [channel2.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/channel2.rs)
  - 송신자를 복제하여 여러 생성자 만들기 : multiple producer, single consumer
    - ```let tx1 = mpsc::Sender::clone(&tx);```
    - [channel3.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/channel3.rs)
- 뮤텍스를 사용하여 한번에 한 스레드에서의 데이터 접근을 허용하기
  - Mutex<T>의 API
  - [mutex.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/mutex.rs)
  - 타입 시스템은 m 내부의 값을 사용하기 전에 우리가 락을 얻는 것을 확실히 해줍니다: Mutex<i32>는 i32가 아니므로 우리는 반드시 i32 값을 사용하기 위해 락을 얻어야 합니다. 우리는 이를 잊어버릴 수 없습니다; 잊어버린다면 타입 시스템이 내부의 i32에 접근할 수 없게 할 것입니다.
  - 여러분이 의심한 것처럼, Mutex<T>는 스마트 포인터입니다. 더 정확하게는, lock의 호출은 MutexGuard라고 불리우는 스마트 포인터를 반환합니다. 
- Arc<T>을 이용하는 아토믹 (atomic) 참조 카운팅
  - [arc.rs](https://github.com/cheoljoo/problemSolving/blob/master/rust-linux/test/arc.rs)
- Mutex<T>가 Cell 가족이 그러하듯 내부 가변성을 제공한다는 의미입니다. 우리가 15장에서 Rc<T>의 내용물을 변경할 수 있도록 하기 위해 RefCell<T>을 사용한 것과 같은 방식으로, Arc<T> 내부의 값을 변경하기 위해 Mutex<T>를 이용합니다.
- 두 개의 동시성 개념이 이 언어에 내재되어 있습니다: 바로 std::marker 트레잇인 Sync와 Send입니다.
  - Send를 사용하여 스레드 사이에 소유권 이전을 허용하기
    - Send 마커 트레잇은 Send가 구현된 타입의 소유권이 스레드 사이에서 이전될 수 있음을 나타냅니다. 거의 대부분의 러스트 타입이 Send이지만, 몇 개의 예외가 있는데, 그 중 Rc<T>도 있습니다: 이것은 Send가 될 수 없는데 그 이유는 여러분이 Rc<T> 값을 클론하여 다른 스레드로 복제본의 소유권 전송을 시도한다면, 두 스레드 모두 동시에 참조 카운트 값을 갱신할지도 모르기 때문입니다. 이러한 이유로, Rc<T>는 여러분이 스레드-안전성 성능 저하를 지불하지 않아도 되는 단일 스레드의 경우에 사용되도록 구현되었습니다.
    - 

# 17. (Appendix) miscellaneous 
## 17.1. code coverage
- https://marco-c.github.io/2020/11/24/rust-source-based-code-coverage.html
- 