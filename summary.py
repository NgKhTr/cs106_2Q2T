import matplotlib.pyplot as plt
import os
import seaborn as sns
import pandas as pd

SUMMARY_PATH = "final_summary"
SUMMARY_OUT_PATH = "final_summary.png"

def drawChart(data):
    # Dữ liệu mẫu
    # Tạo DataFrame từ dữ liệu
    # Vẽ biểu đồ cột với mỗi đơn vị trục x có nhiều cột
    sns.set_theme()
    sns.barplot(x='Map', y='Duration', hue='Model', data=data)

    # Hiển thị biểu đồ
    plt.savefig(SUMMARY_OUT_PATH)

def main():
    if not os.path.exists(SUMMARY_PATH):
        return
    data = []
    for map_model_data in os.listdir(SUMMARY_PATH):
        sep = map_model_data[:-4].rsplit('_', 1)
        if len(sep) < 2:
            continue
        _map, model = sep
        dataF = pd.read_csv(os.path.join(SUMMARY_PATH, map_model_data))

        row_dict = dataF.iloc[-1].to_dict()

        dataPoint = {'Map': _map, 'Model': model, 'Duration': dataF['duration'].min()}
        data.append(dataPoint)

    drawChart(pd.DataFrame(data))
    print()
main()