#!/bin/bash

config_alacritty(){
    echo "Installing alacritty"
    git clone https://github.com/alacritty/alacritty.git
    cd alacritty
    sudo pacman -S cmake freetype2 fontconfig pkg-config make libxcb libxkbcommon python
    cargo build --release
    sudo tic -xe alacritty,alacritty-direct extra/alacritty.info
    infocmp alacritty
    sudo cp target/release/alacritty /usr/local/bin # or anywhere else in $PATH
    sudo cp extra/logo/alacritty-term.svg /usr/share/pixmaps/Alacritty.svg
    sudo desktop-file-install extra/linux/Alacritty.desktop
    sudo update-desktop-database
    sudo mkdir -p /usr/local/share/man/man1
    sudo mkdir -p /usr/local/share/man/man5
    scdoc < extra/man/alacritty.1.scd | gzip -c | sudo tee /usr/local/share/man/man1/alacritty.1.gz > /dev/null
    scdoc < extra/man/alacritty-msg.1.scd | gzip -c | sudo tee /usr/local/share/man/man1/alacritty-msg.1.gz > /dev/null
    scdoc < extra/man/alacritty.5.scd | gzip -c | sudo tee /usr/local/share/man/man5/alacritty.5.gz > /dev/null
    scdoc < extra/man/alacritty-bindings.5.scd | gzip -c | sudo tee /usr/local/share/man/man5/alacritty-bindings.5.gz > /dev/null
    cd ..
}

install_dependencies(){
    echo "Installing needed packages..."
    sudo pacman -Sy rofi qtile dunst picom feh networkmanager polybar sddm

    echo "Configuring SDDM..."
    sudo systemctl enable sddm
    sudo systemctl start sddm
}

set_config_files(){
    echo "Configuring alacritty..."
    rm -rf ~/.config/alacritty
    cp -r alacritty ~/.config/alacritty

    echo "Configuring dunst..."
    rm -rf ~/.config/dunst
    cp -r dunst ~/.config/dunst
    killall dunst
    dunst &

    echo "Configuring nvim..."
    rm -rf ~/.config/nvim
    cp -r nvim ~/.config/nvim

    echo "configuring picom..."
    rm -rf ~/.config/picom
    cp -r picom ~/.config/picom

    echo "Configuring polybar..."
    rm -rf ~/.config/polybar
    cp -r polybar ~/.config/polybar
    sudo chmod +x ~/.config/polybar/*.sh

    echo "Configuring qtile..."
    rm -rf ~/.config/qtile
    cp -r qtile ~/.config/qtile

    echo "Configuring rofi..."
    rm -rf ~/.config/rofi
    cp -r rofi ~/.config/rofi

    echo "Configuring scripts..."
    cp -r scripts ~/.local/bin
    sudo chmod +x ~/.local/bin/scripts/*

    fonts_folder="$HOME/.fonts"

    if [ ! -d "$fonts_folder" ]; then
        echo "Creating the fonts folder..."
        mkdir -p "$fonts_folder"
    else
        echo "The .fonts folder already exists; no further action is needed."
    fi

    echo "Copying fonts..."
    cp -r fonts/* "$fonts_folder"
}

set_config_files





setxkbmap latam

