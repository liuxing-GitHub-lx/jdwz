import pyperclip
import pyautogui
import pandas as pd

import time


def clearText(text):
    text = text.replace("	", "")
    idx = text.find('招聘/审核通过人数：')
    text = text[idx + 10:]
    idx = text.find('/')
    return text[idx + 1:]


def queryData(query, pos1, pos2, pos3, pos4):
    time.sleep(0.4)
    # 点击输入框
    pyautogui.click(pos1[0], pos1[1])
    # 全选 用输入数据替代旧数据
    pyautogui.hotkey('ctrl', 'a')

    # 输入数据
    pyperclip.copy(query)
    pyautogui.hotkey('ctrl', 'v')

    # 等待数据查询
    time.sleep(0.4)
    # 确定查询
    pyautogui.click(pos2[0], pos2[1])
    # 移动到复制起点
    pyautogui.moveTo(pos3[0], pos3[1], duration=0.2)
    # 拖拽到复制终点
    pyautogui.dragTo(pos4[0], pos4[1], duration=0.5)
    # 复制
    pyautogui.hotkey('ctrl', 'c')


def click(origin_df, pos1, pos2, pos3, pos4, file_name):
    # 记录查询到的结果
    query_list = []

    print("begin")
    begin = time.time()

    # 获取岗位代码
    idx_list = origin_df['岗位代码'].values

    for query in idx_list:
        print(query)
        queryData(str(query), pos1, pos2, pos3, pos4)

        # 获得剪切板内容
        text = pyperclip.paste()
        print(text)

        # 获得通过人数
        text = clearText(text)

        # 保存
        query_list.append(text)

    origin_df['通过人数'] = query_list
    origin_df.to_csv(file_name)
    print('end！\ntotal using(sec) -> ', end='')
    print(time.time() - begin)


def run():
    # 第一个位置 输入框
    location1 = (1236, 500)
    # 第二个位置 确定查询
    location2 = (1236, 526)
    # 第三个位置 复制起点
    location3 = (600, 1000)
    # 获得第四个位置 复制终点
    location4 = (1780, 1000)

    output_file_name = 'jdwz_update1.csv'

    df = pd.read_csv('jdwz1.csv', index_col=0)
    click(df, location1, location2, location3, location4, output_file_name)


if __name__ == '__main__':
    run()
