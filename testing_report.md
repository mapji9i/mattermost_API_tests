## Отчет о тестировании
Для тестирования требуется настроенный докер doker контейнер с mattepmost настроенный согласно его официальной документации.
При тестировании используется язык программирования python и библиотека для тестирования  pytest, а так же дополнительно библиотека pytest-env
для кастомизации переменных окружения при  тестировании.

Данные библиотеки устанавливаются командами:
  pip install pytest
  pip install pytest-env
Для настройки окружения тестирования нужно заполнить файл pytest.ini
  pytest.ini 

Запуск тестов осуществляется командой:
  pytest -c ./pytest.ini <path_to_file_with_tests>.py

  Важно при первичной настроке mattermost требуется иметь тестовый набор пользователей (заблокированный, неактивированный) согласно условиям тестирования.
В mattermost должно быть включено требование обязательного подтвреждения email, а так же возможность создания токенов доступа, создан токен для одного тестового пользователя. 

Тесты проведены 23.04.25 пользователем Дунайцев А.А.

 | Номер теста | Краткое описание теста | Файл с тестами | Название тестовой функции | Используемые переменные среды | Результат тестирования | Примечание |
 |-------------|-------|-------|-------------|-------------|-------------|-------------|
 | 1 | Попытаться войти в систему с неверными логином и паролем пользователя | Login_tests.py | test_try_login_with_wrong_credentiald() | BASE_URL | Ожидаемые результаты получены | Требуется задавать произвольные неправильные учетные данные пользователя |
| 2 | Попытаться войти в систему с учетными данными заблокированного пользователя | Login_tests.py |test_try_login_in_deactivated_accont() | BASE_URL, DEACTIVATED_USER_MAIL, DEACTIVATED_USER_PASSWORD  | Ожидаемые результаты получены | Требуется задавать учетные данные заблокированного пользователя |
| 3 | Симулирвать отсутствие соединения с сервером аутентификации | Login_tests.py |test_try_login_inactive_auth_server()| BASE_URL, ACTIVE_USER_MAIL, ACTIVE_USER_PASSWORD | Ожидаемые результаты получены | Для симуляции отключенного сервера аутентификации приходится отключать базу данных mattermost, что не очень хорошо. Плюс очень сложно диагностировать причину ошибки, потому что возвращается обычный ответ как при неверных учетных данных. Даже если использовать 100% рабочие учетные данные |
 | 4 | Попытаться войти в систему с учетными данными не активированного пользователя | Login_tests.py |test_try_login_in_email_not_verified_accont()| BASE_URL, NOT_ACTIVATED_USER_MAIL, NOT_ACTIVATED_USER_PASSWORD | Ожидаемые результаты получены | Требуется задавать учетные данные пользователя, не подтвердившего почту |
 | 5 | Проверка успешного создания чата/канала | Create_channel_tests.py | test_try_create_channel() | BASE_URL, TEST_USER_TOKEN, TEST_USER_ID, TEST_TEAM_ID | Ожидаемые результаты получены | Без примечаний |
 | 6 | Проверка создания канала с уже существующим названием | Create_channel_tests.py | test_try_create_existed_channel() | BASE_URL, TEST_USER_TOKEN, TEST_USER_ID, TEST_TEAM_ID | Ожидаемые результаты получены | Требуется tear_down после тестов |
 | 7 | Проверка отправки сообщения в чат/канал | Create_post_to_channel.py | test_try_to_create_post() | BASE_URL, TEST_USER_TOKEN, TEST_USER_ID, TEST_CHANNEL_ID | Ожидаемые результаты получены | Без примечаний |
| 8 | Проверка получения сообщений из чата/канала | Create_post_to_channel.py | test_try_to_get_all_posts() | BASE_URL, TEST_USER_TOKEN, TEST_USER_ID, TEST_CHANNEL_ID | Ожидаемые результаты получены | Без примечаний |
| 9 | Проверка добавления пользователей в чат/канал | Add_users_in_chat.py | test_try_to_add_two_users() | BASE_URL, TEST_USER_TOKEN, TEST_USER_ID,TEST_USER_ID2,TEST_USER_ID3, TEST_CHANNEL_ID | Ожидаемые результаты получены | Без примечаний |
| 10 | Проверка добавления пользователей в чат/канал | Add_users_in_chat.py | test_try_to_delete_some_user() | BASE_URL, TEST_USER_TOKEN, TEST_USER_ID,TEST_USER_ID2,TEST_USER_ID3, TEST_CHANNEL_ID | Ожидаемые результаты получены | Без примечаний |

