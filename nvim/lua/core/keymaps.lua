vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

function keymap(key, command)
  vim.keymap.set('n', key, command)
end

keymap('w', ':w<CR>')
keymap('q', ':wq<CR>')
keymap('s', ':source ~/.config/nvim/init.lua<CR>')
keymap('e', ':bd<CR>')

 
