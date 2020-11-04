from jenkins_example.helloworld import helloworld

def test_helloworld():
    assert helloworld() == "Hello World"