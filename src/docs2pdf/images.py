from pathlib import Path
from urllib.parse import urlparse

import requests


class ImageDownloader:

    def download(self, urls: list[str], output_dir: Path) -> dict[str, str]:

        image_dir = output_dir / "_figures"
        image_dir.mkdir(parents=True, exist_ok=True)

        mapping = {}

        session = requests.Session()

        for url in sorted(set(urls)):

            filename = Path(urlparse(url).path).name

            destination = image_dir / filename

            if not destination.exists():

                print(f"Downloading image: {filename}")

                response = session.get(url, timeout=60)
                response.raise_for_status()

                destination.write_bytes(response.content)

            mapping[url] = f"_figures/{filename}"

        return mapping
