import nltk

def download_required_packages():
    """Downloads the necessary packages NLTK"""

    packages = ['punlt', 'stopwords', 'punkt_tab']

    for package in packages:
        try:
            nltk.download(package)
            print(f"Package '{package} installed successfully")
        except Exception as e:
            print(f"Error with '{package}': {e} ")




if __name__ == "__main__":
    download_required_packages()