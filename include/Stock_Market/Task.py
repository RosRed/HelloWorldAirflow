def _get_Price(ti):
    import json ,requests,logging
    from airflow.hooks.base import BaseHook
    logging.info("Starting _get_Price function")
    data = ti.xcom_pull(task_ids='Yahoo_price')
    url=data['Url']
    STE=data['STE']
    URL_GLOBAL=f"{url}{STE}?metrics=high?&interval=1d&range=1y"
    connection = BaseHook.get_connection("Yahoo_Price")
    logging.info(f"url global: {URL_GLOBAL}")
    Result=requests.get(URL_GLOBAL,headers=connection.extra_dejson['headers']['headers'])
    logging.info(f"Response Status Code: {Result.status_code}")
    print(f"Response JSON: {Result.json()["chart"]["result"]}")


