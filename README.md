# musicpy

<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- ABOUT THE PROJECT -->
## About The Project

This is a simply comand line utility to download tracks and albums to your local computer. 

### Built With

* python
* youtube-dl

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Download the following script and make sure the latest version of `yotube-dl` and `ffmpeg` are downloaded and installed to the machine.

### Prerequisites

Use brew to install the following packages
```sh
brew install youtube-dl
brew install ffmpeg
```

### Installation

1. Get a free API Key at [https://developer.spotify.com](https://developer.spotify.com)
2. Clone the repo
   ```sh
   git clone https://github.com/agrawalekansh02/musicpy.git
   ```
3. Install pip packages
   ```sh
   pip3 install -r requirements.txt
   ```
4. Add the following environment variables to your path
   ```sh
   export SPOTIPY_CLIENT_ID='client_id'
   export SPOTIPY_CLIENT_SECRET='client_secret'
   export SPOTIPY_REDIRECT_URI='https://example.com'
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To simply run the script and download a single track, run the following command.
```sh
python3 music.py -s "Rock and Roll Led Zep"
```

You can use the following tags to modify your download query
```sh
>>> python3 music.py -h

Welcome to MusicPy!
options and arguments:
-s: single track downlaoad
-a: entire album downlaoad
-m: multitrack download
-h: help menu
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/agrawalekansh02/musicpy](https://github.com/agrawalekansh02/musicpy)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/agrawalekansh02/musicpy.svg?style=for-the-badge
[contributors-url]: https://github.com/agrawalekansh02/musicpy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/agrawalekansh02/musicpy.svg?style=for-the-badge
[forks-url]: https://github.com/agrawalekansh02/musicpy/network/members
[stars-shield]: https://img.shields.io/github/stars/agrawalekansh02/musicpy.svg?style=for-the-badge
[stars-url]: https://github.com/agrawalekansh02/musicpy/stargazers
[issues-shield]: https://img.shields.io/github/issues/agrawalekansh02/musicpy.svg?style=for-the-badge
[issues-url]: https://github.com/agrawalekansh02/musicpy/issues
[license-shield]: https://img.shields.io/github/license/agrawalekansh02/musicpy.svg?style=for-the-badge
[license-url]: https://github.com/agrawalekansh02/musicpy/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
