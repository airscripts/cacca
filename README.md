<h1 align="center">
  <img src="https://raw.githubusercontent.com/airscripts/cacca/main/assets/images/logo.png" width="64" alt="Logo"/><br/>
  cacca
</h1>

<p align="center">
  A workflow framework, easy as shit.
</p>

## Contents
- [Installation](#installation)
- [Usage](#usage)
- [Resources](#resources)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## Installation
Follow the steps below to make use of Cacca.

Clone this repository:
```bash
pip install cacca
```

## Usage
This section is under construction but here you go with an `"Hello, Toilet!"` workflow:
```python
from cacca.lib import Cacca

cacca = Cacca()

cacca.insert({"action": print})
cacca.run(0, {"action": "Hello, Toilet!"})
```

## Resources
- [Documentation](https://cacca.airscript.it): Project documentation.
- [Flaticon](https://flaticon.com): Collection of assets.

## Contributing
Contributions and suggestions about how to improve this project are welcome!
Please follow [our contribution guidelines](https://github.com/airscripts/cacca/blob/main/CONTRIBUTING.md).

## Support
If you want to support my work you can do it by following me, leaving a star, sharing my projects or also donating at the links below.  
Choose what you find more suitable for you:  

<a href="https://sponsor.airscript.it" target="blank">
  <img src="https://raw.githubusercontent.com/airscripts/assets/main/images/github-sponsors.svg" alt="GitHub Sponsors" width="30px" />
</a>&nbsp;
<a href="https://kofi.airscript.it" target="blank">
  <img src="https://raw.githubusercontent.com/airscripts/assets/main/images/kofi.svg" alt="Kofi" width="30px" />
</a>

## License  
This repository is licensed under [MIT License](https://github.com/airscripts/cacca/blob/main/LICENSE).
