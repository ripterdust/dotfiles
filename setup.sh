#!/bin/bash
echo "Configuring alacritty..."
rm -rf ~/.config/alacritty
cp -r alacritty ~/.config/alacritty

echo "Configuring dunst..."
rm -rf ~/.config/dunst
cp -r dunst ~/.config/dunst

echo "Configuring nvim..."
rm -rf ~/.config/nvim
cp -r nvim ~/.config/nvim

echo "configuring picom..."
rm -rf ~/.config/picom
cp -r picom ~/.config/picom

echo "Configuring polybar..."
rm -rf ~/.config/polybar
cp -r polybar ~/.config/polybar

echo "Configuring qtile..."
rm -rf ~/.config/qtile
cp -r qtile ~/.config/qtile

echo "Configuring rofi..."
rm -rf ~/.config/rofi
cp -r rofi ~/.config/rofi








