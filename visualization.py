import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def preprocess_data(df):
    # 将日期字符串转换为datetime格式
    df['报告日期'] = pd.to_datetime(df['报告日期'])
    return df

def plot_cost_structure(df):
    """
    绘制成本构成比例的饼图
    """
    cost_values = [float(df['营业总收入'].iloc[0] - df['母公司净利润'].iloc[0]), float(df['营业总收入'].iloc[0] * 0.1), float(df['营业总收入'].iloc[0] * 0.05)]
    cost_labels = ['营业成本', '税费', '其他成本']
    
    # 设置颜色方案和阴影效果
    colors = ['#ff9999','#66b3ff','#99ff99']
    explode = (0.1, 0, 0)  # 突出显示最大成本项
    
    plt.figure(figsize=(8, 8))
    plt.pie(cost_values, labels=cost_labels, autopct='%1.1f%%', colors=colors, 
            explode=explode, shadow=True, startangle=90)
    plt.title('成本构成比例', fontsize=16)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0))
    plt.tight_layout()
    plt.savefig('output1.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('performance_data.csv')
    df = preprocess_data(df)
    plot_cost_structure(df)