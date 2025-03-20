import allure
import pytest

from conftest import run_courier_test
from data import Courier
from helpers import *


class TestCourierLogin:

    @allure.title('Тест авторизации курьера')
    def test_courier_login_success(self, courier_api, run_courier_test):
        response, _ = courier_api.login(run_courier_test)
        assert is_expected_code_and_type(response, *Courier.OK_LOGGED_IN)

    @allure.title('Тест авторизации курьера без логина или пароля')
    @pytest.mark.parametrize('account', [pytest.param(Courier.EMPTY_PASSWORD, id='no password'),
                                         pytest.param(Courier.PASSWORD, id='password only')])
    def test_courier_login_without_credentials_shows_error(self, courier_api, account):
        response, _ = courier_api.login(account)
        assert is_expected_response(response, *Courier.ERR_MISS_DATA_LOGIN)

    @allure.title(
        'Тест авторизации курьера с некорректными парами логин-пароль (включая кейсы типа "правильный логин, неверный пароль"')
    @pytest.mark.parametrize('account', [pytest.param(Courier.WRONG_ACCOUNT, id='wrong account'),
                                         pytest.param(Courier.WRONG_LOGIN, id='incorrect login'),
                                         pytest.param(Courier.WRONG_PASSWORD, id='incorrect password')])
    def test_courier_login_incorrect_credentials_shows_error(self, courier_api, run_courier_test, account):
        test_acc_data = run_courier_test.copy()
        login = account.get('login')
        pwd = account.get('password')
        if login is not None:
            test_acc_data['login'] = login
        if pwd is not None:
            test_acc_data['password'] = pwd

        response, _ = courier_api.login(test_acc_data)
        assert is_expected_response(response, *Courier.ERR_NOT_FOUND_ACC)
