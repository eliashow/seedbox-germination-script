# Seed Box Germination Script
This script collects all magnet links on a specified web page and populates your default torrent client with the collected magnets. I created this script as a quick means to populate remote machines dedicated for seeding torrents.

## Running The Script
1. Clone the repository.
  ```
  git clone https://github.com/eliashow/seedbox-germination-script.git
  ```
2. Change working directory.
  ```
  cd seedbox-germination-script
  ```
3. Run the install script (Debian, Fedora, Arch) or install the prerequisites manually (pip3 install validators pyquery).
  ```
  chmod +x install.sh
  ./install.sh
  ```
4. In your torrent client make sure to uncheck any options that could bring up dialog boxes when adding torrents.
  
5. Run the germination script.
  ```
  python3 germination.py
  ```
