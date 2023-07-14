vim.g.loaded_netrw = 1
vim.g.loaded_netrsPlugin = 1

require('nvim-tree').setup()


vim.keymap.set('n', 't', ':NvimTreeToggle<CR>')