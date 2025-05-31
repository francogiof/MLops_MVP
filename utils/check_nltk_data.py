import nltk
import os
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_nltk_data():
    """Check and download all required NLTK data packages."""
    # Print NLTK data path
    nltk_data_path = nltk.data.path
    logger.info("NLTK data paths:")
    for path in nltk_data_path:
        logger.info(f"  - {path}")
        if os.path.exists(path):
            logger.info(f"    ✓ Directory exists")
        else:
            logger.info(f"    ✗ Directory does not exist")

    # Required packages
    required_packages = [
        'punkt',
        'averaged_perceptron_tagger',
        'stopwords',
        'wordnet'
    ]
    
    # Check each package
    for package in required_packages:
        try:
            logger.info(f"\nChecking {package}...")
            # Try to load the package
            if package == 'punkt':
                nltk.data.find('tokenizers/punkt')
            elif package == 'averaged_perceptron_tagger':
                nltk.data.find('taggers/averaged_perceptron_tagger')
            elif package == 'stopwords':
                nltk.data.find('corpora/stopwords')
            elif package == 'wordnet':
                nltk.data.find('corpora/wordnet')
            
            logger.info(f"✓ {package} is properly installed")
        except LookupError:
            logger.info(f"✗ {package} is not found, downloading...")
            try:
                nltk.download(package, download_dir=nltk_data_path[0], quiet=False)
                logger.info(f"✓ Successfully downloaded {package}")
            except Exception as e:
                logger.error(f"Error downloading {package}: {str(e)}")
                sys.exit(1)

if __name__ == "__main__":
    check_nltk_data() 