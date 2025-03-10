import plotly.graph_objects as go

# 创建图形
fig = go.Figure()

# 添加数据
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 1, 3]))

# 添加文本
fig.update_layout(title="Hello, World")

# 显示图形
fig.show()