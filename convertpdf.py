import os
import glob
import matplotlib.pyplot as plt

pdf_directory = '/Users/duanyiqun/Downloads/IJCAI 2023 -_ NIPS 2023  DeWave Translation/image/yac'
eps_directory = '/Users/duanyiqun/Downloads/submission /IJCAI 2023 -_ NIPS 2023  DeWave Translation/image/yac'

plt.rcParams['path.simplify'] = True
plt.rcParams['path.simplify_threshold'] = 1.0  # 调整此值以找到最佳平衡点
# 如果EPS目录不存在，创建它
if not os.path.exists(eps_directory):
    os.makedirs(eps_directory)

# 获取PDF文件列表
pdf_files = glob.glob(os.path.join(pdf_directory, '*.pdf'))

for pdf_file in pdf_files:
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')  # 隐藏坐标轴

    img = plt.imread(pdf_file, format='pdf')
    ax.imshow(img, aspect='auto')

    # 保存为EPS格式
    
    #eps_file = os.path.join(eps_directory, os.path.basename(pdf_file).replace('.pdf', '.eps'))
    #print("Converting {} to {}".format(pdf_file, eps_file))
    #plt.savefig(eps_file, format='eps', bbox_inches='tight', pad_inches=0)
    #plt.close()
    
    png_file = os.path.join(eps_directory, os.path.basename(pdf_file).replace('.pdf', '.jpg'))
    print("Converting {} to {}".format(pdf_file, png_file))
    plt.savefig(png_file, format='jpg', bbox_inches='tight', pad_inches=0, dpi=500)
    plt.close()


    

print("All files converted successfully!")
