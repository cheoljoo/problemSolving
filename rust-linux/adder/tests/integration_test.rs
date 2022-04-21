extern crate adder;

#[test]
fn integration_test_it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}

