vim.opt.backspace = '2'
vim.opt.showcmd = true
vim.opt.autowrite = true
vim.opt.autoread = true
vim.opt.number = true
vim.opt.mouse = 'a'
vim.opt.showmatch = true

-- Use spaces for tabs an whatnot
vim.opt.tabstop = 2
vim.opt.shiftwidth = 2
vim.opt.shiftround = true
vim.opt.expandtab = true

vim.cmd 'set termguicolors'

vim.cmd [[
  hi StatusLine guibg=#282a36 guifg=#f8f8f2
  hi StatusLineNC guibg=#282a36 guifg=#6272a4
]]

require ('core.keymaps')
require('core.plugins')
require('core.pluginConfig.init')
require('core.configuration')
