'''
This is a file on which I run pylint to check the readability quality.
It contains just an elementary function with an unit test.
'''

def myfunction(x_num):
    '''
    Elementary example
    '''
    return x_num * 2.
#---


def test_myfunction():
    '''
    Test function for myfunction
    '''
    assert myfunction(4.) == 8.
    assert myfunction(0.) == 0.
#---


if __name__ == '__main__':
    print('Use pytest example.py to run the test')
