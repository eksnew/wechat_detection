# WECHAT_DETECTION


## 环境配置与安装流程

以下是一个已经保证成功运行的环境，建议使用具有独立显卡的电脑作为服务器以保证 CUDA 相关驱动与工具的正常安装与使用。

### 依赖

- windows 10/11
- Python 3.9
- Pytorch 1.12
- CUDA 11.6
- GCC 8.1
- MMCV-full 1.6

### 安装流程

1. 准备环境

假设已经安装了 CUDA 11.6 驱动程序，使用 conda 新建虚拟环境并进入：

```shell
conda create -n wechat_detection python=3.9
conda activate wechat_detection
```

2. 安装 cudatoolkit 和 PyTorch 以及相关扩展

请保证 `cudatoolkit` 与驱动程序版本一致，通过以下命令行查看：

```shell
nvidia-smi
```
假设已经配置 `conda forge` ，安装 cudatoolkit 和 cudnn：

```shell
conda install cudatoolkit=11.6
conda install cudnn
```
参考 [PyTorch 官网](https://pytorch.org/) 使用指令安装 PyTorch 和 torchvision
,以当前环境为例：

```shell
conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge
```

3. 安装 MMDetection

安装详细流程建议参考 [MIM](https://github.com/open-mmlab/mim) ，从安装openmim开始：
```shell
pip install openmim
```

请务必安装兼容 CUDA 功能的 MMCV_full，以当前环境为例，使用如下指令：

```shell
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu116/torch1.12.0/index.html
```

安装MMDetection：

```shell
pip install mmdet
```

上述的命令会在环境中安装最新版本的 MMCV-full 和 MMDetection。（截止到2022/10，mmcv-full=1.6.1, mmdet=2.25.1）

如果 MMDetection 环境配置成功，运行测试程序将得到图片结果：

```shell
python image_demo.py
```

4. 服务器环境搭建
在环境 wechat_detection 中运行如下命令以安装搭建Diangle服务器所需要的扩展：

```shell
Please fill in the blanks.
```



## 共同开发wechat_detection

### 将本地的代码上传到wechat_detection的分支branch_name

如果已经安装了git命令行，请使用以下所示的方法将修改后的代码上传到指定的分支 
`branch_name` 中，而不是将代码和权重文件压缩包上传到群聊或分支（直球）。

```shell
git branch branch_name
git checkout bramch_name
git add .
git commit -m "description"
git push origin branch_name
```