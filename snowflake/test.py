import snowflake.client


def get_snowflake_guid():
    snowflake.client.setup('127.0.0.1', '8910')
    guid = snowflake.client.get_guid()
    return guid


if __name__ == '__main__':
    print(snowflake.client.get_stats())
    # for _ in range(100):
    print(get_snowflake_guid())
