use rand::Rng;
use std::io::{self, Write};


fn prompt() {
    print!("Enter your desired password length: ");
    io::stdout().flush().unwrap();
}

fn input_length() -> String {
    let mut s: String = String::new();
    io::stdin().read_line(&mut s).expect("Could not read line");
    return s
}

fn convert_length(s: String) -> u8 {
    let s_res = s.trim().parse();

    let s_new: u8 = match s_res {
        Ok(num) => num,
        Err(_) => {
            println!("Not an integer!");
            get_password_length()
        }
    };
    return s_new
}

fn get_password_length() -> u8 {
    prompt();
    let s: String = input_length();
    let s: u8 = convert_length(s);
    return s
}

fn gen_digit() -> u8 {
    let num: u8 = rand::thread_rng().gen_range(48..=57);
    return num
}

fn gen_uppercase() -> u8 {
    let num: u8 = rand::thread_rng().gen_range(65..=90);
    return num
}

fn gen_lowercase() -> u8 {
    let num: u8 = rand::thread_rng().gen_range(97..=122);
    return num
}

fn generate_password(passes: u8) {
    let mut password: Vec<u8> = Vec::new();

    for _pass in 1..=passes {
        let selector: u8 = rand::thread_rng().gen_range(1..=3);

        match selector {
            1 => {
                password.push(gen_digit());
            }
            
            2 => {
                password.push(gen_uppercase());
            }

            3 => {
                password.push(gen_lowercase());
            }

            _ => (),
        }

    }

    let password: String = String::from_utf8(password).unwrap();

    println!("{password}");
}
fn main() {
    generate_password(get_password_length());
}