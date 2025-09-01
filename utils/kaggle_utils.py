import os, zipfile, subprocess

def kaggle_download(dataset: str, path: str = "./data"):
    """
    Download and extract a Kaggle dataset.
    
    Args:
        dataset (str): Kaggle dataset identifier, e.g. "zzero0/uci-breast-cancer-wisconsin-original"
        path (str): Local folder to save and extract dataset (default: ./data)
    """
    os.makedirs(path, exist_ok=True)
    
    # Run kaggle API download
    subprocess.run(
        ["kaggle", "datasets", "download", "-d", dataset, "-p", path, "--force"],
        check=True
    )

    # Build expected zip file name
    zip_file = os.path.join(path, dataset.split("/")[-1] + ".zip")
    
    # Extract contents
    with zipfile.ZipFile(zip_file, "r") as z:
        extract_dir = os.path.join(path, dataset.split("/")[-1])
        os.makedirs(extract_dir, exist_ok=True)
        z.extractall(extract_dir)
    
    print(f"✅ {dataset} ready at {extract_dir}")
    return extract_dir
