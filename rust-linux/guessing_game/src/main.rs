//extern crate rand;
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1,101);
    println!("The secret number is {}.",secret_number);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();      // mutable

        io::stdin().read_line(&mut guess)           // originally std::io::stdin()
            .expect("Failed to read line");

        println!("You guessed: {}", guess);


        // comparing guess
        // first time , it has error as expected "string" instead of "integer"
        // but makes unexpected reuslt.
        /*
        match guess.cmp(&secret_number.to_string()) {
            Ordering::Less    => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal   => println!("You win!"),
        }
        */

        // guess is string. so guess.cmp want to string as argument variable
        // parse() this string slice into another type.
        //   parse can parse into any type that implements the FromStr trait.
        //
        // let guess: u32 = match guess.trim().parse().expect("Please type a number!");
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match guess.cmp(&secret_number) {
            Ordering::Less    => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal   => {
                println!("You win!");
                break;
            }
        }
    }
}
