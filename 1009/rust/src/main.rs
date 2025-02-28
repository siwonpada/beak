fn main() {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    let n: i32 = line.trim().parse::<i32>().unwrap();
    let mut arr = Vec::<i32>::new();
    for _ in 1..=n {
        let mut lines = String::new();
        std::io::stdin().read_line(&mut lines).unwrap();
        let mut iter = lines.split_whitespace();
        let a: i32 = iter.next().unwrap().parse::<i32>().unwrap();
        let b: i32 = iter.next().unwrap().parse::<i32>().unwrap();
        let mut result = 1;
        for _ in 1..=b {
            result = (result * a) % 10;
        }
        arr.push(if result == 0 { 10 } else { result });
    }
    for i in arr {
        println!("{}", i);
    }
}
