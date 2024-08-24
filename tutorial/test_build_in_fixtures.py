def test_tmpdir(tmpdir):
    test_file = tmpdir.join('test.txt')

    test_file.write('This is a test file.')

    assert test_file.read() == 'This is a test file.'