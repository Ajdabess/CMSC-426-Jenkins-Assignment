from sample_code import digital_root
 
 
def test_digital_root():
    assert digital_root(6832) == 1
    assert digital_root(9875) == 2
    assert digital_root(99) == 9
    assert digital_root(7) == 7
    assert digital_root(0) == 0
    assert digital_root(-5) == -1
 
 
if __name__ == "__main__":
    test_digital_root()
    print("All tests passed!")
 
