import requests
import pytest


class TestCloudYaDisk:
    def setup_method(self):
        self.headers = {
            'Authorization': 'Вставте сюда Ваш OAuth из Яндекса, и запустите код'
        }

    @pytest.mark.parametrize(
        'key,value,statuscode',
        (
                ['path', 'Image', 201],
                ['path', 'Image', 409]
        )
    )
    def test_create_folder_and_cant_create_used_name(self, key, value, statuscode):
        params = {key: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == statuscode, \
            f"Expected code - {statuscode} but got - {response.status_code}"

    @pytest.mark.parametrize(
        'key,value,statuscode',
        (
                ['pat', 'Image', 400],
                ['path', '', 400]
        )
    )
    def test_incorrect_path_and_empty_name_in_create_folder(self, key, value, statuscode):
        params = {key: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == statuscode, f"Expected code - {statuscode} but got - {response.status_code}"

    @pytest.mark.parametrize(
        'key,value,statuscode',
        (
                ['path', 'Папка', 204],
                ['path', '6987', 204]
        )
    )
    def test_create_and_delete_folder_latinic_cyrillic_letters(self, key, value, statuscode):
        params = {key: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        if response.status_code == '201':
            response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                        headers=self.headers,
                                        params=params)
            assert response.status_code == statuscode, f"Expected code - {statuscode} but got - {response.status_code}"
        else:
            pass

    def test_get_non_existent_folder(self):
        params = {('path', 'Abcdefg')}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == 404, f"Expected code - 404 but got - {response.status_code}"

    def test_delete_non_existent_folder(self):
        params = {('path', 'Abcdefg')}
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == 404, f"Expected code - 404 but got - {response.status_code}"

    def test_create_and_check_created_folder(self):
        params = {('path', 'Abcdefg')}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == 201, f"Expected code - 201 but got - {response.status_code}"
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == 200, f"Expected code - 200 but got - {response.status_code}"
