import requests
import configuration
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)


def get_logs_p2(count):
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH2 + "?count=" + str(count))


def get_logs_p(count):
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)



# response = get_logs()
#
# print("code: ", response.status_code, "\nheaders: ", response.headers)
#
# response = get_logs_p(20)
#
# print("code: ", response.status_code, "\nheaders: ", response.headers)
#
# response = get_users_table()
#
# print(response.status_code)
#
# response = post_new_user(data.user_body)
#
# print(response.status_code, "\n", response.json(), response.__dict__)
# response = post_products_kits(data.product_ids)
#
# print(response.status_code, "\n", response.json())