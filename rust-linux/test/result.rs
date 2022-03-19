use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");
    let f = match f {
        Ok(file) => file ,
        Err(error) => {
            println!("AAA {:?}",error.kind());
            panic!("There was a problem opening the file: {:?}", error);
        }
    };
}
