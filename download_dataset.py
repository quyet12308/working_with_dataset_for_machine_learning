# from simple_image_download import simple_image_download as simp

# response = simp.simple_image_download

# keywords = ["building workers"]

# for kw in keywords:
#     response().download(kw,200)

from bing_image_downloader.downloader import download

query_string = 'hurman'

download(query_string, limit=200,  output_dir='dataset_for_hurman', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)