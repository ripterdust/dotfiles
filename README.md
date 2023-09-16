# Bryan Arevalo's dotfiles

!["Imagen de prueba"](./images/cover.png)

# Needed packages

- qtile
- Dunst
- picom
- feh
- nm-applet
- polybar
- slack
- rofi
- nvim

# Arch instalation

```
$ sudo pacman -Sy qtile dunst picom feh networkmanager polybar rofi nvim
```

# Setup

### automatically

Clone the repository

```
git clone https://github.com/ripterdust/dotfiles.git

cd dotfiles

sudo bash ./setup.sh
```

## Scripts

- Copy every file on <scripts> folder into ~/.local/bin
- Run

```
$ sudo chmod 777 <script-list>
```

## Config files

- Copy the resting folders into ~/.config
