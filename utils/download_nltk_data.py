import nltk
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_nltk_data():
    """Download all required NLTK data packages."""
    required_packages = [
        'punkt',
        'averaged_perceptron_tagger',
        'stopwords',
        'wordnet'
    ]
    
    for package in required_packages:
        try:
            logger.info(f"Downloading {package}...")
            nltk.download(package, quiet=False)
            logger.info(f"Successfully downloaded {package}")
        except Exception as e:
            logger.error(f"Error downloading {package}: {str(e)}")

if __name__ == "__main__":
    download_nltk_data() 