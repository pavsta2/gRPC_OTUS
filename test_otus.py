import pytest
import client
# from grpc._channel import _InactiveRpcError


def test_creat_user_posit():
    res = client.register_user('Star', 'Pavel', 22, True)
    assert isinstance(res.Id, int)


@pytest.mark.parametrize('params',
                         [22],
                         ids=['lastname - int'])
def test_creat_user_negot(params):
    with pytest.raises(TypeError):
        client.register_user(params, 'Pavel', 22, True)


