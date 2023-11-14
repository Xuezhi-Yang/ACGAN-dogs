## GAN网络生成小狗图像——使用说明
1. **数据加载**
    * 数据集下载链接 https://www.kaggle.com/competitions/generative-dog-images/data
    * 请下载数据集后将all-dogs解压至本文件夹下，路径为'/input/all-dogs', 将Annotation解压至'/input/annotation'
    * 若仍无法运行,请查看Train_ACGAN.ipynb文件中的ROOT是否正确赋值为'/input/'
2. **模型使用**
    * mygan中定义了生成器并载入了我们已经训练好的生成器模型
    * 确保当前目录包含generator_w.h5即可完成模型载入
3. **用户交互界面**
    * 我们采用PYQT5实现用户交互界面
    * 确保当前目录包含window.ui文件
    * 运行代码之后会生成交互界面，输入数字作为种子，按下生成按钮