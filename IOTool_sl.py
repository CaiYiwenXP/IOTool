import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
st.write('IOTool Demo')
st.title('IO硬件资源管理工具')
st.write('分析EEA4.0 部件、集成方案可行性')

im = Image.open(r"D:\\001-Projets\\cin_xml_generation\\IOTool\\F30CAR.jpg")
# st.button('Say hello or not')
# if st.button('Say hello',on_click=None,key=1):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')

# uploaded_file = st.file_uploader('上传硬件资源配置文件',type=['csv','xlsx','xls'])
# st.header('LDCU硬件接口使用总计')
# if uploaded_file is None:
#     st.write('请上传硬件资源配置文件')
#     st.stop()
# st.write('硬件资源配置文件内容如下，按所选项目进行显示')
# @st.cache_data
# def load_data(file):
#     print("正在执行加载数据......")
#     return pd.read_excel(file,None)
# dfs = pd.read_excel(uploaded_file,sheet_name=None)
# names = list(dfs.keys())
# sheet_selected = st.multiselect('项目',names,[])
# if len(sheet_selected) == 0:
#     st.stop()
# tabs = st.tabs(sheet_selected)
# for tab,name in zip(tabs,sheet_selected):
#     with tab:
#         df = dfs[name]
#         st.dataframe(df)
#         # for i in range(1,df.shape[0]+1):
#         #     st.write(df.iloc[i-1])
#         print(df)

# button1 = button(username="fake-username", text = '',emoji= '⚪',floating=False, width=221)
# #streamlit 显示图形，类似电路框图
# random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")
# # Row 1:
# my_grid.dataframe(random_df, use_container_width=True)
# my_grid.line_chart(random_df, use_container_width=True)
# # Row 2:
# my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
# my_grid.text_input("Your name")
# my_grid.button("Send", use_container_width=True)
# # Row 3:
# my_grid.text_area("Your message", height=40)
# # Row 4:
# my_grid.button("⚪",key = 1, use_container_width=True)
# my_grid.button("⚪", key = 2,use_container_width=True)
# my_grid.button("⚪", key = 3,use_container_width=True)
# my_grid.button("⚪",key = 4, use_container_width=True)
# # Row 5 (uses the spec from row 1):
# with my_grid.expander("Show Filters", expanded=True):
#     st.slider("Filter by Age", 0, 100, 50)
#     st.slider("Filter by Height", 0.0, 2.0, 1.0)
#     st.slider("Filter by Weight", 0.0, 100.0, 50.0)
# my_grid.dataframe(random_df, use_container_width=True)
# 根据关联域控的值将形状改为方形

def get_symbol(rel_domain):
    if rel_domain != '非独立模块':
        return 'square'
    else:
        return 'circle'
st.write('硬件资源配置原理图如下')

# uploaded_file = st.file_uploader('上传硬件资源配置文件',type=['csv','xlsx','xls'])
uploaded_file = 'D:\\001-Projets\cin_xml_generation\IOTool\Interface_new.xlsx'
st.header('车型部件线束分析')
st.write('文件内容如下，按所选项目进行显示')
@st.cache_data
def load_data(file):
    print("正在执行加载数据......")
    return pd.read_excel(file,None)
dfs = pd.read_excel(uploaded_file,sheet_name=None)
names = list(dfs.keys())
sheet_selected = st.multiselect('pages',names,['Interface'])
if len(sheet_selected) == 0:
    st.stop()
tabs = st.tabs(sheet_selected)
for tab,name in zip(tabs,sheet_selected):
    with tab:
        df = dfs[name]
        st.dataframe(df)
        # for i in range(1,df.shape[0]+1):
        #     st.write(df.iloc[i-1])
        print(df)
dfs = pd.read_excel(uploaded_file,sheet_name='布置信息',header=0, usecols="A:G")
ecuData = dfs
print(ecuData.columns)
fig = px.scatter(
    ecuData,
    x='x坐标',
    y='y坐标',
    hover_name='零件名称',
    color=ecuData['关联域控'],#.apply(lambda x: 'yellow' if x == 'cdcu' else 'blue'),
    symbol=ecuData['模块名称'].apply(get_symbol) ,#.apply(lambda x: 'diamond' if x == 'CDCU'|'RDCU'|'LDCU'|'XPU' else 'circle'),
    # hover_data={'模块名称': True}
)

# # 在布局中添加背景图片
# fig.update_layout(
#         images=[
#         dict(
#             source=im,
#             xref="paper", yref="paper",
#             x=0, y=1,
#             sizex=1, sizey=1,
#             sizing="stretch",
#             opacity=0.3,
#             layer="below"
#         )
#     ]
# )
# fig.update_layout(
#     images=[
#         dict(
#             source=im,  # 换为背景图片的URL或文件路径
#             xref="x",
#             yref="paper",
#             x=ecuData['x坐标'].min(),  # 根据数据的最小值来设置背景图片的位置
#             y=1,
#             sizex=ecuData['x坐标'].max() - ecuData['x坐标'].min(),  # 根据数据的范围调整背景图片的大小
#             sizey=1,
#             sizing="stretch",
#             opacity=0.5,
#             layer="below"
#         )
#     ]
# )
fig.update_layout(
    images=[
        dict(
            source=im,  # 换为背景图片的URL或文件路径
            xref="x",
            yref="y",
            x=650,  # 根据数据的最小值来设置背景图片的位置
            y=1000,
            sizex=5300-650,  # 根据数据的范围调整背景图片的大小
            sizey=2000,
            sizing="stretch",
            opacity=0.3,
            layer="below"
        )
    ]
)
fig.update_traces(marker=dict(line=dict(color='black', width=1)))
# 设置X和Y轴的坐标范围
fig.update_layout(
    xaxis=dict(range=[0, 5500]),  # 设置X轴的范围
    yaxis=dict(range=[-1000, 1000])   # 设置Y轴的范围
)
fig.update_traces(marker=dict(size=8))
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

print(ecuData)
