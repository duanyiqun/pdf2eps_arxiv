# Convert Matplotlib PDF to EPS
A simple script for converting matplotlib-generated images to eps. 
Many times it will fail if you want to submit it to Arxiv.


If the pdf image could directly open by os:
```sh
python convert_raw.py
```

If not, directly using matplotlib to re-write.

```sh
python convertpdf.py
```
