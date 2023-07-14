local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)
  use 'wbthomason/packer.nvim'
  use 'nvim-tree/nvim-tree.lua'
  use 'nvim-tree/nvim-web-devicons'
  use 'ellisonleao/gruvbox.nvim'
  use 'nvim-lualine/lualine.nvim'
  use 'neovim/nvim-lspconfig'
  use {
    'nvim-telescope/telescope.nvim', 
    tag = '0.1.0',
    requires = {{'nvim-lua/plenary.nvim'}}
  }
  use 'nvim-treesitter/nvim-treesitter'
  use {
    'folke/tokyonight.nvim',
    lazy = false,
    proprity = 1000,
    opts = {}
  }
  use {
    'alexghergh/nvim-tmux-navigation'
  }
  use {'akinsho/bufferline.nvim', tag = "*", requires = 'nvim-tree/nvim-web-devicons'}
  use {'rebelot/terminal.nvim'}
  use {'m4xshen/autoclose.nvim'}
  use {'folke/lsp-colors.nvim'}
  use {'folke/trouble.nvim'}
  use {'voldikss/vim-floaterm'}
  use {'neoclide/coc.nvim', branch = 'release'}
  use { 'feline-nvim/feline.nvim', branch = '0.5-compat' }
  -- My plugins here
  -- use 'foo1/bar1.nvim'
  -- use 'foo2/bar2.nvim'

  -- Automatically set up your configuration after cloning packer.nvim
  -- Put this at the end after all plugins
  if packer_bootstrap then
    require('packer').sync()
  end
end)
