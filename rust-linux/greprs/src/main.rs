extern crate greprs;   // lib.rs
use greprs::Config;

use std::env;
//use std::fs::File;
//use std::io::prelude::*;
use std::process;
//use std::error::Error;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    println!("Searching for '{}'", config.query);
    println!("In file : {}", config.filename);
    println!();

    if let Err(e) = greprs::run(config){
        println!("Application error: {}",e);
        process::exit(1);
    }
}

/*
fn parse_config(args: &[String]) -> Config {
    let query = args[1].clone();
    let filename = args[2].clone();

    Config { query, filename }
}
*/
