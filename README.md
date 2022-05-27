<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![Michael's LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p align="center">
    This simple package takes in a city located in the United States and creates a markdown file containing its weather forecast.
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python]

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Here is how to get a local copy of the code up and running.

### Prerequisites

For this project, you will require both the requests and geopy package:
* To manually install the packages, enter this in your terminal
  ```sh
  pip install requests
  pip install geopy
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MichaelC03/US_Weather
   ```
2. Import the desired modules at the top of your Python file
   ```sh
   from us_weather.src import wquery as wquery
   from us_weather.src import wformat as wformat
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Michael Cheng - mccheng37@gmail.com

Project Link: [https://github.com/MichaelC03/US_Weather](https://github.com/MichaelC03/US_Weather)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MichaelC03/US_Weather.svg?style=for-the-badge
[contributors-url]: https://github.com/MichaelC03/US_Weather/graphs/contributors
[license-shield]: https://img.shields.io/github/license/MichaelC03/US_Weather.svg?style=for-the-badge
[license-url]: https://github.com/MichaelC03/US_Weather/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-cheng-2561a5220