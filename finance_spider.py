import requests
import pandas as pd
import json

def get_performance_data():
    # API接口URL
    url = 'https://datacenter-web.eastmoney.com/api/data/v1/get'
    
    # 请求参数
    params = {
        'sortColumns': 'UPDATE_DATE',
        'sortTypes': '-1',
        'pageSize': '50',
        'pageNumber': '1',
        'reportName': 'RPT_LICO_FN_CPD',
        'columns': 'ALL',
        'filter': '(SECURITY_CODE="688671")',
        'source': 'WEB',
        'client': 'WEB'
    }
    
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://data.eastmoney.com/bbsj/688671.html',
        'Accept': '*/*',
    }
    
    try:
        # 发送请求
        response = requests.get(url, params=params, headers=headers)

        # 提取JSON数据
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(f'JSON解析错误: {str(e)}')
            return
        
        # 提取表格数据
        if data['result'] and data['result']['data']:
            df = pd.DataFrame(data['result']['data'])
            # 选择需要的列并重命名
            columns_map = {
                'SECURITY_CODE': '证券代码',
                'SECURITY_NAME_ABBR': '证券简称',
                'TRADE_MARKET_CODE': '交易市场代码',
                'TRADE_MARKET': '交易市场',
                'SECURITY_TYPE_CODE': '证券类型代码',
                'SECURITY_TYPE': '证券类型',
                'UPDATE_DATE': '更新日期',
                'REPORTDATE': '报告日期',
                'BASIC_EPS': '基本每股收益',
                'DEDUCT_BASIC_EPS': '扣非每股收益',
                'TOTAL_OPERATE_INCOME': '营业总收入',
                'PARENT_NETPROFIT': '母公司净利润',
                'WEIGHTAVG_ROE': '加权平均净资产收益率',
                'YSTZ': '营业收入同比增长',
                'SJLTZ': '净利润同比增长',
                'BPS': '每股净资产',
                'MGJYXJJE': '每股经营现金流量',
                'XSMLL': '销售毛利率',
                'YSHZ': '营业收入环比增长',
                'SJLHZ': '净利润环比增长',
                'ASSIGNDSCRPT': '分配方案',
                'PAYYEAR': '分红年度',
                'PUBLISHNAME': '发布机构',
                'ZXGXL': '最新股本',
                'NOTICE_DATE': '公告日期',
                'ORG_CODE': '机构代码',
                'TRADE_MARKET_ZJG': '交易市场中介机构',
                'ISNEW': '是否新股',
                'QDATE': '季度日期',
                'DATATYPE': '数据类型',
                'DATAYEAR': '数据年份',
                'DATEMMDD': '数据日期',
                'EITIME': '录入时间',
                'SECUCODE': '证券统一代码',
                'BOARD_NAME': '板块名称',
                'ORI_BOARD_CODE': '原板块代码',
                'BOARD_CODE': '板块代码'
            }
            
            df = df[list(columns_map.keys())].rename(columns=columns_map)
            
            # 保存为CSV文件
            df.to_csv('performance_data.csv', index=False, encoding='utf-8-sig')
            print('数据已成功保存到performance_data.csv')
        else:
            print('未获取到数据')
            
    except Exception as e:
        print(f'发生错误: {str(e)}')

if __name__ == '__main__':
    get_performance_data()