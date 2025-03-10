from nicegui import ui
import plotly.graph_objects as go

# 初始化存储数据的列表
x_data = []
y_data = []
z_data = []

# 创建 NiceGUI 应用
ui.label("请输入 x、y 和 z 的值，点击按钮生成或更新图表")

# 创建输入框
x_input = ui.input(label="X 轴值", placeholder="输入 x 值")
y_input = ui.input(label="Y 轴值", placeholder="输入 y 值")
z_input = ui.input(label="Z 轴值", placeholder="输入 z 值")

# 创建 Plotly 图表
plotly_figure = go.Figure()
plotly_plot = ui.plotly(plotly_figure).classes('w-full h-128')

# 更新图表的函数
def update_plot():
    try:
        # 获取输入的值并转换为浮点数
        x_value = float(x_input.value)
        y_value = float(y_input.value)
        z_value = float(z_input.value)

        # 将值添加到数据列表中
        x_data.append(x_value)
        y_data.append(y_value)
        z_data.append(z_value)

        # 更新 Plotly 图表
        plotly_figure.add_trace(go.Scatter3d(x=x_data, y=y_data, z=z_data, mode='markers', name='数据点'))
        plotly_plot.update()

        # 清空输入框
        x_input.value = ""
        y_input.value = ""
        z_input.value = ""

        ui.notify(f"添加点 ({x_value}, {y_value}, {z_value}) 成功！", type='positive')
    except ValueError:
        ui.notify("请输入有效的数字！", type='negative')

# 删除点的函数
def delete_point():
    try:
        # 获取输入的值并转换为浮点数
        x_value = float(x_input.value)
        y_value = float(y_input.value)
        z_value = float(z_input.value)

        # 查找并删除点
        if x_value in x_data and y_value in y_data and z_value in z_data:
            index = x_data.index(x_value)
            x_data.pop(index)
            y_data.pop(index)
            z_data.pop(index)

            # 更新 Plotly 图表
            plotly_figure.data = []  # 清空现有数据
            plotly_figure.add_trace(go.Scatter3d(x=x_data, y=y_data, z=z_data, mode='markers', name='数据点'))
            plotly_plot.update()

            ui.notify(f"删除点 ({x_value}, {y_value}, {z_value}) 成功！", type='positive')
        else:
            ui.notify("未找到该点！", type='negative')
    except ValueError:
        ui.notify("请输入有效的数字！", type='negative')

# 创建按钮
ui.button("增加点", on_click=update_plot)
ui.button("删除点", on_click=delete_point)

# 启动 NiceGUI 应用
ui.run(port=8880)