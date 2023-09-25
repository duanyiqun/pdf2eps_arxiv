import os
import glob
import os
import glob
import subprocess

pdf_directory = '/Users/duanyiqun/Downloads/IJCAI 2023 -_ NIPS 2023  DeWave Translation/image/emp'
eps_directory = '/Users/duanyiqun/Downloads/IJCAI 2023 -_ NIPS 2023  DeWave Translation/image/emp'



# Create the EPS directory if it doesn't exist
pdf_files = glob.glob(os.path.join(pdf_directory, '*.pdf'))

for pdf_file in pdf_files:
    # 转化PDF到PS格式
    ps_file = pdf_file.replace('.pdf', '.ps')
    subprocess.run(['pdftops', pdf_file, ps_file], check=True)
    
    # 转化PS到EPS格式
    eps_file = os.path.join(eps_directory, os.path.basename(ps_file).replace('.ps', '.eps'))
    subprocess.run(['ps2eps', ps_file], check=True)

    # 删除临时PS文件
    # if os.path.exists(ps_file):
    #     os.remove(ps_file)

print("All files converted successfully!")