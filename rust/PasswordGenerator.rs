use rand::Rng;
use std::io::{self, Write};

fn main() {
    let mut passes: String = String::new();
    print!("Enter desired password length: ");
    io::stdout().flush().unwrap();

    io::stdin()
        .read_line(&mut passes)
        .expect("Could not read line");

    let passes: u8 = passes.trim()
                       .parse()
                       .expect("Could not parse");

    let mut password: Vec<u8> = Vec::new();

    for _pass in 1..=passes {
        let selector: u8 = rand::thread_rng().gen_range(1..=3);

        match selector {
            1 => {
                let new: u8 = rand::thread_rng().gen_range(48..=57);
                password.push(new);
            }
            
            2 => {
                let new: u8 = rand::thread_rng().gen_range(65..=90);
                password.push(new);
            }

            3 => {
                let new: u8 = rand::thread_rng().gen_range(97..=122);
                password.push(new);
            }

            _ => (),
        }

    }

    let password: String = String::from_utf8(password).unwrap();

    println!("{password}");


}