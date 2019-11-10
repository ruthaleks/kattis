use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n)
        .expect("Failed to read line");
    let n: u32 = n.trim().parse()
        .expect("Not a number");

    for _i in 0..n{
        let mut test_case = String::new();
        io::stdin().read_line(&mut test_case)
            .expect("Failed to read line");

        if test_case.trim() == "P=NP"{
            println!("skipped");
        } else {
            let num:Vec<&str>= test_case.trim().split("+").collect();
            let x:u32 = num[0].parse()
                .expect("Not a number.");
            let y:u32 = num[1].parse()
                .expect("Not a number.");
            println!("{}", x+y);
        }
        
            
    }
}
